# define a function
def my_function():
    print("it is function")

# call a function
my_function()

# function with arguments
def my_func(a, b):
    # print function can be used as below also in python. f is called format strings
    print(f"b is: {b} and a is: {a}")
    res = a + b
    print("result is :", res)

my_func(5, 6)   # function takes a = 5, b = 6
my_func(b=5, a=6)   # function takes a = 6, b = 5

# function with return
def func(a, b):
    return a+b

result = func(2, 3)
print(f"result is : {result}")

# function with default arguments
def fun1(a=10, b=20, c):
    print(c)
    retirn(f"{a+b}")
res = fun1(b=12, c={"f": 13, "g": 11})
print(type(res))
print(res)

# keyword arguments with ** - called as **kwargs
def fun2(a=10, b=20, **c):
    print(type(c))
    print(c)    # o/p: {'c': {"f": 13, "g": 11}}  
fun2(c={"f": 13, "g": 11})
    
# in python we see *args, **kwargs in function.
def fun3(*args, **kwargs):
    print(args, kwargs)
    print(sum(args), kwargs)

res = fun3(20, 30, 40, 50, 60, 10, b=9, c=7) #o/p: (20, 30, 40, 50, 60, 10) {'b': 9, 'c': 7}
# args become tuple as (20, 30, 40, 50, 60, 10) and kwargs is dict {'b': 9, 'c': 7}
# all the arguments will go to args, and key word arguments goto kwargs


