

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-movie ratings data
ratings_dict = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Carol', 'Carol', 'Carol'],
    'Movie': ['Titanic', 'Avatar', 'Inception', 'Titanic', 'Inception', 'Avatar', 'Inception', 'Interstellar'],
    'Rating': [5, 4, 5, 5, 3, 4, 5, 5]
}

df = pd.DataFrame(ratings_dict)

# Create pivot table (user-item matrix)
pivot_table = df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)

# Compute item-to-item similarity (transpose to get items as rows)
item_similarity = cosine_similarity(pivot_table.T)
similarity_df = pd.DataFrame(item_similarity, index=pivot_table.columns, columns=pivot_table.columns)

def recommend_movies(movie_name, num_recommendations=3):
    if movie_name not in similarity_df:
        return f"Movie '{movie_name}' not found in data."
    similar_scores = similarity_df[movie_name].sort_values(ascending=False)
    recommendations = similar_scores.iloc[1:num_recommendations+1]
    return recommendations

# Example usage
if __name__ == "__main__":
    movie = input("Enter a movie you've liked: ")
    print(f"\n🎥 Because you liked '{movie}', you might also like:")
    recs = recommend_movies(movie)
    print(recs)
