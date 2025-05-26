# def my_decorator(func):
#     def wrapper():
#         print('befort')
#         func()
#         print('after')
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print('hello')
#
# say_hello()
#
# @my_decorator
# def age():
#     a=int(input('age'))
#     print(a)
#
# age()
# from datetime import datetime
#
# def somedec(func):
#     def wrapper():
#         print(datetime.now())
#         func()
#         print(datetime.now())
#     return wrapper
#
# @somedec
# def time():
#     print("what time is it")
# time()

# def a_decorator(x):
#     def wrapper():
#         print(f"Hello {x}")
#         x()
#         print(f"Bye {x}")
#     return wrapper
#
# @a_decorator
# def greetings():
#     print('nazik')
#
# greetings()
#
# def counter(func):
#     count=0
#     def wrapper():
#         nonlocal count
#         func()
#         count += 1
#         print(f"Function {func.__name__} was called {count} times")
#     return wrapper
#
# @counter
# def hello():
#     print('hello')
#
# hello()
# hello()


def repeat(n):
    def myydecorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return myydecorator


@repeat(3)
def hello():
    print('hello')

hello()





