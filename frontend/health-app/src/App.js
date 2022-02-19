import Dashboard from './pages/Dashboard/Dashboard';
import {Routes, Route} from 'react-router-dom';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Dashboard/>}/>
      </Routes>
    </>
  );
}

export default App;
