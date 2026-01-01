import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("%", "percent")
    )
    return df

def drop_missing_community(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["community_area"].notna()]
