import { BrowserRouter } from 'react-router-dom';
import { ChakraProvider } from '@chakra-ui/react';
import { RouterConfig } from './navigation';

function App() {
  return (
    <BrowserRouter>
      <ChakraProvider>
        <RouterConfig />
      </ChakraProvider>
    </BrowserRouter>
  );
}

export default App;
