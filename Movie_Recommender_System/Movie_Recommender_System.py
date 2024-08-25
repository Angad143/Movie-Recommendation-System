import streamlit as st  
import pickle  
import pandas as pd  
# Import requests for making HTTP requests to external APIs (to fetch movie posters)
import requests  

# Function to Fetch Movie Poster
def fetch_poster(movie_id):
    # Construct the URL for the API request to fetch movie details, including the poster
    url = "here we have to pass api url"
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the response JSON to a Python dictionary
    data = response.json()
    # Extract the poster path from the data
    poster_path = data["poster_path"]
    # Construct the full URL for the poster image
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    # Return the full path to the poster image
    return full_path

# Load Movie Data and Similarity Matrix
# Load the movie data from the pickle file and convert it to a DataFrame
movies_dict = pickle.load(open("movies_dict.pkl","rb"))
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

    recommended_movies = []
    recommended_movies_posters = []

    # Loop through the top 5 similar movies
    for i in movies_list:
        # Get the movie ID for the similar movie
        movie_id = movies.iloc[i[0]].movie_id
        # Append the movie title to the recommended movies list
        recommended_movies.append((movies.iloc[i[0]].title))
        # Fetch the poster for the movie and append it to the posters list
        recommended_movies_posters.append(fetch_poster(movie_id))

    # Return the list of recommended movie titles and their posters
    return recommended_movies, recommended_movies_posters

# ###############################################################
# The following section is for displaying posters with names without download links.

# Web App Title
st.title("Movies Recommender System")

# Dropdown Menu for Selecting a Movie
selected_movie_name = st.selectbox(
    'Enter the name of the movie you are searching for:',
    movies["title"].values)

# When the "Recommend" Button is Clicked
if st.button("Recommend"):
    # Get the recommended movies and their posters
    names, posters = recommend(selected_movie_name)

    # Display the Recommended Movies and Posters in a Row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])  # Display the name of the first recommended movie
        st.image(posters[0], use_column_width=True)  # Display the poster

    with col2:
        st.text(names[1]) 
        st.image(posters[1], use_column_width=True)  

    with col3:
        st.text(names[2]) 
        st.image(posters[2], use_column_width=True) 

    with col4:
        st.text(names[3]) 
        st.image(posters[3], use_column_width=True)

    with col5:
        st.text(names[4])  
        st.image(posters[4], use_column_width=True) 

##########################################################################################
# The following section is for displaying posters with names with download links of poster.

# # Set Background Color of the Web App
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #36454F;
#         color: Blue;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Web App Title
# st.title("Movies Recommender System")

# # Dropdown Menu for Selecting a Movie
# selected_movie_name = st.selectbox(
#     'Enter the name of the movie you are searching for:',
#     movies["title"].values)

# # When the "Recommend" Button is Clicked
# if st.button("Recommend"):
#     # Get the recommended movies and their posters
#     names, posters = recommend(selected_movie_name)

#     # Display the Recommended Movies and Posters in a Row
#     col1, col2, col3, col4, col5 = st.columns(5)
    
#     with col1:
#         st.text(names[0])  # Display the name of the first recommended movie
#         link_1 = f'<a href="{posters[0]}" download>Download </a>'  # Create a download link for the poster
#         st.image(posters[0], use_column_width=True)  # Display the poster
#         st.markdown(link_1, unsafe_allow_html=True)  # Show the download link

#     with col2:
#         st.text(names[1])  # Display the name of the second recommended movie
#         link_2 = f'<a href="{posters[1]}" download>Download </a>'  # Create a download link for the poster
#         st.image(posters[1], use_column_width=True)  # Display the poster
#         st.markdown(link_2, unsafe_allow_html=True)  # Show the download link

#     with col3:
#         st.text(names[2])  # Display the name of the third recommended movie
#         link_3 = f'<a href="{posters[2]}" download>Download </a>'  # Create a download link for the poster
#         st.image(posters[2], use_column_width=True)  # Display the poster
#         st.markdown(link_3, unsafe_allow_html=True)  # Show the download link

#     with col4:
#         st.text(names[3])  # Display the name of the fourth recommended movie
#         link_4 = f'<a href="{posters[3]}" download>Download </a>'  # Create a download link for the poster
#         st.image(posters[3], use_column_width=True)  # Display the poster
#         st.markdown(link_4, unsafe_allow_html=True)  # Show the download link

#     with col5:
#         st.text(names[4])  # Display the name of the fifth recommended movie
#         link_5 = f'<a href="{posters[4]}" download>Download </a>'  # Create a download link for the poster
#         st.image(posters[4], use_column_width=True)  # Display the poster
#         st.markdown(link_5, unsafe_allow_html=True)  # Show the download link
