

nums=range(1,5)
a=list(map(lambda x : x **2, nums))
print(a)

str_nums=['10','20','30']
int_nums=list(map(lambda x : int(x),str_nums ))
print(int_nums)

hello='Hello world!'
cap=list(map(lambda x : x.upper(),hello))
cap1= ''.join(cap)
print(cap1)

nums123=[1,5,7]
multiply123=list(map(lambda  y : y * 2 , nums123))
print(multiply123)

names=['max','alex','john']
len_of_names=list(map(lambda x : len(x), names))
print(len_of_names)

nums1234=[1,-3,2,-5,8]
positive_nums=list(filter(lambda m : m >=0 , nums1234 ))
print(positive_nums)

just_nums=[i for i in range(1,7)]
even_numbs=list(filter(lambda y : y % 2 == 0, just_nums))
print(even_numbs)

words123=['hello','yes','world','hi']
len_words123=list(filter(lambda x :  len(x) > 4, words123))
print(len_words123)

nums1234 = [-1, 0, 5, 8]
bool_num=list(map(lambda y :  bool(y) > 0, nums1234))
print(bool_num)

numbers12=[1,2,3]
plus_five=list(map(lambda c : c + 5, numbers12))
print(plus_five)

theenums=[1,2,3]
prefix=list(map(lambda e : "№" + str(e),theenums))
print(prefix)

names = ["John", "peter", "Mary", "jane"]
capital_names=list(filter(lambda d :  d.istitle(), names))
print(capital_names)

prices = [10.5, 20, 5.99]
theprices=list(map(lambda y : f"{y:.2f}",prices))
print(theprices)

celsius = [0, 100, 20]
farengeit=list(map(lambda x : x * 9/5 + 32, celsius ))
print(farengeit)

phrases = ["hello world", "hi", "good morning", "yo"]
more_than_oneword=list(filter(lambda y : len(y.split(" ")) > 1, phrases))
print(more_than_oneword)

mixed = ["one", 2, "three", 4]
ints_only=list(filter(lambda w: str(w).isdigit(), mixed))
print(ints_only)

words123456 = ["hi", "hello"]
r=list(map(lambda y : y + "!", words123456))
print(r)

wordssssaa = ["apple", "orange", "kiwi", "grape"]
a_words=list(filter(lambda x : 'a' in x, wordssssaa))
print(a_words)

people = [{"name": "John", "age": 20}, {"name": "Anna", "age": 15}]
age_18=list(filter(  lambda x :   x.get("age") >= 18, people))
print(age_18)