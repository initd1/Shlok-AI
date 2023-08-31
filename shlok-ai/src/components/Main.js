import { LaptopOutlined, NotificationOutlined, UserOutlined } from '@ant-design/icons';
import { Layout, Menu, Space, theme } from 'antd';
import React, { useState, useEffect } from 'react';
import ShlokaForm from './ShlokaForm';
import '../App.css';
import { Typography } from 'antd';
import VideoModal from './VideoModal';

const { Header, Content, Sider, Footer } = Layout;
const items1 = ['1', '2'].map((key) => ({
  key,
  label: `Menu ${key}`,
}));
const items2 = [UserOutlined, LaptopOutlined, NotificationOutlined].map((icon, index) => {
  const key = String(index + 1);
  return {
    key: `sub${key}`,
    icon: React.createElement(icon),
    label: `Menu ${key}`,
    children: new Array(2).fill(null).map((_, j) => {
      const subKey = index * 2 + j + 1;
      return {
        key: subKey,
        label: `option${subKey}`,
      };
    }),
  };
});

const MainLayout = () => {
  const [videoModalOpen, setVideoModalOpen] = useState(true);
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  useEffect(() => {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.ready.then(registration => {
        registration.unregister();
      });
    }
  }, []);

  return (
    <Layout>
      <Layout>
        {videoModalOpen && (
          <VideoModal isOpen={videoModalOpen} closeModal={() => setVideoModalOpen(false)} />
        )}
        <Layout
          style={{
            padding: '1px 15px 24px',
          }}
        >
          <Content
            className="site-layout-background"
            style={{
              padding: 24,
              margin: 0,
              minHeight: 1100,
            }}
          >
            <Typography className="text-center mt-5">
              <Space>
                <p className='heading'><i>Shlok-AI</i></p>
              </Space>
            </Typography>
            <ShlokaForm />
          </Content>
        </Layout>
      </Layout>
      <Footer style={{ textAlign: 'right' }}>
        <p class="footer-style">
          Shlok-AI ©2023 Made with <img src="heart.svg" alt="heart" width="20" height="20" />
          &nbsp;for&nbsp;
          <img src="india-flag.svg" alt="India" width="30" height="30" />
        </p>
      </Footer>
    </Layout>
  );
};

export default MainLayout;