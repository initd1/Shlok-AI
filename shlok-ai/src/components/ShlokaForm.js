import '../App.css';
import React, { useState } from 'react';
import {InputGroup} from 'react-bootstrap';
import Textarea from 'rc-textarea';
import axios from 'axios';
import { LoadingOutlined, SearchOutlined, EditOutlined, EllipsisOutlined, SettingOutlined } from '@ant-design/icons';
import { Avatar, Card, Skeleton, Switch, Divider, Button } from 'antd';

// import SearchBar from './SearchBar';
const { Meta } = Card;
function ShlokaForm() {
  const [prompt, setQuestion] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(true);
 
  const onChange = (checked) => {
    setLoading(!checked);
  };
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
      {loading && <div><LoadingOutlined />Loading</div>}
      {result && 
        <Card 
          type="inner" 
          title="Shlok-AI Responds ..." 
          bordered={false}
          // description={result}        
          style={{
            textAlign: 'center',
            marginTop: 16
          }}
          // loading={loading}
        >
          <Meta
            // avatar={<Avatar src="https://xsgames.co/randomusers/avatar.php?g=pixel&key=1" />}
            // title="Shlok-AI Responds ..."
            description={result}
          />
        </Card>}
      <Divider />
    <>
    <Switch checked={!loading} onChange={onChange} />
      <Card 
        type="inner" 
        title="Shlok-AI Responds ..." 
        bordered={false}
        // description={result}        
        style={{
          textAlign: 'center',
          marginTop: 16
        }}
        loading={loading}
      >
        <Meta
          // avatar={<Avatar src="https://xsgames.co/randomusers/avatar.php?g=pixel&key=1" />}
          // title="Shlok-AI Responds ..."
          description={result}
        />
      </Card>
      {/* <Card
        style={{
          width: 650,
          marginTop: 16,
        }}
        actions={[
          <SettingOutlined key="setting" />,
          <EditOutlined key="edit" />,
          <EllipsisOutlined key="ellipsis" />,
        ]}
      >
        <Skeleton loading={loading} avatar active>
          <Meta
            avatar={<Avatar src="https://xsgames.co/randomusers/avatar.php?g=pixel&key=2" />}
            title="Shlok-AI Responds ..."
            description={result}
          />
        </Skeleton>
      </Card> */}
    </>
    </div>
  );
}

export default ShlokaForm;
