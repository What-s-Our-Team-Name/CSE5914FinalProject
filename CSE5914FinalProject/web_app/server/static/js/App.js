import React from "react";
import "./App.css";

import Chatbot from "react-chatbot-kit";

import config from "./components/chatbot/config";
import ActionProvider from "./components/chatbot/ActionProvider";
import MessageParser from "./components/chatbot/MessageParser";


function App() {
  return (
    <div className="App">
      <div style={{ maxWidth: "300px" }}>
        <Chatbot
          config={config}
          actionProvider={ActionProvider}
          messageParser={MessageParser}
        />
      </div>
    </div>
  );
}

export default App;
