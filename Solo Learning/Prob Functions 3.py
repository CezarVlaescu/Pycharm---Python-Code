# 1. Write a function that counts the number of given times a patterns appear in a string, include overlap

# def overlap(pattern, text):
#     """
#     overlap('hah','hahahaha') = 3
#     'hahahah'.count('hah') returns 2
#
#     """
#     if pattern in text:
#         return text.count(pattern)
#
# print(overlap('hah', 'hahahah'))

# 2. Paper doll : Given string returns a string where every character in the original are three characters

# def paper_doll(string):
#     """
#     string = 'Mississippi'
#     return 'MMMiiissssssiiissssssiiippppppiii'
#     """
#     result = ''
#     for char in string:
#         result += char*3
#     return result
#
# print(paper_doll('Mississippi'))

# 3. Blackjack : Given 3 integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven reduce the total sum by 10.
# Finally, if the sum exceeds 21, return BUST.

# def blackjack(a, b, c):
#     var = a + b + c
#     if var >= 21:
#         return var
#     elif var < 21 and a or b or c == 11:
#         return var - 10
#     elif var < 21:
#         return 'BUST'
#
#
# print(blackjack(2, 11, 2))

# 4. Return sum of numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9. Return 0 for no numbers

# def summer_of_69(*arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total
#
# print(summer_of_69(3, 5, 6, 7, 8, 9))
# print(summer_of_69(1, 3, 5))


