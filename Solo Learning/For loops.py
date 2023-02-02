# Objects in Python are iterable, means we can itarate over every item

# Exemples : even numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list: # Check the even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Number is odd : {num}")

# List sum

list_sum = 0 # initial list empty
for num in my_list: # for every elements on my list
    list_sum = list_sum + num  # I take my old value from list_sum and add the current number and resign the value to list_sum
print(list_sum) # if this print is in for loop will print the sum in row : 1 , 1+2(3), 1+2+3 (6) to the end 55

# Tuple unpacking

my_lista = [(1,2), (3,4), (5,6)]
for (a,b) in my_lista:
    print(a)
    print(b)

