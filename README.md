# Movie-Recommendation-System
A Content-Based Movie Recommendation System suggests movies similar to a chosen title by analyzing attributes like genre, overview, keywords, and cast. 
It uses text preprocessing, vectorization (TF-IDF), and cosine similarity to identify and recommend the top 5 most related movies, providing personalized suggestions.
Step 1: Dataset Loading

The TMDb dataset is loaded using pandas.read_csv().

It contains fields like title, overview, genres, keywords, cast.

The dataset is cleaned: missing values are replaced with empty strings, and irrelevant columns are removed.

Step 2: Feature Extraction

Content-based filtering relies on textual attributes of movies.

For each movie, relevant text fields (overview, genres, keywords) are combined into a single string.

TF-IDF (Term Frequency-Inverse Document Frequency) vectorization is applied using TfidfVectorizer.

TF-IDF converts text into numeric vectors.

Words that are common across many movies get lower weight, while unique words get higher weight.

Step 3: Similarity Calculation

Cosine similarity is computed between the TF-IDF vectors of all movies.

Cosine similarity measures the angle between vectors; closer vectors mean more similar content.

This produces a similarity matrix where each entry [i][j] indicates how similar movie i is to movie j.

Step 4: Recommendation Function

A function takes a movie title as input.

Finds the index of the movie in the DataFrame.

Retrieves the similarity scores for that movie from the similarity matrix.

Sorts the scores in descending order.

Returns the top 5 movies (excluding the input movie itself).

Step 5: Streamlit Application

Streamlit is used to create an interactive web interface.

Users select a movie from a dropdown (st.selectbox).

On clicking “Recommend”, the top 5 similar movies are displayed using st.write().

Step 6: Deployment on Heroku

The app is deployed to Heroku for web access.

Required files include requirements.txt and Procfile.

The pickled data (movie_dict.pkl and similarity.pkl) are loaded in the app.

Users can access the app online without running Python locally.
