import { configureStore } from "@reduxjs/toolkit";
import counterReducer from '../freatures/counter/counterSlice'

export const store = configureStore({
    reducer: {
        counter: counterReducer,
    },
})