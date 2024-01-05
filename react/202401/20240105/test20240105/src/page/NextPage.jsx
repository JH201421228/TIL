import React from "react";
import styled from "styled-components";
import Button from "../ui/Button";
import { useNavigate } from "react-router-dom";

function NextPage(props){
    const navigate = useNavigate()

    return(
        <Button
            title="돌아가기"
            onClick={() => {
                navigate("/main-page")
            }}
        >

        </Button>
    )
}

export default NextPage;