import React from 'react';
import { CHAT_STATE } from './constants/constants';


const MessageParser = (props) => {

  const {
    children,
    actions,
  } = props


  const parse = (message) => {
    actions.handleMessage(message);
  };


  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          parse: parse,
          actions: {},
        });
      })}
    </div>
  );
};

export default MessageParser;