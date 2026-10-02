"""Domain errors independent of HTTP and persistence frameworks."""


class TodoNotFoundError(Exception):
    """Raised when a requested todo does not exist."""
