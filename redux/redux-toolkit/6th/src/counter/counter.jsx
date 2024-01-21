import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { minus, plus, plusBy } from "./counterSlice";


const Counter = () => {

    const num = useSelector((state) => state.counter.value)
    const dispatch = useDispatch()

    const [addNum, setAddNum] = useState('')

    const handleAddNum = () => {
        dispatch(plusBy(Number(addNum)))
        setAddNum('')
    }

    return (
        <div>
            <div>
                <button onClick={() => dispatch(plus())}>+</button>
                <span>{num}</span>
                <button onClick={() => dispatch(minus())}>-</button>
            </div>
            <div>
                <input type="text" onChange={(e) => setAddNum(e.target.value)} value={addNum || ''} />
                <button onClick={handleAddNum}>+</button>
            </div>
        </div>
    )
}

export default Counter