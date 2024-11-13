#Если все числа равны между собой, то вывести 3
first = 25
second = 25
third = 25

if first == second == third:
    print(3)

#Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
first = 25
second = 30
third = 25

if first == second or first == third or second == third:
    print(2)

#Если равных чисел среди 3-х вообще нет, то вывести 0
first = 25
second = 30
third = 25
if first != second or first!= third or second != third:
    print(0)





