from time import sleep, time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #print('Inside wrapper')
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper

def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #print('Inside max_result')
        result = func(*args, **kwargs)
        if result > 100:
            print('Result is too big ({0}). Max allowed is 100.'.format(result))
        return result
    return wrapper

@max_result
@measure
def cube(n):
    #print('Inside cube')
    return n**3

print(cube(2))
print(cube(5))
