// src/components/ChatWindow.jsx

import React from 'react';
import Message from './Message';
import './ChatWindow.css'; // Import the CSS file for styling

const ChatWindow = ({ messages }) => {
  return (
    <div className="chat-window">
      {messages.map((msg, index) => (
        <Message key={index} text={msg.text} sender={msg.sender} />
      ))}
    </div>
  );
};

export default ChatWindow;
