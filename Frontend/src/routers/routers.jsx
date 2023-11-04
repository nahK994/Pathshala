import * as React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import LanddingPage from '../views/landing-page/landing-page'


function RouterConfig() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' Component={LanddingPage} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default RouterConfig