import { useState } from "react";
import { IoCheckmark, IoClose } from "react-icons/io5";


function TodoEditForm({ todo, updateTodo, isUpdating, onClose }) {
  const [title, setTitle] = useState(todo.title);
  const [description, setDescription] = useState(todo.description);

  const save = () => {
    if (!title.trim()) return;
    updateTodo({ id: todo.id, updates: { title, description } });
    onClose();
  };

  return (
    <div style={{ flex: 1 }}>
      <input
        className="todo-input"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
        data-testid={`edit-title-${todo.id}`}
        style={{ marginBottom: 8, fontWeight: 500 }}
      />
      <textarea
        className="todo-input"
        value={description}
        onChange={(event) => setDescription(event.target.value)}
        data-testid={`edit-description-${todo.id}`}
        rows={2}
        style={{ marginBottom: 10 }}
      />
      <div style={{ display: "flex", gap: 8 }}>
        <button
          onClick={save}
          data-testid={`save-edit-${todo.id}`}
          disabled={isUpdating}
          style={{ display: "flex", alignItems: "center", gap: 4, padding: "7px 14px", background: "#2563eb", color: "#fff", border: "none", borderRadius: 6, cursor: "pointer" }}
        >
          <IoCheckmark size={14} /> Save
        </button>
        <button
          onClick={onClose}
          data-testid={`cancel-edit-${todo.id}`}
          style={{ display: "flex", alignItems: "center", gap: 4, padding: "7px 14px", background: "transparent", color: "#64748b", border: "1.5px solid #e2e8f0", borderRadius: 6, cursor: "pointer" }}
        >
          <IoClose size={14} /> Cancel
        </button>
      </div>
    </div>
  );
}

export default TodoEditForm;
