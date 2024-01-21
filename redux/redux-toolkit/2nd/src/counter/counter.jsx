import React from "react";
import { useDispatch, useSelector } from "react-redux";
import {plus, minus} from './counterSlice'

const Counter = () => {
    const count = useSelector((state) => state.counter.value)
    const dispatch = useDispatch()

    return (
        <div>
            <div>
                <button onClick={() => dispatch(plus())}>+</button>
                <span>{count}</span>
                <button onClick={() => dispatch(minus())}>+</button>
            </div>
        </div>
    )
}

export default Counter