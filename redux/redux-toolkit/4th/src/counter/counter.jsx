import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { minus, plus, plusBy } from "./counterSlice";

const Counter = () => {
    const num = useSelector((state) => state.counter.value)
    const dispatch = useDispatch()
    const [plusNum, setPlusNum] = useState(0)
    
    const changePlusNum = (e) => {
        setPlusNum(e.target.value)
        console.log(plusNum)
    }

    const handlePlusNum = () => {
        dispatch(plusBy(Number(plusNum) || 0))
        setPlusNum(0)
    }

    return (
        <div>
            <div>
            <button onClick={() => dispatch(plus())}>+</button>
            <span>{num}</span>
            <button onClick={() => dispatch(minus())}>-</button>
            </div>
            <div>
                <input type="text" value={plusNum} onChange={changePlusNum}/>
                <button onClick={handlePlusNum}>+</button>
            </div>
        </div>

    )
}

export default Counter