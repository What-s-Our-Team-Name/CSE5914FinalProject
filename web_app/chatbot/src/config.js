import { createChatBotMessage } from 'react-chatbot-kit';

const config = {
    initialMessages: [
        createChatBotMessage(`Welcome to the movie recommendation system!`),
        createChatBotMessage(`Do you want recommendations based on Movie Names or Genres?`)
    ],
};

export default config;