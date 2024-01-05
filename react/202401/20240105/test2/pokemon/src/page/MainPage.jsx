import React from "react";
import {useNavigate} from "react-router-dom"
import styled from "styled-components";
import Pokemon from "../components/Pokemon";
import Button from "../ui/Button";
import data from "../../data.json";

const Wrapper = styled.div`
    padding: 16px;
    width: calc(100% - 32px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`;

const Container = styled.div`
    width: 100%;
    max-width: 720px;

    & > * {
        :not(:last-child){
            margin-bottom: 16px;
        }
    }
`;

function MainPage(props){
    const {} = props;
    const navigate = useNavigate();

    return (
        <Wrapper>
            <Container>
                <Button
                    title="Add Pokemon"
                    onClick={() => {
                        navigate("/add-pokemon");
                    }}
                />

                <Pokemon
                    pokemons={data}
                    onClickPokemon={(pokemon) => {
                        navigate(`/pokemon/${pokemon.id}`);
                    }}
                />
            </Container>
        </Wrapper>
    );
}

export default MainPage;