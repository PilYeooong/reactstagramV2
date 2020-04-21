import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import { AppProvider } from "stores/store";
import "antd/dist/antd.css"
import Root from "pages";

ReactDOM.render(
  <BrowserRouter>
    <AppProvider>
        <Root />
    </AppProvider>
  </BrowserRouter>,
  document.getElementById('root')
);