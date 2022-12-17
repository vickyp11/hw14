"""
Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!
"""

def logger(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(func.__name__, func.__code__.co_varnames)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(3,4)
square_all(5,6,7,8,9)
