import Navbar from './components/Navbar/Navbar';
import Dashboard from './pages/Dashboard/Dashboard';
import {Routes, Route} from 'react-router-dom';

function App() {
  return (
    <>
      <Navbar/>
      <Routes>
        <Route path='/' element={<Dashboard/>}/>
      </Routes>
    </>
  );
}

export default App;
