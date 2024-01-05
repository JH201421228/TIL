// PokemonList.jsx

import React, { useEffect, useState } from "react";
import Pokemon from "./Pokemon";
import { getPokemonData } from "./api";
import styled from "styled-components";

const Wrapper = styled.div`
  padding: 16px;
  width: calc(100% - 32px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`

const PokemonList = () => {
  const [pokemonData, setPokemonData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getPokemonData();
      setPokemonData(data);
    };
    fetchData();
  }, []);

  return (
    <Wrapper>
      <h1>Pokemon 1st Generation</h1>
      {pokemonData.map((pokemon, index) => (
        <Pokemon
          key={index + 1}
          id={index + 1}
          name={pokemon.name}
          type="Unknown" // You may need to fetch the type from the Pokemon API
          imageUrl={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${index + 1}.png`}
          description="Description not available" // You may need to fetch the description from the Pokemon API
        />
      ))}
    </Wrapper>
  );
};

export default PokemonList;
