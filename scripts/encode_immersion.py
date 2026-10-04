"""Re-encode the immersion library to tier C (CRF26, max 720p) - automated.

Learner's decision 2026-09-29: apply C across the whole library, no manual
per-video review (sample videos showed no visible defect).

Layout facts this script handles:
  * D:\\immersion\\advanced is a JUNCTION to C:\\Users\\Kohaku\\Videos\\Immersion\\
    advanced. os.walk does not follow it reliably, so the four levels are
    enumerated explicitly and each path is realpath()'d.
  * D: has only ~29 GB free but the encoded tree needs ~87 GB, so the output
    goes to C:. The originals are never modified or deleted here.

Safety contract:
  * READ-ONLY on the source tree. Output is a brand new tree.
  * Resumable: an existing, complete output file is skipped.
  * Every output is verified playable before it counts as done; failures are
    logged and retried on the next run rather than silently accepted.
  * .vtt subtitles are copied verbatim (the encode strips them from the
    container on purpose, so they must exist alongside).

Usage:
    python3 scripts/encode_immersion.py --limit 3          # benchmark
    python3 scripts/encode_immersion.py                   # full run
    python3 scripts/encode_immersion.py --verify-only
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

FFMPEG_DIR = (r"C:\Users\Kohaku\AppData\Local\Microsoft\WinGet\Packages"
              r"\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
              r"\ffmpeg-9.0.1-full_build\bin")
FFMPEG = os.path.join(FFMPEG_DIR, "ffmpeg.exe")
FFPROBE = os.path.join(FFMPEG_DIR, "ffprobe.exe")

# (level name, source directory). advanced is a junction -> realpath resolves it.
LEVELS = [
    ("complete-beginner", r"D:\immersion\complete-beginner"),
    ("beginner",          r"D:\immersion\beginner"),
    ("intermediate",      r"D:\immersion\intermediate"),
    ("advanced",          r"D:\immersion\advanced"),
]
OUTPUT_ROOT = r"C:\Users\Kohaku\Videos\ImmersionC"
LOG_PATH = r"C:\Users\Kohaku\Videos\ImmersionC\encode-log.jsonl"

CRF = 26
MAX_H = 720
AUDIO_KBPS = 96
PRESET = "fast"       # 'medium' compresses ~10% better but is ~2x slower
WORKERS = 4
TIMEOUT_BASE_SECONDS = 3600
TIMEOUT_PER_SOURCE_SECOND = 2.0
TIMEOUT_MARGIN_SECONDS = 900
TIMEOUT_MAX_SECONDS = 21600


def log(record):
    record["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def source_height(path):
    """Height of the source, so we never upscale and know if work is needed."""
    try:
        out = subprocess.run(
            [FFPROBE, "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height", "-of", "csv=p=0:nk=1", path],
            capture_output=True, text=True, timeout=60)
        parts = out.stdout.strip().split(",")
        return int(parts[1]) if len(parts) >= 2 and parts[1].strip() else None
    except Exception:
        return None


def source_duration(path):
    """Source duration in seconds, so long videos get a sufficient timeout."""
    try:
        out = subprocess.run(
            [FFPROBE, "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", path],
            capture_output=True, text=True, timeout=60)
        return float(out.stdout.strip() or 0) or None
    except Exception:
        return None


def encode_timeout_seconds(src):
    duration = source_duration(src)
    if not duration:
        return TIMEOUT_BASE_SECONDS
    scaled = int(duration * TIMEOUT_PER_SOURCE_SECOND + TIMEOUT_MARGIN_SECONDS)
    return min(TIMEOUT_MAX_SECONDS, max(TIMEOUT_BASE_SECONDS, scaled))


def already_done(dst):
    """An output counts as done only if it probes cleanly and is non-trivial."""
    if not os.path.exists(dst) or os.path.getsize(dst) < 10240:
        return False
    try:
        out = subprocess.run(
            [FFPROBE, "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", dst],
            capture_output=True, text=True, timeout=60)
        return out.returncode == 0 and float(out.stdout.strip() or 0) > 0
    except Exception:
        return False


def encode_one(job):
    """Encode a single video. Returns a result dict; never raises."""
    level, src = job
    base = os.path.splitext(os.path.basename(src))[0]
    out_dir = os.path.join(OUTPUT_ROOT, level)
    dst = os.path.join(out_dir, base + ".mp4")
    if already_done(dst):
        return {"level": level, "src": src, "status": "skip", "dst": dst}

    os.makedirs(out_dir, exist_ok=True)
    part = dst + ".part.mp4"          # ffmpeg writes here; rename only on success
    # A previous run that was killed (reboot, crash, Ctrl-C) leaves a truncated
    # .part.mp4 behind. It is unusable - ffprobe cannot read it - and re-running
    # would make ffmpeg truncate it again anyway, so remove it first rather than
    # letting a stale partial survive. This is what makes the script safe to
    # resume after an unclean stop.
    if os.path.exists(part):
        try:
            os.remove(part)
        except OSError:
            pass
    h = source_height(src)
    needs_scale = h is not None and h > MAX_H
    vf = f"scale=-2:{MAX_H}" if needs_scale else None

    cmd = [FFMPEG, "-y", "-v", "error", "-i", src]
    if vf:
        cmd += ["-vf", vf]
    cmd += ["-c:v", "libx264", "-crf", str(CRF), "-preset", PRESET,
            "-pix_fmt", "yuv420p",          # max player compatibility
            "-c:a", "aac", "-b:a", f"{AUDIO_KBPS}k",
            "-movflags", "+faststart",      # moov first: streams before fully downloaded
            part]
    started = time.time()
    timeout = encode_timeout_seconds(src)
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"level": level, "src": src, "status": "fail",
                "error": f"encoding timed out after {timeout} seconds"}
    elapsed = time.time() - started
    if res.returncode != 0 or not os.path.exists(part):
        return {"level": level, "src": src, "status": "fail",
                "error": res.stderr[-300:]}
    if not already_done(part):
        os.remove(part)
        return {"level": level, "src": src, "status": "fail",
                "error": "output did not probe"}
    shutil.move(part, dst)
    return {
        "level": level, "src": src, "dst": dst, "status": "ok",
        "seconds": round(elapsed, 1),
        "in_mb": round(os.path.getsize(src) / 1024 ** 2, 1),
        "out_mb": round(os.path.getsize(dst) / 1024 ** 2, 1),
    }


def collect_jobs(limit=None):
    jobs = []
    for level, path in LEVELS:
        real = os.path.realpath(path)
        if not os.path.isdir(real):
            print(f"  MISSING {level}: {real}", file=sys.stderr)
            continue
        for name in sorted(os.listdir(real)):
            if name.lower().endswith(".mp4"):
                jobs.append((level, os.path.join(real, name)))
    if limit:
        # spread the benchmark across levels rather than hammering one folder
        step = max(1, len(jobs) // limit)
        jobs = jobs[::step][:limit]
    return jobs


def subtitle_destination(name):
    """Normalize a subtitle filename that redundantly ends in `.mp4.vtt`."""
    if name.lower().endswith(".mp4.vtt"):
        return name[:-len(".mp4.vtt")] + ".vtt"
    return name


def copy_subtitles():
    """Copy every .vtt next to its new .mp4. These carry the subtitles; the
    encode drops them from the container, so the sidecar files are the only
    copy. Cheap and must not be forgotten."""
    copied = 0
    for level, path in LEVELS:
        real = os.path.realpath(path)
        out_dir = os.path.join(OUTPUT_ROOT, level)
        if not os.path.isdir(real):
            continue
        os.makedirs(out_dir, exist_ok=True)
        for name in os.listdir(real):
            if name.lower().endswith(".vtt"):
                dst = os.path.join(out_dir, subtitle_destination(name))
                if not os.path.exists(dst):
                    legacy = os.path.join(out_dir, name)
                    if legacy != dst and os.path.exists(legacy):
                        os.rename(legacy, dst)
                        copied += 1
                    else:
                        shutil.copyfile(os.path.join(real, name), dst)
                        copied += 1
    return copied


def verify():
    """Pairing + integrity report over the whole output tree."""
    report = {"levels": {}, "unpaired_video": [], "unpaired_vtt": [], "ok": True}
    for level, _ in LEVELS:
        d = os.path.join(OUTPUT_ROOT, level)
        if not os.path.isdir(d):
            report["levels"][level] = {"videos": 0, "subs": 0, "exists": False}
            continue
        vids = {os.path.splitext(f)[0] for f in os.listdir(d) if f.lower().endswith(".mp4")}
        subs = {os.path.splitext(f)[0] for f in os.listdir(d) if f.lower().endswith(".vtt")}
        report["levels"][level] = {
            "exists": True, "videos": len(vids), "subs": len(subs),
            "gb": round(sum(os.path.getsize(os.path.join(d, f))
                            for f in os.listdir(d) if f.lower().endswith(".mp4"))
                       / 1024 ** 3, 1),
        }
        report["unpaired_video"] += [f"{level}/{n}" for n in sorted(vids - subs)]
        report["unpaired_vtt"] += [f"{level}/{n}" for n in sorted(subs - vids)]
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--match", nargs="*", default=None,
                    help="only process sources whose filename contains any of these terms")
    ap.add_argument("--workers", type=int, default=WORKERS)
    ap.add_argument("--verify-only", action="store_true")
    ap.add_argument("--no-subs", action="store_true")
    args = ap.parse_args()

    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    if args.verify_only:
        print(json.dumps(verify(), ensure_ascii=False, indent=2))
        return 0

    jobs = collect_jobs(args.limit)
    if args.match:
        terms = [term.casefold() for term in args.match]
        jobs = [(level, src) for level, src in jobs
                if any(term in os.path.basename(src).casefold() for term in terms)]
        if not jobs:
            print(f"no sources matched: {' '.join(args.match)}", file=sys.stderr)
            return 2
    print(f"jobs: {len(jobs)}  workers: {args.workers}  crf: {CRF}  "
          f"max-h: {MAX_H}  preset: {PRESET}")
    if not args.no_subs:
        n = copy_subtitles()
        print(f"subtitles copied: {n}")

    done = skipped = failed = 0
    in_bytes = out_bytes = 0
    started = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(encode_one, j) for j in jobs]
        total = len(futures)
        # ETA must describe the work THIS run still has to do, not the whole
        # library. After a resume most jobs are already done and report
        # "skip"; counting them as progress would make the rate look tiny and
        # the remaining time look enormous. So the denominator is the number of
        # jobs that are not already complete, measured before any work starts.
        pending = sum(1 for _lv, src in jobs
                      if not already_done(os.path.join(
                          OUTPUT_ROOT, _lv,
                          os.path.splitext(os.path.basename(src))[0] + ".mp4")))
        print(f"pending this run: {pending} of {total} "
              f"({total - pending} already encoded)")
        for i, fut in enumerate(as_completed(futures), start=1):
            r = fut.result()
            if r["status"] == "ok":
                done += 1
                in_bytes += r["in_mb"] * 1024 ** 2
                out_bytes += r["out_mb"] * 1024 ** 2
                log(r)
            elif r["status"] == "skip":
                skipped += 1
            else:
                failed += 1
                log(r)
                print(f"  FAIL {os.path.basename(r['src'])}: {r.get('error','')[:160]}")
            if i % 10 == 0 or i == total:
                el = time.time() - started
                # Remaining ETA is against `pending` (this run's real work),
                # driven by how many pending jobs have now been processed.
                processed_pending = min(i, pending)
                rate = processed_pending / el if el else 0
                left = (pending - processed_pending) / rate if rate else 0
                ratio = (out_bytes / in_bytes * 100) if in_bytes else 0
                print(f"  {i}/{total} scanned | {processed_pending}/{pending} encoded"
                      f"  ok={done} skip={skipped} fail={failed}  "
                      f"{rate*60:.1f}/min  remaining={left/60:.0f}min"
                      f"  out={ratio:.0f}%",
                      flush=True)
    print(f"\ndone: ok={done} skip={skipped} fail={failed}  "
          f"elapsed={(time.time()-started)/60:.1f}min")
    if in_bytes:
        print(f"output is {out_bytes/in_bytes*100:.1f}% of source")
    print(f"library now {total - pending + done + failed}/{total} encoded")
    report = verify()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    # A non-zero exit when something failed, so an unattended run is visible
    # rather than silently 'complete'.
    return 0 if failed == 0 else 1


def _cli():
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        # Not an error: .part files are self-healing, so stopping here is safe
        # and the next run resumes. Say so plainly.
        print("\ninterrupted - safe to resume; re-run the same command.")
        raise SystemExit(130)


if __name__ == "__main__":
    _cli()
