import { FC, ComponentProps, lazy, Suspense } from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';
import { Box, Text } from '@chakra-ui/react';

import { Layout } from '../layout';

import { ROUTES } from './router-constants';

// eslint-disable-next-line react/display-name
const Loader = (Component: FC) => (props: ComponentProps<typeof Component>) => (
  <Suspense
    fallback={
      <Box
        style={{
          position: 'fixed',
          left: 0,
          top: 0,
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Text>Loading...</Text>
      </Box>
    }
  >
    <Component {...props} />
  </Suspense>
);

const LandingPage = Loader(lazy(() => import('../pages/landing-page')));

export const RouterConfig: FC = () => {
  const location = useLocation();

  const background =
    location.state && (location.state.background as typeof location);
  return (
    <Routes location={background || location}>
      <Route element={<Layout />}>
        <Route index path={ROUTES.LANDING_PAGE} element={<LandingPage />} />
      </Route>
    </Routes>
  );
};
