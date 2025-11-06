import axios from 'axios'

export const addTodo = text => ({ type: 'ADD_TODO', text })
export const removeTodo = id => ({ type: 'REMOVE_TODO', id })
export const receiveTodos = data => ({ type: 'GET_TODO', data })

// this is the thunk
export const loadTodos = () => (
    async (dispatch, getState) => {
        const { data } = await axios.get('http://localhost:8000/todos')
        dispatch(receiveTodos(data))
    }
)
