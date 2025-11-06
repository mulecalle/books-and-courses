import React from 'react'

// destructuring props coming from todo-list.jsx
const Todo = ({ todo, remove }) => (
    <li>
        {todo.text}
        <span onClick={() => { remove(todo.id) }}>
      <b>&nbsp; x</b>
    </span>
    </li>
)

export default Todo
