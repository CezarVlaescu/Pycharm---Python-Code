# 1. Write a function that capitalize the first and the fourth letter of a string.

# def capitalize(text):
#     first_half = text[:3]
#     second_half = text[3:]
#     return first_half.capitalize() + second_half.capitalize()
#
# print(capitalize("macdonalds"))

# def capitalize(text):
#     first_letter = text[0]
#     inbetween = text[1:3]
#     fourth_letter = text[3]
#     rest = text[4:]
#     return first_letter.upper() + inbetween + fourth_letter.upper() + rest
#
# print(capitalize("abcdefghijklmnopq"))


# 2. Master Yoda : return a reversed sentence

# def master_yoda(text):
#     texted_split = text.split()
#     reverse = texted_split[::-1]
#     return " ".join(reverse)
#
# print(master_yoda("Buna ziua sunt Cezar"))

# 3 . Almost there : Given integer, return True if is within 10 of either 100 or 200

# def almost_there(n):
#     return (abs(100-n) <= 10) or (abs(200-n) <= 10)
#
# print(almost_there(200))