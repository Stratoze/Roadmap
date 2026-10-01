#!/usr/bin/env python3
"""Progress ledger, scoring, and dashboard for the learn -> test -> record loop.

Ownership: this script owns progress state, exactly as `review.py` owns review
state. Never hand-compute a floor, a readiness number, or a slope; call it here.

The append-only JSONL files under each domain directory are the source of truth:

    <domain>/probes.jsonl    one line per probe
    <domain>/progress.jsonl  one line per session

`dashboard` renders a self-contained HTML file from those files. It is a
convenience, not a requirement - the page reads the JSONL directly, so the
learner never has to run anything to view progress.

See `_system/learning/loop.md` for the ladder, the rules, and the scoring table.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import os
import sys
from datetime import datetime, timezone

VAULT_ROOT = os.path.realpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)
DOMAINS = ("Japanese", "Mechatronics")

LEVEL_NAMES = {
    0: "toddler",
    1: "child",
    2: "short answer",
    3: "full sentence",
    4: "nuance",
    5: "free production",
    6: "transfer",
}

# Scoring constants. Documented in `_system/learning/loop.md`.
#
# Two different quantities are deliberately kept apart, because conflating them
# makes the ratchet unusable:
#
#   * PROBE_TARGET is the learner's existing `target_success` (0.85): a
#     *per-probe* success rate over a short recent window. This is what the
#     floor ratchet is allowed to act on.
#   * Wilson lower bound is a *confidence* bound. At small n it is far below the
#     raw rate (6/6 reads 0.61, not 1.0), and needs ~22 consecutive passes to
#     clear 0.85. So it is reported as a confidence/trend signal, and never as
#     an advance gate - gating on it would pin the floor at L0 for weeks.
PROBE_TARGET = 0.85       # per-probe success target over RECENT_WINDOW probes
RECENT_WINDOW = 6         # recent probes behind the ratchet (short, ~1 session)
WINDOW_PROBES = 20        # rolling window for the confidence readout
ADVANCE_STREAK = 3        # consecutive passes at floor required to advance
DROP_MISSES = 2           # consecutive misses required to drop
SLOPE_SESSIONS = 10       # sessions used for the velocity slope
REANCHOR_PROBES = 3       # toddler re-anchor probes after a drop


class ProgressError(RuntimeError):
    """Raised for malformed records or missing domains. Never swallowed."""


# --- paths -----------------------------------------------------------------

def domain_dir(domain: str) -> str:
    return os.path.join(VAULT_ROOT, domain)


def probes_path(domain: str) -> str:
    return os.path.join(domain_dir(domain), "probes.jsonl")


def progress_path(domain: str) -> str:
    return os.path.join(domain_dir(domain), "progress.jsonl")


def check_domain(domain: str) -> str:
    if domain not in DOMAINS:
        raise ProgressError(f"unknown domain {domain!r}; expected one of {', '.join(DOMAINS)}")
    return domain


# --- append-only storage ---------------------------------------------------

def append_jsonl(path: str, record: dict) -> dict:
    """Append one record. Append-only by contract: never rewrite a ledger."""
    if not isinstance(record, dict):
        raise ProgressError(f"record for {path} must be an object")
    line = json.dumps(record, ensure_ascii=False, sort_keys=True)
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return record


def read_jsonl(path: str) -> list:
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, "r", encoding="utf-8") as handle:
        for number, raw in enumerate(handle, start=1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                rows.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise ProgressError(f"{path}:{number}: malformed JSON: {exc}") from exc
    return rows


def record_probe(domain, concept, level, result, signature="", when=None):
    """Record one probe outcome. `result` must be exactly pass or miss."""
    check_domain(domain)
    if result not in ("pass", "miss"):
        raise ProgressError("probe result must be 'pass' or 'miss'")
    level = int(level)
    if level not in LEVEL_NAMES:
        raise ProgressError(f"level must be 0-6, got {level}")
    record = {
        "ts": when or datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "domain": domain,
        "concept": concept,
        "level": level,
        "result": result,
        "signature": signature,
    }
    return append_jsonl(probes_path(domain), record)


def record_session(domain, floor_start, floor_end, probes, passed, missed,
                   peak_level, anchored=False, date=None, note=""):
    """Record one session's summary line. Counts must be internally consistent."""
    check_domain(domain)
    probes, passed, missed = int(probes), int(passed), int(missed)
    if probes < 0 or passed < 0 or missed < 0:
        raise ProgressError("counts must be non-negative")
    if passed + missed > probes:
        raise ProgressError(
            f"passed+missed ({passed}+{missed}) exceeds probes ({probes})"
        )
    record = {
        "date": date or datetime.now(timezone.utc).date().isoformat(),
        "domain": domain,
        "floor_start": int(floor_start),
        "floor_end": int(floor_end),
        "probes": probes,
        "pass": passed,
        "miss": missed,
        "peak_level": int(peak_level),
        "anchored": bool(anchored),
        "note": note,
    }
    return append_jsonl(progress_path(domain), record)


# --- scoring ---------------------------------------------------------------

def wilson_lower_bound(successes: int, total: int, z: float = 1.959963985) -> float:
    """Wilson score interval lower bound at ~95%.

    Returns 0.0 for an empty sample rather than raising: "no evidence" is a
    legitimate readiness value and must not crash a report. The naive
    successes/total is badly overconfident at small n, and sessions here are
    short, so the whole point is to not use it.
    """
    if total <= 0:
        return 0.0
    if successes < 0 or successes > total:
        raise ProgressError(f"successes {successes} out of range for total {total}")
    p = successes / total
    denominator = 1.0 + z * z / total
    centre = p + z * z / (2 * total)
    margin = z * math.sqrt((p * (1 - p) + z * z / (4 * total)) / total)
    return max(0.0, (centre - margin) / denominator)


def recent_rate(probe_rows: list) -> float:
    """Raw pass rate over the most recent RECENT_WINDOW probes.

    This is the quantity `target_success` was always about: how the learner is
    doing right now, over roughly one session. Unlike the Wilson bound it is
    meaningful at small n, which is exactly why the ratchet uses it.
    """
    window = probe_rows[-RECENT_WINDOW:]
    if not window:
        return 0.0
    passed = sum(1 for row in window if row.get("result") == "pass")
    return passed / len(window)


def readiness(probe_rows: list) -> float:
    """Wilson lower bound over the most recent WINDOW_PROBES probes.

    A confidence readout, not an advance gate. Small 9/10 reads 0.60 here,
    which is the correct epistemic signal for a short session: plausible, not
    established.
    """
    window = probe_rows[-WINDOW_PROBES:]
    if not window:
        return 0.0
    passed = sum(1 for row in window if row.get("result") == "pass")
    return wilson_lower_bound(passed, len(window))


def _streak(rows: list, result: str, count: int) -> int:
    """Length of the trailing run of `result`, capped at `count`."""
    run = 0
    for row in reversed(rows):
        if row.get("result") == result:
            run += 1
            if run >= count:
                break
        else:
            break
    return run


def suggested_floor(probe_rows: list, current_floor: int) -> int:
    """Recommend a floor move: +1 to advance, -1 to drop, else unchanged.

    Advance needs ADVANCE_STREAK consecutive passes *at the current floor*
    plus a recent pass rate at or above PROBE_TARGET. Drop needs DROP_MISSES
    consecutive misses at the current floor. A drop never pushes below 0.
    """
    at_floor = [row for row in probe_rows if row.get("level") == current_floor]
    if _streak(at_floor, "pass", ADVANCE_STREAK) >= ADVANCE_STREAK and \
            recent_rate(probe_rows) >= PROBE_TARGET:
        return min(current_floor + 1, max(LEVEL_NAMES))
    if _streak(at_floor, "miss", DROP_MISSES) >= DROP_MISSES:
        return max(current_floor - 1, 0)
    return current_floor


def _slope(values: list) -> float:
    """Ordinary least-squares slope of values against session index."""
    if len(values) < 2:
        return 0.0
    return _ols(list(range(len(values))), values)


def _ols(x: list, y: list) -> float:
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den = sum((xi - mean_x) ** 2 for xi in x)
    if den == 0:
        return 0.0
    return num / den


def velocity(session_rows: list, probe_rows: list) -> float:
    """Slope of readiness across the last SLOPE_SESSIONS sessions.

    Readiness is recomputed cumulatively at each session boundary, so this is
    a trend over time rather than a per-session bar. Positive means the learner
    is getting more reliable; negative means relarning or too-hard; flat means
    plateau, which calls for a strategy change, not a difficulty change.
    """
    if len(session_rows) < 2:
        return 0.0
    series = []
    upto = 0
    for row in session_rows[-SLOPE_SESSIONS:]:
        upto += int(row.get("probes", 0) or 0)
        series.append(readiness(probe_rows[:upto]))
    return _slope(series)


def coverage(probe_rows: list) -> dict:
    """concept -> level -> 'pass' | 'miss' (best result wins)."""
    rank = {"miss": 0, "pass": 1}
    grid: dict = {}
    for row in probe_rows:
        concept = row.get("concept") or "?"
        level = int(row.get("level", 0))
        result = row.get("result", "miss")
        cell = grid.setdefault(concept, {})
        if rank.get(result, 0) >= rank.get(cell.get(level, "miss"), 0):
            cell[level] = result
    return grid


def summarise(domain: str) -> dict:
    """Everything the reports and the dashboard need for one domain."""
    check_domain(domain)
    sessions = read_jsonl(progress_path(domain))
    probes = read_jsonl(probes_path(domain))
    sessions.sort(key=lambda row: row.get("date", ""))
    floor = sessions[-1]["floor_end"] if sessions else 0
    return {
        "domain": domain,
        "sessions": sessions,
        "probes": probes,
        "session_count": len(sessions),
        "probe_count": len(probes),
        "floor": floor,
        "recent_rate": recent_rate(probes),
        "readiness": readiness(probes),
        "suggested_floor": suggested_floor(probes, floor),
        "velocity": velocity(sessions, probes),
        "coverage": coverage(probes),
        "total_pass": sum(1 for row in probes if row.get("result") == "pass"),
    }


# --- text report -----------------------------------------------------------

def render_text(domains: list) -> str:
    out = []
    for domain in domains:
        s = summarise(domain)
        out.append(f"=== {domain} ===")
        if not s["sessions"]:
            out.append("  no sessions recorded yet")
            out.append("")
            continue
        trend = s["velocity"]
        direction = "improving" if trend > 0.002 else (
            "slipping" if trend < -0.002 else "flat (strategy change, not difficulty)")
        out.append(f"  sessions {s['session_count']}   probes {s['probe_count']} "
                   f"({s['total_pass']} pass)")
        out.append(f"  floor {s['floor']} ({LEVEL_NAMES.get(s['floor'], '?')})"
                   f"   suggested {s['suggested_floor']}")
        out.append(f"  recent rate {s['recent_rate']:.2f} (target {PROBE_TARGET:.2f})"
                   f"   confidence {s['readiness']:.2f} (Wilson, 20 probes)"
                   f"   velocity {trend:+.3f} {direction}")
        if s["coverage"]:
            out.append("  coverage (concept: levels passed)")
            for concept in sorted(s["coverage"]):
                passed = sorted(lv for lv, r in s["coverage"][concept].items() if r == "pass")
                shown = ",".join(str(lv) for lv in passed) if passed else "-"
                out.append(f"    {concept}: {shown}")
        out.append("")
    return "\n".join(out)


# --- dashboard -------------------------------------------------------------

def _svg_chart(s: dict, width: int = 620, height: int = 160) -> str:
    """Floor step-line + readiness slope, drawn server-side as inline SVG."""
    sessions = s["sessions"]
    if not sessions:
        return "<p class='empty'>no sessions yet</p>"
    pad = 28
    w, h = width, height
    n = len(sessions)

    def x_of(i):
        return pad + (i * (w - 2 * pad) / max(1, n - 1))

    def y_floor(level):
        # level 0 at the bottom, 6 at the top
        return h - pad - (level * (h - 2 * pad) / 6)

    parts = [f"<svg viewBox='0 0 {w} {h}' class='chart' role='img'>"]
    # readiness as a faint area line
    upto = 0
    pts = []
    for i, row in enumerate(sessions):
        upto += int(row.get("probes", 0) or 0)
        r = readiness(s["probes"][:upto])
        pts.append((x_of(i), h - pad - r * (h - 2 * pad)))
    if len(pts) > 1:
        poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        parts.append(f"<polyline points='{poly}' class='readiness'/>")
    # floor as a step line
    prev = None
    for i, row in enumerate(sessions):
        level = int(row.get("floor_end", 0))
        x = x_of(i)
        y = y_floor(level)
        if prev is not None:
            parts.append(f"<line x1='{prev[0]:.1f}' y1='{prev[1]:.1f}' "
                         f"x2='{x:.1f}' y2='{prev[1]:.1f}' class='floor-step'/>")
        parts.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='3' class='floor-dot'/>")
        prev = (x, y)
    # axis labels
    parts.append(f"<line x1='{pad}' y1='{h - pad}' x2='{w - pad}' y2='{h - pad}' class='axis'/>")
    parts.append(f"<text x='4' y='{y_floor(0):.0f}' class='lab'>L0</text>")
    parts.append(f"<text x='4' y='{y_floor(6):.0f}' class='lab'>L6</text>")
    first, last = sessions[0].get("date", "?"), sessions[-1].get("date", "?")
    parts.append(f"<text x='{pad}' y='{h - 6}' class='lab'>{html.escape(str(first))}</text>")
    parts.append(f"<text x='{w - pad}' y='{h - 6}' class='lab end'>{html.escape(str(last))}</text>")
    parts.append("</svg>")
    return "".join(parts)


def _svg_matrix(s: dict) -> str:
    grid = s["coverage"]
    if not grid:
        return "<p class='empty'>no probes yet</p>"
    concepts = sorted(grid)
    cell = 26
    left = 170
    top = 34
    width = left + 7 * cell + 12
    height = top + len(concepts) * cell + 10
    parts = [f"<svg viewBox='0 0 {width} {height}' class='matrix' role='img'>"]
    for lv in range(7):
        x = left + lv * cell + cell / 2
        parts.append(f"<text x='{x:.0f}' y='{top - 12}' class='lab mid'>L{lv}</text>")
    for row, concept in enumerate(concepts):
        y = top + row * cell
        name = concept if len(concept) <= 22 else concept[:21] + "…"
        parts.append(f"<text x='4' y='{y + cell / 2 + 4:.0f}' class='lab'>{html.escape(name)}</text>")
        for lv in range(7):
            state = grid[concept].get(lv)
            x = left + lv * cell
            if state is None:
                parts.append(f"<rect x='{x + 2}' y='{y + 2}' width='{cell - 4}' "
                             f"height='{cell - 4}' class='cell untested'/>")
            else:
                parts.append(f"<rect x='{x + 2}' y='{y + 2}' width='{cell - 4}' "
                             f"height='{cell - 4}' class='cell {state}'/>")
    parts.append("</svg>")
    return "".join(parts)


def render_dashboard(domains: list) -> str:
    """Self-contained HTML: inline data + vanilla JS, no dependencies."""
    data = {}
    for domain in domains:
        check_domain(domain)
        data[domain] = {
            "sessions": read_jsonl(progress_path(domain)),
            "probes": read_jsonl(probes_path(domain)),
        }
    # `<` is escaped so a concept name or note containing "</script>" cannot
    # close the data block and break the page. Safe because this JSON is only
    # ever parsed as JSON, never rendered as HTML.
    embedded = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    cards = []
    for domain in domains:
        s = summarise(domain)
        trend = s["velocity"]
        cards.append(f"""
        <section class='card'>
          <h2>{html.escape(domain)}</h2>
          <div class='stat'><b>{s['floor']}</b><span>floor ({html.escape(LEVEL_NAMES.get(s['floor'], '?'))})</span></div>
          <div class='stat'><b>{s['recent_rate']:.2f}</b><span>recent rate (target {PROBE_TARGET:.2f})</span></div>
          <div class='stat'><b>{s['readiness']:.2f}</b><span>confidence (Wilson)</span></div>
          <div class='stat'><b>{s['suggested_floor']}</b><span>suggested floor</span></div>
          <div class='stat'><b>{trend:+.3f}</b><span>velocity / session</span></div>
          {_svg_chart(s)}
          {_svg_matrix(s)}
        </section>""")
    return f"""<!doctype html>
<html lang='en'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>Learning progress</title>
<style>
  :root {{ color-scheme: dark; }}
  body {{ background:#111417; color:#e6e9ec; font:15px/1.5 ui-sans-serif,system-ui,sans-serif;
         margin:0; padding:24px; }}
  h1 {{ font-size:20px; margin:0 0 4px; }}
  .sub {{ color:#8b949e; margin:0 0 24px; font-size:13px; }}
  .card {{ background:#181c20; border:1px solid #262c33; border-radius:10px;
           padding:18px 20px; margin-bottom:22px; max-width:760px; }}
  h2 {{ margin:0 0 14px; font-size:16px; }}
  .stats {{ display:flex; flex-wrap:wrap; gap:18px; margin-bottom:16px; }}
  .stat b {{ display:block; font-size:22px; }}
  .stat span {{ color:#8b949e; font-size:12px; }}
  .chart, .matrix {{ width:100%; height:auto; background:#0e1114;
                     border:1px solid #21262d; border-radius:8px; margin:12px 0 4px; }}
  .floor-step {{ stroke:#58a6ff; stroke-width:2; }}
  .floor-dot  {{ fill:#58a6ff; }}
  .readiness  {{ fill:none; stroke:#3fb950; stroke-width:1.5; stroke-dasharray:4 3; }}
  .axis       {{ stroke:#30363d; }}
  .lab        {{ fill:#8b949e; font-size:11px; }}
  .lab.mid, .lab.end {{ text-anchor:middle; }}
  .lab.end    {{ text-anchor:end; }}
  .cell {{ rx:3; }}
  .cell.pass     {{ fill:#238636; }}
  .cell.miss     {{ fill:#6e4044; }}
  .cell.untested {{ fill:#21262d; }}
  .empty {{ color:#8b949e; font-size:13px; }}
  footer {{ color:#6e7681; font-size:12px; max-width:760px; }}
</style></head><body>
<h1>Learning progress</h1>
<p class='sub'>learn &rarr; test &rarr; record &middot; sourced from the append-only ledgers
   &middot; solid blue = floor, dashed green = Wilson confidence</p>
{''.join(cards)}
<footer>Generated by scripts/progress.py. The JSONL ledgers remain the source of truth;
        this page is a view.</footer>
<script id='data' type='application/json'>{embedded}</script>
</body></html>"""


def write_dashboard(domains: list, out_path: str) -> str:
    document = render_dashboard(domains)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(document)
    return out_path


# --- CLI -------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="progress ledger, Wilson scoring, and dashboard")
    parser.add_argument("--domain", action="append", dest="domains",
                        choices=DOMAINS, help="restrict to a domain; repeatable")
    sub = parser.add_subparsers(dest="command", required=True)

    probe = sub.add_parser("probe", help="record one probe outcome")
    probe.add_argument("domain", choices=DOMAINS)
    probe.add_argument("concept")
    probe.add_argument("level", type=int)
    probe.add_argument("result", choices=("pass", "miss"))
    probe.add_argument("--signature", default="")

    session = sub.add_parser("session", help="record one session summary")
    session.add_argument("domain", choices=DOMAINS)
    session.add_argument("--floor-start", type=int, required=True)
    session.add_argument("--floor-end", type=int, required=True)
    session.add_argument("--probes", type=int, required=True)
    session.add_argument("--pass", dest="passed", type=int, required=True)
    session.add_argument("--miss", dest="missed", type=int, required=True)
    session.add_argument("--peak-level", type=int, required=True)
    session.add_argument("--anchored", action="store_true")
    session.add_argument("--date", default="")
    session.add_argument("--note", default="")

    sub.add_parser("show", help="plain-text dashboard")
    dash = sub.add_parser("dashboard", help="write a self-contained HTML dashboard")
    dash.add_argument("--out", default=os.path.join(
        VAULT_ROOT, "_system", "learning", "progress.html"))
    return parser


def run(args):
    domains = args.domains if getattr(args, "domains", None) else list(DOMAINS)

    if args.command == "probe":
        record = record_probe(args.domain, args.concept, args.level,
                              args.result, args.signature)
        print(json.dumps(record, ensure_ascii=False))
        return 0

    if args.command == "session":
        record = record_session(args.domain, args.floor_start, args.floor_end,
                                args.probes, args.passed, args.missed,
                                args.peak_level, args.anchored, args.date,
                                args.note)
        print(json.dumps(record, ensure_ascii=False))
        return 0

    if args.command == "show":
        print(render_text(domains))
        return 0

    if args.command == "dashboard":
        path = write_dashboard(domains, os.path.abspath(args.out))
        print(path)
        return 0

    raise ProgressError(f"unknown command {args.command!r}")


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    args = build_parser().parse_args(argv)
    try:
        return run(args)
    except ProgressError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
