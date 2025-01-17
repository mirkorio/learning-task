import time

# Decorator for timing a function's execution
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.2f} seconds to execute")
        return result
    return wrapper

# Decorator for logging function calls
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@timing_decorator
@logging_decorator
def slow_function(delay):
    time.sleep(delay)
    return f"Slow operation completed after {delay} seconds"

result = slow_function(2)