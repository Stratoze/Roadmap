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

Evidence it rests on (Opus checked the sources 2026-10-26):
- More weekly hard sets per muscle → more growth, at least up to ~10
  (Schoenfeld 2017 meta-analysis). Start at ~9-12 per muscle.
- Each muscle at least twice a week (Schoenfeld 2016 meta-analysis).
- Light loads grow muscle about as well as heavy ones when sets end close
  to failure; heavy loads build more strength (Schoenfeld 2017, low vs high
  load). So 20 kg dumbbells are enough for growth; for strength, use harder
  one-limb and lever variations.
- Stopping 1-3 reps short of failure works about as well as failure
  (Refalo 2023).
- Push-ups at matched effort grow chest and triceps like bench press
  (Kikuchi & Nakazato 2017).
- Ab training does not burn belly fat (Vispute 2011): visible abs come from
  the deficit. Abs are trained as a muscle, with moves that can get harder.
- Protein: gains level off around 1.6 g/kg (Morton 2018); 160 g is above it.

Buy: a doorway pull-up bar. Without it there is no vertical pull and no
hanging leg raise.

3 full-body sessions a week, a day apart, about 45 minutes. Same session
each time.

| Exercise (log name) | Sets × reps | Make it harder |
|---|---|---|
| Push-up (`pushup`) | 3 × 6-20 | feet up → backpack with books |
| Pull-up or chin-up (`pullup`); row until the bar arrives (`row`) | 3 × 5-12; row 3 × 8-15 each arm | slower lowering → backpack |
| Bulgarian split squat, dumbbells (`split_squat`) | 3 × 8-15 each leg | 2 × 20 kg → pause at the bottom |
| Dumbbell Romanian deadlift (`rdl`) | 3 × 8-15 | single-leg RDL |
| Dumbbell overhead press (`ohp`) | 2 × 8-15 | slower lowering → pike push-up |
| Hanging knee raise → leg raise (`leg_raise`); crunch holding a dumbbell until the bar arrives (`crunch`) | 3 × 8-15 | straight legs → slower |

Effort: every set ends 1-3 reps before you could not do another rep with
good form. Push-ups, pull-ups and abs may go to failure on the last set; the
leg moves never do.

Progression: when every set reaches the top of the range, use the next
"harder" step at the next session. A lift that stalls three sessions in a
row → Fitness review.

Sources:
- Schoenfeld, Ogborn, Krieger 2017, J Sports Sci (weekly sets)
- Schoenfeld, Ogborn, Krieger 2016, Sports Med (frequency)
- Schoenfeld, Grgic, Ogborn, Krieger 2017, JSCR 31(12) (load)
- Refalo et al. 2023, Sports Med 53(3) (failure)
- Kikuchi & Nakazato 2017, J Exerc Sci Fit (push-up vs bench)
- Vispute et al. 2011, JSCR (ab training and belly fat)
- Morton et al. 2018, Br J Sports Med 52(6) (protein)

## Haiku accuracy

- No calibration meals yet.

## Last fitness review

2026-10-26 (Opus, setup).
