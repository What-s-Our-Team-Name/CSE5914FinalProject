import pandas as pd
import numpy as np


titles = pd.read_csv('recom_title.csv')
titleids = pd.read_csv('recom_titleid.csv')
sim_records = pd.read_csv('sim_record.csv')

titleids_set = set(titleids['title_id'].to_numpy().flatten())

"""
DESCRIPTION 
    - Get the recommendations for the top 15 movies
@parameters
    user_movie_ids - the title_ids from the user movie list
@return
    - the top 15 movies that can be recommended given the user's choice
"""
def get_recommendations(user_movie_ids):
    #user_movie_list,idss = ml.getMovieList()
    result = {}
    for user_movie_id in user_movie_ids:
        recom_ids = titleids[titleids['title_id'] == user_movie_id].to_numpy().tolist()[0][1:]
        #print(recom_ids)
        sim_scores = sim_records[titleids['title_id'] == user_movie_id].to_numpy().tolist()[0][1:]
        #print(recom_ids)
        for i in range(15):
            if recom_ids[i] in result:
                result[recom_ids[i]] += sim_scores[i]
            else:
                result[recom_ids[i]] = sim_scores[i]
    recom_list = sorted(list(result.keys()), key = lambda x: result[x], reverse = True)
    recom_movies = [titles.loc[titleids['title_id'] == recom_id, 'title'].tolist()[0] for recom_id in recom_list]
    movie_dict = {}
    top15_movies = recom_movies[:15]
    for i in range(len(top15_movies)):
        movie_dict[i] = top15_movies[i]

    return movie_dict

def is_valid_movie_id(movie_id):
    return movie_id in titleids_set
