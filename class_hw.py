


class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        print('Some sound')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name,breed)

    def make_sound(self):
        print('Woof')


obj = Dog('sharik','bulldog')
print(obj.make_sound())
print(obj.name)
print(obj.breed)


class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

some_worker = Employee('minor','1134577')
print(some_worker.name)
print(some_worker.employee_id)


class Vehicle:
    def start_engine(self):
        print('Starting engine')


class Car(Vehicle):
    def start_engine(self):
        print('Pulling the car key')

class Truck(Vehicle):
    def start_engine(self):
        print('Ignition system activating..')

class Bike(Vehicle):
    def start_engine(self):
        print('initiating combustion to power')

car = Car()
car.start_engine()
truck = Truck()
truck.start_engine()
bike = Bike()
bike.start_engine()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def access_level(self):
        return 'Access granted'


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def access_level(self):
        if self.password == 1234:
            return'Access granted'
        else:
            return 'Access denied'

    def ban(self):
        print('You are banned')


class Moderator(User):
    def __init__(self, username, password):
        super().__init__(username,password)

    def access_level(self):
        if self.password == 1234:
            return 'Access granted'
        else:
            return 'Access denied'

    def change_someones_role(self):
            print('Changing roles')


class Guest(User):
    def __init__(self, username, register, password = None):
        super().__init__(username, password )
        self.register = register

    def access_level(self):
        if self.register.isalpha():
            return 'Access granted'
        else:
            return 'Error'

    def like_a_comment(self):
         print('You liked user`s comment')

admin = Admin('admin_1',1234)
print(admin.access_level())
admin.ban()

moderator = Moderator('moderator01', 1234)
print(moderator.access_level())
moderator.change_someones_role()

guest = Guest('guest01','someguest')
print(guest.access_level())
guest.like_a_comment()


class Loger:
    def log(self, message):
        pass


class Filelogger(Loger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open('filelogger.txt', 'a') as f:
            f.write(message)


class Consolelogger(Loger):
    def log(self, message):
        print(message)

fileik = Filelogger('filelogger.txt')
fileik.log('hello pycharm')

consol = Consolelogger()
consol.log('hello codify')


class Product:
    def __init__(self, name_of_the_product, quantity = 2):
        self.name_of_the_product = name_of_the_product
        self.quantity = quantity
        self.was_called = False

    def is_available(self):
        if self.quantity > 0:
            print('Is available')
            self.quantity -= 1
        else:
            print('Is not available')

class Book(Product):
    def __init__(self, name_of_the_product, author, quantity = 2 ):
        super().__init__(name_of_the_product,quantity)
        self.author = author

    def is_available(self):
        if self.quantity > 0:
            print(f'{self.name_of_the_product} by {self.author} is available')
            self.quantity -= 1
        else:
            print(f'{self.name_of_the_product} by {self.author} is not available')




class Electronika(Product):
    def __init__(self, name_of_the_product, warranty, quantity = 2):
        super().__init__(name_of_the_product, quantity)
        self.warranty = warranty

    def is_available(self):
        if self.quantity > 0:
            print(f'{self.name_of_the_product} with {self.warranty} year warranty is available')
            self.quantity -= 1
        else:
            print(f'{self.name_of_the_product} with {self.warranty} year warranty is not available')



some_book = Book('dorian gray', 'Wild Oskar')
some_book.is_available()
some_book.is_available()
some_book.is_available()

someelct = Electronika('Dishwasher', 3)
someelct.is_available()
someelct.is_available()
someelct.is_available()


class BankAccount:
    def __init__(self, owner, balance, cash_out):
        self.owner = owner
        self.balance = balance
        self.cash_out = cash_out

    def withdraw(self):
        if self.balance < self.cash_out:
            raise ValueError('Erorr')
        else:
            return self.balance - self.cash_out


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, cash_out, limit = 500):
        super().__init__(owner, balance, cash_out)
        self.limit = limit

    def withdraw(self):
        if self.balance - self.cash_out < self.limit:
            raise ValueError('Limit reached')
        else:
            return self.balance - self.cash_out


class CreditAccount(BankAccount):
    def __init__(self, owner, balance, cash_out, limit = -1000):
        super().__init__(owner, balance, cash_out)
        self.limit = limit

    def withdraw(self):
        if self.balance - self.cash_out < self.limit:
            raise ValueError('Limit reached')
        else:
            return self.balance - self.cash_out

mybank = BankAccount('Nazik', 1000, 900)
print(mybank.withdraw())

mysavings = SavingsAccount('Nazik', 1000, 100)
print(mysavings.withdraw())

mycredit = CreditAccount('Nazik', 1000, 500)
print(mycredit.withdraw())


class Animal:
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print('Meow')

class Dog(Animal):
    def make_sound(self):
        print('Woof')

class Cow(Animal):
    def make_sound(self):
        print('Moo')

class Sheep(Animal):
    def make_sound(self):
        print('Baaa bee')

class Bird(Animal):
    def make_sound(self):
        print('Chirip chirip')



#
# person={
#     'name' : 'Alisa',
#     'age' : 25 ,
#     'city' : 'Moscow'
# }
# person['job']='programmer'
# person['age']=18
# person.pop('city')
# a=person.get('name')
# print(person)
# print(a)
#
# students={'anna': 85, 'boris': 90, 'victor': 78, 'galina' : 92}
# print(max(students.values()))
#
# nums={i: i**2 for i in range(1,6)}
# print(nums)
#
# keys=['name','age','city']
# values=['ivan',30,'Moscow']
# thelist=zip(keys,values)
# getdict=list(thelist)
# finaldict=dict(getdict)
# print(finaldict)
#
# words = ["cat", "dog", "cat", "bird", "dog", "cat"]
# cat = 0
# dog = 0
# bird = 0
# for i in words:
#     if i == 'cat':
#         cat += 1
#     elif i == 'dog':
#         dog += 1
#     elif i == 'bird':
#         bird += 1
# print(cat , dog , bird)
# print(f"cat = {cat}, dog = {dog}, bird = {bird}")

# try:
#     file_ = open('est.txt' , 'r')
#     content = f.read()
#
#
#import pprint
#
# with open('est.txt','w') as f:
#     content=f.read()
#     for line in content:
#         print(line)
#     pprint.pprint(content)
#
# with open('est.txt','w') as f:
#     a = [i for i in range(1,21)]
#     for a in a:
#     f.write(str(a))

# file = open('est.txt', 'r')
# file_content = file.read()
# print(file_content)
# file.close()
#
# try:
#     file = open('est.txt', 'r')
#     contents = file.read()
#     print(contents)
# except Exception as e:
#     print(e)
#
# try:
#     file = open('est.txt', 'w')
#     file.write('hello pycharm')
# except Exception as e:
#     print(e)
#
#
# try:
#     file = open('est.txt', 'a')
#     file.write('hello hello')
# except Exception as e:
#     print(e)
#
# with open('est.txt','w') as f:
#     content=f.write()
#     print('aaaaa')
#     for line in content:
#         print(line)
#     pprint.pprint(content)

# with open('est.txt','w') as f:
#     a = [i for i in range(1,21)]
#     for an in a:
#         f.write(str(an))
#
# nums = [str(i) for i in range(1,21)]  # это writelines
# with open('est.txt', 'w' ) as f:
#     f.writelines(nums)
#
# nums12= [str(i) for i in range(1,51)]  #  это writeline  ****
# with open('est.txt', 'w') as f:
#     for num123 in nums12:
#         f.write('/n' + num123)

# import pprint
#
# data = {
#     'имя': 'Алиса',
#     'возраст': 30,
#     'интересы': ['программирование', 'чтение', 'музыка'],
#     'навыки': {
#         'Python': 'продвинутый',
#         'JavaScript': 'средний'
#     }
# }
#
# pprint.pprint(data)

# import pprint
#
# data = [
#     {'name': 'Alice', 'hobbies': ['reading', 'gaming', 'hiking'], 'age': 30},
#     {'name': 'Bob', 'hobbies': ['chess', 'music'], 'age': 25},
#     {'name': 'Charlie', 'hobbies': ['coding', 'traveling', 'photography', 'blogging'], 'age': 35}
# ]
#
# print("Обычный print:")
# print(data)
#
# print("\nС pprint:")
# pprint.pprint(data)
#
# #   homework






#######
