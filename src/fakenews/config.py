from pathlib import Path

# project root = 2 folders up from this file  (src/fakenews/config.py -> project/)
ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_DIR      = ROOT_DIR / "data"
RAW_DIR       = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXTERNAL_DIR  = DATA_DIR / "external"
MODELS_DIR    = ROOT_DIR / "models"
FIGURES_DIR   = ROOT_DIR / "reports" / "figures"

RANDOM_STATE = 42          # same number everywhere -> reproducible results
TEST_SIZE    = 0.2         # 80% train / 20% test