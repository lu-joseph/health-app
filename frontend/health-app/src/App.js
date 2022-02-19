import Dashboard from './pages/Dashboard/Dashboard';
import {Routes, Route} from 'react-router-dom';
import Hero from './pages/Hero/Hero';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Hero/>}/>
      </Routes>
    </>
  );
}

export default App;
