import pandas as pd
import numpy as np
import movie_list as ml


total_movies = pd.read_csv('genres.csv')

if __name__ == '__main__':
    genre = input("Enter a genre: {animation, news, action, history, family, \
thriller, fantasy, horror, music, mystery, war, \
reality-tv, drama, talk-show, game-show, talk-show, musical, \
crime, romance, biography, comedy, reality-tv, horror, adventure, \
sci-fi, sport, adult, western, film-noir, sport}")
    print(total_movies[total_movies['genres'].str.contains(genre)].head(15))
