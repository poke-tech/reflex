from http.client import responses

import streamlit as st
import pickle
import  pandas as pd
import  requests

import requests


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=5441070866351157246d4064331b7b0a&language=en-US"
    response = requests.get(url)
    data = response.json()

    # Check if 'poster_path' is in the response
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/original" + data['poster_path']
    else:
        # Return a default poster or handle missing poster
        return "https://via.placeholder.com/300x450?text=No+Poster"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recomended_movies = []
    recomended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # need to fetch the poster
        recomended_movies.append(movies.iloc[i[0]].title)
        recomended_movies_poster.append(fetch_poster(movie_id))

    return recomended_movies,recomended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie recomender system')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)


if st.button("Recommend"):
    names,poster = recommend(selected_movie_name)

    col1, col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])




#  5441070866351157246d4064331b7b0a

