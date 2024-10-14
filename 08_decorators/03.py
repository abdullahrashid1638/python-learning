import time

def cache(func):
    cache = {}
    print(cache)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        res = func(*args, **kwargs)
        cache[args] = res
        return res
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(2, 5))
