import pandas as pd

def merge_datasets(census, crime, education) -> pd.DataFrame:
    df = census.merge(crime, on="community_area", how="inner")
    df = df.merge(education, on="community_area", how="inner")
    return df
