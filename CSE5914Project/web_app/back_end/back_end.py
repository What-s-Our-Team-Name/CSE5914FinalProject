from flask import Flask
from requests import request

app = Flask(__name__)

@app.route("/imdb")
def get_imdb_results():
    movie = request.args.get('user_movie')
    URL = "https://imdb-api.com/en/API/AdvancedSearch/k_z9p2w7dy"
    PARAMS = {'title':movie, 'title_type':'feature', 'release_date':',2021-01-01', 'languages':'en'} 
    r = request.get(url = URL, params = PARAMS)
    data = r.json()
    return data

@app.route("/database")
def get_database_results():
    pass

app.run()