// src/components/Chatbot.jsx

import React, { useState } from 'react';
import ChatWindow from './ChatWindow';
import Input from './Input';

const Chatbot = () => {
  const [messages, setMessages] = useState([
    { text: 'Hello! How can I help you today?', sender: 'bot' },
  ]);

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const handleSendMessage = (text) => {
    if (!text) return;

    const userMessage = { text, sender: 'user' };
    // setMessages((prevMessages) => [...prevMessages, userMessage]);

    // Simulate a bot response
    // setTimeout(() => {
    //   // const botResponse = { text: `You said: "${text}"`, sender: 'bot' };
    //   const botResponse  = http://localhost:5000/messages?str=whats happening with Alice;
    //   setMessages((prevMessages) => [...prevMessages, botResponse]);
    // }, 1000);

      fetch(`http://localhost:5000/messages?str=${text}`)
        .then(response => {
          console.log(text)
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          console.log(data);
          setMessages((prevMessages) => [...prevMessages, { text: data, sender: 'bot' }]);
          // setMessages( { text: data, sender: 'bot' });
          // setData(data);
          
        })
        .catch(error => {
          setError(error);
          setLoading(false);
        });
  };

 
  return (
    <div className="chatbot-container">
      <ChatWindow messages={messages} />
      <Input onSendMessage={handleSendMessage} />
    </div>
  );
};

export default Chatbot;
