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
        Welcome to Shlok-AI! This website is designed to help you explore and understand Shlokas and Hindu scriptures.
        To get started, follow these steps:
      </p>
      <ol style={{ fontSize: '16px' }}>
        <li>Enter a Shloka or Hindu verse in the search bar above.</li>
        <li>Click the search button or press Enter to submit your query.</li>
        <li>Shlok-AI will process your request and provide the interpretation and insights related to your query.</li>
        <li>Explore the results and gain a deeper understanding of the spiritual and cultural significance of the Shlokas.</li>
      </ol>
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
