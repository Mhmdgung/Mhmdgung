import datetime
import math
import json
import os

# x = datetime.datetime.now()
# # print(x.year)
# print(x.strftime("%d.%m.%Y"))

# arr_1 = [5, 78, 2, 0]

# assert(min(arr_1)) == 0
# assert(max(arr_1)) == 78

# assert(pow(5, 5)) == 3125

# try:
#     f = open('demofile.txt')
#     try: 
#         f.write('Lorem Ipsum')
#     except:
#         print("Soemthing went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Soemthing went wrong when writing to the file")
# try:
#     x = 'hello world'
#     try:
#         print(x)
#     except:
#         print('Something went wrong')
#     finally:
#         print('The try except is finished')
# except:
#     print('Something went wrong')

# json
# x = '{"name":"John", "age":30, "city":"New York"}'

# # parse x
# y = json.loads(x)

# # hasil menjadi dictonary
# print(y["age"])

# dictonary
# x = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# # convert
# y = json.dumps(x)

# # hasil json (string)
# print(y)

# f = open("demofile.txt" , "r")
# print(f.read())

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# f = open("demofile2.txt", "r")
# print(f.read())

f = open('json_read.txt')

json_string = f.read()
print(json_string)

users = [
    {
        'email': "smkn@gmail.com",
        'pass': "123"
    },
    {
        'email': "smkn1@gmail.com",
        'pass': "123"
    }
]

json_string = json.dumps(users)

f = open('json_write.txt', "w")
f.write(json_string)
f.close()

def dump_and_write():
    pass


