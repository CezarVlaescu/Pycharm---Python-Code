from tkinter import *
import pyperclip
import random

root = Tk()
root.geometry('700x700')
root.resizable(False, False)
root.title('Password generator')
passwordword = StringVar()
passwordlen = IntVar()
passwordlen.set(0)

def pass_gen():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ''
    for x in range(passwordlen.get()):
        password = password + random.choice(pass1)
    passwordword.set(password)

def pass_clip():
    random_password = passwordword.get()
    pyperclip.copy(random_password)

Label(root, text="Password Generator", font="Courier 30 bold").pack()
Label(root, text="By Caesar", font="Courier 20 italic").pack()
Label(root, text="Enter the number to get password").pack(pady=3)
Entry(root, textvariable=passwordlen).pack(pady=3)
Button(root, text="Generate", command=pass_gen).pack(pady=7)
Entry(root, textvariable=passwordword).pack(pady=3)
Button(root, text="Copy to clipboard", command=pass_clip).pack()
root.mainloop()

