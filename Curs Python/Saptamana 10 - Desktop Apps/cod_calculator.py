from tkinter import *

window = Tk()
window.geometry('500x354')
window.title('Calculator')
window.resizable(False, False)



def click(item):
    global expression
    expression += str(item) # concatenare
    input_text.set(expression)


def stergere():
    global expression
    expression = ""
    input_text.set("")

def egalitate():
    try:
        global expression
        rezultat = str(eval(expression))  # imi calculeaza ecuatia ,,eval"
        input_text.set(rezultat)
        expression = ""
    except Exception:
        expression = ""
        input_text.set("Eroare! Te rugam sa apesi tasta C")


expression = ''
input_text = StringVar()
input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)



window.mainloop()

