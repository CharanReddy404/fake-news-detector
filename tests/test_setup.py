import importlib


def test_libraries_import():
  for name in ["pandas", "sklearn", "nltk", "spacy", "gensim"]:
    importlib.import_module(name)

def test_spacy_model_loads():
  import spacy
  nlp = spacy.load("en_core_web_sm")
  doc = nlp("Reuters reported from Washington.")
  assert len(doc) == 5

def test_config_paths():
  from fakenews.config import RAW_DIR, ROOT_DIR
  assert (ROOT_DIR/ "pyproject.toml").exists()
  assert RAW_DIR.name == "raw"