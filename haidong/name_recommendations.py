import pandas as pd
import numpy as np
import movie_list as ml


titles = pd.read_csv('recom_title.csv')
titleids = pd.read_csv('recom_titleid.csv')
sim_records = pd.read_csv('sim_record.csv')

if __name__ == '__main__':
    user_movie_list,idss = ml.getMovieList()
    result = {}
    for ids in idss:
        recom_ids = titleids[titleids['title_id'] == ids].to_numpy().tolist()[0][1:]
        #print(recom_ids)
        sim_scores = sim_records[titleids['title_id'] == ids].to_numpy().tolist()[0][1:]
        #print(recom_ids)
        for i in range(15):
            if recom_ids[i] in result:
                result[recom_ids[i]] += sim_scores[i]
            else:
                result[recom_ids[i]] = sim_scores[i]
    recom_list = sorted(list(result.keys()), key = lambda x: result[x], reverse = True)
    recom_movies = [titles.loc[titleids['title_id'] == recom_id, 'title'].tolist()[0] for recom_id in recom_list]
    for movie in recom_movies[:15]:
        print(movie)
