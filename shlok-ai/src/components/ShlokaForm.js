import '../App.css';
import React, { useState } from 'react';
import { InputGroup } from 'react-bootstrap';
import Textarea from 'rc-textarea';
import axios from 'axios';
import { SearchOutlined } from '@ant-design/icons';
import { Card, Switch, Divider, Button, Alert } from 'antd';

const { Meta } = Card;

function ShlokaForm() {
  const [prompt, setQuestion] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const onChange = (checked) => {
    setLoading(!checked);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post('http://localhost:5001/api/shloka-prompt', { prompt });
      const { data } = response;
      console.log(response);
      setResult(data.Result); // Set the result directly

      if (data.Error) {
        setError(data.Error);
      }
    } catch (error) {
      console.log(error);
      setError('An error occurred. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  const renderCard = (title, content) => {
    return (
      <Card
        style={{
          color: '#e9c46a',
          textAlign: 'center',
          marginTop: 16,
        }}
        type="inner"
        title={<p className="ai-heading">{title}</p>}
      >
        <Meta description={<p className="ai-response">{content}</p>} />
      </Card>
    );
  };

  const renderShlokaCards = () => {
    const shlokaData = result ? JSON.parse(result) : null;
    const cards = [];

    for (const key in shlokaData) {
      if (shlokaData[key]) {
        cards.push(renderCard(key, shlokaData[key]));
      }
    }

    return cards;
  };

  return (
    <div className="text-center mt-5">
      <form onSubmit={handleSubmit}>
        <InputGroup className='search-bar-box'>
          <Textarea
            placeholder="Type/Paste any Shloka or Hindu verse to understand OR Ask any question about Indian culture, Hinduism, Vedic Scriptures or Sanatana Dharma."
            name="prompt"
            value={prompt}
            onChange={(e) => setQuestion(e.target.value)}
            autoSize
            rows={3}
            className="search-bar"
          />
          <Button className="btn btn-primary shloka-submit-button" variant="primary" type="submit" onClick={handleSubmit}>
            <SearchOutlined />
          </Button>
        </InputGroup>
      </form>
      <Divider />
      {loading && (
        <div>
          <Switch checked={!loading} onChange={onChange} />
          <Card type="inner" bordered={false} style={{ textAlign: 'center', marginTop: 16 }} loading={loading}></Card>
        </div>
      )}
      {error && <Alert message={error} type="error" />}
      {result && renderShlokaCards()}
      <Divider />
    </div>
  );
}

export default ShlokaForm;
