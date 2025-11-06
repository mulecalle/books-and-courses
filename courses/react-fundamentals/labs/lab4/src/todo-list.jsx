import React from 'react';
import Todo from './todo.jsx';

const TodoList = ({ todos, handleRemove }) => (
  <div>
    <p><b>Your Todos:</b></p>
    {todos.length > 0 ? (
      todos.map(todo => (
        <Todo todo={todo} remove={handleRemove} key={todo.id} />
      ))
    ) : (
      <h3>No Todos remaining!</h3>
    )}
  </div>
)

export default TodoList
