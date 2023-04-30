"""
def repeat(num_repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_repeats):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def my_function():
    print("Hello, world!")
my_function()
"""


def logger(func):
    def wrapper(*args, **kwargs):
        # Log the arguments
        print(f"the value of args{args} and kwargs{kwargs}")

        # Call the function
        res = func(*args, **kwargs)

        # Log the return value
        print(f"{func.__name__} returned {res}")

        # Return the result
        return res

    return wrapper


@logger
def add(a, b):
    return a + b


result = add(3, 4)
