# Генераторы списков - можно в одну строчку создавать заполненные списки
# list1 = [i for i in range (1, 11)]
# print(list1)
#
# list2 = []
# for i in range(1, 11):
#     list2.append(i)
# print(list2)
#
# list3_even = [i for i in range(1, 11) if i % 2 == 0]
# print(list3_even)
#
# list4_odd = [i for i in range(1, 11) if i % 2 == 1]
# print(list4_odd)


# Lambda - оператор создающий анонимную функцию без имени. Для простых операций. Записывается в одну строчку, быстрая.
# lambda_func = lambda x, y: x + y
# print(lambda_func(5, 2))

# Обычно используется вместе с другими функциями (например с функцией map):
# map принимает какую то функцию и список и применяет эту функцию к каждому элементу данного списка.
# list1 = ['1', '2', '3', '4', '5', '6']
# print(list1)
# new_list = list(map(int, list1))
# print(new_list)

# list_ = [x for x in range(1, 51)]
# def my_func(x):
#     return x * x
# new_list = list(map(my_func, list_))
# print(new_list)

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def my_func(element):
#     element = str(element) + ' element'
#     return element
# new_tuple = tuple(map(my_func, list_))
# print(new_tuple)

# text = 'hello world'
# # text2 = list(text)
# # def new_func(a):
# #     a = a.upper
# #     return a
# # new_text = str(map(new_func, text2))
# # print(new_text)


# Функция filter (принимает функцию и список)
# mixed_list = ['мак', 'проссо', 'мак', 'пшено', 'проссо']
# zolushka = list(filter(lambda x : x == 'мак', mixed_list))
# print(zolushka)

# def filter_odd_num(in_num):
#     if (in_num % 2) == 0:
#         return True
#     else:
#         return False
# nums = [1, 2, 3, 4, 5, 6, 7]
# out_filter = filter(filter_odd_num, nums)
# print(list(out_filter))


# Функция reduce - последовательно применяет функцию к каждому элементу и суммирует их.
# from functools import reduce
#
# items = [1, 2, 3, 4, 5]
# sum_all = reduce(lambda x, y: x + y, items)
# print(sum_all)
#
# def lambda_f(x, y):
#     return x + y
# sum2 = reduce(lambda_f, items)
# print(sum2)


# Функция zip - объединяет в кортежи (кроме словаря) элементы из последовательностей переданных в качестве аргументов.
# Функция останавливается, когда заканчивается самый короткий элемент.
# a = [1, 2, 3]
# b = 'xyz'
# c = (None, True)
# res = list(zip(a, b, c))
# print(res)

# a = [1, 2, 3]
# b = ['Erkin', 'Tom', 'John']
# dict1 = dict(zip(a, b))
# print(dict1)
# tuple1 = tuple(zip(a, b))
# print(tuple1)
# set1 = set(zip(a, b))
# print(set1)


# Function enumerate - создаёт объект, который генерирует кортежи с индексом элемента и самим элементом.
# list_ = [1, 2, 3, 4, 5, 6, 7]
# new_list = []
# for num in enumerate(list_):
#     new_list.append(num)
# print(new_list)
#
# text = 'hello world'
# for i in enumerate(text):
#     print(i)

# Function decorator - позволяет обернуть другую функцию для расширения ее функциональности не изменяя при этом код.
# @decorator_function

# def wrapper_func():
#     def hello():
#         print('hello')
#     hello()
# wrapper_func()

# def hello():
#     print('hello')
# h = hello()


# def burger(func):
#     def bur(*args, **kwargs):
#         print('верхняя булочка')
#         func(*args, **kwargs)
#         print('нижняя булочка')
#     return bur
#
# def kotleta(func):
#     def kot(*args, **kwargs):
#         print('курочка')
#         func(*args, **kwargs)
#         print('говядина')
#     return kot
# @burger
# @kotleta
# def nachinka(cheese, tomatoes, cucumber, sous):
#     print('\n', cheese, '\n', tomatoes, '\n', cucumber, '\n', sous, '\n')
# nachinka('сыр', 'помидоры', 'огурцы', 'соус')