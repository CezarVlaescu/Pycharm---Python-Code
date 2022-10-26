from tkinter import *
from mendeleev import element


window = Tk()
window.geometry('1200x744')
window.title('Chemestry App')
window.resizable(False, False)

def click(item):
    global expression
    expression += str(item) # concatenare
    input_text.set(expression)

def stergere():
    global expression
    expression = ""
    input_text.set("")

expression = ''
input_text = StringVar()
input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)

window.mainloop()

