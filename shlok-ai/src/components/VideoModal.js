import React from 'react';
import { Modal } from 'antd';

const VideoModal = ({ isOpen, closeModal }) => {
  return (
    <Modal
      visible={isOpen}
      onCancel={closeModal}
      footer={null}
      destroyOnClose
      centered
      width="90%"
      bodyStyle={{
        padding: '20px',
      }}
    >
      <p style={{ fontSize: '18px', marginBottom: '20px' }}>
        Shlok-AI: Experience the richness of the Indian civilization and ancient Vedic literature with AI-powered insights.
        Presenting Shlok-AI, a ready to use interface to understand the essence of the culture of Bharat/India.
      </p>
      <ol style={{ fontSize: '18px' }}>
        <li>Would you love to know more about the Indian heritage and it's cultures?</li>
        <li>Have you ever wondered what the different Sanskrit Shlokas actually mean?</li>
        <li>Have you ever been curious to unlock the timeless teachings of Sanatana Dharma, the eternal way of life for all Hindus?</li>
      </ol>
      <p style={{ fontSize: '18px', marginBottom: '20px' }}>
          Enter a Shloka or Hindu verse in the search bar.
      </p>
      <p style={{ fontSize: '18px', marginBottom: '20px' }}>OR</p>
      <p style={{ fontSize: '18px', marginBottom: '20px' }}>                  
          Ask any question related to Indian Civilization and Culture, Yoga, Hinduism, Vedic Scriptures, Sanatana Dharma etc.
      </p>
      <div style={{ position: 'relative', paddingTop: '56.25%', width: '100%' }}>
        <iframe
          title='Shlok-AI Introduction'
          src='https://www.youtube.com/embed/U2lNVSMqiAA'
          frameBorder='0'
          allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture'
          allowFullScreen
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
          }}
        />
      </div>
    </Modal>
  );
};

export default VideoModal;
