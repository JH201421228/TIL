import React from 'react';
import logo from './logo.svg';
import './App.css';

type Props = {
  num: any
  plus: () => void
  minus: () => void
}

function App({num, plus, minus}: Props) {
  return (
    <div className='App'>
      Clicked: {num} times
      <button onClick={plus}>+</button>
      <button onClick={minus}>-</button>
    </div>
  );
}

export default App;
