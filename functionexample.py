# def add_two(n):
#   return n + 2

# print(add_two(5)) 

#def f(*args): makes it into list, accepts any num of arguments 
#   for arg in args:
#       print(arg)

#params = (1,2,3,4,5, "slay") #this is a tuple
#f(*params)

def f(**kwargs): # double asterisks means dictionary
    for item in kwargs.items():
        print(item)

#test_dict: {"a": 1, "b" : 2, "c" : 3}
#f(test_dict)

vars()

lst = [1,2,3,4,5,6,7,8,9,10]
def is_even(num):
    return num % 2 == 0

result = filter(is_even,lst)
for num in result:
    print(num)
    
res = filter(lambda n: n % 2, lst)
for num in res:
    print(num)
    
mapp = map(lambda n: n % 2, lst) #returns true of false ( 0 or 1 )
for num in mapp:
    print(num)
    
raise ValueError #to raise errors