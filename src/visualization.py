import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(corr_df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

def plot_scatter(df, x, y):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(f"{x} vs {y}")
    plt.tight_layout()
    plt.show()
