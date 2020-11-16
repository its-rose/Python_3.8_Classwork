# Списки - множество элементов в одной переменной

# Method append дополняет список какими-либо элементами, дополняет только в конце списка
# list1 = []
# list1.append('1')
# print(list1)
# print(len(list1))
# list1.append('hello')
# print(list1)
# print(len(list1))
# string = ' '.join(list1)
# print(string)
# list1.append(['good', 'bye'])
# print(list1)
# print(len(list1))

# Method range создает списки каких-либо чисел
# list1 = list(range(1, 50, 2))
# print(list1)

# Method insert получает два аргумента, первый индекс (куда добавить), второй - элемент, который нужно добавить.
# Дополняет согласно ииндексу.
# cars = ['Mercedes', 'Subaru', 'Honda']
# print(len(cars))
# cars.insert(0, 'Toyota')
# print(cars)

# Method remove удаляет элементы по названию
# laptops = ['Lenovo', 'Asus', 'Acer', 'Lenovo']
# print('before', laptops)
# laptops.remove('Lenovo')
# print('after', laptops)

# Method pop удаляет и возвращает элемент (по умолчанию удаляет последний элемент, но можно указать индекс элемента,
# который нужно удалитьпосле pop). Последний элемент можно сохранить, указав для него переменную.
# programming = ['c', 'python', 'js', 'go', 'java']
# print('before', programming)
# last_element = programming.pop(1)
# print('after', programming)
# print(last_element)

# Method index возвращает индекс элемента
# movies = ['Star wars', 'Harry Potter', 'Why him?', '1+1']
# print(movies.index('1+1'))
# number_in_list = movies.index('1+1')
# print(number_in_list)
# print(number_in_list + number_in_list)
# print(type(number_in_list))

# Method count считает количество элементов
# list1 = ['apple', 'orange', 'grapefruit', 'apple']
# print(list1.count('apple'))
# string = 'hello world'
# print(string.count('l'))
# new_list = list(string)
# print(new_list)

# Method reverse разворачивает список в другую сторону
# list1 = [1, 2, 3, 4, 5]
# print(list1)
# list1.reverse()
# print(list1)

# Перевод строки в список и метод reverse
# string = 'hello world'
# new = list(string)
# new.reverse()
# new_string = ''.join(new)
# print(new_string)

# Method sort сортирует элементы в списке по ключу
# numbers = [2, 3, 4, 5, 1]
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# list1 = ['apple', 'orange', 'grapefruit', 'apple']
# list1.sort(key=len)
# print(list1)
# list1.sort(key=len, reverse=True)
# print(list1)

# Method copy копирует список
# list1 = ['apple', 'orange', 'grapefruit', 'apple']
# new_list = list1.copy()
# print(new_list)
# print(list1)
# new_list.append('strawberry')
# print(new_list)

# Method extend расширяет список другим списком (складывает)
# nums = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums = nums + nums2
# print(nums)
# nums += nums2
# print(nums)
# nums.extend(nums)
# print(nums)

# Method clear очищает список
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(nums)
# nums.clear()
# print(nums)
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(nums[2])
# print(nums[0:6])

# Tuple (кортеж) - неизменяемый тип данных

# nums = (1, 2, 3, 4, 5, 6, 7, 1)
# print(nums.count(1))
# print(nums.index(3))