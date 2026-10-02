import TodoListItem from "./TodoListItem.jsx";


function TodoList({ todos, isLoading, error, ...actions }) {
  if (error) {
    return (
      <div style={{ padding: "12px 16px", background: "#fef2f2", border: "1px solid #fecaca", borderRadius: 8, color: "#dc2626" }}>
        Failed to load todos — {error.message}
      </div>
    );
  }

  if (isLoading) {
    return <div style={{ textAlign: "center", padding: "48px 0", color: "#94a3b8" }}>Loading…</div>;
  }

  if (todos.length === 0) {
    return (
      <div style={{ textAlign: "center", padding: "64px 0" }}>
        <div style={{ fontFamily: "'Fraunces', Georgia, serif", fontSize: 48, color: "#dbeafe" }}>✓</div>
        <p style={{ color: "#94a3b8", fontSize: 15, margin: 0 }}>No todos yet</p>
        <p style={{ color: "#cbd5e1", fontSize: 13, margin: "6px 0 0" }}>Add your first todo above</p>
      </div>
    );
  }

  return (
    <>
      <div style={{ marginBottom: 8, display: "flex", alignItems: "center", gap: 12 }}>
        <span style={{ fontSize: 11, fontWeight: 700, color: "#94a3b8", letterSpacing: "1.2px", textTransform: "uppercase" }}>Todos</span>
        <div style={{ flex: 1, height: 1, background: "#e2e8f0" }} />
      </div>
      <div style={{ paddingLeft: 24 }}>
        {todos.map((todo) => <TodoListItem key={todo.id} todo={todo} {...actions} />)}
      </div>
    </>
  );
}

export default TodoList;
