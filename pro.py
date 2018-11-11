from tkinter import *
from tkinter import messagebox
import sqlite3 
conn = sqlite3.connect('Database.db')
def main(p):
    p.destroy()
    root=Tk()
    filename = PhotoImage(file = "img2.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root["bg"]="red"
    root.minsize(600,500)
    root.maxsize(600,500)
    button=Button(root,text="Sign Up",command=lambda: form(root),anchor=CENTER,bg="yellow",fg="red",padx=65,pady=10,font=("Helvetica", 16),relief="groove")
    p=Button(root,text="Login",command=lambda: login(root),anchor=CENTER,bg="pink",fg="blue",padx=75,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=200,y=250)
    p.place(x=200,y=180)
    root.mainloop()

def login(p):
    p.destroy()
    root1=Tk()
    filename = PhotoImage(file = "img4.png")
    background_label = Label(root1, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    ac=StringVar()
    pn=StringVar()
    root1["bg"]="#49E3CE"
    root1.minsize(700,800)
    root1.maxsize(700,800)
    label=Label(root1,text="User-Name:",bg='white',font=("Helvetica", 16),image=filename,compound=CENTER)
    label.place(x=150,y=300)
    e1=Entry(root1,textvariable=ac)
    e1.place(x=360,y=305)
    label1=Label(root1,text="PIN:",bg='white',font=("Helvetica", 16))
    label1.place(x=150,y=350)
    e2=Entry(root1,textvariable=pn,show="*")
    e2.place(x=360,y=350)
    p=Button(root1,text="LOGIN",command=lambda: valid(root1,ac,pn),anchor=CENTER,bg="green",fg="black",padx=75,pady=10,font=("Helvetica", 16),relief="groove")
    p.place(x=220,y=430)
    root1.mainloop()


def valid(p,ac,pn):
    ac=ac.get()
    pn=int(pn.get())
    c.execute('select * from accounts where uname="%s" AND pi="%i"' % (ac,pn))
    l=c.fetchone()
    if(l!=None):
        home(p,l)
    else:
        messagebox.showerror("Invalid Account","User not Found")
        login(p)

def form(p):
    p.destroy()
    root2=Tk()
    filename = PhotoImage(file = "imgf.png")
    background_label = Label(root2, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root2["bg"]="#F0AE59"
    root2.minsize(650,600)
    root2.maxsize(650,600)
    label1=Label(root2,text="Register Account",font=("Helvetica",32))
    label1.place(x=150,y=150)
    Name = Label(root2, text="Name: ",font=("Helvetica", 16))
    Name.place(x=140, y=240)
    U_Name = Label(root2, text="User Name: ",font=("Helvetica", 16))
    U_Name.place(x=140, y=280)
    Mail = Label(root2, text="Enter Mail:",font=("Helvetica", 16))
    Mail.place(x=140, y=320)
    Pin= Label(root2, text="Enter Pin:",font=("Helvetica", 16))
    Pin.place(x=140, y=360)


    name = StringVar()
    name_ent = Entry(root2, width=30, textvariable=name).place(x=320 , y=240)
    u_name= StringVar()
    U_name = Entry(root2, width=30, textvariable=u_name).place(x=320 , y=280)
    email= StringVar()
    passwd_ent = Entry(root2, width=30, textvariable=email).place(x=320 , y=320)
    pin = StringVar()
    Pin_g = Entry(root2,show="*", width=30, textvariable=pin).place(x=320 , y=360)
    button=Button(root2,text="Submit",command=lambda: Clarification(root2,name,u_name,email,pin),anchor=CENTER,bg="Grey",fg="yellow",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=270,y=440)
    root2.mainloop()



def Clarification(p,name,u_name,email,pin):
    
    
    name=name.get()
    u_name=u_name.get()
    email=email.get()
    pin=pin.get()

    if(name==u_name):
        messagebox.showerror("Wrong Input","Name and User-Name cannot be same")
        form(p)
    elif(list(set(email)).count("@")!=1 or list(set(email)).count(".")<1):
        messagebox.showerror("Wrong Input","E-Mail FieldError")
        form(p)
    elif(len(pin)!=4):
        messagebox.showerror("Wrong Input","PIN should be four Digits")
        form(p)
    i=0
    while(i<4):
        if(pin[i]=="1" or pin[i]=="2" or pin[i]=="3" or pin[i]=="4" or pin[i]=="5" or pin[i]=="6" or pin[i]=="7" or pin[i]=="8" or pin[i]=="9" or pin[i]=="0"):
            i+=1
        else:
            messagebox.showerror("Wrong Input","PIN should contain Digits only")
            form(p)
            
    
    c.execute('select max(id) from accounts')
    lst=c.fetchone()
    lst=list(lst)
    acc=int(lst[0])+1
    pin=int(pin)
    p.destroy()
    root3=Tk()
    filename = PhotoImage(file = "img5.png")
    background_label = Label(root3, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root3.lift()
    root3.attributes('-topmost',True)
    
    root3["bg"]="white"
    root3.minsize(470,500)
    root3.maxsize(470,500)
    tex=Label(root3,text="Confirm Details",bg="white",fg="black",font=("Helvetica",45))
    tex.place(x=30,y=40)
    labelact=Label(root3,text="Acc No:",bg="white",fg="black",font=("Helvetica", 16))
    labelact.place(x=60,y=150)
    label=Label(root3,text="Name:",bg="white",fg="black",font=("Helvetica", 16))
    label.place(x=60,y=200)
    label2=Label(root3,text="User-Name:",bg="white",fg="black",font=("Helvetica", 16))
    label2.place(x=60,y=250)
    label3=Label(root3,text="Email:",bg="white",fg="black",font=("Helvetica", 16))
    label3.place(x=60,y=300)
    label3=Label(root3,text="Pin:",bg="white",fg="black",font=("Helvetica", 16))
    label3.place(x=60,y=350)
    #Entering Values...
    labelac=Label(root3,text=acc,bg="white",fg="black",font=("Helvetica", 16))
    labelac.place(x=230,y=150)
    labela=Label(root3,text=name,bg="white",fg="black",font=("Helvetica", 16))
    labela.place(x=230,y=200)
    label2a=Label(root3,text=u_name,bg="white",fg="black",font=("Helvetica", 16))
    label2a.place(x=230,y=250)
    label3a=Label(root3,text=email,bg="white",fg="black",font=("Helvetica", 16))
    label3a.place(x=230,y=300)
    label3a=Label(root3,text=pin,bg="white",fg="black",font=("Helvetica", 16))
    label3a.place(x=230,y=350)
    button=Button(root3,text="Confirm",command=lambda: conf(root3,name,u_name,email,pin,acc),anchor=CENTER,bg="Grey",fg="yellow",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=180,y=400)
    
    root3.mainloop()
    
    
def conf(p,name,u_name,email,pin,acc):
    bal=0
    c.execute("""insert into accounts values (?,?,?,?,?,?)""",(acc,u_name,pin,name,email,bal))
    conn.commit()
    login(p)


    
def home(p,l):
    
    p.destroy()
    root4=Tk()
    filename = PhotoImage(file = "img11.png")
    background_label = Label(root4, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root4["bg"]="black"
    root4.minsize(800,600)
    root4.maxsize(800,600)
    label=Label(root4,text="Welcome "+str.upper(l[3]),bg="yellow",fg="red",font=("Helvetica", 40))
    label.place(x=180,y=80)
    label2=Label(root4,text="Account Number:",bg="black",fg="white",font=("Helvetica", 16))
    label2.place(x=100,y=150)
    label3=Label(root4,text="Current balance:",bg="black",fg="white",font=("Helvetica", 16))
    label3.place(x=100,y=190)
    #Entering Values...
    labela=Label(root4,text=l[0],bg="black",fg="white",font=("Helvetica", 16))
    labela.place(x=300,y=150)
    label2a=Label(root4,text=l[5],bg="black",fg="white",font=("Helvetica", 16))
    label2a.place(x=300,y=190)
    button=Button(root4,text="Deposit Money",command=lambda: deposit(root4,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=30,y=300)
    button=Button(root4,text="Withdraw",command=lambda: withdraw(root4,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=220,y=300)
    button=Button(root4,text="Send Money",command=lambda: send(root4,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=360,y=300)
    button=Button(root4,text="Account Management",command=lambda: management(root4,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=525,y=300)
    button=Button(root4,text="Logout",command=lambda: main(root4),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=400,y=450)
    root4.mainloop()

def deposit(p,l):
    p.destroy()
    root5=Tk()
    filename = PhotoImage(file = "dep.png")
    background_label = Label(root5, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root5["bg"]="black"
    root5.minsize(600,500)
    root5.maxsize(600,500)
    labeld=Label(root5,text="Deposit",bg="black",fg="white",font=("Helvetica", 40))
    labeld.place(x=180,y=50)
    label=Label(root5,text="Current Balance:",bg="black",fg="white",font=("Helvetica", 16))
    label.place(x=60,y=150)
    label1=Label(root5,text="Add Amount:",bg="black",fg="white",font=("Helvetica", 16))
    label1.place(x=60,y=200)
    label2=Label(root5,text=l[5],bg="black",fg="white",font=("Helvetica", 16))
    label2.place(x=230,y=150)
    am=IntVar()
    e=Entry(root5,textvariable=am)
    e.place(x=230,y=205)
    button=Button(root5,text="ADD",command=lambda: ad(root5,am,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=250,y=300)
    button=Button(root5,text="Home",command=lambda: home(root5,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=140,y=400)
    button=Button(root5,text="Logout",command=lambda: main(root5),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=350,y=400)
    root5.mainloop()

def ad(p,bal,l):
    l=list(l)
    bal=int(bal.get())
    bal=l[5]+bal
    l[5]=bal
    c.execute('update accounts set bal="%i" where id="%i"' %(bal,l[0]))
    conn.commit()
    messagebox.showinfo("Deposit Amount","Money Successfully Added")
    deposit(p,l)


def withdraw(p,l):
    p.destroy()
    root6=Tk()
    filename = PhotoImage(file = "wit.png")
    background_label = Label(root6, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root6["bg"]="black"
    root6.minsize(600,500)
    root6.maxsize(600,500)
    labeld=Label(root6,text="Withdraw",bg="black",fg="white",font=("Helvetica", 40))
    labeld.place(x=180,y=50)
    label=Label(root6,text="Current Balance:",bg="black",fg="white",font=("Helvetica", 16))
    label.place(x=60,y=150)
    label1=Label(root6,text="Withdraw Amt",bg="black",fg="white",font=("Helvetica", 16))
    label1.place(x=60,y=200)
    label2=Label(root6,text=l[5],bg="black",fg="white",font=("Helvetica", 16))
    label2.place(x=250,y=150)
    am=IntVar()
    e=Entry(root6,textvariable=am)
    e.place(x=250,y=205)
    button=Button(root6,text="Withdraw",command=lambda: dec(root6,am,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=250,y=300)
    button=Button(root6,text="Home",command=lambda: home(root6,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=140,y=400)
    button=Button(root6,text="Logout",command=lambda: main(root6),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=350,y=400)
    root6.mainloop()

def dec(p,bal,l):
    l=list(l)
    bal=int(bal.get())
    if(bal>l[5]):
        messagebox.showerror("WithDraw Amount","Insufficient Balance in Account")
        withdraw(p,l)
    bal=l[5]-bal
    l[5]=bal
    c.execute('update accounts set bal="%i" where id="%i"' %(bal,l[0]))
    conn.commit()
    messagebox.showinfo("Withdraw Amount","Money Successfully Withdrawn")
    withdraw(p,l)


def send(p,l):
    p.destroy()
    root7=Tk()
    filename = PhotoImage(file = "tran.png")
    background_label = Label(root7, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root7["bg"]="black"
    root7.minsize(600,500)
    root7.maxsize(600,500)
    labeld=Label(root7,text="Money Transfer",bg="black",fg="white",font=("Helvetica", 40))
    labeld.place(x=130,y=50)
    label=Label(root7,text="Current Balance:",bg="black",fg="white",font=("Helvetica", 16))
    label.place(x=60,y=150)
    label1=Label(root7,text="Receiver Account-Number:",bg="black",fg="white",font=("Helvetica", 16))
    label1.place(x=60,y=200)
    label2=Label(root7,text="Amount to transfer:",bg="black",fg="white",font=("Helvetica", 16))
    label2.place(x=60,y=240)
    label2=Label(root7,text=l[5],bg="black",fg="white",font=("Helvetica", 16))
    label2.place(x=330,y=150)
    ac=IntVar()
    b=IntVar()
    e=Entry(root7,textvariable=ac)
    e.place(x=330,y=205)
    e2=Entry(root7,textvariable=b)
    e2.place(x=330,y=245)
    button=Button(root7,text="Send",command=lambda: tra(root7,l,ac,b),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=250,y=300)
    button=Button(root7,text="Home",command=lambda: home(root7,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=140,y=400)
    button=Button(root7,text="Logout",command=lambda: main(root7),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=350,y=400)
    root7.mainloop()

def tra(p,l,ac,b):
    b=int(b.get())
    ac=int(ac.get())
    l=list(l)
    if(b>l[5]):
        messagebox.showerror("Transfer Amount","Insufficient Balance in Account")
        send(p,l)
    
    c.execute('select * from accounts where id="%i"' %(ac))
    lst=c.fetchone()
    if(lst==None):
        messagebox.showerror("Invalid Account","Reciever Account not Found")
        send(p,l)
    b=l[5]-b
    l[5]=b    
    lst=list(lst)
    lst[5]=lst[5]+b
    c.execute('update accounts set bal="%i" where id="%i"' %(b,l[0]))
    conn.commit()
    c.execute('update accounts set bal="%i" where id="%i"' %(lst[5],ac))
    conn.commit()
    messagebox.showinfo("Transfer Amount","Money Successfully Transferred")
    withdraw(p,l)


def management(p,l):
    p.destroy()
    root8=Tk()
    filename = PhotoImage(file = "act.png")
    background_label = Label(root8, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root8["bg"]="black"
    root8.minsize(600,600)
    root8.maxsize(600,600)
    labeld=Label(root8,text="Account Managment",bg="black",fg="white",font=("Helvetica", 36))
    labeld.place(x=100,y=50)
    label=Label(root8,text="Change login Credentials",bg="black",fg="white",font=("Helvetica",20))
    label.place(x=140,y=150)
    button=Button(root8,text="Pin Change",command=lambda: pinn(root8,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button.place(x=70,y=200)
    button1=Button(root8,text="User-Name Change",command=lambda: un(root8,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button1.place(x=300,y=200)
    label1=Label(root8,text="Change Personal Details",bg="black",fg="white",font=("Helvetica", 20))
    label1.place(x=140,y=280)
    button2=Button(root8,text="Email Change",command=lambda: em(root8,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button2.place(x=70,y=350)
    button3=Button(root8,text="Account-Name Change",command=lambda: na(root8,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    button3.place(x=300,y=350)
    buttona=Button(root8,text="Home",command=lambda: home(root8,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttona.place(x=140,y=520)
    buttonb=Button(root8,text="Logout",command=lambda: main(root8),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonb.place(x=350,y=520)
    root8.mainloop()

def un(p,l):
    p.destroy()
    root9=Tk()
    filename = PhotoImage(file = "set.png")
    background_label = Label(root9, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root9["bg"]="black"
    root9.minsize(600,600)
    root9.maxsize(600,600)
    labeld=Label(root9,text="Account Managment",bg="black",fg="white",font=("Helvetica", 36))
    labeld.place(x=100,y=50)
    labela=Label(root9,text="Changing User-Name",bg="black",fg="white",font=("Helvetica", 20))
    labela.place(x=140,y=130)
    label=Label(root9,text="Old User-Name:",bg="black",fg="white",font=("Helvetica", 16))
    label.place(x=60,y=180)
    labelaa=Label(root9,text=l[1],bg="black",fg="white",font=("Helvetica", 16))
    labelaa.place(x=240,y=180)
    labele=Label(root9,text="New User-Name:",bg="black",fg="white",font=("Helvetica", 16))
    labele.place(x=60,y=230)
    ch=StringVar()
    e=Entry(root9,textvariable=ch)
    e.place(x=240,y=235)
    buttonc=Button(root9,text="Change",command=lambda: alt1(root9,l,ch),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonc.place(x=200,y=280)
    buttona=Button(root9,text="Home",command=lambda: home(root9,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttona.place(x=140,y=400)
    buttonb=Button(root9,text="Logout",command=lambda: main(root9),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonb.place(x=350,y=400)
    root9.mainloop()

def alt1(p,l,ch):
    ch=str(ch.get())
    l=list(l)
    l[1]=ch
    c.execute('update accounts set uname="%s" where id="%i"' %(ch,l[0]))
    conn.commit()
    messagebox.showinfo("Change Details","Changed User-Name Successfully")
    management(p,l)


def pinn(p,l):
    p.destroy()
    root9=Tk()
    filename = PhotoImage(file = "set.png")
    background_label = Label(root9, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root9["bg"]="black"
    root9.minsize(600,600)
    root9.maxsize(600,600)
    labeld=Label(root9,text="Account Managment",bg="black",fg="white",font=("Helvetica", 36))
    labeld.place(x=100,y=50)
    labela=Label(root9,text="Changing PIN",bg="black",fg="white",font=("Helvetica", 20))
    labela.place(x=140,y=130)
    label=Label(root9,text="Old PIN:",bg="black",fg="white",font=("Helvetica", 16))
    label.place(x=60,y=180)
    labelaa=Label(root9,text=l[2],bg="black",fg="white",font=("Helvetica", 16))
    labelaa.place(x=240,y=180)
    labele=Label(root9,text="New PIN:",bg="black",fg="white",font=("Helvetica", 16))
    labele.place(x=60,y=230)
    ch=IntVar()
    e=Entry(root9,textvariable=ch)
    e.place(x=240,y=235)
    buttonc=Button(root9,text="Change",command=lambda: alt2(root9,l,ch),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonc.place(x=200,y=280)
    buttona=Button(root9,text="Home",command=lambda: home(root9,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttona.place(x=140,y=400)
    buttonb=Button(root9,text="Logout",command=lambda: main(root9),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonb.place(x=350,y=400)
    root9.mainloop()

def alt2(p,l,ch):
    ch=int(ch.get())
    l=list(l)
    l[2]=ch
    c.execute('update accounts set pi="%i" where id="%i"' %(ch,l[0]))
    conn.commit()
    messagebox.showinfo("Change Details","Changed PIN Successfully")
    management(p,l)

def na(p,l):
    p.destroy()
    root9=Tk()
    filename = PhotoImage(file = "set.png")
    background_label = Label(root9, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root9["bg"]="black"
    root9.minsize(600,600)
    root9.maxsize(600,600)
    labeld=Label(root9,text="Account Managment",bg="black",fg="white",font=("Helvetica", 36))
    labeld.place(x=100,y=50)
    labela=Label(root9,text="Changing Acct Holder Name",bg="black",fg="white",font=("Helvetica", 20))
    labela.place(x=140,y=130)
    label=Label(root9,text="Old Name:",bg="black",fg="white",font=("Helvetica", 16))
    label.place(x=60,y=180)
    labelaa=Label(root9,text=l[3],bg="black",fg="white",font=("Helvetica", 16))
    labelaa.place(x=240,y=180)
    labele=Label(root9,text="New Name:",bg="black",fg="white",font=("Helvetica", 16))
    labele.place(x=60,y=230)
    ch=StringVar()
    e=Entry(root9,textvariable=ch)
    e.place(x=240,y=235)
    buttonc=Button(root9,text="Change",command=lambda: alt3(root9,l,ch),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonc.place(x=200,y=280)
    buttona=Button(root9,text="Home",command=lambda: home(root9,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttona.place(x=140,y=400)
    buttonb=Button(root9,text="Logout",command=lambda: main(root9),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonb.place(x=350,y=400)
    root9.mainloop()

def alt3(p,l,ch):
    ch=str(ch.get())
    l=list(l)
    l[3]=ch
    c.execute('update accounts set name="%s" where id="%i"' %(ch,l[0]))
    conn.commit()
    messagebox.showinfo("Change Details","Changed Account Holder Name Successfully")
    management(p,l)

def em(p,l):
    p.destroy()
    root9=Tk()
    filename = PhotoImage(file = "set.png")
    background_label = Label(root9, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root9["bg"]="black"
    root9.minsize(600,600)
    root9.maxsize(600,600)
    labeld=Label(root9,text="Account Managment",bg="black",fg="white",font=("Helvetica", 36))
    labeld.place(x=100,y=50)
    labela=Label(root9,text="Changing E-mail Address",bg="black",fg="white",font=("Helvetica", 20))
    labela.place(x=140,y=130)
    label=Label(root9,text="Old E-mail:",bg="black",fg="white",font=("Helvetica", 16))
    label.place(x=60,y=180)
    labelaa=Label(root9,text=l[4],bg="black",fg="white",font=("Helvetica", 16))
    labelaa.place(x=240,y=180)
    labele=Label(root9,text="New E-mail:",bg="black",fg="white",font=("Helvetica", 16))
    labele.place(x=60,y=230)
    ch=StringVar()
    e=Entry(root9,textvariable=ch)
    e.place(x=240,y=235)
    buttonc=Button(root9,text="Change",command=lambda: alt4(root9,l,ch),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonc.place(x=200,y=280)
    buttona=Button(root9,text="Home",command=lambda: home(root9,l),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttona.place(x=140,y=400)
    buttonb=Button(root9,text="Logout",command=lambda: main(root9),anchor=CENTER,bg="yellow",fg="red",padx=15,pady=10,font=("Helvetica", 16),relief="groove")
    buttonb.place(x=350,y=400)
    root9.mainloop()

def alt4(p,l,ch):
    ch=str(ch.get())
    l=list(l)
    l[4]=ch
    c.execute('update accounts set email="%s" where id="%i"' %(ch,l[0]))
    conn.commit()
    messagebox.showinfo("Change Details","Changed E-mail Address Successfully")
    management(p,l)

c = conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS accounts (
                id integer PRIMARY KEY,
                uname text NOT NULL,
                pi integer,
                name text,
                email text); """)


conn.commit()

test=Tk()
main(test)



