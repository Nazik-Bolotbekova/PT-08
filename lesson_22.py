# from abc import ABC
#
# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
#
#     @abstractmethod
#     def walk(self):
#         pass
#
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name
#
#
#     def make_sound(self):
#         print('meow')
#
#
#     def eat(self):
#         print('eating')
#
#
#     def walk(self):
#         print('walking')
#


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def __str__(self):
        return f'{self.name},{self.age}'


    def __repr__(self):
        return f'User = {self.name}, age = {self.age}'





p = Person('nazik',16)

print(p)

print([p])


class Book:
    def __init__(self,pages):
        self.pages = pages


    def __add__(self, other):
        return Book(self.pages + other.pages)


    def __mul__(self, other):
        return Book(self.pages * other.pages)


    def __truediv__(self, other):
        return Book(self.pages / other.pages)


    def __isub__(self, other):
        self.pages -= other.pages
        return self


    def __mod__(self, other):
        return Book(self.pages % other.pages)


    def __pow__(self, other):
        return Book(self.pages ** other.pages)


    def __eq__(self, other):
        return Book(self.pages == other.pages)


    def __floordiv__(self, other):
        return Book(self.pages // other.pages)


    def __iadd__(self, other):
        self.pages += other.pages
        return self


    def __len__(self):
        return self.pages


    def __lt__(self, other):
      return  self.pages < other.pages


    def __gt__(self, other):
        return self.pages > other.pages


    def __ge__(self, other):
        return self.pages >= other.pages



b1 = 20
b2 = 30
c = b1 * b2
print(c)

b1 += b2
print(b1)

b2 -= b1
print(b2)

print(b1 == b2)

print(b1 > b2)
print(b1 < b2)

class School:
    def __init__(self,name,students):
        self.name = name
        self.students = students


    def __str__(self):
        return f'School name is {self.name}, number of students is {self.students}'


    def __repr__(self):
        return 'some code : aaazzzwwww'

some_school = School('shoha',2500)

print(some_school)

print([some_school])

#solid , class method , statistic method











