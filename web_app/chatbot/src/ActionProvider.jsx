import React from 'react';

import { queryIMDB, addMovie, clearMovies, queryDatabase, queryGenre } from './utils/request_handler';
import { CHAT_STATE, RECOMMENDATION_TYPE, GENRES } from './constants/constants';
import { useState } from 'react';
import { useEffect } from 'react';
import { useCallback } from 'react';

const ActionProvider = ({
    createChatBotMessage,
    setState,
    children 
}) => {
    const [recommendationType, setRecommendationType] = useState(RECOMMENDATION_TYPE.MOVIE_NAME);
    const [chatState, setChatState] = useState(CHAT_STATE.STARTING);
    const [currentMovieList, setCurrentMovieList] = useState([]);

    const handleMessage = (message) => {
        if (chatState === CHAT_STATE.FINISHED) {
            return;
        }
        if (message === 'exit' || message === 'Exit') {
            setChatState(CHAT_STATE.FINISHED);
            return;
        } else if (message === 'e') {
            setChatState(CHAT_STATE.FINISHED_INPUT_MOVIE_NAME);
        } else if (chatState === CHAT_STATE.WAITING_FOR_RECOMMENDATION_TYPE) {
            handleRecommendationType(message);
        } else if (chatState === CHAT_STATE.WAITING_FOR_MOVIE_NAME) {
            handleMovieNameQuery(message);
        } else if (chatState === CHAT_STATE.WAITING_FOR_SELECTION) {
            handleMovieSelection(message);
        } else if (chatState === CHAT_STATE.WAITING_FOR_GENRE) {
            handleGenre(message);
        }
    };

    const addMessage = useCallback((botMessage) => {
        setState((prev) => ({
            ...prev,
            messages: [...prev.messages, createChatBotMessage(botMessage)],
            }));
    }, [createChatBotMessage, setState]);

    const handleQueryDatabase = useCallback(async() => {
        if (recommendationType === RECOMMENDATION_TYPE.GENRE) {
            return;
        }
        try {
            const results = await queryDatabase();
            const movies = Object.values(results);
            if (movies.length === 0) {
                addMessage('You have not put any movie yet.')
            } else {
                addMessage('Here is the Top 15 most similar movies:');
                addMessage(movies.join('\n'));
                await clearMovies();
            }
            setChatState(CHAT_STATE.WAITING_FOR_RECOMMENDATION_TYPE);
        } catch (error) {
            addMessage('Something went wrong. Please try again later.')
            console.log(error);
        }
    }, [addMessage, recommendationType]);

    const handleExit = useCallback(() => {
        addMessage('Goodbye!');
        setChatState(CHAT_STATE.FINISHED);
    }, [addMessage]);

    useEffect(() => {
        setChatState(CHAT_STATE.WAITING_FOR_RECOMMENDATION_TYPE);
    }, []);

    useEffect(() => {
        if (chatState === CHAT_STATE.WAITING_FOR_RECOMMENDATION_TYPE) {
            addMessage(`Do you want recommendations based on Movie Names or Genres or Exit?`);
        } else if (chatState === CHAT_STATE.WAITING_FOR_MOVIE_NAME) {
            addMessage('Enter the name of the movie or enter e to stop:');
        } else if (chatState === CHAT_STATE.WAITING_FOR_GENRE) {
            addMessage('Here is a list of all genres, please choose one from it:');
            addMessage(`${GENRES.join('\n')}`);
        } else if (chatState === CHAT_STATE.FINISHED_INPUT_MOVIE_NAME) {
            handleQueryDatabase();
        }
        else if (chatState === CHAT_STATE.FINISHED) {
            handleExit();
        }
    }, [chatState, addMessage, handleQueryDatabase, handleExit]);

    const handleRecommendationType = (message) => {
        message = message.toLowerCase();
        if (message === 'movie name' || message === 'movie names') {
            setRecommendationType(RECOMMENDATION_TYPE.MOVIE_NAME);
            setChatState(CHAT_STATE.WAITING_FOR_MOVIE_NAME);
        } else if (message === 'genre' || message === 'genres') {
            setRecommendationType(RECOMMENDATION_TYPE.GENRE);
            setChatState(CHAT_STATE.WAITING_FOR_GENRE);
        } else {
            addMessage('Sorry I don\'t understand');
        }
    };

    const handleMovieNameQuery = async (movieName) => {
        try {
            // Query for movie info
            addMessage('One second! Loading movie information...');
            const movieList = await queryIMDB(movieName);

            if (movieList.length === 0) {
                addMessage('Not movie found! Please input a valid movie name.');
                return;
            }

            // Display movie list
            for (let i = 0; i < movieList.length; i++) {
                const movie = movieList[i];
                const title = `${i}. ${movie.title} ${movie.description}`
                if (!!movie.plot) {
                    addMessage(title + '\n' + movie.plot);
                } else {
                    addMessage(`${title}`);
                }
            }

            // Ask the user to select one
            setChatState(CHAT_STATE.WAITING_FOR_SELECTION);
            setCurrentMovieList(movieList);
            addMessage(`Enter the selected movie (0-${movieList.length - 1}):`);
        } catch (error) {
            addMessage('Something went wrong. Please try again later.')
            console.log(error);
        }
    };

    const handleMovieSelection = async (movieIndex) => {
        try {
            // Add movie to saved movie list
            const index = parseInt(movieIndex);
            if (isNaN(index) || index < 0 || index >= currentMovieList.length) {
                addMessage('Please put a valid number');
                return;
            }
            console.log(`[handleMovieSelection] Adding movie id ${currentMovieList[index].id}`)
            await addMovie(currentMovieList[index].id);
            setChatState(CHAT_STATE.WAITING_FOR_MOVIE_NAME);
            setCurrentMovieList([]);
        } catch (error) {
            addMessage('Something went wrong. Please try again.')
            console.log(error);
        }
    };

    const handleGenre = async(genre) => {
        if (!GENRES.includes(genre)) {
            addMessage('Invalid genre, please try again.');
            return;
        }
        try {
            const results = await queryGenre(genre);
            const movies = Object.values(results);
            addMessage(`Here is the Top ${movies.length} most popular movies in your genre:`);
            addMessage(movies.join('\n'));
            setChatState(CHAT_STATE.WAITING_FOR_RECOMMENDATION_TYPE);
            setRecommendationType(RECOMMENDATION_TYPE.MOVIE_NAME);
        } catch (error) {
            addMessage('Something went wrong. Please try again later.')
            console.log(error);
        }
    };


    return (
        <div>
        {React.Children.map(children, (child) => {
            return React.cloneElement(child, {
            actions: {
                handleMessage,
                handleRecommendationType,
            },
            });
        })}
        </div>
    );
};

export default ActionProvider;