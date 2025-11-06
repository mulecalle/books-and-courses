import React, { useState } from 'react'
import Title from './title'
import AddTodo from './add-todo'
import TodoList from './todo-list'
import styles from './todos.module.css'

const TodoApp = () => {

  const [todoState, setTodoState] = useState(
    [
      { id: 1, text: 'This is a simple todo list app written in React and Redux!' },
      { id: 2, text: 'Hover over todos and click on the `XX` to delete them!' },
      { id: 3, text: 'Add new todos if you like!' },
    ],
  )

  const addTodo = (todo) => {
    setTodoState([...todoState, todo])
  }

  const removeTodo = (id) => {
    setTodoState(todoState.filter(todo => todo.id !== id))
  }

  return (
    <div className={styles.wrapper}>
      <Title />
      <AddTodo handleAdd={addTodo} />
      <TodoList todos={todoState} handleRemove={removeTodo} />
    </div>
  )
}

export default TodoApp
