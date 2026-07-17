# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function.
def decorator(func):
    def wraper():
        print("i AM PRINTING HELLO....")
        func()
        print("I've executed this function")
    return wraper
@decorator
def say_hello():
    print("Hello, GOAT")

say_hello()
  
# f = decorator(say_hello)
# f()
'''
f will look like 
def f():
    print("i AM PRINTING HELLO....")
    print("Hello, GOAT")
    print("I've executed this function")
'''

def repeat(n):
    def decorator (func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_Hi(a):
    print(f"Hi {a}")
say_Hi("Dev")