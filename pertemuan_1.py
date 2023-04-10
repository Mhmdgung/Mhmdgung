print("Hello World")

# a = 3
# b = 3

# if a == b:
#     print('A sama dengan B')
# else: 
#     print('A tidak sama dengan B')

# x = 5
# y = 'agung'
# print(type(x))
# print(type(y))

# a, b, c = "agung", "muhamad", "yoransah"
# print(a)
# print(b)
# print(c)

# a = b = "SMK"
# print(a)
# print(b)

# fruits = ['apple','manggo']
# x, y = fruits
# print(x)
# print(y)

# x = "agung"
# y = "muhamad"
# z = 'yoransah'
# print(x, y, z)

# x = "agung"
# y = "muhamad"
# z = 'yoransah'
# print(x + y + z)

# x = "Agung"

# def func():
#     x = "dimas"
#     print('Ganteng' + x)

# func()

# print('Ganteng banget ' + x)

# a = """hsgrehtrfyuejkdkfhjweg,
# kjefbjkerfbjjfb"""
# print(a)

# a = "Hello World"
# print(a[1])

# for x in "banana":
#     print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("ekspensive" not in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
    # print("yes, 'free' is present")

# a = "Agung"
# print(a.upper())

# a = " agung "
# print(a.strip())

# a = "Agung! Muhamad"
# print(a.split("!"))

# def sum_int_or_str(a, b):
#     return int(a) + int(b)

# assert(sum_int_or_str(1, '2')) == 3
# assert(sum_int_or_str(2, 2)) == 4

# def get_second_character(a):
#     if len(a) > 1:
#         return a[1]
#     else:
#         return 0
    
# assert(get_second_character("ab")) == "b"
# assert(get_second_character("a")) == 0

# car = {
#     'brand': 'toyota',
#     'year': 2022
# }

# print(car['brand'])

# assert(car['brand']) == 'toyota'

# cars = [
#     {
#         'brand': 'Toyota'
#     },
#     {
#         'brand': 'Honda',
#         'products': [
#             'civic'
#         ]
#     }
# ]

# print(cars[0]['brand'])

# assert(cars[1]['products'][0]) == 'civic'

# row_cars = 'toyota,honda,indiacar'

# assert(row_cars.split(",")) == ['toyota', 'honda', 'indiacar']

# # row_cars = row_cars.upper()
# assert(row_cars.upper().split(",")) == ['TOYOTA', 'HONDA', 'INDIACAR']

# raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'

# raw_cars = raw_cars.split(',')
# raw_cars = set(raw_cars)
# raw_cars = list(raw_cars)

# assert(raw_cars) == ['toyota', 'honda', 'indiacar']

# raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'
# raw_cars = raw_cars.split(',')
# raw_cars = set(raw_cars)
# raw_cars = len(raw_cars)
# assert(raw_cars) == 3
