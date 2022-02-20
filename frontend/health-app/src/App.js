import Dashboard from './pages/Dashboard/Dashboard';
import {Routes, Route} from 'react-router-dom';
import Hero from './pages/Hero/Hero';
import Sleep from './pages/Sleep/Sleep';
import Mood from './pages/Mood/Mood';
import Physical from './pages/Physical/Physical';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Hero/>}/>
        <Route path='/form/physical' element={<Physical/>}/>
        <Route path='/dashboard' element={<Dashboard/>}/>
        <Route path='/form/sleep' element={<Sleep/>}/>
        <Route path='/form/mood' element={<Mood/>}/>
      </Routes>
    </>
  );
}

export default App;
