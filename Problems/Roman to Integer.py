# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 100, 'C': 100, 'D': 500, 'M': 1000}
s = input("Giving string: ")
number = 0

s = s.replace("IV", "IIII").replace("IX", "VIIII")
s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
for char in s:
    number += dict_roman[char]
print(number)



