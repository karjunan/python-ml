// src/components/Input.jsx

import React, { useState } from 'react';
import './Input.css'; // Import the CSS file for styling

const Input = ({ onSendMessage }) => {
  const [text, setText] = useState('');

  const handleInputChange = (e) => {
    setText(e.target.value);
  };

  const handleSendClick = () => {
    onSendMessage(text);
    setText('');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSendClick();
    }
  };

  return (
    <div className="input-container">
      <input
        type="text"
        value={text}
        onChange={handleInputChange}
        onKeyPress={handleKeyPress}
        placeholder="Type a message..."
        className="input-field"
      />
      <button onClick={handleSendClick} className="send-button">
        Send
      </button>
    </div>
  );
};

export default Input;
