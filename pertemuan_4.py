import datetime
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_my_name(self):
#             print('Hello my name is ' + self.name)

#     def change_my_name(self, new_name):
#          self.name = new_name

# class Student(Person):
     
#     def __init__(self, nisn, name, age):
#           super().__init__(name, age)
#           self.nisn = nisn

#     def say_by_name(self):
#      print('Im student ' + self.name)


# person_1 = Person('John', 18)
# person_1.name = 'agung'
# person_1.change_my_name('john')
# person_1.say_my_name()

# student_1 = Student('0089', 'agung', 12)
# student_1.say_my_name()
# # print(person_1.name)
# # print(person_1.age)
# # print(person_1.say_my_name())

# class Mathematic:

#     def __init__(self):
#          self.value = 0

#     def increment(self):
#          self += 2
         
#     def decrement(self):
#          self -= 2

#     def add(self, a, b):
#           return a + b
          
#     def substraction(self, a, b):
#         return a - b
    
#     def multiply(self, a, b):
#         return a + b
    
# math = Mathematic()

# print(math.add(1, 2))
# print(datetime.datetime.now())


# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#         self.door = 'Closed'
#         self.car = 'Off'

#     def open(self):
#         if self.door == 'Closed':
#             print('Door Has Opened')
#             self.door = 'Opened'
#         else:
#             print('Door Is Closed')

#     def close(self):
#         if self.door == 'Opened':
#             print('Door Has Closed')
#             self.door = 'Closed'
#         else:
#             print('Door Is Open')

#     def on(self):
#         if self.car == 'Off':
#             print('Machine Has On')
#             self.car = 'On'
#         else:
#             print('Machine Is Off')

#     def off(self):
#         if self.car == 'On':
#             print('Machine Has Off')
#             self.car = 'Off'
#         else:
#             print('Machine Is On')

    

# car_1 = Car('Honda', 2023)
# car_1.open()
# car_1.close()
# car_1.on()
# car_1.off()
