# REGISTRATION PAGE:

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3 as sql

# creating a window:
root=Tk()

# window title:
root.title('Sign Up')
root.geometry('800x450+300+200')
root.configure(bg="white")
root.resizable(False, False)

git
##############--------------------------
# Image frame:
frame1=Frame(root,width=350, height=300)
frame1.place(x=400, y=10)
image=(Image.open("reg.jpg"))
resize_image=image.resize((400,350))
imagess=ImageTk.PhotoImage(resize_image)
lbl=Label(frame1, image=imagess, width=400, height=400)
lbl.pack()


##############--------------------------
# Creating database table:
try:
    conn=sql.connect('admin.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE users(
        fname text,
        lname text,
        username text PRIMARY KEY,
        mail text,
        pwd text,
        cpwd text,
        q1 text,
        q2 text,
        q3 text,
        status boolean
    )""" )
    conn.commit()
    conn.close()
except:
    pass


##############--------------------------
# to open another window:
# signup sunction:
def signup():
    def signin():
        root.destroy()
        import Login


##############--------------------------
# Registration frame:
    frame=Frame(root, width=370, height=380, bg='white')
    frame.place(x=50, y=10)

# Registration text:
    heading=Label(frame, text='Registration', fg="#917991", font=('Officina',23,'bold'), bg='white')
    heading.place(x=130, y=1)


##############--------------------------
# First name input:
# This function acts as placeholders so that when users click on the netry box, inserted text is deleted.
    def on_enter(e):
        fname.delete(0, 'end')

    def on_leave(e):
        name=fname.get()
        if name=='':
            fname.insert(0, 'First Name')

    fname=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
    fname.place(x=30, y=82)
    fname.insert(0,'First Name')
    # bind function:
    fname.bind('<FocusIn>', on_enter)
    fname.bind('<FocusOut>', on_leave)

    Frame(frame, width=145, height=2, bg='black').place(x=25, y=107)


##############--------------------------
# Last name input:
    def on_enter(e):
        lname.delete(0, 'end')

    def on_leave(e):
        name=lname.get()
        if name=='':
            lname.insert(0, 'Last Name')

    lname=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
    lname.place(x=190, y=82)
    lname.insert(0,'Last Name')
    # bind function:
    lname.bind('<FocusIn>', on_enter)
    lname.bind('<FocusOut>', on_leave)

    Frame(frame, width=154, height=2, bg='black').place(x=180, y=107)


##############--------------------------
# Username input:
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0, 'Username')

    user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
    user.place(x=30, y=124)
    user.insert(0,'Username')
    # bind function:
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=310, height=2, bg='black').place(x=25, y=149)


##############--------------------------
# Email input:
    def on_enter(e):
        mail_entry.delete(0, 'end')

    def on_leave(e):
        name=mail_entry.get()
        if name=='':
            mail_entry.insert(0, 'Email address')

    mail_entry=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
    mail_entry.place(x=30, y=166)
    mail_entry.insert(0, 'Email address')
    # bind function:
    mail_entry.bind('<FocusIn>', on_enter)
    mail_entry.bind('<FocusOut>', on_leave)

    Frame(frame, width=310, height=2, bg='black').place(x=25, y=191)


#############----------------------
# function to show password:
    def show():
        if (show1.get()==1):
            pwd.config(show='')
        else:
            pwd.config(show='*')

    def showw():
        if (show2.get()==1):
            c_pwd.config(show='')
        else:
            c_pwd.config(show='*')

##############--------------------------
# Password input:
    def on_enter(e):
        pwd.delete(0, 'end')

    def on_leave(e):
        name=pwd.get()
        if name=='':
            pwd.insert(0, 'Password')

    pwd=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
    pwd.place(x=30, y=208)
    pwd.insert(0, 'Password')
    # bind function:
    pwd.bind('<FocusIn>', on_enter)
    pwd.bind('<FocusOut>', on_leave)
    show1=IntVar(value=1)
    Checkbutton(text='Show', offvalue=0, variable=show1, bg='white', command=show).place(x=335, y=220)

    Frame(frame, width=310, height=2, bg='black').place(x=25, y=233)


##############--------------------------
# Confirm Password input:
    def on_enter(e):
        c_pwd.delete(0, 'end')

    def on_leave(e):
        name=c_pwd.get()
        if name=='':
            c_pwd.insert(0, 'Confirm Password')

    c_pwd=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
    c_pwd.place(x=30, y=250)
    c_pwd.insert(0, 'Confirm Password')
    # bind function:
    c_pwd.bind('<FocusIn>', on_enter)
    c_pwd.bind('<FocusOut>', on_leave)
    show2=IntVar(value=1)
    Checkbutton(text='Show', offvalue=0, variable=show2, bg='white', command=showw).place(x=335, y=265)

    Frame(frame, width=310, height=2, bg='black').place(x=25, y=275)

    
##############--------------------------
# verification function:
    def verify():
        a=fname.get()
        b=lname.get()
        c=mail_entry.get()
        d=user.get()
        e=pwd.get()
        f=c_pwd.get()
                
        if (a=="" or a=="First Name") or (b=="" or b=="Last Name") or (c=="" or c=="Enter Your Email") or (d=="" or d=="Enter Your Username") or (e=="" or e=="Create Password") or (f=="" or f=="Confirm Password"):
            messagebox.showerror("Error","One or More Fields Empty.")
        elif "@" and ".com" not in c:
            messagebox.showerror("Error","Invalid Email")
        elif len(e)<6 or len(f)<6:
            messagebox.showerror("Error","Password must be more than 6 characters")
        elif len(d)<2:
            messagebox.showerror("Error"," Username too short")
        elif e!=f:
            messagebox.showerror("Error","Passwords Mismatch")
        else:
            question()


##############--------------------------
# Already have an account text:
    label=Label(frame, text="Already have an account?", fg='black', bg='white', font=('Officina',8))
    label.place(x=100, y=344)

# Register/Sign up button:
    Button(frame, width=39, pady=7, text='Register', bg='#917991', fg='white', border=0, command=verify).place(x=35, y=305)


##############--------------------------
# function for security questions:
    def question():

        a=StringVar()
        b=StringVar()
        d=StringVar()
        
        frame2=Frame(bg='white', width=400, height=450).place(x=0, y=0)
        Label(frame2,text="Security Questions",font=('Officina',20,'bold'),fg='#917991',bg='white').place(x=100,y=10)

        Label(frame2,text="Q1: What is your favourite food?",fg='#917991',bg='white',font=('Officina',12)).place(x=30,y=100)
        Entry(width=50,textvariable=a).place(x=30, y=130)
        
        Label(text="Q2: What is the name of your first pet?",fg='#917991',bg='white',font=('Officina',12)).place(x=30,y=190)
        Entry(width=50,textvariable=b).place(x=30, y=220)

        Label(text="Q3: What is the name of your childhood best friend?",fg='#917991',bg='white',font=('Officina',12)).place(x=30,y=280)
        Entry(width=50,textvariable=d).place(x=30, y=310)


##############--------------------------
#verification for security questions
        def verifyy():
            aa=a.get()
            bb=b.get()
            cc=d.get()

            if aa=="" or bb=="" or cc=="":
                messagebox.showerror("Security Questions","One or more fields empty")
            else:
                submit()

        #database connection for signup
        def submit():
            conn=sql.connect('admin.db')
            c=conn.cursor()
            c.execute("INSERT INTO users VALUES (:fname, :lname, :mail_entry, :user, :pwd, :cpwd, :q1, :q2, :q3, :status)",
            {
                'fname':fname.get(),
                'lname':lname.get(),
                'mail_entry':mail_entry.get(),
                'user':user.get(),
                'pwd':pwd.get(),
                'cpwd':c_pwd.get(),
                'q1':a.get(),
                'q2':b.get(),
                'q3':d.get(),
                'status':False
                })
            conn.commit()
            conn.close()

            messagebox.showinfo("Signup","User Registered Successfully")

            signin()

# Confirm_buttom:
        #signup button
        Button(text="Confirm",font=('Officina',12,'bold'),fg='white',bg="#917991",width=16,height=1,cursor='hand2',command=verifyy).place(x=120, y=360)
            #(complete registration is done with above questions)


##############--------------------------
# Sign_in button:(Back to Login Page button)
    sign_in=Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#917991', command=signin)
    sign_in.place(x=231, y=344)

    root.bind('<Return>',lambda event:signup())

signup()

root.mainloop()
