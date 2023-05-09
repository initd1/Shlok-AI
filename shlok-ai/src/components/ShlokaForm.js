import '../App.css';
import React, { useState } from 'react';
import {InputGroup, Button } from 'react-bootstrap';
import Textarea from 'rc-textarea';
import axios from 'axios';
import { SearchOutlined, EditOutlined, EllipsisOutlined, SettingOutlined } from '@ant-design/icons';
import { Avatar, Card, Skeleton, Switch, Divider } from 'antd';

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
      <Divider />

      {/* <Card type="inner" title="Results" bordered={false}> */}
    <>
      <Switch checked={!loading} onChange={onChange} />
      <Card type="inner" title="Query Results" bordered={false}
        style={{
          textAlign: 'center',
          width: 650,
          marginTop: 16,
        }}
        loading={loading}
      >
        <Meta
          avatar={<Avatar src="veda-vyasa-logo.webp" />}
          title="Query Results"
          description={result}
        />
      </Card>
      {/* {result && (
        <div>
          <p>{result}</p>
        </div>
      )} */}
      <Card
        style={{
          width: 300,
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
            title="Card title"
            description="This is the description"
          />
        </Skeleton>
      </Card>
    </>
    </div>
  );
}

export default ShlokaForm;
