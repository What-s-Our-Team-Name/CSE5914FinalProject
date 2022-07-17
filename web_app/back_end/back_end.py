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
from genre_recommendations import get_genre_recommendations
import requests
import traceback

app = Flask(__name__)
cors = CORS(app)

user_movie_list = set()

class InvalidRequestException(Exception):
    pass

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidRequestException as e:
            response = jsonify({'error': str(e)})
            response.status_code = 400
            return response
        except Exception as e:
            response = jsonify({'error': str(e)})
            response.status_code = 500
            return response
    wrapper.__name__ = func.__name__ # Necessary to decorate more than one endpoint
    return wrapper

@app.route("/add_movie", methods=["POST"])
@exception_handler
def add_movie_to_list():
    movie_id = request.form.get('selected_movie', None)
    if movie_id is None:
        raise InvalidRequestException('Invalid request format')
    if is_valid_movie_id(movie_id):
        user_movie_list.add(movie_id)
        resp = jsonify(success=True)
        return resp
    else:
        raise InvalidRequestException('Invalid movie id')

@app.route("/clear", methods=["POST"])
@exception_handler
def clear_movies():
    user_movie_list.clear()
    resp = jsonify(success=True)
    return resp

@app.route("/imdb", methods=["GET"])
@exception_handler
def get_imdb_results():
    movie_name = request.args.get('movie_name', '')
    URL = "https://imdb-api.com/en/API/AdvancedSearch/k_fz1k341l"
    # Feel free to make any changes to the params
    PARAMS = {'title':movie_name, 'release_date': '2000-01-01,', 'languages':'en'}
    movies = requests.get(url = URL, params = PARAMS).json()['results']
    movies = list(filter(lambda movie: is_valid_movie_id(movie['id']), movies))
    return jsonify(movies)

@app.route("/database", methods=["GET"])
@exception_handler
def get_database_results():
    rec_movies = get_recommendations(user_movie_list)
    return rec_movies

@app.route("/genre", methods=["GET"])
@exception_handler
def get_genre_results():
    genre = request.args.get('genre', '')
    rec_movies = get_genre_recommendations(genre)
    return rec_movies

@app.route('/')
def home():
    return render_template('index.html')


app.run(host='0.0.0.0', port=8080, debug=True, use_debugger=False, use_reloader=False)