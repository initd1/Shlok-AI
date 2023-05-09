import React, { useState } from 'react';
import {InputGroup, Button} from 'react-bootstrap';
import Textarea from 'rc-textarea';
import axios from 'axios';
// import SearchBar from './SearchBar';
import '../App.css';

function ShlokaForm() {
  const [prompt, setQuestion] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('/api/shloka-prompt', { prompt });
    console.log(response.data);
  };

  return (
    <div className="text-center mt-5">
      <form onSubmit={handleSubmit}>
        <InputGroup className="shloka-search-bar">
          <Textarea 
            placeholder="Ask a question"
            value={prompt}
            onChange={(e) => setQuestion(e.target.value)}
            autoSize
            rows={3}
            className="search-bar"
          />
          <Button 
            className="btn btn-primary shloka-submit-button" 
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
