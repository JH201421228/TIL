import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { minus, plus } from "./counterSlice";

const Counter = () => {
    const count = useSelector((state) => state.counter.value)
    const dispatch = useDispatch()

    return (
        <div>
            <button onClick={() => dispatch(plus())}>+</button>
            <span>{count}</span>
            <button onClick={() => dispatch(minus())}>-</button>
        </div>
    )
}

export default Counter