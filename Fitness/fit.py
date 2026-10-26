#!/usr/bin/env python3
"""Fitness log and calculator. All arithmetic lives here; the caller only
names foods and grams.

  fit.py check  ITEM...            what a meal adds, and whether it fits today
  fit.py meal   MEAL ITEM... [--source S] [--photo-kcal N] [--note T]
  fit.py body   [--weight KG] [--waist CM]
  fit.py close  [DATE]             mark a day's food log complete
  fit.py lift   EXERCISE WEIGHT_KG REPS     e.g. pushup 0 12,10,9
  fit.py today
  fit.py week
  fit.py bmr    WEIGHT_KG HEIGHT_CM AGE     Mifflin-St Jeor, male

ITEM is food=grams (a name from foods.csv; food=2x for unit_g foods like
egg=2x), or name@P/C/F/A*N for a label: grams of protein/carbs/fat/alcohol
per serving, times N servings.
"""
import argparse, csv, json, sys
from datetime import datetime, date, timedelta
from pathlib import Path
from statistics import mean
from zoneinfo import ZoneInfo

HERE = Path(__file__).parent
LOG = HERE / "log"
KCAL = {"protein": 4, "carbs": 4, "fat": 9, "alcohol": 7}
KCAL_PER_KG = 7700  # energy in 1 kg of body weight change, approximate

FILES = {
    "food": ["date", "meal", "item", "grams", "protein", "carbs", "fat",
             "alcohol", "kcal", "source", "photo_kcal", "note"],
    "body": ["date", "weight_kg", "waist_cm"],
    "days": ["date"],
    "lifts": ["date", "exercise", "weight_kg", "reps"],
}


def today():
    return datetime.now(ZoneInfo("Asia/Tokyo")).date().isoformat()


def rows(name):
    p = LOG / f"{name}.csv"
    if not p.exists():
        return []
    with p.open() as f:
        return list(csv.DictReader(f))


def append(name, row):
    LOG.mkdir(exist_ok=True)
    p = LOG / f"{name}.csv"
    new = not p.exists()
    with p.open("a", newline="") as f:
        w = csv.DictWriter(f, FILES[name], lineterminator="\n")
        if new:
            w.writeheader()
        w.writerow(row)


def foods():
    with (HERE / "foods.csv").open() as f:
        return {r["food"]: r for r in csv.DictReader(f)}


def targets():
    return json.loads((HERE / "targets.json").read_text())


def kcal(m):
    return sum(m[k] * KCAL[k] for k in KCAL)


def parse_item(text, table):
    if "@" in text:
        name, rest = text.split("@", 1)
        n = 1.0
        if "*" in rest:
            rest, n = rest.split("*")
            n = float(n)
        parts = [float(x) for x in rest.split("/")]
        if len(parts) != 4:
            sys.exit(f"{text}: a label needs P/C/F/A, four numbers")
        m = dict(zip(KCAL, (x * n for x in parts)))
        return {"item": name, "grams": "", **m}
    if "=" not in text:
        sys.exit(f"{text}: write food=grams or name@P/C/F/A*N")
    name, amount = text.split("=", 1)
    if name not in table:
        sys.exit(f"{name}: not in foods.csv. Ask for the label, or log it "
                 f"as {name}@P/C/F/A and add a Proposals.md item.")
    r = table[name]
    if amount.endswith("x"):
        if not r["unit_g"]:
            sys.exit(f"{name}: no unit size; give grams")
        grams = float(amount[:-1]) * float(r["unit_g"])
    else:
        grams = float(amount)
    m = {k: float(r[k]) * grams / 100 for k in KCAL}
    return {"item": name, "grams": round(grams), **m}


def totals(items):
    t = {k: sum(i[k] for i in items) for k in KCAL}
    t["kcal"] = kcal(t)
    return t


def day_totals(d):
    items = [{k: float(r[k]) for k in KCAL} for r in rows("food") if r["date"] == d]
    return totals(items) if items else {**{k: 0.0 for k in KCAL}, "kcal": 0.0}


def show(label, t):
    print(f"{label}: {t['kcal']:.0f} kcal | P {t['protein']:.0f} g  "
          f"C {t['carbs']:.0f} g  F {t['fat']:.0f} g"
          + (f"  A {t['alcohol']:.0f} g" if t["alcohol"] else ""))


def advise(meal_t, before):
    tg = targets()
    left = tg["kcal"] - before["kcal"]
    p_left = tg["protein_g"] - before["protein"]
    if meal_t["kcal"] <= left:
        print(f"Fits. Left after it: {left - meal_t['kcal']:.0f} kcal, "
              f"{max(p_left - meal_t['protein'], 0):.0f} g protein.")
    elif left <= 0:
        print(f"Over: today is already at {before['kcal']:.0f} of {tg['kcal']} kcal. "
              f"Eat only the protein part, or skip.")
    else:
        share = left / meal_t["kcal"]
        print(f"Over by {meal_t['kcal'] - left:.0f} kcal. Eat about "
              f"{share:.0%} of it: keep the protein, leave rice/bread/fried parts.")


def cmd_check(a):
    table = foods()
    items = [parse_item(t, table) for t in a.items]
    for i in items:
        show(f"  {i['item']} {i['grams']}g" if i["grams"] else f"  {i['item']}", totals([i]))
    t = totals(items)
    show("Meal", t)
    advise(t, day_totals(a.date or today()))
    return items, t


def cmd_meal(a):
    items, t = cmd_check(a)
    d = a.date or today()
    for n, i in enumerate(items):
        append("food", {
            "date": d, "meal": a.meal, "item": i["item"], "grams": i["grams"],
            **{k: round(i[k], 1) for k in KCAL}, "kcal": round(kcal(i)),
            "source": a.source,
            "photo_kcal": a.photo_kcal if (n == 0 and a.photo_kcal) else "",
            "note": a.note if n == 0 else "",
        })
    show("Day so far", day_totals(d))


def cmd_body(a):
    if a.weight is None and a.waist is None:
        sys.exit("give --weight and/or --waist")
    append("body", {"date": a.date or today(),
                    "weight_kg": a.weight if a.weight is not None else "",
                    "waist_cm": a.waist if a.waist is not None else ""})
    print("Logged.")


def cmd_close(a):
    d = a.day or (date.fromisoformat(today()) - timedelta(days=1)).isoformat()
    if any(r["date"] == d for r in rows("days")):
        print(f"{d} already complete.")
        return
    if not any(r["date"] == d for r in rows("food")):
        sys.exit(f"{d}: no food logged, so it cannot be complete.")
    append("days", {"date": d})
    show(f"{d} complete", day_totals(d))


def cmd_lift(a):
    append("lifts", {"date": a.date or today(), "exercise": a.exercise,
                     "weight_kg": a.weight, "reps": a.reps})
    prev = [r for r in rows("lifts") if r["exercise"] == a.exercise][:-1]
    if prev:
        p = prev[-1]
        print(f"Last time ({p['date']}): {p['weight_kg']} kg x {p['reps']}")
    print("Logged.")


def cmd_today(a):
    d = a.date or today()
    t, tg = day_totals(d), targets()
    show(d, t)
    print(f"Left: {tg['kcal'] - t['kcal']:.0f} kcal, "
          f"{max(tg['protein_g'] - t['protein'], 0):.0f} g protein")


def avg_weight(body, start, end):
    w = [float(r["weight_kg"]) for r in body
         if r["weight_kg"] and start <= r["date"] <= end]
    return (mean(w), len(w)) if w else (None, 0)


def slope(points):
    """Least-squares slope of (day_number, kg) points, kg per day."""
    xs, ys = zip(*points)
    mx, my = mean(xs), mean(ys)
    den = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den if den else 0.0


def cmd_week(a):
    end = date.fromisoformat(a.date or today())
    iso = lambda d: d.isoformat()
    body = rows("body")
    this, n1 = avg_weight(body, iso(end - timedelta(6)), iso(end))
    last, n2 = avg_weight(body, iso(end - timedelta(13)), iso(end - timedelta(7)))
    print(f"Weight 7-day avg: {this and round(this, 1)} kg ({n1} weigh-ins); "
          f"week before: {last and round(last, 1)} kg ({n2})")
    if this and last:
        print(f"Change: {this - last:+.2f} kg/week")
    waists = [r for r in body if r["waist_cm"]]
    if waists:
        print("Waist: " + ", ".join(f"{r['date'][5:]} {r['waist_cm']}" for r in waists[-4:]))

    closed = {r["date"] for r in rows("days")}
    window = [iso(end - timedelta(i)) for i in range(7)]
    full = [d for d in window if d in closed]
    if full:
        ts = [day_totals(d) for d in full]
        print(f"Food: {len(full)}/7 days complete; avg {mean(t['kcal'] for t in ts):.0f} kcal, "
              f"{mean(t['protein'] for t in ts):.0f} g protein (target "
              f"{targets()['kcal']} / {targets()['protein_g']})")
    else:
        print("Food: no complete days this week.")

    # Measured maintenance: intake on complete days, corrected by the
    # weight trend. Needs about two weeks of data to mean anything.
    start = end - timedelta(20)
    pts = [((date.fromisoformat(r["date"]) - start).days, float(r["weight_kg"]))
           for r in body if r["weight_kg"] and iso(start) <= r["date"] <= iso(end)]
    days21 = [d for d in closed if iso(start) <= d <= iso(end)]
    if len(pts) >= 10 and len(days21) >= 10:
        intake = mean(day_totals(d)["kcal"] for d in days21)
        tdee = intake - slope(pts) * KCAL_PER_KG
        print(f"Measured maintenance (21 days): ~{tdee:.0f} kcal "
              f"({len(days21)} complete days, {len(pts)} weigh-ins)")
    else:
        print(f"Measured maintenance: not enough data yet "
              f"({len(days21)}/10 complete days, {len(pts)}/10 weigh-ins in 21 days)")

    cal = [r for r in rows("food") if r["photo_kcal"]]
    if cal:
        errs = []
        for r in cal:
            real = sum(float(x["kcal"]) for x in rows("food")
                       if x["date"] == r["date"] and x["meal"] == r["meal"])
            errs.append((float(r["photo_kcal"]) - real) / real)
        print(f"Photo estimates vs scale: {len(errs)} meals, avg error "
              f"{mean(errs):+.0%}, worst {max(errs, key=abs):+.0%}")

    lifts = rows("lifts")
    names = sorted({r["exercise"] for r in lifts})
    for n in names:
        rs = [r for r in lifts if r["exercise"] == n]
        print(f"{n}: first {rs[0]['weight_kg']} kg x {rs[0]['reps']} ({rs[0]['date'][5:]}), "
              f"last {rs[-1]['weight_kg']} kg x {rs[-1]['reps']} ({rs[-1]['date'][5:]})")


def cmd_bmr(a):
    b = 10 * a.weight + 6.25 * a.height - 5 * a.age + 5
    print(f"BMR {b:.0f} kcal; x1.375 {b * 1.375:.0f}; x1.4 {b * 1.4:.0f}; "
          f"x1.55 {b * 1.55:.0f}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--date", help="YYYY-MM-DD, default today in JST")
    s = p.add_subparsers(dest="cmd", required=True)
    c = s.add_parser("check"); c.add_argument("items", nargs="+")
    m = s.add_parser("meal"); m.add_argument("meal"); m.add_argument("items", nargs="+")
    m.add_argument("--source", choices=["scale", "label", "photo"], required=True)
    m.add_argument("--photo-kcal", type=float, help="photo estimate made before weighing")
    m.add_argument("--note", default="", help="what the photo showed, doubts")
    b = s.add_parser("body"); b.add_argument("--weight", type=float); b.add_argument("--waist", type=float)
    cl = s.add_parser("close"); cl.add_argument("day", nargs="?")
    l = s.add_parser("lift"); l.add_argument("exercise"); l.add_argument("weight", type=float)
    l.add_argument("reps", help="reps per set, e.g. 12,10,9")
    s.add_parser("today"); s.add_parser("week")
    r = s.add_parser("bmr"); r.add_argument("weight", type=float)
    r.add_argument("height", type=float); r.add_argument("age", type=int)
    a = p.parse_args()
    {"check": cmd_check, "meal": cmd_meal, "body": cmd_body, "close": cmd_close,
     "lift": cmd_lift, "today": cmd_today, "week": cmd_week, "bmr": cmd_bmr}[a.cmd](a)


if __name__ == "__main__":
    main()
