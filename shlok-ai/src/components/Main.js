import { LaptopOutlined, NotificationOutlined, UserOutlined } from '@ant-design/icons';
import { Layout, Menu, Space, theme } from 'antd';
import React from 'react';
import ShlokaForm from './ShlokaForm';
import '../App.css';
import {Typography} from 'antd';

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
    label: `subnav ${key}`,
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
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  return (
    <Layout>
      <Header className="header">
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']} items={items1} />
      </Header>
      <Layout>
        <Sider
          width={150}
          style={{
            background: colorBgContainer,
          }}
        >
          <Menu
            mode="inline"
            defaultSelectedKeys={['1']}
            defaultOpenKeys={['sub1']}
            style={{
              height: '100%',
              borderRight: 0,
            }}
            items={items2}
          />
        </Sider>
        <Layout
          style={{
            padding: '15px 15px 24px',
          }}
        >         
          <Content
            style={{
              padding: 24,
              margin: 0,
              minHeight: 1200,
              // backgroundImage: "url('background.jpg')",
              // backgroundSize: 'cover',
              // backgroundRepeat: 'no-repeat',
              // backgroundPosition: 'center',

            }}
          >
            <Typography className="text-center mt-5">
              <Space>
                <h1><b><i>Shlok-AI</i></b></h1>
              </Space>
            </Typography>

            <ShlokaForm />
          </Content>
          {/* <Content
            style={{
              padding: 24,
              margin: 20,
              minHeight: 500,
              background: colorBgContainer,
            }}
          >
            <ShlokaForm />
          </Content> */}
        </Layout>
      </Layout>
        <Footer style={{ textAlign: 'right' }}>
          <p class="footer-style">
            Shlok-AI ©2023 Made with <img src="heart.svg" alt="heart" width="20" height="20"/> 
              &nbsp;for&nbsp;
            <img src="india-flag.svg" alt="India" width="30" height="30" />
          </p>
        </Footer>
    </Layout>
  );
};
export default MainLayout;