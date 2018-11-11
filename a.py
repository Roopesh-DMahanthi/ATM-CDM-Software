from tkinter import *

def home(root):
    root.destroy()
    root=Frame(tes)
    root.pack()
    root.columnconfigure(0, weight=10)
    root.rowconfigure(0, weight=10)
    button=Button(root,text="Sign Up",command=lambda: form(root),anchor=CENTER,bg="yellow",fg="red",padx=65,pady=10,font=("Helvetica", 16),relief="groove")
    p=Button(root,text="Login",command=lambda: login(root),anchor=CENTER,bg="pink",fg="blue",padx=75,pady=10,font=("Helvetica", 16),relief="groove")
    button.grid(row=140,column=50,pady=50,sticky="s")
    p.grid(row=180,column=50,sticky="n")

def login(p):
    p.destroy()
    root1=Frame(tes)
    root1.pack()
    label=Label(root1,text="Enter Login Id:",bg='#49E3CE',font=("Helvetica", 16))
    label.grid(row=10,column=20)
    e1=Entry(root1)
    e1.grid(row=10,column=30)
    label1=Label(root1,text="Enter PinNumber:",bg='#49E3CE',font=("Helvetica", 16))
    label1.grid(row=30,column=20)
    e2=Entry(root1)
    e2.grid(row=30,column=30)
    button=Button(root1,text="Back To Home Page",command=lambda: home(root1),anchor=CENTER,bg="Grey",fg="yellow",padx=65,pady=10,font=("Helvetica", 16),relief="groove")
    button.grid(row=50,column=20)
    root1.mainloop()



def form(p):
    p.destroy()
    root2=Frame(tes)
    root2.grid(row=1000,column=1000)
    root2["bg"]="#F0AE59"

    Name = Label(root2, text="Name: ", bg='#F0AE59')
    F_Name = Label(root2, text="Father Name: ", bg='#F0AE59')
    Passwd = Label(root2, text="Genreate U r Password: ", bg='#F0AE59')
    Address= Label(root2, text="Enter U R Address", bg='#F0AE59')

    Name.place(x=0, y=60)
    F_Name.place(x=0, y=100)
    Passwd.place(x=0, y=140)
    Address.place(x=0, y=180)


    name = StringVar()
    name_ent = Entry(root2, width=30, textvariable=name).place(x=150 , y=60)
    Father_Name= StringVar()
    F_Name_ent = Entry(root2, width=30, textvariable=Father_Name).place(x=150 , y=100)
    passwd= StringVar()
    passwd_ent = Entry(root2, width=30, textvariable=passwd).place(x=150 , y=140)
    address = StringVar()
    address_ent = Entry(root2, width=30, textvariable=address).place(x=150 , y=180)
    root2.mainloop()
tes=Tk()
tes.geometry('600x600')
test=Frame(tes)
test.pack()
home(test)
tes.mainloop()



