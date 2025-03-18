import csv
import json
import os
import matplotlib.pyplot as plt

# Find the script directory
current_folder = os.path.dirname(__file__)
print("Running from:", current_folder)

# File path
csv_file = os.path.join(current_folder, 'new_christmas.csv')

# Empty list for movies
all_movies = []

# Read the CSV file and collect data for top movies
try:
    with open(csv_file, encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            try:
                rating = float(line['IMDB_RATING']) if line['IMDB_RATING'] else None
                votes = int(line['VOTES']) if line['VOTES'] else None
                if rating is not None and votes is not None:
                    all_movies.append({
                        "title": line['TITLE'],
                        "rating": rating,
                        "votes": votes,
                        "category": line['RATING']
                    })
            except:
                pass
    print(f"Loaded {len(all_movies)} movies.")
except Exception as e:
    print("Could not read file:", e)
    exit()

# Top 10 by rating
top_rated = sorted(all_movies, key=lambda m: m['rating'], reverse=True)[:10]

# Top 10 by votes
top_voted = sorted(all_movies, key=lambda m: m['votes'], reverse=True)[:10]

# Optionally save to movies_data.json
json_file = os.path.join(current_folder, 'movies_data.json')
try:
    with open(json_file, 'w') as jf:
        json.dump({
            "top_movies": {
                "titles": [m['title'] for m in top_rated],
                "ratings": [m['rating'] for m in top_rated]
            },
            "top_votes": {
                "titles": [m['title'] for m in top_voted],
                "votes": [m['votes'] for m in top_voted]
            }
        }, jf, indent=4)
    print(" Saved top 10 data to movies_data.json")
except Exception as e:
    print(" Failed to save movies_data.json:", e)

# Generate Top 10 Rated Movies Chart (PNG)
try:
    plt.figure(figsize=(9, 5))
    titles = [m['title'] for m in top_rated]
    ratings = [m['rating'] for m in top_rated]

    plt.barh(titles, ratings, color='steelblue')
    plt.xlabel('Rating')
    plt.title('Top 10 Christmas Movies by IMDb Rating')
    plt.gca().invert_yaxis()
    plt.tight_layout()

    chart1_file = os.path.join(current_folder, 'top_10_ratings_chart.png')
    plt.savefig(chart1_file)
    print(f" Saved chart 1 to {chart1_file}")
    plt.close()
except Exception as e:
    print("Chart 1 error:", e)

# Generate Top 10 Voted Movies Chart (PNG)
try:
    plt.figure(figsize=(9, 5))
    titles = [m['title'] for m in top_voted]
    votes = [m['votes'] for m in top_voted]

    plt.barh(titles, votes, color='indianred')
    plt.xlabel('Votes')
    plt.title('Top 10 Christmas Movies by Number of Votes')
    plt.gca().invert_yaxis()
    plt.tight_layout()

    chart2_file = os.path.join(current_folder, 'top_10_votes_chart.png')
    plt.savefig(chart2_file)
    print(f" Saved chart 2 to {chart2_file}")
    plt.close()
except Exception as e:
    print(" Chart 2 error:", e)
