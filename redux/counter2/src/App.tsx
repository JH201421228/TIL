import React from 'react';
import logo from './logo.svg';
import './App.css';

type Props = {
  value: number
  plus: () => void
  minus: () => void
}

function App({value, plus, minus}: Props) {
  return (
    <div className='App'>
      Clicked: {value} times
      <button onClick={plus}>+</button>
      <button onClick={minus}>-</button>
    </div>
  );
}

export default App;
