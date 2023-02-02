# 1. Use for, split, if to create a statement that print out the words which start with letter 's'

# string = 'Print only the words that start with letter s in this sentence'
#
# for word in string.split():
#     if word[0] == 's': # startwith
#         print(word)

# 2. Use range to print all even numbers from 0, 10.

# for num in range(0, 10, 2):
#     print(num)

# 3. Use list comprehension to print all number from 1, 50 and divide by 3.
#
# my_list = [x for x in range(1, 50) if x % 3 == 0]
# print(my_list)

# 4. If the lenght of string is Even print even

# mystring = 'Print every word in this sentence that has an even number of letters'
#
# for word in mystring.split():
#     if len(word) % 2 == 0:
#         print(word)

# 5. Write a program that print the integers from 1 to 100. But for multiples of 3 print Fizz, for 5 print Buzz and for both print FizzBuss

# for num in range(1, 101):
#     if num % 5 == 0 and num % 3 == 0:
#         num = 'FizzBuzz'
#     elif num % 5 == 0:
#         num = 'Buzz'
#     elif num % 3 == 0:
#         num = 'Fizz'
#     print(num)

# 6. Use list comprehension to print the first letter of every element of string

# my_string = 'Create a list of first letters of every word of the string'
#
# my_list = [letter[0] for letter in my_string.split()]
# print(my_list)
#
