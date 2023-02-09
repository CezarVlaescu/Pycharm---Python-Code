import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('400x400')
root.resizable(True, True)
root.title('YouBet')

img = Image.open('Football_(soccer_ball).svg.png')
img = img.resize((300, 300))
test = ImageTk.PhotoImage(img)
label = tkinter.Label(image=test)
label.image = test
label.place(x=1.2, y=2)


root.mainloop()
