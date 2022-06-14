#from bs4 import ResultSet
#@author: What is our team name?

#imports
import requests

"""
DESCRIPTION 
    - Have the user input numerically what movie they are interested in
@parameters
    data_results - the api list of the movies that closely relate to what the user searched up
@return
    - the number index of the movie that they had selected
"""
def inputSelectedMovie(data_results):
    x = input("Enter the selected movie(0-{}):".format(len(data_results)-1))
    if (x.isdigit):
        return int(x)
    else:
        return False


"""
DESCRIPTION 
    - Display the movies that closest match to what the user searched
@parameters
    data_results - the api list of the movies that closely relate to what the user searched up
"""
def displaySelectedMovies(data_results):
    for i in range(len(data_results)):
        print('{}. {}'.format(i, data_results[i]['title']))


"""
DESCRIPTION 
    - Given a series of movies the user must select from the list
@parameters
    data_results - the api list of the movies that closely relate to what the user searched up
@return
    - the movie dictionary that the user selected
"""
def selectMovie(data_results):
    displaySelectedMovies(data_results)
    x = inputSelectedMovie(data_results)
    print(x)
    if(x<0 or x>=len(data_results)):
        print("Please enter valid movie")
        displaySelectedMovies(data_results)
        x = inputSelectedMovie(data_results)
    return data_results[x]


"""
DESCRIPTION 
    - Have the user input movies and add to the list if they are valid
@parameters
@return
    - returns a list of dictionaries from the imdb api of the movies that the user is interested in
"""
def getMovieList():
    temp = []
   
    while(True):
        user_movie_name = input("Enter the name of the movie: ")
        if(not user_movie_name):
            break
        else:
            URL = "https://imdb-api.com/API/AdvancedSearch/k_z9p2w7dy"
            PARAMS = {'title':user_movie_name, 'title_type':'feature', 'release_date':',2021-01-01', 'languages':'en'}
            r = requests.get(url = URL, params = PARAMS)
            data = r.json()
            print(data)

            if(len(data['results'])>0):
                movie = selectMovie(data['results'])
                if(movie not in temp):
                    temp.append(movie)
            else:
                print("Input a valid movie name!")
    
    return temp

#main function of the getting the user movie list
def main():

    user_movie_list = getMovieList()
    #kalva.5: error will determine when a wrong movie is chosen and there is already more than one 
    #movie in the list
    print(user_movie_list)




if __name__ == "__main__":
    main()