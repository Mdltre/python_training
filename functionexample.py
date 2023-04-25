# def add_two(n):
#   return n + 2

# print(add_two(5)) 

def f(*args):
    for arg in args:
        print(arg)

params = (1,2,3,4,5, "slay")
f(*params)