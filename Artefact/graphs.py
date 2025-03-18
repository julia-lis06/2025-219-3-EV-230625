import csv
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px



# Read data from the CSV file
file_path = '/mnt/data/new_Christmas.csv'
data = []
with open("C:/Users/19JLison.ACC/Desktop/project/new_christmas.csv", encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Load CSV file
df = pd.read_csv('new_christmas.csv', encoding='UTF-8')

#Bar chart - top 10 movies by avg imdb rating

# Convert IMDB_RATING to numeric
df['IMDB_RATING'] = pd.to_numeric(df['IMDB_RATING'], errors='coerce')  # Converts, handling errors

# Drop rows where IMDB_RATING is NaN
df = df.dropna(subset=['IMDB_RATING'])

# Sort data by IMDb rating
sorted_data = df.sort_values(by='IMDB_RATING', ascending=False)

# Get the top 10 movies
top_10_movies = sorted_data.head(10)

# Create a horizontal bar chart
plt.figure(figsize=(12, 7))
bars = plt.barh(top_10_movies['TITLE'], top_10_movies['IMDB_RATING'], color='darkred')

# Add labels on bars
for bar, rating in zip(bars, top_10_movies['IMDB_RATING']):
    plt.text(bar.get_width() - 0.2, bar.get_y() + bar.get_height()/2, 
             f'{float(rating):.1f}', ha='center', va='center', color='white', fontsize=12)

plt.xlabel('IMDB Rating')
plt.title('Top 10 Movies by IMDB Rating')
plt.gca().invert_yaxis()  # Highest rating on top
plt.xlim(0, 10)  # Set x-axis limit
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Light grid for readability
plt.show()

# Top 10 movies by avg votes -histogram 


# Convert VOTES to numeric (in case it's stored as a string)
df['VOTES'] = pd.to_numeric(df['VOTES'], errors='coerce')

# Drop NaN values in VOTES
df = df.dropna(subset=['VOTES'])

# Sort data by VOTES in descending order
sorted_data = df.sort_values(by='VOTES', ascending=False)

# Get the top 10 movies
top_10_movies = sorted_data.head(10)

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_10_movies['TITLE'], top_10_movies['VOTES'], color='purple', alpha=0.7)

# Labels and title
plt.xlabel('Movie Name')
plt.ylabel('Number of Votes')
plt.title('Top 10 Movies by Votes')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show plot
plt.show()

#Pie chart - distribution of imdb rating
RATING = df.groupby(['RATING']).size().reset_index(name='counts')
fig = px.pie(RATING, names = 'RATING',values = 'counts',
              title = 'Distribution of ratings',height =  600 , width = 600)

fig.write_html("pie_chart.html")
fig.show()


        
#print(df.columns)
        