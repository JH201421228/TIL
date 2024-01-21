import React from "react";
import { UseDispatch, useDispatch, useSelector } from "react-redux";
import { decrement, increment } from "./counterSlice";

export function Counter() {
    const count = useSelector((state) => state.counter.value)
    const dispatch = useDispatch()

    return (
        <div>
            <div>
                <button aria-label="Increment value" onClick={() => dispatch(increment())}>
                    +
                </button>
                <span>{count}</span>
                <button aria-label="Decrement value" onClick={() => dispatch(decrement())}>
                    -
                </button>

            </div>
        </div>
    )
}