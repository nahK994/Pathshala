import { Box } from '@chakra-ui/react';
import { Outlet } from 'react-router-dom';

export const Layout = () => {
  return (
    <Box
      style={{
        width: '100%',
        minHeight: '100vh',
        height: 'auto',
        overflowY: 'scroll',
      }}
    >
      <Outlet />
    </Box>
  );
};

export default Layout;
