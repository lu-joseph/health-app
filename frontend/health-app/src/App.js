import Dashboard from './pages/Dashboard/Dashboard';
import {Routes, Route} from 'react-router-dom';
import Hero from './pages/Hero/Hero';
import Sleep from './pages/Sleep/Sleep';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Hero/>}/>
        <Route path='/form/sleep' element={<Sleep/>}/>
      </Routes>
    </>
  );
}

export default App;
