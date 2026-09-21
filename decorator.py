"""def decorator_name(func):
    def wrapper():
        print("namaskara")
        func()
        print("take care")
    return wrapper
@decorator_name
def into():
    print("i am appu")
into()
"""
def decorator_name(func):
    def wrapper(a,b):
        print("result is ")
        func(a,b)
        print("hope u got the reult")
    return wrapper
@decorator_name
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
add(2,4)
sub(20,10)