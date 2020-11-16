# Объекто - ориентированное программирование и классы

# Метод наследования
# Родительские и дочесрние классы (дочерние классы наследуют все методы и атрибуты родительского класса).

# class Dog():
#     def __init__(self, size, name):
#         self.size = size
#         self.name = name
#
#     def speak(self):
#         if self.size == 'small':
#             print('This is a small dog')
#         elif self.size == 'middle':
#             print('This is a middle dog')
#         elif self.size == 'large':
#             print('This is a large dog')
#
# class Doberman(Dog):
#     def __init__(self, name, size='large'):
#         self.name = name
#         self.size = size
#
#     def speak(self):
#         print('This dog is doberman')
#
# rex = Doberman('Rex')
# rex.speak()
#
# bobik = Dog('small', 'Bobik')
# bobik.speak()


# class Pet():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('We have a new pet.')
# obj1 = Pet('Bobik')

#     def talk(self):
#         print('.....')
#
# class Fish(Pet):
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#         print('We have a new fish.')
#
# class Cat(Pet):
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         print('We have a new cat.')
#
#     def talk(self):
#         print('Meow!')
#
# class Turtle(Pet):
#     def run(self, x, y):
#         self.x = x
#         self.y = y
#         print(f'Turtle has run distance {self.x + self.y} meters')


# class Dog(Pet):
#     def __init__(self, name, age, breed, size):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.size = size
#         print('We have a new dog.')
#
#     def speak(self):
#         if self.size == 'little' or self.size == 'medium':
#             print('Gav!')
#         elif self.size == 'large':
#             print('Woof!')
#
# dori = Fish('Dori', '1', 'blue')
# dori.talk()
#
# rex = Dog('Rex', '3', 'doberman', 'large')
# rex.speak()
#
# gray = Dog('Gray', '2', 'dachshund', 'medium')
# gray.speak()
#
# lily = Cat('Lily', '4', 'mainkun')
# lily.talk()
#
# donatello = Turtle('Donatello', 5)
# donatello.run(1, 2)


# class Animals():
#     def __init__(self, name):
#         self.name = name
#
#     def breath(self):
#         print(f'{self.name} is breathing')
#
#     def move(self):
#         print(f'{self.name} is moving')
#
#     def eat(self):
#         print(f'{self.name} is eating')
#
# class Mammals(Animals):
#     def feed_young_with_milk(self):
#         print('These animals are fed with milk.')
#
# class Giraffes(Mammals):
#     def eat_leaves_from_trees(self):
#         print('These animals are eating leaves from trees.')
#
# melman = Giraffes('Melmon')
# melman.breath()
# melman.move()
# melman.eat()
# melman.feed_young_with_milk()
# melman.eat_leaves_from_trees()