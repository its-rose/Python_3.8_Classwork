# Работа с файлами

# Создание файла из списка
# list_ = [num for num in range(1, 51)]
# with open('test.txt', 'w') as file:
#     for i in list_:
#         file.write(str(i) + '\n')

# Открытие файла
# with open('test.txt', 'r') as file2:
#     for line in file2:
#         print(line)

# Дополнение файла текстом
# text_add = 'hello world'
# write_file = open('test.txt', 'a')
# write_file.write(text_add)
# write_file.close()


# Поиск ошибок, обход ошибок и продолжение выполнения кода
# try:
#     num = 1 / 0
#     print(num)
# except ZeroDivisionError as error:
#     print(error)
#     num = 0
# print('Код отработал')

# try:
#     num = 1 / 0
#     print(num)
# except Exception as error:
#     print(error)
#     num = 0
# print('Код отработал')

# блок finally - в нем код отработается в любом случае не смотря на ошибку
# f = open('test.txt')
# nums = []
# try:
#     for line in f:
#         nums.append(int(line))
# except ValueError:
#     print('Это не число. Выходим.')
# except Exception:
#     print('Что это вообще такое?')
# else:
#     print('Всё хорошо!')
# finally:
#     f.close()
#     print('Я закрыл файл.')
#     print(nums)