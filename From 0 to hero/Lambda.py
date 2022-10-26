# var1 = lambda x : x + 15
# print(var1(15))
# var2 = lambda x,y : x + y
# print(var2(1,2))

def funct(y):
    return lambda x : x * y

result = funct(2)
print('Dublul lui 15 este = ', result(15))