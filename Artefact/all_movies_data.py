import pandas as pd
import json
import os

script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, 'new_christmas.csv')
df = pd.read_csv(csv_path, encoding='UTF-8')

df['IMDB_RATING'] = pd.to_numeric(df['IMDB_RATING'], errors='coerce')
df['VOTES'] = pd.to_numeric(df['VOTES'], errors='coerce')

df = df.dropna(subset=['IMDB_RATING', 'VOTES'])

all_movies_data = {
    "titles": df['TITLE'].tolist(),
    "ratings": df['IMDB_RATING'].tolist(),
    "ratings_raw": df['RATING'].tolist(),
    "votes": df['VOTES'].tolist()
}

rating_counts = df.groupby('RATING').size().reset_index(name='counts')
rating_distribution_data = {
    "ratings": rating_counts['RATING'].tolist(),
    "counts": rating_counts['counts'].tolist()
}

output_path = os.path.join(script_dir, "all_movies_data.json")
with open(output_path, "w") as f:
    json.dump({
        "all_movies": all_movies_data,
        "rating_distribution": rating_distribution_data
    }, f, indent=4)


