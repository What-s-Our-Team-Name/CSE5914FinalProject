import axios from "axios";
import configData from "../config/config.json";

export const addMovie = async (movieId) => {
  const form = new FormData();
  form.append('selected_movie', movieId);
  const response = await axios.post(configData.SERVER_URL + configData.ROUTES.ADD_MOVIE, form); // send http request toward server
  return response.data;
};

export const clearMovies = async () => {
  await axios.post(configData.SERVER_URL + configData.ROUTES.CLEAR);
};

export const queryIMDB = async (movieName) => {
  const headers = {'params': {'movie_name': movieName}};
  const response = await axios.get(configData.SERVER_URL + configData.ROUTES.IMDB, headers); // send http request toward server
  return response.data;
};

export const queryDatabase = async () => {
  const response = await axios.get(configData.SERVER_URL + configData.ROUTES.DATABASE); // send http request toward server
  return response.data
};

export const queryGenre = async (genre) => {
  const headers = {'params': {'genre': genre}}
  const response = await axios.get(configData.SERVER_URL + configData.ROUTES.GENRE, headers); // send http request toward server
  return response.data
}
