import { Route, Routes } from 'react-router-dom'
import './App.css'
import Test from './test_page'
import Main from './main_page'

function App() {

  return (
    <>
      <Routes>
        <Route path='/test' element={<Test />} />
        <Route path='/' element={<Main />} />
      </Routes>
    </>
  )
}

export default App
