# # # class Animal:
# #     def make_sound(self):
# #         print('Some sound')
# #
# #
# # class Cat(Animal):
# #     def make_sound(self):
# #         print('Meow')
# #
# #
# # class Dog(Animal):
# #     def make_sound(self):
# #         print('Bark!')
# #
# # cat = Cat()
# # cat.make_sound()
# # dog = Dog()
# # dog.make_sound()
# #
# #
# # class Human:
# #
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #
# #
# class Car:
#     type = 'electro car'
#
#     def __init__(self,brand,colour):
#         self.brand = brand
#         self.colour = colour
#     def draw(self):
#         print('Car is moving')
#
#
#     def check_engine(self):
#         self.engine = False
#
#
#     def start(self):
#         self.engine = True
#
#
# bmw = Car('bmw','red')
#
# print(bmw.type)
#
# print(bmw.colour)
#
# bmw.colour = 'black'
#
# print(bmw.colour)
#
# bmw.draw()

#
# class BankAcount:
#
#
#     def __init__(self,number,owner,balance = 0,):
#         self.number = number
#         self.balance = balance
#         self.owner = owner
#         self.transfers = []
#
#
#
#     def check_card(self):
#         print(self.balance)
#
#
#     def cash_in(self,amount):
#
#         self.balance += amount
#         print(self.balance)
#
#
#
#     def cash_out(self,amount):
#         self.balance -= amount
#         print(self.balance)
#
#
#
#
#
#
#
#
# nazik_account = BankAcount(1234567)
# nazik_account.check_card()
# nazik_account.cash_in(15000)
# nazik_account.check_card()
# nazik_account.cash_out(3000)


class Transport:
    def __init__(self, brand , color):
        self.brand = brand
        self.color = color


    def move(self):
        pass


class Auto(Transport):
    def __init__(self,brand,color,speed):
        super().__init__( brand, color )
        self.speed = speed


    def move(self):
        return self.speed


class Motorbike(Transport):
    def __init__(self,brand,color,speed):
        super().__init__(color, brand)
        self.speed = speed


    def move(self):
        return self.speed


class Walking:
    def walk(self):
        return 'walking'

class Flying:
    def fly(self):
        return 'flying'

class Bird(Flying,Walking):
    pass

bird = Bird()
print(bird.walk())
print(bird.fly())


class Player:
    def __init__(self, name , hp):
        self.name = name
        self.hp = hp

class Mac(Player):
    def __init__(self,name,hp,mana):
        super().__init__(name,hp)
        self.mana = mana

    def casting(self,target):
        if self.mana <= 0:
            raise Exception('You cant cast spell')
        else:
            self.mana -= 20
        return self.mana


pllayer = Mac('uran',500,200)
slave = Mac('tilek', 300)
print(pllayer.casting(slave))
print(pllayer.casting(slave))


class User:
    def __init__(self,username,balance):
        self.username = username
        self.balance = balance


    def role(self):
        return f'user , {self.username}'


class Admin(User):
    def __init__(self,username,permissions):
        super().__init__(username)
        self.permissions = permissions


    def role(self):
        return 'admin'


class Company(User):
    def role(self):
        return 'Company'















