import pandas as pd
import numpy as np


total_movies = pd.read_csv('genres.csv')

def get_genre_recommendations(genre):
    movie_dict = {rank : movie
                  for rank, movie in enumerate(total_movies[total_movies['genres'].str.contains(genre)].head(15)['title'].to_numpy().tolist(), 1)}
    return movie_dict
