import requests

print("Please Enter the movie names: ")

title = input("Movie name: ")

URL = "https://imdb-api.com/en/API/Search/k_z9p2w7dy/"+title

PARAMS = {'title':title}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

print(data)
