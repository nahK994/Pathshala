import * as React from 'react';
import RouterConfig from './routers/routers';
import NavBar from './shared/components/nav-bar/nav-bar';

function App() {
  return (
    <NavBar content={<RouterConfig />} />
  );
}

export default App