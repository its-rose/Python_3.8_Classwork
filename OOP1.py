# Объекто - ориентированное программирование и классы

# Создание классов

# class MyClass:
#     pass


# class Person():
#     pass
#
# Person.money = 150
#
# obj1 = Person()
# obj2 = Person()
# obj1.name = 'Bob'
# obj2.name = 'Masha'
# print(obj1.name, 'has', obj1.money, 'dollars')
# print(obj2.name, 'has', obj1.money, 'dollars')


# class Person():
#     name = ''
#     money = 0
#
# obj1 = Person()
# obj2 = Person()
#
# obj1.name = 'Bob'
# obj1.money = 200
# obj2.name = 'Masha'
#
# print(obj1.name, 'has', obj1.money, 'dollars')
# print(obj2.name, 'has', obj2.money, 'dollars')


# class Person():
#     name = ''
#     money = 0
#
#     def out(self):
#         print(self.name, 'has', self.money, 'dollars')
#
#     def change_money(self, new_money):
#         self.money = new_money
#
# # self - это ссылка на объект (на экземпляр класса)
#
# obj1 = Person()
# obj2 = Person()
#
# obj1.name = 'Bob'
# obj2.name = 'Masha'
#
# obj1.out()
# obj2.out()
#
# obj1.change_money(100)
# obj1.out()


# class Pet():
#     """Virtual pet"""
#
#     def __init__(self, name):  # метод-конструктор класса, срабатывает при создании нового объекта
#         print('We have new animal from class Pet')
#         self.name = name
#
#     def __str__(self):  # возращает строку, которая содержит значение атрибута name
#         rep = 'Object from class Pet\n'
#         rep += 'name: ' + self.name + '\n'
#         return rep
#
#     def talk(self):
#         print(f'Hello, I am a sample from class Pet. My name is {self.name}\n')
# pet1 = Pet('Bobik')
# pet1.talk()
# pet2 = Pet('Sharik')
# pet2.talk()
# print(pet1)
# print(pet2)


# class Pet():
#     total = 0
#
#     @staticmethod
#     def status():
#         print(f"\n Total number of animals now is {Pet.total}")
#
#     def __init__(self, name):
#         self.name = name
#         print('We have new animal from class Pet')
#         Pet.total += 1
#
# print(Pet.total)
#
# pet1 = Pet('Bobik')
# pet2 = Pet('Sharik')
# pet3 = Pet('Tuzik')
#
# Pet.status()


# Инкапсуляция - ограничение доступа к составляющим объект компонентам (методам и переменным)

# class A():
#     def _private(self): #- _ приватный метод
#         print('This is private method')
#
# a = A()
# a._private()
#
#
# class B:
#     def __private(self): #- __ закрытый метод
#         print('This is closed method')
#
# b = B()
# b.__private()

# b._B__private()


# class Pet():
#     def __init__(self, name, mood):
#         print('We have new pet')
#         self.name = name
#         self.__mood = mood
# 
#     def talk(self):
#         print('\My name is', self.name)
#         print('Now I feel', self.__mood, '\n')
# 
#     def __private_method(self):
#         print('This is closed method')
# 
#     def public_method(self):
#         print('This is public method')
#         self.__private_method()
# pet = Pet(name='Bobik', mood='fine')
# pet.talk()
# pet.public_method()
# pet._Pet__private_method()


# class Pet():
#     # конструктор класса, инициализирует 3 открытых атрибута
#     def __init__(self, name, hunger=0, boredom=0):
#         self.name = name
#         self.hunger = hunger
#         self.boredom = boredom
#
#     # закрытый метод увеличивающий чувство голода
#     def __pass_time(self):
#         self.hunger += 1
#         self.boredom += 1
#
#     # свойство отражает самочувствие питомца
#     @property    # этот декоратор обращается к свойствам в закрытом методе
#     def mood(self):
#         unhappiness = self.hunger + self.boredom
#         if unhappiness < 5:
#             m = 'fine'
#         elif 5 <= unhappiness <= 10:
#             m = 'normal'
#         elif 11 <= unhappiness <= 15:
#             m = 'bad'
#         else:
#             m = 'terrible'
#         return m
#
#     # метод сообщает о самочувствии питомца
#     def talk(self):
#         print('My name is', {self.name})
#         print('and now I feel', self.mood)
#
#     # метод снижает уровень голода питомца
#     def eat(self, food=4):
#         print('Thanks')
#         self.hunger -= food
#         if self.hunger < 0:
#             self.hunger = 0
#         self.__pass_time()
#
#     # метод снижает уровень уныния питомца
#     def play(self, fun=4):
#         print('Yes! I love playing!')
#         self.boredom -= fun
#         if self.boredom < 0:
#             self.boredom = 0
#         self.__pass_time()
#
# def main():
#     pet_name = input('What is the name of your pet: ')
#     pet = Pet(pet_name)
#     choice = None
#     while choice != '0':
#         print(
#             """
#             My pet
#             0 - exit
#             1 - how does he feel
#             2 - feed my pet
#             3 - play with my pet
#             """
#         )
#         choice = input('Your choice: ')
#         if choice == '0':
#             print('Bye!')
#         elif choice == '1':
#             pet.talk()
#         elif choice == '2':
#             pet.eat()
#         elif choice == '3':
#             pet.play()
#         else:
#             print(f'Sorry, there is no choice', {choice})
#
# main()
# input('Push Enter to quit')