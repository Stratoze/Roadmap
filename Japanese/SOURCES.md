# Japanese source map

Raw source material lives in the private repository:

- <https://github.com/Stratoze/private-jp>
- Yokubi is a submodule in the private repository; the commit used for the
  current map is recorded in `source-map.json` and must be refreshed by
  regenerating the map after a source update.
- The IMABI mirror and its assets are stored there; the public vault does not
  copy the full HTML or image set.

## Roles

| Source | Role | Authority |
|---|---|---|
| [Yokubi](https://github.com/Morgawr/yokubi) | Ordered 64-lesson beginner grammar spine | Sequence and source locator; CC-BY-4.0 |
| `今日 IMABI.html` | Detailed reference index and nuance map | Unverified local mirror; derived structural index only. Verify disputed claims against the live source before stating them. |
| Anki | Japanese vocabulary scheduling and card storage | Runtime deck state; not a vault curriculum |

Yokubi is the ordered spine: it decides what is taught next and supplies the
lesson locator. IMABI is a lookup layer for nuance; it never reorders the spine
and never overrides a Yokubi lesson. The IMABI mirror's licence is unverified,
so nothing is quoted from it — only its anchor index and structure are used.

## Locators

Each lesson carries a public HTML URL derived from the private path:
`https://yoku.bi/<Section>/<Part>/<Lesson>.html`. Regenerate before using a
locator, and confirm the URL resolves. `scripts/tests/test_source_schema.py`
checks the derivation; run the live check with:

```bash
JAPANESE_SOURCE_LIVE_CHECK=1 python3 -m unittest scripts.tests.test_source_schema
```

## Regeneration

The machine-readable map is `Japanese/source-map.json`. Regenerate it from a
private checkout with:

```bash
python3 scripts/build_japanese_source_map.py \
  --private-root <private-repo> \
  --yokubi-root <private-repo>/sources/yokubi \
  --imabi-file <private-repo>/sources/今日 IMABI.html
```

The build is verified, not asserted. It aborts without writing anything unless

- the private checkout's `origin` is the repository declared above;
- the Yokubi checkout's `origin` is <https://github.com/Morgawr/yokubi>;
- both sources live inside the declared private root; and
- every SUMMARY lesson has a unique, contiguous numeric id.

A build without `--private-root` records `private_root_verified: false` and is
refused unless `--allow-unverified` is passed; an explicitly unverified build
still exits `1` so it cannot be mistaken for a verified regeneration. An
unverified build also refuses to overwrite a map that already records a
verified private root.

The map records the private verification result, Yokubi lesson IDs, titles,
paths, URLs, the pinned commit, and the IMABI anchor index. It does not mirror
the raw prose.

## Verifying the public side

`scripts/build_japanese_curriculum.py` compares the source map against the
public grammar table. It only ever compares the `id`, `aim`, and `prereqs`
columns and never writes, so a regeneration cannot destroy SRS state, rung,
`next_review`, or learner evidence. Exit status `2` means the table and the
source map disagree; the printed diff is the review input.
