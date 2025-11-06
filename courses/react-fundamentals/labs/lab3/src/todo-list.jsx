import React, { useEffect } from 'react'
import { connect } from 'react-redux'
import Todo from './todo.jsx'

import {receiveTodos, loadTodos, removeTodo} from './actions'

const TodoList = ({ todos, removeTodo, dispatch }) => {
    useEffect(() => {
        dispatch(loadTodos())
    }, [])

    removeTodo = id => (dispatch({type: 'REMOVE_TODO', id}))

    return (
        <div>
        <p><b>Your Todos:</b></p>
        {todos.length > 0 ? (
            todos.map(todo => (
                <Todo todo={todo} remove={removeTodo} key={todo.id} />
            ))
        ) : (
            <h3>No Todos remaining!</h3>
        )}
    </div>)
}

const mapStateToProps = (state) => ({
    todos: state,
})

export default connect(mapStateToProps, null)(TodoList)
