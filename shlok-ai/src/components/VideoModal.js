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
      <video controls style={{ width: '100%' }}>
        <source src="../public/shlok-ai-edited.mp4" type="video/mp4" />
      </video>
    </Modal>
  );
};

export default VideoModal;
