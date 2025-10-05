def decorator(func):
    def wrapper():
        print("run before the function")
        func()
        print("run after the function")
    return wrapper

def say_hello():
    print("hello")


#decorator working
decorator1=decorator(say_hello)
decorator1()
