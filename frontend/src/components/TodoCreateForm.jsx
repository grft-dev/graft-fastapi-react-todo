import { useState } from "react";
import { IoAdd } from "react-icons/io5";


function TodoCreateForm({ createTodo, isCreating }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!title.trim()) return;
    createTodo({ title, description });
    setTitle("");
    setDescription("");
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: 48 }}>
      <input
        className="todo-input"
        placeholder="What needs to be done?"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
        data-testid="todo-title-input"
        style={{ marginBottom: 10, fontSize: 15, fontWeight: 500 }}
      />
      <textarea
        className="todo-input"
        placeholder="Add a note (optional)"
        value={description}
        onChange={(event) => setDescription(event.target.value)}
        data-testid="todo-description-input"
        rows={2}
        style={{ marginBottom: 12 }}
      />
      <button
        type="submit"
        data-testid="create-todo-btn"
        disabled={isCreating || !title.trim()}
        style={{
          fontFamily: "'Plus Jakarta Sans', sans-serif",
          display: "flex",
          alignItems: "center",
          gap: 6,
          padding: "10px 20px",
          background: title.trim() ? "#2563eb" : "#dbeafe",
          color: title.trim() ? "#fff" : "#93c5fd",
          border: "none",
          borderRadius: 8,
          fontSize: 14,
          fontWeight: 600,
          cursor: title.trim() ? "pointer" : "default",
        }}
      >
        <IoAdd size={16} />
        {isCreating ? "Adding…" : "Add todo"}
      </button>
    </form>
  );
}

export default TodoCreateForm;
