# decorators are used to pass a function through another function which can add functionality without changing the original code.

import time

def timer(func):
    def wrapper(*args, **kwargs):  # always try to keep arguments and keyword arguments both in the wrapper function. Because they are the arguments of the function called through decorator.
        start = time.time()
        result = func(*args, **kwargs)  # this runs the function passed through timer.
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")  # example_function ran in 2.0008273124694824 time. __name__ gives the name of the function passed through timer.
        return result  # result is empty because example_function just used time.sleep.
    return wrapper  # this returns the wrapper functions definition.


@timer
def example_function(n):  # example_function will pass through timer function.
    time.sleep(n)

example_function(2)