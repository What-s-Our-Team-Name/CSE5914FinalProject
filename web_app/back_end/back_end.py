# Note: front end request must contain user_movie as a parameter

from flask import Flask
from flask import request
import name_recommendations
import requests

app = Flask(__name__)

user_movie_list = []

@app.route("/add_movie", methods=["POST"])
def add_movie_to_list():
    movie = request.form['selected_movie']
    user_movie_list.append(movie)

@app.route("/imdb", methods=["GET"])
def get_imdb_results():
    movie = request.args.get('user_movie', '')
    URL = "https://imdb-api.com/en/API/AdvancedSearch/k_z9p2w7dy"
    PARAMS = {'title':movie, 'title_type':'feature', 'release_date':',2021-01-01', 'languages':'en'} 
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    return data

@app.route("/database", methods=["GET"])
def get_database_results():
    rec_movies = name_recommendations.getRecommendations(user_movie_list)
    return rec_movies

app.run(debug=True, use_debugger=False, use_reloader=False)