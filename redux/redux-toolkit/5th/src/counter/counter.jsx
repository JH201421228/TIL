import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { minus, plus, plusBy } from "./counterSlice";

const Counter = () => {
    const val = useSelector((state) => state.counter.value)
    const dispatch = useDispatch()
    const [plusNum, setPlusNum] = useState(null)

    const handlePlusNum = () => {
        dispatch(plusBy(Number(plusNum) || 0))
        setPlusNum("")
    }

    return (
        <>
            <div>
                <button onClick={() => dispatch(plus())}>+</button>
                <span>{val}</span>
                <button onClick={() => dispatch(minus())}>-</button>
            </div>
            <div>
                <input type="text" value={plusNum || ''} onChange={(e) => setPlusNum(e.target.value)}/>
                <button onClick={handlePlusNum}>+</button>
            </div>
        </>
    )
}

export default Counter