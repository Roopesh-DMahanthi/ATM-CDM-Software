from tkinter import *
from tkinter import messagebox
root=Tk()

label1=Label(root,text="\t\t\t\t\t HELLO HII \n\n\n \t\t\t\t\t ROOP")
img2 = PhotoImage(file="C:\\Users\\Roopesh\\Desktop\\Project\\img5.png")
label1.configure(image = img2, compound=RIGHT)
label1.pack()

root.mainloop()
