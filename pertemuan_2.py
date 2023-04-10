# thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(thislist[2:5])

# thislist = ["apple","banana","cherry"]
# if "apple" in thislist:
#     print("yes apple is already exist")

# thislist = ["apple","banana","cherry","orange","kiwi","mango"]
# thislist[1:3] = ["blackcurrant","watermelon"]
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.insert(0,"watermelon")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.append("watermelon")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist2 = ["manggo"]

# thislist.extend(thislist2)
# print(thislist)

# thislist = ["apple","banana"]
# thislist.remove("apple")
# thislist.pop(0)
# print(thislist)

# thislist = ["apple","banana"]
# thislist.clear()
# print(thislist)

# thislist = ["apple","banana"]
# for x in thislist:
#     print(x)

# thislist = ["apple","banana"]
# i = 0
# while i <len(thislist):
#     print(thislist[i])
#     i = i  + 1

# thislist = ["apple","banana","manggo"]
# # [print(x) for x in thislist]
# thislist.pop(1)
# assert(thislist) == ["apple","manggo"]

# thislist.append("kiwi")
# assert(thislist) == ["apple","manggo","kiwi"]

# new_list = ["apple","apple","apple","apple","manggo","kiwi","apple","apple","apple","apple"]

# assert(new_list[4:6]) == ["manggo","kiwi"]

# new_list = ["apple","apple","apple","apple","manggo","kiwi","apple","apple","manggo","kiwi","apple","apple"]

# assert([x for x in new_list if x != "apple"]) == ["manggo","kiwi","manggo","kiwi"]

# list1 = [1,4,5,6,2,4]

# assert([x for x in list1 if x != 4]) == [1,5,6,2]

# assert([x for x in list1 if x == 4]) == [4,4]

# list1 = [1, 4, 5, 6, 2, 4]
# list2 = list1.copy()
# list2.pop()
# print(list1, list2)

# list1 = [1, 4, 5, 7]
# list3 = list1.copy()
# list3.pop()

# assert(list3) == [1, 4, 5]
# assert(list1) == list1

# tuple
# fruits = ("apple","banana","cherry","strawberry","rasberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# cars = {
#     'brand': 'honda',
#     'products': 'civic'
# }

# assert(list(cars.keys())[1]) == 'products'

# cars.update(
#     {
#         'year': 2023
#     }
# )

# def my_function(fname, lname):
#     return fname + " " + lname

# result = my_function("Agung","Muhamad")
# print(result)

# def my_function(*kids):
#     print(kids)
#     for kid in kids:
#         print(kid)

# my_function("Agung","Muhamad")

# def full_name(first_name, lastname):
#     print(first_name + " " + lastname)

# full_name(lastname="Muhamad", first_name="agung")

# def full_name_2(**full_name):
#     print(full_name)
#     print("First name is " + full_name['fname'], )

# full_name_2(fname="Agung", lname="muhamad")

# def upper_case_country(country = "Norway"):
#     print(country.upper())

# upper_case_country("Swiss")

# def multiply_by_two(free):
#     return 2 * free

# assert(multiply_by_two(3)) == 6

# def multiply_by_x(w, x = 2):
#     return w * x

# assert(multiply_by_x(3)) == 6
# assert(multiply_by_x(3, 1)) == 3

# user_input = input('input dikali dengan 2 : ')
# print(multiply_by_two(int(user_input)))

# how_many_input = input('Berapa kali input: ')
# i = 0
# while i < int(how_many_input):
#     user_input = input('input kali dengan 2: ')
#     print(multiply_by_two(int(user_input)))
#     i += 1

# how_many_input = input('Berapa kali input: ')
# i = 0
# while True:

#     if i == 0:
#         break

#     user_input = input('input kali dengan 2: ')
#     print(multiply_by_two(int(user_input)))
#     i += 1

# def avg(grades):
#     grade = 0
#     grades = grades.split(',')
#     for i in grades:
#         grade += float(i)
#     grade = grade/len(grades)
#     return grade

# how_many_input = input("Enter the number of students: ")

# students = []

# for i in range(int(how_many_input)):
#     nama = input('Enter the name: ')
#     grades = input('Enter the grade (comma-separated): ')
#     students.append(
#         {
#         'nama' : nama,
#         'grade' : grades,
#         'avg': avg(grades)
#         }
#     )

# print()
# print("average grades: ")
# for x in students:
#     print(x['nama'], ":", x['avg'])
