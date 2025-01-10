import matplotlib.pyplot as plt
import seaborn as sns

def eda(df):
    # Distribution of User Ratings
    sns.histplot(df['user_rating'], kde=True)
    plt.title('Distribution of User Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.show()

    # Genre Analysis
    genre_counts = df.explode('genres')['genres'].value_counts()
    sns.barplot(x=genre_counts.index, y=genre_counts.values)
    plt.title('Most Watched Genres')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.show()

    # Average Ratings by Year
    sns.lineplot(x='year', y='user_rating', data=df)
    plt.title('Average User Rating by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Rating')
    plt.show()

    # Top Directors and Actors
    directors = df.explode('director')['director'].value_counts().head(10)
    actors = df.explode('actors')['actors'].value_counts().head(10)
    
    sns.barplot(x=directors.values, y=directors.index)
    plt.title('Top 10 Directors by Number of Movies Watched')
    plt.xlabel('Count')
    plt.ylabel('Director')
    plt.show()
    
    sns.barplot(x=actors.values, y=actors.index)
    plt.title('Top 10 Actors by Number of Movies Watched')
    plt.xlabel('Count')
    plt.ylabel('Actor')
    plt.show()
