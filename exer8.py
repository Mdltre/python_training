from time import time

def timer(func):
        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f"Time it took the run the function : {(t2-t1):.2f} ms")
            print(f"The sum is {result}.")           
        return wrap_func


@timer
def adding_function(x,y):
    return x+y

adding_function(3,5)