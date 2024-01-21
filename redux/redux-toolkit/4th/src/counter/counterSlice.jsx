import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    value: 0
}

const counterSlice = createSlice({
    name: 'counter',
    initialState,
    reducers: {
        plus: (state) => {
            state.value += 1
        },
        minus: (state) => {
            state.value -= 1
        },
        plusBy: (state, action) => {
            state.value += action.payload
        }
    },
})

export const {plus, minus, plusBy} = counterSlice.actions
export default counterSlice.reducer