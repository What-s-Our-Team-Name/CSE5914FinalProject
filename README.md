# CSE5914FinalProject

# Get Started (⚠️ Note the steps should be performed on Ubuntu Server)
## To install environment
- `cd /root/CSE5914FinalProject`
- `. setup.sh`

## To deploy backend server
- `cd /root/CSE-Final-Proj/server`
- `. deploy.sh`

## After deployment, the web app should be accessible on `xxx:8080`, i.e., http://164.92.78.243:8080/


# Description
1. (COMPLETE) Get a list from the client
    - Ask the user for the name of the first movie and check if it's validity(Need at least one valid movie)
    - Continue asking for more movies if the client chooses to share


2. Use Cosine Similarity
    - Compare the movies chosen by the client and the movies from the database and find the cosine similarity.
    - When given a list from the user we might have to create a vector from the average or the sum of the cosine similariy for each of the movies.
    - https://towardsdatascience.com/the-4-recommendation-engines-that-can-predict-your-movie-tastes-109dc4e10c52
    - Get the Top 20 for each movie

    #TODO - inputs: Title, Genre, Title Group(Awards), Ratings, Years, RunTime

3. Create the Final List of 20 movies
    - From the list of 20 for each of movies find the most similar 20 and return that to the command line.

4. Connecting the RASA chatbot to the python files:
    - chatbot must ask for a movie.
    - make sure that the chatbot chooses the correct movie
    - have the chatbot ask for multiple movies if needed
    - have the chatbot use the cosine similarity to recommend movies
    - display the movies
    - (optional) user can select the movie and see where they can watch the movie

5. FIXME Fix AccurateSearch

6. TODO Web App:
    index.html:
        - Navigational Panel
        - Services
        - Product
        - Advanced Stats
        - Footer
    index.css:
        - Clean up the stylesheet and make sure the page looks as good as possible at the end.