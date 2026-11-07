# Data

Data files are not committed (see `.gitignore`). Download them into the folders below.

## Dataset A: ISOT Fake News (train / validation / test)

- Source: University of Victoria ISOT lab, https://onlineacademiccommunity.uvic.ca/isot/datasets/
  (downloaded as `News-_dataset.zip`)
- Files: `data/raw/isot/Fake.csv`, `data/raw/isot/True.csv`
- Size: 44,898 articles (23,481 fake, 21,417 real)
- Columns: title, text, subject, date. The label comes from the file name.
- Loader: `fakenews.data.load_isot()`
- License: research use (check the ISOT page before redistributing)
- Known issues:
  - Real articles are all from Reuters and start with "CITY (Reuters) -" -> source leak
  - Fake titles often start with a space; fake text has "couldn t" (apostrophe -> space)
    and double spaces; real text uses curly quotes -> formatting leaks
  - `subject` values differ by class -> do not use as a feature
  - `wc -l` shows more lines than articles because some texts contain line breaks

## Dataset B: WELFake (cross-dataset evaluation only)

- Source: Zenodo record 4561253 (Verma et al., IEEE TCSS 2021), https://zenodo.org/record/4561253
- File: `data/external/welfake/WELFake_Dataset.csv`
- Size: 72,134 articles (37,106 fake, 35,028 real)
- Columns: (unnamed index), title, text, label (0/1)
- Loader: `fakenews.data.load_welfake()`
- Label mapping used: **0 = real, 1 = fake**
  - Verified by reading 8 titles per label: label 1 = ALL CAPS, `[VIDEO]`, "UNBELIEVABLE!";
    label 0 = Reuters / NYT-style headlines.
  - The published description says the opposite (0 = fake). Locked in by
    `tests/test_data.py::test_welfake_mapping_not_flipped`.
- License: not clearly stated on the record; research use only
- Known issues:
  - Missing values: 558 titles, 39 texts (handled in Phase 2 cleaning)
  - Merged from 4 sources including Reuters -> may overlap ISOT (deduplicate in Phase 10)
  - Labels come from the source site, not per-article fact-checking -> noisy
    (e.g. a Breitbart article is labelled real)
  - Some real titles end with the outlet name ("- The New York Times") -> source leak
