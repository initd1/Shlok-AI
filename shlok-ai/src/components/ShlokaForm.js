import React, { useState } from 'react';
import axios from 'axios';

function ShlokaForm() {
  const [question, setQuestion] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('/api/shloka-prompt', { question });
    console.log(response.data);
  };

  return (
    <form onSubmit={handleSubmit}/>)
  }