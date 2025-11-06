import React from 'react'
import ReactDOM from 'react-dom'
import TodoApp from './todo-app'
import 'milligram'
import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'
import { todos } from './reducer'
import thunk from 'redux-thunk'
import axios from 'axios'

window.axios = axios;

const store = createStore(todos, applyMiddleware(thunk))

ReactDOM.render(
  <Provider store={store}>
    <TodoApp />
  </Provider>,
  document.getElementById('root'),
)

// thunk, redux lib to handle async calls, redux out of the box is not able to manage async calls
// • Redux thunk is a library that we will install and use
//  • Currently in Redux, we dispatch({ADD_TODO, todoItem})
//  • But what if we are waiting on an external server for that todoItem?  In other words I do NOT know what my payload is…then what that means is that I can NOT dispatch the action object immediately
//  • Dispatch always expects an action object
//  • dispatch(function(function(CALL THE SERVER FOR THE ACTION OBJECT PAYLOAD…))
// • By default Redux will not understand that!
//  • So, what we need is an additional library that will essentially keep track of the call to the server and “wait” for the result (the todo payload data that we want), and THEN when it’s ready dispatch the action object
//  • So, this is essentially what thunks do..

// is middleware between actions and reducers
