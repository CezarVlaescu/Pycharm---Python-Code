# While - when we have a boolean condition, and we need to do something

x = 0
while x < 5:
    print(f"x value is : {x}")
    x += 1

# Break - breaks the current, close the loop
# Continue - Goes to the top of the closing loop
# Pass - Does nothing

my_string = "Cezar"
for letter in my_string:
    if letter == "a":
        # continue # print without the statement, goes back to for loop ( at beginning ) and run again ( C e z r )
        # break # print the string, but stops at statement and all after ( C e z )
        pass # Nothing
    print(letter)

# Other exemple

y = 0
while y < 5:
    if y == 2:
        continue
    print(y)
    y += 1
