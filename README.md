# CSE5914FinalProject

1. Get a list from the client
    - Ask the user for the name of the first movie and check if it's validity(Need at least one valid movie)
    - Continue asking for more movies if the client chooses to share

    #TODO - Figure out how to warn the client of an unvalid input.
        - How to stop asking for movies
        - Send the user_movie_list to the algorithm
        - Clean up and comment


2. Use Cosine Similarity
    - Compare the movies chosen by the client and the movies from the database and find the cosine similarity.
    - When given a list from the user we might have to create a vector from the average or the sum of the cosine similariy for each of the movies.
    - https://towardsdatascience.com/the-4-recommendation-engines-that-can-predict-your-movie-tastes-109dc4e10c52
    - Get the Top 20 for each movie

3. Create the Final List of 20 movies
    - From the list of 20 for each of movies find the most similar 20 and return that to the command line.

