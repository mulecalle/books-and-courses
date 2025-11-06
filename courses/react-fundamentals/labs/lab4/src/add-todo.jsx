import React, { useState } from 'react'

const AddTodo = ({ handleAdd }) => {
  const [todoText, setTodoText] = useState('')

  const handleChange = (event) => {
    setTodoText(event.target.value)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    let text = todoText.trim()
    if (!text) return
    const newTodo = { id: Date.now(), text: text }
    handleAdd(newTodo)
    setTodoText('')
  }

  return (
    <form onSubmit={handleSubmit} className="row">
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

export default AddTodo