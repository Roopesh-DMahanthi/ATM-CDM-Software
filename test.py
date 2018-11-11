import time
from tkinter import *

def fun(mainfram):
    mainfram.destroy()
    mainfram = Frame(root)
    mainfram.pack()
    button=Button(mainfram,text="Sign Up",command=lambda: fun1(mainfram),anchor=CENTER,bg="yellow",fg="red",padx=65,pady=10,font=("Helvetica", 16),relief=RAISED).grid(row=20,column=50)
    p=Button(mainfram,text="Login",command=mainfram.destroy,anchor=CENTER,bg="pink",fg="blue",padx=75,pady=10,font=("Helvetica", 16),relief=RAISED).grid(row=60,column=50)
def fun1(mainfram):
    
    mainfram.destroy()
    mainfram = Frame(root)
    mainfram.pack()
    button=Button(mainfram,text="Login",command=mainfram.destroy,anchor=CENTER,bg="yellow",fg="red",padx=65,pady=10,font=("Helvetica", 16)).pack()
    p=Button(mainfram,text="Sign Up",command=lambda: fun(mainfram),anchor=CENTER,bg="pink",fg="blue",padx=75,pady=10,font=("Helvetica", 16)).pack()

root = Tk()
root.geometry('600x600')
 
mainframe = Frame(root)
mainframe.grid(column=1000, row=1000)

l=Label(mainframe,text="Start").pack()
b=Button(mainframe,text="Press",command=lambda: fun(mainframe)).pack() 
root.mainloop() 

