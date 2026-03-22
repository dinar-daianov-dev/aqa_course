from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Лог вызова
            print(f"-> Calling {func.__name__}{args}")

            result = func(*args, **kwargs)

            # Лог результата
            print(f"<- {func.__name__} returned {result}")
            return result
        except Exception as e:
            # Лог ошибки
            print(f"-> {func.__name__} raised {type(e).__name__}: {e}")
            raise

    return wrapper
    
def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if attempt == max_attempts - 1:
                        raise last_error

        return wrapper

    return decorator