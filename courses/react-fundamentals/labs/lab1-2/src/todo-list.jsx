import React from 'react';
import Todo from './todo.jsx';
import { connect } from 'react-redux';
import { handleRemove } from "./actions";

// destructuring props coming from todo-app.jsx
// todos, is coming as prop from the redux (mapStateToProps)
// handleRemove, is coming as prop from the redux (mapDispatchToProps)
const TodoList = ({todos, handleRemove}) => (
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

// this is a read from the redux db, something like a select in sql
const mapStateToProps = (todos) => ({todos});

// use shorthand notation with the event coming from actions.js
const mapDispatchToProps = { handleRemove };

export default connect(mapStateToProps, mapDispatchToProps)(TodoList);

// reducers, update state in the redux db, event handler for events
// actions, events to update state
