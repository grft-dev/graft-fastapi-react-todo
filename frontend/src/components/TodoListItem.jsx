import { useState } from "react";
import { IoCreate, IoTrash } from "react-icons/io5";
import TodoEditForm from "./TodoEditForm.jsx";


const actionButtonStyle = {
  background: "none",
  border: "none",
  cursor: "pointer",
  color: "#94a3b8",
  padding: 6,
  borderRadius: 6,
  display: "flex",
  alignItems: "center",
};


function TodoListItem({ todo, updateTodo, toggleTodo, deleteTodo, isUpdating, isToggling, isDeleting }) {
  const [isEditing, setIsEditing] = useState(false);

  return (
    <div className="todo-item todo-row" data-testid={`todo-${todo.id}`}>
      {isEditing ? (
        <TodoEditForm
          todo={todo}
          updateTodo={updateTodo}
          isUpdating={isUpdating}
          onClose={() => setIsEditing(false)}
        />
      ) : (
        <>
          <div style={{ flex: 1, minWidth: 0 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
              <input
                type="checkbox"
                className="todo-checkbox"
                checked={todo.completed}
                onChange={() => toggleTodo(todo.id)}
                data-testid={`toggle-${todo.id}`}
                disabled={isToggling}
              />
              <p
                data-testid={`title-${todo.id}`}
                style={{
                  margin: 0,
                  fontSize: 15,
                  fontWeight: 500,
                  color: todo.completed ? "#94a3b8" : "#0f172a",
                  textDecoration: todo.completed ? "line-through" : "none",
                }}
              >
                {todo.title}
              </p>
            </div>
            {todo.description && (
              <p
                data-testid={`description-${todo.id}`}
                style={{ margin: "4px 0 0", paddingLeft: 34, fontSize: 13, color: todo.completed ? "#cbd5e1" : "#64748b" }}
              >
                {todo.description}
              </p>
            )}
          </div>
          <div style={{ display: "flex", gap: 4 }} className="todo-actions">
            <button onClick={() => setIsEditing(true)} data-testid={`edit-${todo.id}`} aria-label="Edit" style={actionButtonStyle}>
              <IoCreate size={16} />
            </button>
            <button onClick={() => deleteTodo(todo.id)} data-testid={`delete-${todo.id}`} aria-label="Delete" disabled={isDeleting} style={actionButtonStyle}>
              <IoTrash size={16} />
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default TodoListItem;
