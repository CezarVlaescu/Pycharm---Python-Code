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

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg='#eee', bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()

frame_buttoane = Frame(window, width=500, height=304, bg='grey')
frame_buttoane.pack()

Button(frame_buttoane, text='C', width=37, height=3, bg='#eee', cursor='hand2',
       command=lambda: stergere()).grid(row=0, column=0, columnspan=3)

Button(frame_buttoane, text='/', width=10, height=3, bg='#FFA500', cursor='hand2',
                  command=lambda: click('/')).grid(row=0, column=3)

Button(frame_buttoane, text='7', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('7')).grid(row=1, column=0)
Button(frame_buttoane, text='8', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('8')).grid(row=1, column=1)
Button(frame_buttoane, text='9', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('9')).grid(row=1, column=2)
Button(frame_buttoane, text='*', width=10, height=3, bg='#FFA500', cursor='hand2',
                  command=lambda: click('*')).grid(row=1, column=3)

Button(frame_buttoane, text='4', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('4')).grid(row=2, column=0)
Button(frame_buttoane, text='5', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('5')).grid(row=2, column=1)
Button(frame_buttoane, text='6', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('6')).grid(row=2, column=2)

Button(frame_buttoane, text='-', width=10, height=3, bg='#FFA500', cursor='hand2',
                  command=lambda: click('-')).grid(row=2, column=3)

Button(frame_buttoane, text='1', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('1')).grid(row=3, column=0)
Button(frame_buttoane, text='2', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('2')).grid(row=3, column=1)
Button(frame_buttoane, text='3', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('3')).grid(row=3, column=2)

Button(frame_buttoane, text='+', width=10, height=3, bg='#FFA500', cursor='hand2',
                  command=lambda: click('+')).grid(row=3, column=3)

Button(frame_buttoane, text='0', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('0')).grid(row=4, column=0)
Button(frame_buttoane, text='.', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('.')).grid(row=4, column=1)
Button(frame_buttoane, text='00', width=10, height=3, bg='#eee', cursor='hand2',
               command=lambda: click('00')).grid(row=4, column=2)

Button(frame_buttoane, text='=', width=10, height=3, bg='#FFA500', cursor='hand2',
                  command=lambda: egalitate()).grid(row=4, column=3)


window.mainloop()

