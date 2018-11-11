'''from tkinter import *

root = Tk()


root.title('Unick Locker')

canvas = Canvas(root, width=730, height=600)

canvas.grid(row=0, column=0)

bgImg = PhotoImage(file="C:\\Users\\Roopesh\\Pictures\\ball.png")

canvas.create_image(370, 330, image=bgImg)

login = PhotoImage(file="C:\\Users\\Roopesh\\Pictures\\logo.png")

lo = Label(root, image=login)

lo.grid(row=0, column=0)

root.mainloop()'''

from tkinter import *
from tkinter import messagebox
top = Tk()
top.minsize(600,600)
C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\Roopesh\\Pictures\\logo1.png")
background_label = Label(top, image=filename)
background_label.grid(row=0,column=0)
l=Label(top,text="MY LOGO",font=("Helvetica", 26))
l.grid(row=0,column=0)




top.mainloop
