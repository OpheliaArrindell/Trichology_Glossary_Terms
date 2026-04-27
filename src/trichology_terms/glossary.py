import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT_DIR / "data" / "trichology_terms.csv"


def load_terms() -> pd.DataFrame:
    """Load the trichology glossary as a pandas DataFrame."""
    return pd.read_csv(DATA_FILE)

def search_terms(keyword: str) -> pd.DataFrame:
    """Search across term, definition, and category."""
    df = load_terms()
    keyword = str(keyword)
    mask = (
        df["term"].str.contains(keyword, case=False, na=False)
        | df["definition"].str.contains(keyword, case=False, na=False)
        | df["category"].str.contains(keyword, case=False, na=False)
    )
    return df.loc[mask].reset_index(drop=True)

def get_definition(term: str) -> str | None:
    """Return the definition for an exact term match, or None if not found."""
    df = load_terms()
    match = df[df["term"].str.casefold() == str(term).casefold()]
    if match.empty:
        return None
    return match.iloc[0]["definition"]

def filter_by_category(category: str) -> pd.DataFrame:
    """Return rows where category contains the supplied category text."""
    df = load_terms()
    mask = df["category"].str.contains(str(category), case=False, na=False)
    return df.loc[mask].reset_index(drop=True)

def list_categories() -> list[str]:
    """Return sorted unique categories."""
    return sorted(load_terms()["category"].dropna().unique().tolist())
