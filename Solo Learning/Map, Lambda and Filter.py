# 1. Map - return the instance of a function based by a list
def funct(num):
    return num**3

my_list = [1, 3, 5, 7]
for item in map(funct, my_list):
    print(item)

# char = '#'
# # empty_list = []
# # # n = int(input("Put your number : "))
# char1 = ''
#
# rows = 3
# columns = 3
#
# empty_list = [[char1] * columns] * rows
# empty_list[0][0] = char
# print(empty_list)

# m, n = 3, 3
# matrix = [[''] * n for i in range(m)]
# matrix[0][1] = '#'
# matrix[1][0] = '#'
# matrix[1][1] = '#'
# matrix[1][2] = '#'
# print(matrix)

# 2. Filter - filtring based by the function condition

# def check_even(num):
#     return num % 2 == 0
# my_list = [2, 3, 4, 5]
# for i in filter(check_even, my_list):
#     print(i)

# 3. Lambda - like a function

# square = lambda num : num % 2 == 0
# print(square(3))

# 4. Exemples with anonime functions combined
#
# my_list = [2, 3, 4, 5, 6, 7]
# print(list(map(lambda num: num % 2, my_list)))


