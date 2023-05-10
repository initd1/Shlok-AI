import '../App.css';
import React, { useState } from 'react';
import {InputGroup} from 'react-bootstrap';
import Textarea from 'rc-textarea';
import axios from 'axios';
import { LoadingOutlined, SearchOutlined, EditOutlined, EllipsisOutlined, SettingOutlined } from '@ant-design/icons';
import { Card, Switch, Divider, Button } from 'antd';

// import SearchBar from './SearchBar';
const { Meta } = Card;
function ShlokaForm() {
  const [prompt, setQuestion] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
 
  const onChange = (checked) => {  
    setLoading(!checked);
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/api/shloka-prompt', { prompt });
      setResult(response.data.result);
      console.log(response.data);
    }
    catch (error) {
      console.log(error);
    }
    finally {
      setLoading(false);
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
      <Divider />
      {/* While results are loading, display the loading card animation */}
      {loading &&
        <div>
        <Switch checked={!loading} onChange={onChange} />
          <Card 
            type="inner" 
            bordered={false}   
            style={{
              textAlign: 'center',
              marginTop: 16
            }}
            loading={loading}
          >        
          </Card>
        </div>
      }
      {/* Once results have loaded, display the results in the card in below */}
      {result && 
        <Card 
          bordered={true}  
          style={{
            textAlign: 'center',
            marginTop: 16
          }}
        >
          <Meta
            title={`Shlok-AI Responds to: "${prompt}"`}
            description={
              <p className='ai-response'>{result}</p>
              }
          />
        </Card>
      }
      <Divider />
    </div>
  );
}

export default ShlokaForm;
