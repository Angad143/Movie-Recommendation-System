# Import Libraries
import streamlit as st
import pickle
import pandas as pd 
import requests  

# Function to Fetch Movie Poster and Homepage
def fetch_poster(movie_id):
    # Construct the URL for the API request to fetch movie details, including the poster and homepage
    url = "here we have to pass api url"
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the response JSON to a Python dictionary
    data = response.json()
    # Extract the poster path from the data
    poster_path = data["poster_path"]
    # Construct the full URL for the poster image
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    # Extract the homepage URL from the data
    homepage = data["homepage"]
    # Return the full path to the poster image and the homepage URL
    return full_path, homepage

# Load Movie Data and Similarity Matrix
# Load the movie data from the pickle file and convert it to a DataFrame
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
# Load the similarity matrix from the pickle file
similarity = pickle.load(open("similarity.pkl", "rb"))

# Movie Recommendation Function
def recommend(movie):
    # Find the index of the selected movie in the DataFrame
    movie_index = movies[movies["title"] == movie].index[0]
    # Get the similarity scores for the selected movie
    distances = similarity[movie_index]
    # Sort the movies based on similarity scores in descending order and take the top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Initialize lists to store recommended movie titles, posters, and homepages
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_homepage = []

    # Loop through the top 5 similar movies
    for i in movies_list:
        # Get the movie ID for the similar movie
        movie_id = movies.iloc[i[0]].movie_id
        # Append the movie title to the recommended movies list
        recommended_movies.append((movies.iloc[i[0]].title))
        # Fetch the poster and homepage for the movie
        poster, homepage = fetch_poster(movie_id)
        # Append the poster and homepage to their respective lists
        recommended_movies_posters.append(poster)
        recommended_movies_homepage.append(homepage)

    # Return the list of recommended movie titles, posters, and homepages
    return recommended_movies, recommended_movies_posters, recommended_movies_homepage

# Web App Title
st.title("Movies Recommender System")

# Dropdown Menu for Selecting a Movie
selected_movie_name = st.selectbox(
    'Enter the name of the movie you are searching for:',
    movies["title"].values)

# When the "Recommend" Button is Clicked
if st.button("Recommend"):
    # Get the recommended movies, their posters, and homepages
    names, posters, homepages = recommend(selected_movie_name)

    # Display the Recommended Movies, Posters, and Homepages in a Row
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(5):
        with eval(f'col{i+1}'):
            st.text(names[i])  # Display the name of the recommended movie
            st.image(posters[i], use_column_width=True)  # Display the poster
            if homepages[i]:  # If a homepage exists for the movie
                link = f'<a href="{homepages[i]}" target="_blank">View Homepage</a>'  # Create a clickable link to the homepage
                st.markdown(link, unsafe_allow_html=True)  # Display the link in the web app
