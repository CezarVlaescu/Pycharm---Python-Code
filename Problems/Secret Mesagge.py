print("Welcome to Secret Message printer")
print('\n Take a choice : [1] ENCODE or [2] DECODE \n')
choice = input('Your choice : ')

def funct_choice(choice):
    if choice == '1':
        encode()
    elif choice == '2':
        decode()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.']

def encode():
    codeword = input("Code word : ").lower()
    codeword_letters = [char for char in codeword]
    used_letters = []
    for letter in codeword_letters:
        if letter in used_letters:
            print('No repeating letters in codeword')
            exit()
        else:
            used_letters.append(letter)
    message = input("Your message : ")
    message_characters = [char for char in message]
    scrambled_chars = [char for char in codeword]
    for letter in alphabet:
        if letter in scrambled_chars:
            pass
        else:
            scrambled_chars.append(letter)
    output = " "
    for letter in message_characters:
        normal_index = alphabet.index(letter)
        output += scrambled_chars[normal_index]
    print("Encoded Message: " + output)

def decode():
    codeword = input("Code word : ").lower()
    codeword_letters = [char for char in codeword]
    used_letters = []
    for letter in codeword_letters:
        if letter in used_letters:
            print('No repeating letters in codeword')
            exit()
        else:
            used_letters.append(letter)
    message = input("Your message : ")
    message_characters = [char for char in message]
    scrambled_chars = [char for char in codeword]
    for letter in alphabet:
        if letter in scrambled_chars:
            pass
        else:
            scrambled_chars.append(letter)
    output = " "
    for letter in message_characters:
        scrambled_index = scrambled_chars.index(letter)
        output += alphabet[scrambled_index]

