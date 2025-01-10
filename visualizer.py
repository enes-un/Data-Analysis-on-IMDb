import matplotlib.pyplot as plt
import seaborn as sns

def visualization(df):
    # Heatmap for Correlations
    corr = df[['user_rating', 'imdb_rating', 'runtime', 'year']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

    # Pair Plot
    sns.pairplot(df[['user_rating', 'imdb_rating', 'runtime', 'year']], diag_kind='kde')
    plt.suptitle('Pair Plot of Key Features', y=1.02)
    plt.show()

    # Stacked Bar Chart for Genre vs. User Ratings
    genre_df = df.explode('genres')
    genre_rating_pivot = genre_df.pivot_table(index='genres', columns='user_rating', aggfunc='size', fill_value=0)
    genre_rating_pivot.plot(kind='bar', stacked=True, figsize=(15, 7), colormap='viridis')
    plt.title('Stacked Bar Chart of Genres by User Ratings')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.show()

    # Movies vs. TV Series: Average Ratings
    type_rating = df.groupby('type')['user_rating'].mean()
    sns.barplot(x=type_rating.index, y=type_rating.values)
    plt.title('Average Ratings: Movies vs. TV Series')
    plt.xlabel('Type')
    plt.ylabel('Average Rating')
    plt.show()
