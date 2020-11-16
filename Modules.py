# Встроенные функции

# Module math
# import math
# print(math.pi)
#
# PI = math.pi
# print(PI)

# округление в большую сторону
# print(math.ceil(PI))
# округление  вменьшую сторону
# print(math.floor(PI))

# функция abs возращает обсолютное (положительное) значение числа
# num1 = -10
# print(abs(num1))



# Module random выводит случайные значения из указанного диапазона
# import random
# print(random.randint(1, 100))

# возращает случайное дробное число от 0 до 1
# print(random.random())

# выводит случайные дробные значения из указанного диапазона
# print(random.uniform(0, 10))

# возращает случайное значение любого итеррируемого объекта
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(random.choice(list_))

# перемешивает элементы списка
# random.shuffle(list_)
# print(list_)



# Module statistics содержит функции для осуществления статистических операций.
# import statistics
#
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = int(sum(list_) / len(list_))
# print(result)
# print(statistics.mean(list_))




# Работа со временем
import datetime   # - работа с датой или временем
import time       # - работа со временем
import calendar   # - работа с календарем
# import pytz     # - работа с часовыми поясами

# print(datetime.datetime.now())
# time.sleep(2)     # - останавливает выполнение программы на кол-во указанных секунд
# print(datetime.datetime.now())
# print(datetime.date(2020, 11, 2))

# years = [2015, 2016, 2017, 2018, 2019, 2020]
# monthes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# days = [i for i in range(1, 32)]
# print(datetime.date(years[0], monthes[0], days[0]))

# print(datetime.datetime.today())
# print(datetime.datetime.utcnow())



import sys            # -переменные и функции, которые используются/взаимодействуют с интерпретатором
import platform       # - низкоуровневая информация о платформе
import os             # - способ доступа к системным функциям для разных платформ
import shutil         # - высокоуровневые операции с файлами (копирование, удаление и др.)
import subprocess     # - запуск процессов, присоединение к потокам их ввода.вывода и получение кодов возврата

# print(platform.machine())     # - возращает тип машины
# print(platform.node())        # - возращает сетевое имя машины
# print(platform.processor())   # - возращает наименование процессора
# print(platform.system())      # - возращает название операционной системным
# print(platform.version())     # - возращает версию ОС
# print(platform.uname())       # - возращает именнованный кортеж из результатов функций прописанных выше

# print(sys.maxsize)    # - возращает наибольшее число, которое поддерживает ОС
# print(sys.platform)   # - строка, содержащая идентификатор платформы

# os.startfile('/home/roza/PycharmProjects/pythonParsingSTIgov/parserSTIgov.py') - работает на Windows
# os.mkdir('new_folder')
# shutil.copy('pep_8.py', 'new_folder')
# print(os.path.getsize('venv'))  # - возращает объем папки в байтах

