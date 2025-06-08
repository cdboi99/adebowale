def deco(color: str):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(colors.get(color, ""), end="")
            result = func(*args, **kwargs)
            print(colors["reset"], end="")
            return result
        return wrapper
    return decorator
