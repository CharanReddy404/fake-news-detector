import pandas as pd

from fakenews.config import EXTERNAL_DIR, RAW_DIR

ISOT_DIR = RAW_DIR / "isot"
WELFAKE_FILE = EXTERNAL_DIR / "welfake" / "WELFake_Dataset.csv"

STANDARD_COLUMNS = ["title", "text", "label", "dataset"]
WELFAKE_LABELS = {0: "real", 1: "fake"}

def load_isot() -> pd.DataFrame:
  """Load ISOT (Fake.csv + True.csv) in the standard format, keeping subject and date."""
  fake = pd.read_csv(ISOT_DIR / "Fake.csv")
  real = pd.read_csv(ISOT_DIR / "True.csv")
  fake["label"] = "fake"
  real["label"] = "real"
  df = pd.concat([fake, real], ignore_index=True)
  df["dataset"] = "isot"
  return df[STANDARD_COLUMNS + ["subject", "date"]]

def load_welfake() -> pd.DataFrame:
  """Load WELFake in the standard format (label mapping verified by reading samples)."""
  df = pd.read_csv(WELFAKE_FILE, index_col=0)
  df["label"] = df["label"].map(WELFAKE_LABELS)
  df["dataset"] = "welfake"
  return df[STANDARD_COLUMNS]