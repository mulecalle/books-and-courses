import React from "react";
import Title from "./title";
import AddTodo from "./add-todo";
import TodoList from "./todo-list";
import styles from './todos.module.css'

const TodoApp = () => {
    // these are "props" (handleAdd/todos/handleRemove)
    // So “props” are some short of way to make functions/variables from a component to it child components?
    return (
        <div className={styles.wrapper}>
            <Title/>
            <AddTodo/>
            <TodoList/>
        </div>
    )
}

export default TodoApp;
