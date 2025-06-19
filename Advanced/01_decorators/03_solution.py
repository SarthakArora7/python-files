import time

def cache(func):
    cache_value = {}  # This is defined ONCE when the decorator is applied
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        print(cache_value)
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

# So the cache_value dictionary is created only once when cache(long_running_function) is first called. It stays enclosed within the wrapper function, which is what actually runs every time you call long_running_function.

# This is called a closure — the wrapper function “remembers” the cache_value dictionary from its enclosing scope even after the outer cache() function has finished executing.

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(4, 3))