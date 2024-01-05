// index.jsx

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import PokemonList from "./components/PokemonList";

ReactDOM.render(
  <React.StrictMode>
    < PokemonList/>
  </React.StrictMode>,
  document.getElementById("root")
);
