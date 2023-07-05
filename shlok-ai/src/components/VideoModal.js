import React from 'react';
import { Modal } from 'antd';

const VideoModal = ({ isOpen, closeModal }) => {
  return (
    <Modal
      open={isOpen}
      onCancel={closeModal}
      footer={null}
      destroyOnClose
      centered
      width="80%"
    >
    <iframe src='https://www.youtube.com/embed/U2lNVSMqiAA'
        title='Shlok-AI Introduction'
        width="560"
        height="750"
        
        // frameBorder='0'
        // allow="accelerometer; autoplay; encrypted-media;"
        allowFullScreen
        
    />
    </Modal>
  );
};

export default VideoModal;
