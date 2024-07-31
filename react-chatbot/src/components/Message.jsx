// src/components/Message.jsx

import React from 'react';
import './Message.css'; // Import the CSS file for styling

const Message = ({ text, sender }) => {
  const isUser = sender === 'user';

  return (
    <div className={`message ${isUser ? 'user' : 'bot'}`}>
      {text}
    </div>
  );
};

export default Message;
