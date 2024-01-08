import React from 'react'
import './App.css'
import { Routes, Route } from 'react-router-dom'
import ChatPage from './pages/ChatPage/ChatPage'
import LoginPage from './pages/LoginPage/LoginPage'
import RegisterPage from './pages/RegisterPage/RegisterPage'

function App() {


  return (
    <Routes>
      <Route path='/' element={<ChatPage/>} />
      <Route path='/login' element={<LoginPage/>} />
      <Route path='/register' element={<RegisterPage/>} />
    </Routes>
    )
}

export default App
