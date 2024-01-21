import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createStore } from 'redux';
import counter from './reducers'
import { createScanner } from 'typescript';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

const store = createStore(counter)

const render = () => root.render(
  <React.StrictMode>
    <App
      value = {store.getState() || 0}
      plus = {() => store.dispatch({type:'+'})}
      minus = {() => store.dispatch({type:'-'})}
    />
  </React.StrictMode>
);

render()

store.subscribe(render)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
