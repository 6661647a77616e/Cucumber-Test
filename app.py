def greet_user(name):
    if not name.strip():
        return "Hello, Guest!"
    return f"Hello, {name}!"
