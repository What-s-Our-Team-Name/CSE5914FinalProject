# Note: front end request must contain user_movie as a parameter

from flask import (
    Flask,
    abort,
    jsonify,
    render_template,
    request,
)
from flask import request
from flask_cors import CORS
from name_recommendations import (
    get_recommendations,
    is_valid_movie_id,
)
import requests
import traceback

app = Flask(__name__)
cors = CORS(app)

user_movie_list = []

@app.route("/add_movie", methods=["POST"])
def add_movie_to_list():
    try:
        movie_id = request.form['selected_movie']
    except Exception:
        abort(400, "Invalid request")
    if is_valid_movie_id(movie_id):
        user_movie_list.append(movie_id)
        resp = jsonify(success=True)
        return resp
    else:
        abort(400, "Invalid movie id")



@app.route("/imdb", methods=["GET"])
def get_imdb_results():
    try:
        movie = request.args.get('user_movie', '')
        URL = "https://imdb-api.com/en/API/AdvancedSearch/k_z9p2w7dy"
        PARAMS = {'title':movie, 'title_type':'feature', 'release_date':',2021-01-01', 'languages':'en'} 
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
    except Exception as e:
        print(traceback.format_exc())
        abort(500, 'Internal Server Error')
    return data

@app.route("/database", methods=["GET"])
def get_database_results():
    print(user_movie_list)
    try:
        rec_movies = get_recommendations(user_movie_list)
        return rec_movies
    except Exception:
        print(traceback.format_exc())
        abort(500, "Internal Server Error")

@app.route('/')
def home():
    return render_template('index.html')


app.run(host='0.0.0.0', port=8080, debug=True, use_debugger=False, use_reloader=False)