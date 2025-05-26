def ractangle_area(lenght,width):
    solution=lenght*width
    return solution

print(ractangle_area(4,5))


def to_seconds(hours,minuets):
    sec=(hours*3600)+(minuets*60)
    return sec

print(to_seconds(1,30))


def square(x):
    squared_num=x*x
    return squared_num

print(square(7))


def is_even(num):
    if num % 2 == 0 :
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))


def first_and_last(text):
    return text[0] + text[-1]


print(first_and_last('python'))


def compare(a, b ):
    if a > b :
        return "Больше"
    elif a < b :
        return "Меньше"
    elif a == b :
        return "Равны"

print(compare(10,5))
print(compare(3,9))
print(compare(7,7))


def count_letters(word):
    return len(word)

print(count_letters("python"))
print(count_letters("codinggg"))


def reverse_string(text):
    a=text[::-1]
    return a

print(reverse_string('hello'))
print(reverse_string('codify'))