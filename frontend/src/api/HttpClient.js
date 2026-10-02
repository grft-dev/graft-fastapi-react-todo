/**
 * Minimal JSON HTTP client used by resource-specific API clients.
 */
class HttpClient {
  constructor(baseUrl = import.meta.env.VITE_API_URL || "http://localhost:8000") {
    this.baseUrl = baseUrl;
  }

  async request(method, endpoint, data) {
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method,
      headers: data === undefined ? undefined : { "Content-Type": "application/json" },
      body: data === undefined ? undefined : JSON.stringify(data),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `${method} ${endpoint} failed: ${response.statusText}`);
    }

    return response.json();
  }

  get(endpoint) {
    return this.request("GET", endpoint);
  }

  post(endpoint, data) {
    return this.request("POST", endpoint, data);
  }

  put(endpoint, data) {
    return this.request("PUT", endpoint, data);
  }

  delete(endpoint) {
    return this.request("DELETE", endpoint);
  }
}

export default HttpClient;
