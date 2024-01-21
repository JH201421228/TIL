import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    value: []
}

const todosSlice = createSlice({
    name: 'todos',
    initialState,
    reducers: {
        addTodo: (state, action) => {
            state.value.push(action.payload)
        },
    },
})

export const {addTodo} = todosSlice.actions
export default todosSlice.reducer