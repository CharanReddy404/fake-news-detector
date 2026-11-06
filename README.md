# Fake News Detector

Detects likely fake news articles using classical NLP (TF-IDF, Logistic Regression, SVM)
and transformers (DistilBERT), with a leakage audit and cross-dataset evaluation.

## Status

Work in progress: Phase 0 (setup) done.

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
