# class Electronika:
#     def __init__(self,volt,work):
#         self.volt = volt
#         self.work = work
#
#
#     def working(self):
#         return 'working'
#
#
#     def check_volt(self):
#         return f'the volt id {self.volt}'
#
#
# class Human:
#     def __init__(self,health,work,name):
#         self.health = health
#         self.work = work
#         self.name = name
#
#     def check_health(self):
#         return f'healt is {self.health}'
#
#
#     def working(self):
#         return f'{self.name} is working'
#
#
# ploika = Electronika(100,'straightening')
# print(ploika.working())
# print(ploika.check_volt())
#
#
# class BankAccount:
#     def __init__(self,card_number,balance,cvv):
#         self.card_number = card_number
#         self._balance = balance
#         self.__cvv = cvv
#
#
#     def get_cvv(self,role):
#         if role != 'admin':
#             raise ValueError('Role must be Admin')
#         else:
#             return self.__cvv
#
#
#
#
#     def set_cvv(self,cvv,role):
#         self.__cvv = cvv
#         if role != 'admin':
#             raise ValueError("Role must be 'Admin")
#         else:
#              self.__cvv = cvv
#
#
#     @property
#     def cvv(self):
#         return self.__cvv
#
#
#     @cvv.setter
#     def cvv(self,cvv):
#          self.__cvv = cvv
#
#
# nazik = BankAccount('12345',1200,789)
#
# print(nazik.card_number)
#
# print(nazik._balance)
#
# print(nazik.cvv)
#
# print(nazik.set_cvv(567,'admin'))
#
# print(nazik.get_cvv('user'))
#
# print(nazik.cvv(456))
#
# print(nazik.cvv)
#
# nazik.cvv = 345
#
# print(nazik.cvv)



class CreditCard:
    def __init__(self, owner, balance,credit_number):
        self.owner = owner
        self._balance = balance
        self.__credit_number = credit_number

    def get_credit_number(self):
        return self.__credit_number

    @property
    def credit_card(self):
        return self.__credit_number


    def set_credit_number(self,credit_number):
        self.__credit_number = credit_number


    @credit_card.setter
    def credit_number(self,credit_number):
        self.__credit_number = credit_number

naz = CreditCard('nazik',5000,'3456789')
print(naz._balance)

print(naz.credit_number)
naz.credit_number = '2345678'
print(naz.credit_number)