import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def eda_and_analysis(df):
    # Research Question 1: Most-Watched vs Favorite Genres
    genre_df = df.explode('genres')
    genre_counts = genre_df['genres'].value_counts()
    genre_avg_ratings = genre_df.groupby('genres')['user_rating'].mean()

    # Visualization: Most-Watched Genres
    sns.barplot(x=genre_counts.index, y=genre_counts.values)
    plt.title('Most-Watched Genres')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.savefig('most_watched_genres.png')
    plt.show()

    # Visualization: Favorite Genres (Average Ratings)
    sns.barplot(x=genre_avg_ratings.index, y=genre_avg_ratings.values)
    plt.title('Favorite Genres (Average Ratings)')
    plt.xlabel('Genre')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=90)
    plt.savefig('favorite_genres.png')
    plt.show()

    print("Research Question 1:")
    print("Most-Watched Genres:\n", genre_counts)
    print("Favorite Genres (Average Ratings):\n", genre_avg_ratings)

    # Research Question 2: Alignment of User vs IMDb Ratings
    correlation, p_value = pearsonr(df['user_rating'], df['imdb_rating'])
    print(f"Research Question 2: Correlation between user and IMDb ratings: {correlation:.2f} (p-value: {p_value:.5f})")

    # Visualization: User vs IMDb Ratings
    sns.scatterplot(x=df['imdb_rating'], y=df['user_rating'])
    plt.title('User Ratings vs IMDb Ratings')
    plt.xlabel('IMDb Rating')
    plt.ylabel('User Rating')
    plt.savefig('user_vs_imdb_ratings.png')
    plt.show()

    # Research Question 3: Favorite Directors and Actors
    directors = genre_df.explode('director')['director'].value_counts()
    actors = genre_df.explode('actors')['actors'].value_counts()
    top_directors = directors.head(10)
    top_actors = actors.head(10)

    # Visualization: Top Directors
    sns.barplot(x=top_directors.values, y=top_directors.index)
    plt.title('Top 10 Directors by Viewing Count')
    plt.xlabel('Count')
    plt.ylabel('Director')
    plt.savefig('top_directors.png')
    plt.show()

    # Visualization: Top Actors
    sns.barplot(x=top_actors.values, y=top_actors.index)
    plt.title('Top 10 Actors by Viewing Count')
    plt.xlabel('Count')
    plt.ylabel('Actor')
    plt.savefig('top_actors.png')
    plt.show()

    print("Research Question 3:")
    print("Top 10 Directors:\n", top_directors)
    print("Top 10 Actors:\n", top_actors)

    # Research Question 4: Likes vs Dislikes by Properties
    likes = df[df['user_rating'] >= 7]
    dislikes = df[df['user_rating'] <= 4]
    likes_genres = likes.explode('genres')['genres'].value_counts()
    dislikes_genres = dislikes.explode('genres')['genres'].value_counts()

    # Visualization: Likes vs Dislikes by Genre
    likes_dislikes_df = pd.DataFrame({
        'Likes': likes_genres,
        'Dislikes': dislikes_genres
    }).fillna(0)

    likes_dislikes_df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Likes vs Dislikes by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.savefig('likes_dislikes_by_genre.png')
    plt.show()

    print("Research Question 4:")
    print("Likes by Genre:\n", likes_genres)
    print("Dislikes by Genre:\n", dislikes_genres)

    # Research Question 5: Movies vs TV Series Preferences
    movies = df[df['type'] == 'movie']
    tv_series = df[df['type'] == 'tv_series']

    movie_genres = movies.explode('genres')['genres'].value_counts()
    tv_series_genres = tv_series.explode('genres')['genres'].value_counts()

    movie_runtime_avg = movies['runtime'].mean()
    tv_series_runtime_avg = tv_series['runtime'].mean()

    # Visualization: Genre Preferences for Movies vs TV Series
    genre_prefs_df = pd.DataFrame({
        'Movies': movie_genres,
        'TV Series': tv_series_genres
    }).fillna(0)

    genre_prefs_df.plot(kind='bar', figsize=(10, 6))
    plt.title('Genre Preferences: Movies vs TV Series')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.savefig('genre_preferences_movies_vs_tv.png')
    plt.show()

    print("Research Question 5:")
    print(f"Average Runtime (Movies): {movie_runtime_avg:.2f} mins")
    print(f"Average Runtime (TV Series): {tv_series_runtime_avg:.2f} mins")
    print("Movie Genres:\n", movie_genres)
    print("TV Series Genres:\n", tv_series_genres)

