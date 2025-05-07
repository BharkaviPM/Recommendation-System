#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Read the CSV files
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

# Display sample data from each
ratings_df.head(), movies_df.head()


# In[4]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv("movies.csv")

# Drop rows with missing values just in case
movies.dropna(inplace=True)

# Combine genres and titles as "tags" (content features)
movies["tags"] = movies["title"] + " " + movies["genres"]

# Create TF-IDF matrix from tags
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["tags"])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Mapping from movie title to index
indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()

# Recommendation function
def recommend_movies(title, num_recommendations=5):
    idx = indices.get(title)
    if idx is None:
        return f"Movie '{title}' not found in dataset."
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    
    return movies["title"].iloc[movie_indices].tolist()

# Example usage
target_movie = "Toy Story (1995)"
recommendations = recommend_movies(target_movie, 5)

print(f"Top 5 movies similar to '{target_movie}':")
for i, movie in enumerate(recommendations, 1):
    print(f"{i}. {movie}")

