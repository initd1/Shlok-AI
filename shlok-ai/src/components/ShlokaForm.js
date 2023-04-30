import React, { useState } from 'react';
import {InputGroup, FormControl, Button} from 'react-bootstrap';
import axios from 'axios';
import SearchBar from './SearchBar';

function ShlokaForm() {
  const [question, setQuestion] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('/api/shloka-prompt', { question });
    console.log(response.data);
  };

  return (
    <div className="d-flex justify-content-center mt-5">
      <InputGroup style={{ width: "50%" }}>
        <FormControl 
          placeholder="Ask a question"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <Button variant="primary" type="submit" onClick={handleSubmit}>
          Submit
        </Button>
      </InputGroup>
    </div>
  );
}

export default ShlokaForm;
