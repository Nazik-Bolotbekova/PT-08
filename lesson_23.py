from abc import ABC, abstractmethod
#
#
# class Weather:
#     def __init__(self,gradus,flow):
#         self.gradus = gradus
#         self.flow = flow
#
#
#     @staticmethod
#     def farengeit_to_celsius(farengeit):
#         return (farengeit - 32) * 5/9
#
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#
#     @staticmethod
#     def area(a,b):
#         return a * b
#
# print(Rectangle.area(2,3))


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def from_dict(cls, data : dict):
        return cls(data)


    def __str__(self):
        return f'[name : {self.name}, age : {self.age}]'







class Math:


    @staticmethod
    def is_even(x : int):
        if x % 2 == 0:
            return "The number is even"
        else:
            return 'The number is not even'

print(Math.is_even(4))
print(Math.is_even(7))


class User:
    def __init__(self, name):
        self.name = name


    @classmethod
    def from_string(cls, name):
        return cls(name)


    def __str__(self):
        return f'Users name - {self.name}'

a = User.from_string('Nazik')
print(a)


