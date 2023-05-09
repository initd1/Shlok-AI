import React, { useState } from 'react';
import {InputGroup, Button} from 'react-bootstrap';
import Textarea from 'rc-textarea';
import axios from 'axios';
import { SearchOutlined } from '@ant-design/icons';
// import SearchBar from './SearchBar';
import '../App.css';

function ShlokaForm() {
  const [prompt, setQuestion] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/shloka-prompt', { prompt });
      setResult(response.data.result);
      console.log(response.data);
    }
    catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="text-center mt-5">
      <form onSubmit={handleSubmit}>
        <InputGroup>
          <Textarea
            placeholder="Ask a question"
            name="prompt"
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
            <SearchOutlined />
          </Button>
        </InputGroup>
      </form>
      
      {result && (
        <div>
          <h2>Result</h2>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default ShlokaForm;
