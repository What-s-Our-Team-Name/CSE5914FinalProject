import pandas as pd
import numpy as np
import movie_list as ml


titles = pd.read_csv('recom_title.csv')
titleids = pd.read_csv('recom_titleid.csv')

if __name__ == '__main__':
    user_movie_list,ids = ml.getMovieList()
    #print(ids)
    #print(user_movie_list)
    
    print(titles[titleids['title_id'] == ids].set_index('title').transpose())
    #name = input('Please enter a name: ')
    #print(recommendations[recommendations['title'] == name].set_index('title').transpose())
