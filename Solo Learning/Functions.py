# Find if dog is in my string with functions

def dog_check(mystring):
    return 'dog' in mystring.lower() # lower all the letters in string to find 'dog' even if it starts with a big letter

print(dog_check("My dog is cute"))

# Pig latin : if word starts with a vower, add 'ay' to the end, else first letter at the end and 'ay'

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

print(pig_latin('word'))

# *args si **kwargs

def calculator(a, b):
    return sum((a, b)) ** 0.05

print(calculator(3, 4))

def calc(*args): # args return a tuple
    return sum(args) * 0.05

print(calc(4, 5))

def my_funct(**kwargs): # kwargs return a dictionary
    if 'fruit' in kwargs:
        print(kwargs)
        return 'My favorite fruit of choice are {}'.format(kwargs['fruit'])
    else:
        return 'I did not find any fruit here'

print(my_funct(fruit='apple', veggie='onion'))

def function(*args, **kwargs):
    return "My favorite food is {} {}".format(args[0], kwargs['food'])

print(function(10, 20, 30, food='Burger', fruit='Bananas'))

