# Fake News Detector

Detects likely fake news articles using classical NLP (TF-IDF, Logistic Regression, SVM)
and transformers (DistilBERT), with a leakage audit and cross-dataset evaluation.

## Status

Work in progress.

- Phase 0 (setup) done.
- Phase 1 (data) done: ISOT and WELFake loaders in a shared format, with tests.
  The WELFake label mapping was verified by reading samples; it is the opposite of
  its published description. See [data/README.md](data/README.md).

## Data

Datasets are not committed. See [data/README.md](data/README.md) for download links,
sizes, label definitions and known issues (source and formatting leaks).

## Setup

    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pip install -e .
    python -m spacy download en_core_web_sm
    python scripts/setup_nltk.py

## Project structure

    data/raw/         original datasets (not committed)
    data/processed/   cleaned data (generated)
    notebooks/        exploration and analysis
    src/fakenews/     reusable package code
    tests/            pytest tests
    models/           trained models (not committed)
    reports/figures/  charts used in this README
    app/              API and demo
