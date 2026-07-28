import datetime

user_logged_in = True

def require_login(func):
    def wrapper(a, b):
        if user_logged_in:
            return func(a, b)
        else:
            print("Access denied. Please log in first.")
    return wrapper

def log_call(func):
    def wrapper(a, b):
        print(f"Calling {func.__name__} at {datetime.datetime.now()}")
        return func(a, b)
    return wrapper

def require_positive_ints(func):
    def wrapper(a, b):
        if not isinstance(a, int) or a <= 0 or not isinstance(b, int) or b <= 0:
            print("Invalid input. All arguments must be positive integers.")
            return
        return func(a, b)
    return wrapper

def count_calls(func):
    def wrapper(a, b):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} time(s).")
        return func(a, b)
    wrapper.calls = 0
    return wrapper

@require_login
@log_call
@require_positive_ints
@count_calls
def add_numbers(a, b):
    result = a + b
    print(f"Result: {result}\n")
    return result

add_numbers(10, 20)
add_numbers(5, 15)
add_numbers(-2, 8)

user_logged_in = False
add_numbers(3, 4)