import pytest

from fakenews.data import ISOT_DIR, WELFAKE_FILE, load_isot, load_welfake

need_isot = pytest.mark.skipif(not (ISOT_DIR / "Fake.csv").exists(), reason="ISOT not downloaded")
need_welfake = pytest.mark.skipif(not (WELFAKE_FILE).exists(), reason="WELFake not downloaded")

@need_isot
def test_isot_standard_formate():
  df = load_isot();
  assert list(df.columns[:4]) == ["title", "text", "label", "dataset"]
  assert set(df["label"]) == {"fake", "real"}
  assert len(df) == 44898

@need_welfake
def test_welfake_standard_formate():
  df = load_welfake();
  assert df["label"].isna().sum() == 0
  assert set(df["label"]) == {"fake", "real"}

@need_welfake
def test_welfake_mapping_not_flipped():
  """Guard the mapping I verified by reading titles: 1 (clickbait) -> fake."""
  df = load_welfake()
  counts = df["label"].value_counts()
  assert counts["fake"] == 37106
  assert counts["real"] == 35028
  assert df.loc[0, "label"] == "fake" # row 0: 'LAW ENFORCEMENT ON HIGH ALERT ... [VIDEO]'