import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    value: 0,
}

export const counterSlice = createSlice({
    name: 'counter',
    initialState,
    reducers: {
        plus: (state) => {
            state.value += 1
        },
        minus: (state) => {
            state.value -= 1
        },
    },
})

export const {plus, minus} = counterSlice.actions
export default counterSlice.reducer