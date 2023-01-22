import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)

upper1 = chr(random.randint(65, 90))
upper2 = chr(random.randint(65, 90))
var = chr(random.randint(30, 65))

password = upper1+upper2+var
password = shuffle(password)

print(password)
