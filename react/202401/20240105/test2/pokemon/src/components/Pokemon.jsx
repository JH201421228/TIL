// Pokemon.jsx

import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  padding: 16px;
  width: 25%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
`
const Container = styled.div`
  padding: 16px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;   
`

const Pokemon = ({ id, name, type, imageUrl, description }) => {
  return (
    <Wrapper>
        <Container>
            <h2>{name}</h2>
            <p>ID: {id}</p>
            <p>Type: {type}</p>
            <img src={imageUrl} alt={name} />
            <p>{description}</p>
        </Container>
    </Wrapper>
  );
};

export default Pokemon;
