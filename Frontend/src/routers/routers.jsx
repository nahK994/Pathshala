import * as React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import LanddingPage from '../views/landing-page/landing-page'
import TeacherRegistration from '../views/registration/teacher-registration';
import StudentRegistration from '../views/registration/student-registration';


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
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default RouterConfig