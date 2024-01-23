import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    value: [],
}

const todosSlice = createSlice({
    name: 'todos',
    initialState,
    reducers: {
        addTodo: (state, action) => {
            state.value.push(action.payload)
        },
        removeTodo: (state, action) => {
            state.value.splice(action.payload, 1)
        }
    },
})

export const {addTodo, removeTodo} = todosSlice.actions
export default todosSlice.reducer