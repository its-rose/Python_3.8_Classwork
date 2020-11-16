# Словари - это упорядоченная структура данных, которая хранит пары - ключ и значение
# dict_ = {}
# print(type(dict_))

# dict_with_pairs = {'Ключ' : 'Значение', ....}
# dict_ = {3: 1, 3.4: 2, 3: 2}

# Method fromkeys ввод данных в словарь
# names = {'name1': 'John', 'name2': 'Tom'}
# print(names['name2'])

# dictionary = dict()
# print(type(dictionary))

# dictionary1 = dict.fromkeys(['key1', 'key2'])
# print(dictionary1)
# dictionary2 = dict.fromkeys(['key1', 'key2'], ['val1', 'val2'])
# print(dictionary2)

# Извлечение данных из словаря
# dict1 = {'name': 'John', 'last name': 'Snow'}
# print(dict1['name'])
# print(dict1['last name'])

# dict1 = {1: 2, 2: 8, 3: 4}
# dict1[4] = 10 + 5
# print(dict1)
# dict1['key'] = 'val'
# print(dict1)
# dict1['dict2'] = {1: 2, 3: 4}
# print(dict1)
# print(dict1['dict2'][3])

# Method get получает по ключу значение
# cars = {'Mersedes': '221', 'BMW': '750i', 'Subaru': 'impreza'}
# print(cars.get('Subaru'))
# print(cars['Subaru'])

# Method keys вывод все ключи
# cars = {'Mersedes': '221', 'BMW': '750i', 'Subaru': 'impreza'}
# print(cars.keys())
# cars_list = cars.keys()
# print(cars_list)
# print(len(cars))
# Mersedes = cars.get('Mersedes')
# print(Mersedes)

# Method values (значения) выводит все значения
# cars = {'Mersedes': '221', 'BMW': '750i', 'Subaru': 'impreza'}
# print(cars.values())
# print(type(cars.values()))

# Method pop удаляет/вырезает по ключу и возвращает значение (можно сохранить в переменную вырезанный ключ)
# dict1 = {'first': '1st', 'second': '2nd', 'third': '3rd'}
# print(dict1)
# dict1.pop('first')
# print(dict1)

# Method popitem вырезает последнюю пару (ключ и значение), но возвращает только значение
# cars = {'Mersedes': '221', 'BMW': '750i', 'Subaru': 'impreza'}
# deleted = cars.popitem()
# print(deleted)
# print(cars)

# Method update объединяет словари в один
# laptops = {'lenovo': 'yoga', 'nacbook': 'pro', 'asus': 'zephyrus'}
# laptops2 = {'dell': 'allienware'}
# laptops.update(laptops2)
# print(laptops)

# Method setdefault похож на метод get - обращение по ключу (сохраняет значение по ключу)
# dict1 = {'key': 'val1', 'key2': 'val2', 'key3': 'val3'}
# new_dict = dict1.setdefault('key2')
# print(new_dict)
# new = dict1['key2']
# print(new)

# capitals = dict(Russia = 'Moscow', Kyrgyzstan = 'Bishkek')
# capitals2 = dict([('Russia', 'Moscow'), ('Kyrgyzstan', 'Bishkek)])
# print(capitals)
# print(capitals2)