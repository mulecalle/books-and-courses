import React, { useState } from 'react';
import { connect } from 'react-redux';
import { handleAdd } from './actions';

const AddTodo = ({ dispatch }) => {
    // this is using the useState hook from react
    // in this case, this allows us to maintain state in function component
    // This doesn't make sense to move it into the redux state because no other component cares
    const [todoText, setTodoText] = useState('');

    const handleChange = (event) => {
        setTodoText(event.target.value);
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        let text = todoText.trim()
        if (!text) return

        // using dispatch directly without a mapDispatchToProps
        dispatch(handleAdd(text))

        // the action object gets sent to a reducer?
        setTodoText('')
    }

    return (
        <form className="row" onSubmit={handleSubmit}>
            <input
                type="text"
                value={todoText}
                placeholder="Add todos here..."
                autoComplete="off"
                onChange={handleChange}
            />
            <button type="submit"> +</button>
        </form>
    )
}

// use shorthand notation with the event coming from actions.js
// const mapDispatchToProps = { handleAdd };

export default connect(null, null)(AddTodo);
