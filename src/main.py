from load_data import load_csv
from clean import clean_column_names, drop_missing_community
from merge import merge_datasets
from analysis import correlation_matrix
from visualization import plot_heatmap

def main():
    census = load_csv("data/census_data.csv")
    crime = load_csv("data/crime_data.csv")
    education = load_csv("data/education_data.csv")

    census = clean_column_names(census)
    crime = clean_column_names(crime)
    education = clean_column_names(education)

    census = drop_missing_community(census)
    crime = drop_missing_community(crime)
    education = drop_missing_community(education)

    merged = merge_datasets(census, crime, education)

    corr = correlation_matrix(
        merged,
        columns=[
            "percent_households_below_poverty",
            "violent_crime_rate",
            "high_school_graduation_rate"
        ]
    )

    plot_heatmap(corr)

if __name__ == "__main__":
    main()
