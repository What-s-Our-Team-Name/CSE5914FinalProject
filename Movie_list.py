#from bs4 import ResultSet
import requests

def inputSelectedMovie(data_results):
    x = input("Enter the selected movie(0-{}):".format(len(data_results)-1))
    if (x.isdigit):
        return int(x)
    else:
        return False



def displaySelectedMovies(data_results):
    for i in range(len(data_results)):
        print('{}. {}'.format(i, data_results[i]['title']))

def selectMovie(data_results):
    displaySelectedMovies(data_results)
    x = inputSelectedMovie(data_results)
    print(x)
    if(x<0 or x>=len(data_results)):
        print("Please enter valid movie")
        displaySelectedMovies(data_results)
        x = inputSelectedMovie(data_results)
    return data_results[x]



def getMovieList():
    temp = []
   
    while(True):
        user_movie_name = input("Enter the name of the movie: ")
        if(not user_movie_name):
            break
        else:
            URL = "https://imdb-api.com/en/API/Search/k_z9p2w7dy/"+user_movie_name
            PARAMS = {'title':user_movie_name}
            r = requests.get(url = URL, params = PARAMS)
            data = r.json()

            if(len(data['results'])>0):
                movie = selectMovie(data['results'])
                if(movie not in temp):
                    temp.append(movie)
            else:
                print("Input a valid movie name!")
    
    return temp




def main():

    user_movie_list = getMovieList()
    #kalva.5: error will determine when a wrong movie is chosen and there is already more than one 
    #movie in the list
    print(user_movie_list)




if __name__ == "__main__":
    main()