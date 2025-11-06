import React from 'react'
import Title from './title'
import AddTodo from './add-todo'
import TodoList from './todo-list'
import styles from './todos.module.css'

const TodoApp = () => (
  <div className={styles.wrapper}>
    <Title />
    <AddTodo />
    <TodoList />
  </div>
)

export default TodoApp
