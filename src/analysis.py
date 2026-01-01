import pandas as pd

def correlation_matrix(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df[columns].corr()

def top_n_by_metric(df: pd.DataFrame, metric: str, n: int = 10) -> pd.DataFrame:
    return df.sort_values(by=metric, ascending=False).head(n)
