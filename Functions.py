# def - define определение функции

# def my_func():
#     a = 10
#     b= 5
#     return a + b
# print(my_func())

# def my_func(a, b):
#     return a + b
# print(my_func(12, 55))
# print(my_func(11, 22))

# def func1():
#     print('hello')

# name = input('input your name: ')
# def func2():
#         print(f 'hello' {name})
# func2()

# def hello(name):
#     print(f'hello {name}')
# hello('Rose')

# def add(a, b, c=10):
#     return a + b + c
# print(add(5, 6, 1))
# print(add(5, 6))

# def func1():
#     a = 1
#     b = 2
#     c = 3
#     result = a + b + c
#     return result
#
# res_func = func1()
# print(res_func)
# print(type(res_func))

# def sqrt(a, b):
#     result = a ** b
#     return result
# print(sqrt(2, 4))

# Когда переменные задаются вне функции - это глобальная видимость переменных, когда внутри функции - локальная
# num1 = 21
# num2 = 12
# def func1():
#     res = num1 + num2
#     return res
# print(func1())

# def func1():
#     a = 10
#     b = 9
#     def func2():
#         c = 8
#         return c + a
#     d = func2()
#     return b + d
# print(func1())

# def f():
#     pass
# print(f())

# def f():
#     global a
#     a = 1
#     print(a)
# a = 0
# print(a)
# f()
# print(a)

# def func1():
#     global a
#     global b
#     a = 1
#     b = 2
# func1()
# c = a + b
# print(c)