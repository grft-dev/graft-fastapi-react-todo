import AppHeader from "./components/AppHeader.jsx";
import TodoCreateForm from "./components/TodoCreateForm.jsx";
import TodoList from "./components/TodoList.jsx";
import useTodos from "./hooks/useTodos.js";


function App() {
  const todoState = useTodos();
  const completedCount = todoState.todos.filter((todo) => todo.completed).length;

  return (
    <div style={{ minHeight: "100vh", background: "#fff" }}>
      <AppHeader
        pendingCount={todoState.todos.length - completedCount}
        completedCount={completedCount}
      />
      <main style={{ maxWidth: 680, margin: "0 auto", padding: "40px 24px 80px" }}>
        <TodoCreateForm
          createTodo={todoState.createTodo}
          isCreating={todoState.isCreating}
        />
        <TodoList
          todos={todoState.todos}
          isLoading={todoState.isLoading}
          error={todoState.error}
          updateTodo={todoState.updateTodo}
          toggleTodo={todoState.toggleTodoCompletion}
          deleteTodo={todoState.deleteTodo}
          isUpdating={todoState.isUpdating}
          isToggling={todoState.isToggling}
          isDeleting={todoState.isDeleting}
        />
      </main>
      <footer style={{ borderTop: "1px solid #e2e8f0", padding: "20px 24px", textAlign: "center" }}>
        <a
          href="https://github.com/grft-dev/graft-fastapi-react-todo"
          rel="noopener noreferrer"
          style={{ color: "#94a3b8", textDecoration: "none", fontSize: 12, fontWeight: 500 }}
        >
          View on GitHub
        </a>
      </footer>
    </div>
  );
}

export default App;
