import React, {useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import { addTodo, removeTodo } from "./todosSlice";

const Todos = () => {

    const todoList = useSelector((state) => state.todos.value)
    const dispatch = useDispatch()
    const [nowTodo, setNowTodo] = useState('')

    const handleTodoList = () => {
        dispatch(addTodo(nowTodo) || '')
        setNowTodo('')
    }

    const handleTodoListByEnter = (e) => {
        
        if (e.key === 'Enter') {
            e.preventDefault()
            dispatch(addTodo(nowTodo) || '')
            setNowTodo('')
        }
    }

    const renderTodoList = () => {
        return (
            <ul>
                {todoList.map((todo, index) => (
                    <li key={index}>
                        {todo}
                        <button onClick={() => dispatch(removeTodo(index))}>-</button>
                    </li>
                ))}
            </ul>
        )
    }

    return (
        <div>
            <div>
                ToDo List
            </div>
            <div>
                {renderTodoList()}
            </div>
            <div>
                <input type="text" value={nowTodo} onKeyUp={handleTodoListByEnter} onChange={(e) => setNowTodo(e.target.value)} />
                <button onClick={handleTodoList} >ADD</button>
            </div>
        </div>
    )
}

export default Todos