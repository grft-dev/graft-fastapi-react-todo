import HttpClient from "./HttpClient.js";

/**
 * Client for the public /api/todos HTTP contract.
 */
class TodosApiClient extends HttpClient {
  constructor() {
    super();
    this.resourcePath = "/api/todos";
  }

  listTodos() {
    return this.get(this.resourcePath);
  }

  getTodo(id) {
    return this.get(`${this.resourcePath}/${id}`);
  }

  createTodo(title, description = "") {
    return this.post(this.resourcePath, { title, description });
  }

  updateTodo(id, updates) {
    return this.put(`${this.resourcePath}/${id}`, updates);
  }

  toggleTodo(id) {
    return this.post(`${this.resourcePath}/${id}/toggle`);
  }

  deleteTodo(id) {
    return this.delete(`${this.resourcePath}/${id}`);
  }
}

export const todosApi = new TodosApiClient();
export default TodosApiClient;
