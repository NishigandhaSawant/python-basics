'''
burger - function
extra cheese - extra feature

msin function > function add
without changing the main function code
'''

def my_decorator(func):
    def wrapper():
        print("smthng is happening before the function is called.")
        return func()
        print("smthng is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()