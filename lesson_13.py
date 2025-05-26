# from hw_funct import is_even
# from main import words
#
# a=lambda c,b: c+b   # анонимная функ-ия лямбда
# x= a(3 ,5)
#
#
# multiply=lambda v : v*2
# print(multiply(5))
#
# add=lambda a,b,c: a+b+c
# n=add(2,7,5)
# print(n)
#
# square=lambda x: x ** x
# print(square(3))
#
# is_even=lambda x: x % 2 == 0
# print(is_even(2))
#
#
# nums=lambda a,b:  True if a > b else False
# print(nums(8,3))
#


# p=lambda a :sorted(a)
# print(p(words))
#
#
# sort=lambda x:sorted(x[-1])
# print(sorted(words, key = lambda x: x[-1]))
# print(sort(words))
#
#
# len_word=lambda x : len(x)
# print(len_word(words))
# print(sorted(words, key = lambda x: len(x)))
#
# def multiplyer(a):
#     return lambda x: x * a
# # # x=multiplyer(3)
# # print(x(7))
#
#
# a= map(lambda x : x.lower(),words) # первое это то что мы делаем с первым, а второе - объект по кот мы итерир
# print(list(a))
#
# num=[i for i in range(1,21)]
# print(num)
# a=map(lambda x:x * 2,num)
# print(list(a))
#
# b = filter(lambda x : x % 2 == 0, num)
# print(list(b))
#
#
word123=['apple', 'banana', '','watermelon', 'blueberry',"", 'poyato','']
# a=list(filter(lambda x : x != "" and '', word))
# print(a)
first=list(map(lambda x: x[0], filter(lambda a : a != "" and a != '', word123)))
print(first)

#
# nums=[i for i in range(1,21)]
# a = list(map(lambda y: y *2 , filter(lambda y: y % 2 != 0,nums)))
# print(a)
#
#
#
#
#
#
#
#
#
#
# # d=filter(lambda a:  len(a) > 5,words)
#
#
#
#
#


# # print(list(d))
#
# nums=[i for i in range(1,21)]
# d=85.00
# price=map(lambda x:x * d,nums)
# print(list(price))

