import requests
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

print("Please Enter the movie names: ")

#title = input("Movie name: ")

URL = "https://imdb-api.com/en/API/Top250TVs/k_z9p2w7dy"

#title = "Iron Man"
#PARAMS = {'title':title}

r = requests.get(url = URL)

data = r.json()

print(data['items'])

ids = [data['items'][i]['id'] for i in range(len(data['items']))]
titles = [data['items'][i]['title'] for i in range(len(data['items']))]
crews = [data['items'][i]['crew'] for i in range(len(data['items']))]
years = [data['items'][i]['year'] for i in range(len(data['items']))]
movies = pd.DataFrame({'ID':ids, 'Title':titles, 'Crew':crews, 'Year':years})
print(movies)


tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix_i = tf.fit_transform(movies['ID'])
tfidf_matrix_t = tf.fit_transform(movies['Title'])
tfidf_matrix_c = tf.fit_transform(movies['Crew'])
tfidf_matrix_y = tf.fit_transform(movies['Year'])
#tf.fit_transform(movies['Title'])
#print(tfidf_matrix_t)


cosine_sim_i = linear_kernel(tfidf_matrix_i, tfidf_matrix_i)
cosine_sim_t = linear_kernel(tfidf_matrix_t, tfidf_matrix_t)
cosine_sim_c = linear_kernel(tfidf_matrix_c, tfidf_matrix_c)
cosine_sim_y = linear_kernel(tfidf_matrix_y, tfidf_matrix_y)
cosine_sims = [cosine_sim_t, cosine_sim_c, cosine_sim_y]
attributes = ['Title', 'Crew', 'Year']
print(cosine_sim_i)

titles = movies['Title']
indices = pd.Series(movies.index, index=movies['Title'])
def movie_recommendations(title):
    recommendations = pd.DataFrame(index = range(20), columns = attributes)
    idx = indices[title]
    for i in range(len(cosine_sims)):
      sim_scores = list(enumerate(cosine_sims[i][idx]))
      sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
      sim_scores = sim_scores[1:21]
      movie_indices = [i[0] for i in sim_scores]
      recommendations[attributes[i]] = titles.iloc[movie_indices]
    return recommendations

movie_recommendations('Planet Earth II')

titles = movies['Title']
indices = pd.Series(movies.index, index=movies['Title'])

# Function that get movie recommendations based on the cosine similarity score of movie genres
def genre_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim_t[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

t = genre_recommendations('Planet Earth II').head(20)
print(t)

indices = pd.Series(movies.index, index=movies['Crew'])

# Function that get movie recommendations based on the cosine similarity score of movie genres
def crew_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim_c[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices], sim_scores

c = crew_recommendations('David Attenborough, Chadden Hunter')

print(c)

indices = pd.Series(movies.index, index=movies['ID'])

# Function that get movie recommendations based on the cosine similarity score of movie genres
def year_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim_i[idx]))
    #print(sim_scores)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices], sim_scores

i = year_recommendations('tt5491994')
print(i)
