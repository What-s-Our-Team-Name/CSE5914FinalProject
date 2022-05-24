from bs4 import ResultSet
import requests

#print("Please Enter the movie names: ")

#title = input("Movie name: ")

#URL = "https://imdb-api.com/en/API/Search/k_z9p2w7dy/"+title

#PARAMS = {'title':title}

#r = requests.get(url = URL, params = PARAMS)

#data = r.json()

#print(data)


def displaySelectedMovies(data_results):
    for i in range(len(data_results)):
        print('{}. {}'.format(i, data_results[i]['title']))
    print

def selectMovie(data_results):
    print()



def main():
    user_movie_list = []
    #kalva.5: error will determine when a wrong movie is chosen and there is already more than one 
    #movie in the list
    error = False
    while(len(user_movie_list)==0 or error):
        user_movie_name = input("Enter the name of the movie: ")
        URL = "https://imdb-api.com/en/API/Search/k_z9p2w7dy/"+user_movie_name
        PARAMS = {'title':user_movie_name}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        if(len(data['results'])>0):
            selectMovie()




if __name__ == "__main__":
    main()