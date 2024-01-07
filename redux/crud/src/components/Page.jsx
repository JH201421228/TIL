import React from "react";
import { createStore } from "redux";

import Header from "./Header";
import Nav from "./Nav";
import Article from "./Article";
import Control from "./Control";

function reducer(state, action){
    if(state === undefined){
        return (
            {
                contents:[
                    {id:1, title:'HTML', desc:'HTML is ..'},
                    {id:2, title:'CSS', desc:'CSS is ..'},
                ]
            }
        )
    }
}

var store = createStore(reducer);

const Page = () => {

    return (
        <body>
            <Header/>
            <Nav/>
            <Control/>
            <Article/>
        </body>
    )
}

export default Page;
