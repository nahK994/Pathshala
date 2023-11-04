import * as React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import LanddingPage from '../views/landing-page/landing-page'
import TeacherRegistration from '../views/registration/teacher-registration';
import StudentRegistration from '../views/registration/student-registration';
import PageNotFound from '../views/404/404';


function RouterConfig() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' Component={LanddingPage} />
          <Route path='/registration'>
            <Route path='teacher' Component={TeacherRegistration}></Route>
            <Route path='student' Component={StudentRegistration}></Route>
          </Route>
          <Route path='*' Component={PageNotFound} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default RouterConfig