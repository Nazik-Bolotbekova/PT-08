from datetime import date


class User:
    def __init__(self, password):
        self._password = password

    def check_password(self):
        return self._password

some_user = User('123456789')
print(some_user.check_password())


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    # def get_balance(self):
    #     return self.__balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError('The balance cannot be negative')
        else:
            self.__balance = balance

    # def set_balance(self, balance):
    #     if self.__balance < 0:
    #         raise ValueError('Error, negative balance')
    #     else:
    #          self.__balance = balance

# owner = BankAccount(500)
# owner.balance = 1000
# print(owner.balance)
# owner.balance = -100
# print(owner.balance)
# print(owner.get_balance())
# print(owner.set_balance(700))
# # print(owner.get_balance())
# print(owner.get_balance)

class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > self.__age:
            self.__age = new_age
        else:
            raise ValueError('Age must be greater than the current one')

# nazik = Person(15)
# print(nazik.age)
# nazik.age = 16
# print(nazik.age)
# nazik.age = 8
# print(nazik.age)

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError('The number is negative')

        elif amount < 30_000:
            raise ValueError('Salary cannot be lower than 30.000')

        elif not isinstance(amount, int):
            raise ValueError('Salary must be a number')

        elif amount > 100_000_000:
            raise ValueError('Unrealistic salary')

        else:
            self.__salary = amount

    def __str__(self):
        return f'Salary is set to {self.__salary}'

some_worker = Employee(50_000)
print(some_worker)
some_worker.salary = 100_000
print(some_worker)

class Freelancer:
    def __init__(self, income):
        self.__income = income

    @property
    def tax_income(self):
        return self.__income - (self.__income * 13/100)

u1 = Freelancer(2000)
print(u1.tax_income)


class User:
    def __init__(self, email):
        self.__email = email

    @property
    def get_email(self):
        return self.__email

u2 = User("@somemail.com")
print(u2.get_email)

class Article:
    def __init__(self, title):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) > 20:
            raise ValueError('The article must not be longer than 20 characters')
        else:
            self.__title = title

some_news = Article('Exams are starting soon')
print(some_news.title)
# some_news.title = 'Exam results are already out'
# print(some_news.title)
some_news.title = 'Attention'
print(some_news.title)


class Order:
    def __init__(self, id_):
        self.__id_ = id_

    @property
    def id_(self):
        return self.__id_

some_order = Order('1234567')
print(some_order.id_)

class PersonNumberTwo:
    def __init__(self, birth_year):
        self.__birth_year = birth_year

    @property
    def age(self):
        today = date.today()
        return today.year - self.__birth_year

nazik = PersonNumberTwo(2009)
print(nazik.age)








