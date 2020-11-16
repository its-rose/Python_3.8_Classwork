# Магичеcкие методы

# Method __hash__
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def __hash__(self):
#         return hash(self.email)
#
#     def __eq__(self, obj):
#         return self.email == obj.email
#
# john = User('John Connor', 'john@gmail.com')
# sonya = User('Sonya Blade', 'sonya@gmail.com')
#
# print(john == sonya)
# print(hash(john.email))
# print(hash(sonya.email))



# Method __getattr__ / __getattribute__
# class Researcher():
#     def __getattr__(self, name):
#         return 'Nothing found!'
#     def __getattribute__(self, name):
#         return 'nope'
#
# obj = Researcher()
#
# print(obj.attr)
# print(obj.method)
# print(obj.DFG2H3J00KLL)

# class Researcher():
#     def __getattr__(self, name):
#         return 'Nothing found!'
#
#     def __getattribute__(self, name):
#         print('Looking for {}', format(name))
#         return object.__getattribute__(self, name)
#
# obj = Researcher()
#
# print(obj.attr)
# print(obj.method)
# print(obj.DFG2H3J00KLL)



# Method __setattr__

# class Ignorant():
#     def __setattr__(self, name, value):
#         print(f'Not gonna set {name}!')
#
# obj = Ignorant()
# obj.math = True
#
# print(obj.math)



# Method __getattr__

# class Polite():
#     def __delattr__(self, name):
#         value = getattr(self, name)
#         print(f'Goodbye {name}, you were {value}!')
#         object.__delattr__(self, name)
#
# obj = Polite()
#
# obj.attr = 10
# del obj.attr



# Method __call__

# class Logger():
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             with open(self.filename, 'a') as f:
#                 f.write('Oh Danny boy...')
#
#             return func(*args, **kwargs)
#         return wrapper
#
# logger = Logger('index.txt')
# @logger



# Method __add__ and __sub__

# import random
# class NoisyInt():
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, obj):
#         noise = random.uniform(-1, 1)
#         return self.value + obj.value + noise
#
# a = NoisyInt(10)
# b = NoisyInt(20)
#
# for _ in range(3):
#     print(a + b)



# Method __getitem__ and __setitem__

# class PascalList:
#     def __init__(self, original_list=None):
#         self.container = original_list or []
#
#     def __getitem__(self, index):
#         return self.container[index - 1]
#
#     def __setitem__(self, index, value):
#         self.container[index - 1] = value
#
#     def __str__(self):
#         return self.container.__str__()
#
# numbers = PascalList([1, 2, 3, 4, 5])
# print(numbers[5])