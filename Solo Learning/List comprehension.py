import random

my_list = [x for x in range(0, 10) if x % 2 == 0]
print(my_list)

celsius = [0, 30, 24.5, 33]
ferenhait = [((9/5)*temp + 23.5) for temp in celsius if temp > 0]
print(ferenhait)

odd_numbers = [x for x in range(0, 100) if x % 3 == 0]
print(odd_numbers)

lotto = [y for y in range(6, 49)]
var = random.choice(lotto)
print(var)


