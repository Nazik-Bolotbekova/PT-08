a=[i for i in range(1,11)]
b=[i**2 for i in a ]
print(b)

a=[i for i in range(0,21)]
b=[i for i in a if i % 2 == 0]
print(b)

some_str='hello world'
myset=[ a for a in some_str if a != ' ']
theset=set(myset)
print(theset)

nums=[-5,3,-1,0,2,-7]
x=[i for i in nums if i >= 1]
print(x)

fruits=['kiwi','banana','apple']
fruits_dict={x: len(x) for x in fruits}
print(fruits_dict)

words=['hi','hello','ok','yes','no']
a=[len(a) for a in words ]
settt=set(a)
print(settt)

float_nums=[3.2,4.8,5.5,6.9]
b=[round(a) for a in float_nums]
print(b)

a=[i for i in range(1,6)]
b={x:  "четное"  if x % 2 == 0 else "нечетное" for x in a}
print(b)

a=[x for x in range(1,11)]
b=[x**2 for x in a if x % 2 != 0]
print(b)

dicttttt={'a':1,'b':2,'c':3}
new_dict={x : a for a ,x in  dicttttt.items()}
print(new_dict)
