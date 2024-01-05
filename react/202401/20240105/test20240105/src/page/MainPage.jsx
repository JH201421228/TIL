import React from "react";
import styled from "styled-components";
import Button from "../ui/Button";
import { useNavigate } from "react-router-dom";

function MainPage(props){
    const navigate = useNavigate();

    return(
        <Button
            title="확인"
            onClick={() => {
                navigate("/next-page")
            }}
        >

        </Button>
    )
}

export default MainPage;