# Циклы
# while бесконечный цикл, выполняется пока условие истинно
# итерация - прохождение одного цикла

# while True:
# operator = input('Введите оператор +, - , /, *:')
# number1 = int(input('Введите первое число '))
# number2 = int(input('Введите второе число '))
# if operator == '+':
#      print(number1 + number2)
# elif operator == '-':
#      print(number1 - number2)
# elif operator == '/':
#      print(number1 / number2)
# elif operator == '*':
#     print(number1 * number2)
# else:
#      print('введен неверный оператор')

# i = 0
# while i <= 10:
#     print(i)
#     i = i + 1
#
# i = 0
# while i <= 100:
#      print(i + 10)
#      i += 1

# Цикл for проходится по любому итерируемому объекту
# list1 = []
# for i in range(1, 101):
#     list1.append(i)
#     print(i)
# print(list1)

# string = 'Hello, how are you?'
# string = string.split()
# for letter in string:
#     print(letter.upper())

# summ = 0
# for num in range(1, 101):
#     summ = summ + num
#     print(summ)
# print(summ)

# Операторы continue и break
# Continue продолжает цикл минуя
# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i * 2, end = '')

# Оператор break досрочно прерывает цикл и выходит из него
# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i)

# Генераторы списков
# list1 = []
# for num in range(1, 21):
#     list1.append(num)
#     print(list1)

# nums = [i for i in range(1, 21)]
# print(nums)

# Для списков с повторяющимися значениями
# A = [0] * 10
# print(A)

# Для списков с условиями, например для списков с четными или нечетными цифрами
# nums = [i for i in range(1, 21) if i % 2 == 0]
# print(nums)

# list1 = [i ** 2 for i in range(1, 11)]
# print(list1)

# Первое вводимое число - это диапазон, второе - то, что добавляется в список
# list1 = [input() for i in range(int(input()))]
# print(list1)


# list1 = [i ** 2 for i in range(1, 11)]
# print(list1)
#
# nums = []
# for number in range(1, 11):
#     number = number * number
#     nums.append(number)
# print(nums)