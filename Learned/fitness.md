# Fitness: status

Opus reads and changes this file. Data lives in `Fitness/log/*.csv` and is
read with `python3 Fitness/fit.py week`. Fitness never counts toward the
daily floor.

## Goal

Visible abs, more muscle, less fat, stronger. Male, 20, 180 cm, 83 kg on
2026-10-26. Fat loss has stalled after the easy cuts (no soda, no snacks).

## Targets (`Fitness/targets.json`)

- 2,100 kcal a day, 160 g protein, at least 60 g fat; carbs fill the rest.
- Why: Mifflin-St Jeor BMR 1,860 kcal; × 1.4 (school, bus, walking, light
  training) ≈ 2,600 maintenance; minus ~500 for about 0.5 kg a week.
  Protein ≈ 1.9 g/kg keeps muscle while losing fat.
- The formula is a starting guess. After 2-3 weeks `fit.py week` prints a
  measured maintenance from intake and weight trend; that replaces it.

## Steering rules (Opus, at each fitness review)

- Use 7-day average weight, never one weigh-in.
- Change targets only with at least 5 of 7 days complete for two weeks.
- Loss under 0.2 kg/week for two weeks → 150 kcal less.
- Loss over 0.8 kg/week, or lifts going down for two weeks → 150 kcal more.
- Waist going down while weight holds still is progress (muscle in, fat out).
- Photo error above ±20% → more scale meals and stricter "unclear" asks.

## Training plan (until the home gym, ~March 2027)

3 full-body sessions a week, a day apart, about 40 minutes.

| Exercise (log name) | Sets × reps |
|---|---|
| Push-up (`pushup`) | 3 × 8-15 |
| One-arm dumbbell row (`row`) | 3 × 8-12 each arm |
| Goblet squat (`goblet_squat`) | 3 × 8-12 |
| Dumbbell Romanian deadlift (`rdl`) | 3 × 8-12 |
| Dumbbell overhead press (`ohp`) | 3 × 8-12 |
| Plank (`plank`, reps = seconds) | 3 × 30-60 s |

Progression: when every set reaches the top of the range, add weight next
session (or harder version: feet-up push-ups, Bulgarian split squat once
20 kg goblet squats are easy). Leave 1-2 reps in reserve each set.

## Haiku accuracy

- No calibration meals yet.

## Last fitness review

2026-10-26 (Opus, setup).
