
def decoretor(func):
    def wrapper(param):
        print("premise operations")
        func(param)
        print("rear operations")
    return wrapper

@decoretor
def main_func(param):
    print(f"Main operation {param}")

main_func(1)

from functools import  wraps
def meta_data(func):
    @wraps(func) #with this power func doesn't lose it's meta info while wrapped with wrapper 
    def wrapper(*args,**kwargs):
        print(f"method name: {func.__name__}")
        print(f"method doc: {func.__doc__}")
        return func(*args,**kwargs)
    return wrapper

@meta_data
def power(x,y):
    '''explanation of method'''
    return x**y
print(power(3,3))
print(power.__name__) #if there is no wraps method then it will print wrapper rather than power

import time
def speed_test(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is started")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        runtime = end - start
        print(f"runtime: {runtime}")
        return result
    return wrapper

#speed test with decorator
@speed_test
def sum_generator(): # () used rather than []
    return sum((x for x in range(1000000)))

@speed_test
def sum_list():
    return sum([x for x in range(1000000)])
print(sum_generator())
print(sum_list())

# sending param to decoretor
def dec_do_count(count):
    def do_count(func):
        def wrapper_do_count(*args,**kwargs):
            for _ in range(count):
                func(*args,**kwargs)
        return wrapper_do_count
    return do_count

@dec_do_count(count=4)
def print4():
    print(4)

print4()