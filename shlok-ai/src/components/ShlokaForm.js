import React, { useState } from 'react';
import {InputGroup, FormControl, Button} from 'react-bootstrap';
import axios from 'axios';
import SearchBar from './SearchBar';
import '../App.css';

function ShlokaForm() {
  const [prompt, setQuestion] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('/api/shloka-prompt', { prompt });
    console.log(response.data);
  };

  return (
    <div className="d-flex justify-content-center mt-5">
      <form onSubmit={handleSubmit}>
        <InputGroup className="shloka-input-group">
          <FormControl 
            className="search-bar"
            placeholder="Ask a question"
            value={prompt}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <Button 
            className="shloka-submit-button" 
            variant="primary"
            type="submit" 
            onClick={handleSubmit}
          > 
            Submit
          </Button>
        </InputGroup>
      </form>
    </div>
  );
}

export default ShlokaForm;
