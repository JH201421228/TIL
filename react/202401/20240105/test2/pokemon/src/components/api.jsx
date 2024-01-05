// api.jsx

import axios from "axios";

const API_URL = "https://pokeapi.co/api/v2/pokemon?limit=151";

export const getPokemonData = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data.results;
  } catch (error) {
    console.error("Error fetching Pokemon data:", error);
  }
};
