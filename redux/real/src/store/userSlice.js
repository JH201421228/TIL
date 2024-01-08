import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    currentUser: {
        uid: '',
        photoURL: '',
        displayName: '',
    }
}

export const userSlice =  createSlice({
    name: 'user',
    initialState,
    reducers: {

    }
})

export default userSlice.reducer