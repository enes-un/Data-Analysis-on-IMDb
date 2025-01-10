import imdb
import pandas as pd

ia = imdb.IMDb()

def fetch_metadata(ratings_df):
    metadata = []

    for imdb_id in ratings_df['imdb_id']:
        try:
            movie = ia.get_movie(imdb_id[2:])  # Remove 'tt' prefix for IMDbPY compatibility
            metadata.append({
                'imdb_id': imdb_id,
                'genres': movie.get('genres'),
                'runtime': movie.get('runtime', [None])[0],
                'year': movie.get('year'),
                'type': 'movie' if 'movie' in movie['kind'] else 'tv_series',
                'director': [d['name'] for d in movie.get('director', [])],
                'actors': [a['name'] for a in movie.get('cast', [])[:5]],
                'imdb_rating': movie.get('rating')  # Fetch IMDb rating
            })
        except Exception as e:
            print(f"Error fetching data for {imdb_id}: {e}")

    metadata_df = pd.DataFrame(metadata)
    return ratings_df.merge(metadata_df, on='imdb_id')


