import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { minus, plus, plusBy } from "./counterSlice";

const Counter = () => {
    const num = useSelector((state) => state.counter.value)
    const dispatch = useDispatch()
    const [plusNum, setPlusNum] = useState('')

    const handlePlusBy = () => {
        console.log(plusNum)
        dispatch(plusBy(Number(plusNum) || 0))
        setPlusNum('')
    }

    return (
        <div>
            <div>
                <button onClick={() => dispatch(plus())}>+</button>
                <span>{num}</span>
                <button onClick={() => dispatch(minus())}>-</button>
            </div>
            <div>
                <input type="text" value={plusNum} onChange={(e) => setPlusNum(e.target.value)} />
                <button onClick={handlePlusBy}>+</button>
            </div>
        </div>
    )
}

export default Counter