import streamlit as st
import pickle
import pandas as pd

# Load stored data
with open('movie_dict.pkl', 'rb') as file:
    movie_data = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity_matrix = pickle.load(file)

# Convert dictionary to DataFrame
movie_df = pd.DataFrame(movie_data)

# Recommendation function
def get_recommendations(selected_title, top_n=5):
    # Locate the index of the chosen movie
    index = movie_df[movie_df['title'] == selected_title].index[0]

    # Fetch similarity scores for that movie
    similarity_scores = similarity_matrix[index]

    # Sort by similarity, excluding the same movie
    ranked_movies = sorted(
        list(enumerate(similarity_scores)),
        key=lambda x: x[1],
        reverse=True
    )[1:top_n+1]

    # Extract titles of recommended movies
    return [movie_df.iloc[i[0]].title for i in ranked_movies]

# Streamlit app layout
st.title("🎥 Movie Recommender")

selected_movie = st.selectbox("Pick a movie you like:", movie_df['title'].values)

if st.button("Show Recommendations"):
    for recommendation in get_recommendations(selected_movie):
        st.write(recommendation)
