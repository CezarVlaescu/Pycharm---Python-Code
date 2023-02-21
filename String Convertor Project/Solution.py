# Creating definited function for every operations

def toUpper(strs):
    return strs.upper()
def toReversed(strs):
    return strs[::-1]
def forVowels(strs):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(strs)):
        if strs[i] in vowels:
            count += 1
    return count
def words(strs):
    word = len(strs.split())
    return word
def title(strs):
    tit = strs.title()
    return tit

def isPalindrome(strs):
    return strs == strs[::-1]

def sortest(strs):
    short = min(strs.split(), key=len)
    long = max(strs.split(), key=len)
    return f"The shortest is {short} and the longest is {long}"

print("Welcome to my converter. Select the operation")
print("1. Upper a string")
print("2. Reverse a string")
print("3. Get the number of vowels from string")
print("4. Get the number of words from string")
print("5. Get the string as title")
print("6. Verify if the word is palindrome")
print("7. Print the sortest and the longest word from string")

def valid(choice):
    while not choice.isdigit():
        choice = input("Put a number please: ")
    return float(choice)

while True:
    UserChoice = input("Choice your operation (1/2/3/4/5/6/7) : ")
    numbers = ['1', '2', '3', '4', '5', '6', '7']
    if UserChoice in numbers:
        strs = input("Put a string : ")
        if UserChoice == '1':
            print(toUpper(strs))
        elif UserChoice == '2':
            print(toReversed(strs))
        elif UserChoice == '3':
            print(forVowels(strs))
        elif UserChoice == '4':
            print(words(strs))
        elif UserChoice == '5':
            print(title(strs))
        elif UserChoice == '6':
            print(isPalindrome(strs))
        elif UserChoice == '7':
            print(sortest(strs))
        keepGoing = input("Wanna do more operations? : ")
        if keepGoing.upper() == "NO":
            break
    else:
        print("Wrong value")









