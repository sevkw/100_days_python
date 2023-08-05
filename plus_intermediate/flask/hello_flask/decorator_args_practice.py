# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwarg):
        func_name = function.__name__
        func_return = function(args[0], args[1])
        print(f"You called {func_name}({args[0]},{args[1]})\nIt returned: {func_return}")
    return wrapper

@logging_decorator
def user_info(name:str, age:int):
    return f"{name} is {age} years old."


# Use the decorator 👇
user_info("Kerry", 18)