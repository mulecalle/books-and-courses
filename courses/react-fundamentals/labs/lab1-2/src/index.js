import React from 'react';
import ReactDOM from 'react-dom';
import TodoApp from './todo-app';
import 'milligram';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import { todos } from './reducer';

const initialTodos = [
    { id: 1, text: 'use redux in todo app' },
    { id: 2, text: 'complete bonus milestone' },
]

const store = createStore(todos, initialTodos);

ReactDOM.render(
    <Provider store={store}>
        <TodoApp />
    </Provider>,
    document.getElementById('root')
);
