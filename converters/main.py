from converters.length import *
from converters.weight import *

print('Выберите тип конвертации:')
print('1. кг - г')
print('2. км - м')

choice = input("Ваш выбор..")

if choice == '1':
    user_number = int(input('Введите число:'))
    from_kg_to_grm(user_number)
elif choice == '2':
    user_number = int(input('Введите число:'))
    from_km_to_m(user_number)
