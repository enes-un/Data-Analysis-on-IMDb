import pandas as pd
from scipy.stats import pearsonr, ttest_ind, chi2_contingency

def test_hypotheses(df):
    # Hypothesis 1: Correlation between user and IMDb ratings
    correlation, p_value = pearsonr(df['user_rating'], df['imdb_rating'])
    print(f"Correlation between user and IMDb ratings: {correlation:.2f} (p-value: {p_value:.5f})")

    # Hypothesis 2: Average rating differences between genres
    genre_df = df.explode('genres')
    genre_means = genre_df.groupby('genres')['user_rating'].mean()
    print("Average ratings by genre:\n", genre_means)

    # Hypothesis 3: Chi-square test for genre preferences
    genre_rating_table = pd.crosstab(genre_df['genres'], genre_df['user_rating'])
    chi2, p, dof, ex = chi2_contingency(genre_rating_table)
    print(f"Chi-square test p-value for genre preference: {p:.5f}")

    # Hypothesis 4: T-test for movies vs. TV series ratings
    movies = df[df['type'] == 'movie']['user_rating']
    series = df[df['type'] == 'tv_series']['user_rating']
    t_stat, p_val = ttest_ind(movies, series)
    print(f"T-test between movie and TV series ratings: t-statistic = {t_stat:.2f}, p-value = {p_val:.5f}")

