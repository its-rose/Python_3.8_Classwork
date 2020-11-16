# *args and **kwargs - функции с переменным кол-вом элементов
# Без *args - аргументы сложно считать
# def add(h, f, g, y, s , v, r)
#     return h + f + g + y + s + v + r
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# *args - работает с простыми аргументами
# def add(*nums):
#     result = 0
#     for num in nums:
#         result = result + num
#     return result
# print(add(1, 2, 3, 4, 5, 6))

# ** kwargs - неограниченное кол-во именнованных аргументов
# def func1(a = 10, b = 10, c = 30):
#     return a + b + c
# print(func1(1, 2))

# dict1 = {'lenovo': 'yoga', 'macbook': 'pro', 'asus': 'zephyrus'}
# def myfunc(**kwargs):
#     for key, value in dict1.items():
#         print(f'{key}: {value}')
# myfunc()

# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
# many(1, 2, 3, name = 'yoga')