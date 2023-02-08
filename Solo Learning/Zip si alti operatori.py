# Range - work on the principle ( start, final, step )

for num in range(0, 10, 2):
    print(num) # print even numbers

index_count = 0
word = 'abcde'
for letter in 'abcde':
    print('The is letter {} on string {}'.format(letter, index_count))
    index_count += 1

# Enumerate - print every item from a string with the specific index as a tuple

for oul in enumerate(word):
    print(oul)

# Zip - its a kind of enumarate, doing same thing

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']
for item in zip(list_1, list_2):
    lista = []
    lista.append(item)
    print(lista)

# from random import randint
#
# number = randint(0,100)
# print('Your number is {}'.format(number))
