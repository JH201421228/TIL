import React from "react";
import styled from "styled-components";
import { BrowserRouter, Route, Routes, useNavigate } from "react-router-dom";

import NextPage from "./page/NextPage";
import MainPage from "./page/MainPage";

function App(props){

  return(
    <BrowserRouter>
      <Routes>
        <Route index element={<MainPage/>}/>
        <Route path="next-page" element={<NextPage/>}/>    
        <Route path="main-page" element={<MainPage/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App;