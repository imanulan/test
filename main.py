
# file = open('test1.txt','r')
# file.write('hello\n')
# file.writelines(['hello','john'])
# file.write('world')
# file.write('hello')
# print(file.read())
# print(file.read())

# f = file.read(2)
# print(f)
# print(f)

# print(file.readline())
# print(file.readlines())

# file.close()

# with open('test1.txt') as file:
#     print(file.read())



# JSON

## сериализация (с python в json) -> dump,dumps
## десериализация (с json в python) -> load,loads

# import json

# # d = {'hello': True, 'age': 2, 'name':None}
# # json_obj = json.dumps(d)
# # print(json_obj)
# # python_obj = json.loads(json_obj)
# # print(python_obj)


# with open('data.json','r') as file:
#     # python_obj = json.loads(file.read())
#     python_obj = json.load(file)
#     print(python_obj)


## OOP, GIT, PostgreSQL,(http,orm)


# class A:
#     amount = 0

#     # def __new__()
#     # def __init__()
#     # def __str__()
    

#     def info(self):
#         pass

#     @classmethod
#     def info2(cls):
#         pass

#     @staticmethod
#     def info3():
#         pass

# obj = A()    


# class A:
#     a = 2

# class B(A):
#     a = 3

# class C(A):
#     a = 4  

# class D(B,C):
#     a = 4      

# f = B()
# print(B.__mro__)


