import pandas as pd

def clean_data(df):
    # Convert columns to numeric, coercing errors to NaN
    df['user_rating'] = pd.to_numeric(df['user_rating'], errors='coerce')
    df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')
    df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')
    df['year'] = pd.to_numeric(df['year'], errors='coerce')

    # Fill list-like columns with empty lists where missing
    df['genres'] = df['genres'].apply(lambda x: x if isinstance(x, list) else [])
    df['director'] = df['director'].apply(lambda x: x if isinstance(x, list) else [])
    df['actors'] = df['actors'].apply(lambda x: x if isinstance(x, list) else [])

    return df.dropna()  # Drop rows with missing data

