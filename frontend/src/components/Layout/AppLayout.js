import React from "react";
import { Input, Menu } from "antd";
import LogoImage from "assets/logo.png";
import "./AppLayout.scss";
import { Link } from "react-router-dom";
function AppLayout({ children, sidebar, username }) {
  return (
    <>
      <div className="wrapper">
        <div className="header">
          <h1 className="header__logo">
            <Link to="/" >
              <img src={LogoImage} alt="logo" />
            </Link>
          </h1>
          <Input.Search
            placeholder="input search text"
            onSearch={(value) => console.log(value)}
            style={{ width: 200 }}
          />
          <Menu mode="horizontal">
            <Menu.Item><Link to="profile-edit">내정보</Link></Menu.Item>
            <Menu.Item>탐색</Menu.Item>
            <Menu.Item><Link to={`${username}`}>프로필</Link></Menu.Item>
          </Menu>
        </div>
        <div className="container">{children}</div>
        <div className="sidebar">{sidebar}</div>
        <div className="footer">&copy; 2020 reactstagram.pilyeooong</div>
      </div>
    </>
  );
}

export default AppLayout;
