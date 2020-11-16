# Правила чистого кода

# все imports должны быть вачале кода и прописываться отдельно друг от друга.
# если классы импортируются из одной библиотеки, то их можно перечислить через запятую.
# сначала импортируются встроенные библиотеки, птом внешние, затем делается импорт из файлов.
# import os
# import sys
# import math
# from subprocess import Popen, PIPE
#
# import requests
#
# from lambda_decorator import burger

# Способы импорта всего года из файла (предпочтителен второй способ.
# from Cycles import *
# import Cycles

# перед и после функции требуется ставить две пустые строки


def func_1():
    pass


tuple_ = (1, 2, 3, 4, 5)

# для объектов со множеством элементов.
tuple_2 = (
    '1-value',
    '2-value',
    '3-value',
    '4-value',
    '5-value',
)

my_list = [
    1, 2, 3,
    4, 5, 6,
]

names = {'name': 'John', 'name': 'Tom', 'name': 'Alice'}
x = 1 + 2


def func_(x, y):
    return x + y
func_(1, 2)


def add(x, y=10):
    return x + y


# имена классов пишутся с большой буквы только первые буквы каждого слова
class MyFirstClass():
    pass

class User:
    pass


def my_function():
    pass


# все константы пишутся с большой буквы
PI = 3.14

# True or False (применяется is, не применять ==)
if my_var is True:
    pass

