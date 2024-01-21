import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addTodo } from "./todosSlice";

const Todos = () => {

    const todos = useSelector((state) => state.todos.value)
    const dispatch = useDispatch()

    const [nowTodo, setNowTodo] = useState('')

    const handleTodo = () => {
        dispatch(addTodo(nowTodo))
        setNowTodo('')
    }

    const renderTodos = (todos) => {
        return(
            <ul>
                {todos.length > 0 &&
                todos.map((todo, index) => (
                    <li key={index}>{todo}</li>
                ))}
            </ul>
        )
    }

    return (
        <>
            <div>
                <h2>List</h2>
                {renderTodos(todos)}
            </div>
            <div>
                <input type="text" value={nowTodo || ''} onChange={(e) => setNowTodo(e.target.value)} />
                <button onClick={handleTodo}>send</button>
            </div>
        </>
    )
}

export default Todos