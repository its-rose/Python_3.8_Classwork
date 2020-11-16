# Strings
# Method split Делит строку по разделителю на отдельные слова
# text = 'Hello,World,Good, Morning'
# print(text.split(','))

# Method isdigit проверяет все ли символы в строке цифры
# num = input('Введите число: ')
# print(num.isdigit())
#
# Method isalpha проверяет является ли вся строка буквами
# text = input('Введите текст')
# print(text.isalpha())
#
# Method isalnum проверяет все ли символы в строке буквы и цифры
# text = input('Заполните строку ')
# print(text.isalnum())
#
# Method replace заменяет часть строки
# string = 'Hello world!'
# print(string.replace('Hello', 'Goodbye'))
#
# Method isupper проверяет все ли символы в верхнем регистре
# text = input('Введите текст ')
# print(text.isupper())
#
# Method islower проверяет все ли символы в нижнем регистре
# text = input('Введите текст ')
# print(text.islower())
#
# Method isspace проверяет все ли символы пробелы, табы или переводы строку
# text = input('Введите текст ')
# print(text.isspace())
#
# Method istitle проверяет является ли первая буква в строке заглавной
# text = 'Hello World!'
# text2 = 'hello world'
# print(text.istitle())
# print(text2.istitle())
#
# Method lower переводит все заглавные буквы в прописные
# text = 'Hello WORLD!'
# print(text.lower())
#
# Method upper переводит буквы в верхний регистр
# string = 'Hello world!'
# print(string.upper())
#
# Method startswith проверяет начинается ли строка с определенных символов
# text = 'Hello world!'
# print(text.startswith('Hello'))
#
# Method endswith
# text = 'mailbox.@gmaiil.com'
# print(text.endswith('.com'))
#
# Method join склеивает строку из разных частей
# text = 'Hello, my name is Rose'
# text_splited = text.split()
# print(text_splited)
# text2 = '_'.join(text_splited)
# print(text2)
#
# Method ord выводит нумерацию символа, согласно таблицы ASCII
# print(ord('A'))
# print('A' > 'a')

# Method count считает количество символов, переданных нами в скобках
# text = 'Hello World!!!!!'
# print(text.count('!'))

# Method strip, lstrip,rstrip удаляет пробелы в начале и в конце строки
# text = '   hello world   '
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())
#
# Method swapcase меняет регистр букв на противоположный
# text = 'Hello World'
# print(text.swapcase())
#
# Срез строки (5 - номер символа по порядку, 2 - шаг)
# text = 'Hello world'
# print(text[0:5:2])
# print(text[0:5:-2])
#
# text = input('Введите текст  ')
# if text == text [::-1]:
#     print('Текст читается одиннаково')
# else:
#      print('Текст читается не одиннаково')

# Форматирование строк
# name = input('введите своё имя:  ')
# age = input('введите свой возраст:  ')
# print('Вас зовут ' + name + '.' 'Ваш возраст ' + age)
# print(f"Вас зовут {name}. Ваш возраст {age}.")
# print("Hello, %s" % name)
# print("Hello, {}".format(name))

# Экранирование последовательности \n, \r, \t
