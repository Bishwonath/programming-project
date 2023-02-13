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


##############--------------------------
# to open another window:
def signin():
    root.destroy()
    import Login


##############--------------------------
# NEEDS TO BE MODIFIED ALOT OR DELETED:
# Signin function:



##############--------------------------
# Image frame:
frame1=Frame(root,width=350, height=300, bg="blue")
frame1.place(x=400, y=10)
image=(Image.open("reg.jpg"))
resize_image=image.resize((400,350))
imagess=ImageTk.PhotoImage(resize_image)
lbl=Label(frame1, image=imagess, width=400, height=400)
lbl.pack()


##############--------------------------
# Registration frame:
frame=Frame(root, width=370, height=380, bg='white')
frame.place(x=50, y=10)

# Registration text:
heading=Label(frame, text='Registration', fg="#917991", font=('Officina',23,'bold'))
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
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=310, height=2, bg='black').place(x=25, y=149)


##############--------------------------
# Email input:
def on_enter(e):
    email_entry.delete(0, 'end')

def on_leave(e):
    name=email_entry.get()
    if name=='':
        email_entry.insert(0, 'email address')

email_entry=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
email_entry.place(x=30, y=166)
email_entry.insert(0, 'email address')
email_entry.bind('<FocusIn>', on_enter)
email_entry.bind('<FocusOut>', on_leave)

Frame(frame, width=310, height=2, bg='black').place(x=25, y=191)


#############----------------------
# function to show password:
def show():
    if (show1.get()==1):
        code.config(show='')
    else:
        code.config(show='*')

def showw():
    if (show2.get()==1):
        confirm_code.config(show='')
    else:
        confirm_code.config(show='*')

##############--------------------------
# Password input:
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')

code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
code.place(x=30, y=208)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
show1=IntVar(value=1)
Checkbutton(text='Show', offvalue=0, variable=show1, bg='white', command=show).place(x=335, y=220)
Frame(frame, width=310, height=2, bg='black').place(x=25, y=233)


##############--------------------------
# Confirm Password input:
def on_enter(e):
    confirm_code.delete(0, 'end')

def on_leave(e):
    name=confirm_code.get()
    if name=='':
        confirm_code.insert(0, 'Confirm Password')

confirm_code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
confirm_code.place(x=30, y=250)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)
show2=IntVar(value=1)
Checkbutton(text='Show', offvalue=0, variable=show2, bg='white', command=showw).place(x=335, y=265)
Frame(frame, width=310, height=2, bg='black').place(x=25, y=275)

def signup():
    first_name=fname.get()
    last_name=lname.get()
    email=email_entry.get()
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()
    conn=sql.connect("registration.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS register(
    first_name text,
    last_name text,
    email text,
    username text,
    password text
    
    
    )""")

    conn=sql.connect("registration.db")
    c=conn.cursor()
    c.execute("INSERT INTO register VALUES(:first_name,:last_name,:email,:username,:password)",{
        "first_name":fname.get(),
        "last_name":lname.get(),
        "email":email_entry.get(),
        "username":user.get(),
        "password":code.get()
        })
    conn.commit()
    conn.close()


    # if password==confirm_password:
    #     try:
    #         file=open('datasheet.txt','r+')
    #         d=file.read()
    #         r=sql.literal_eval(d)

    #         dict2={username:password}
    #         r.update(dict2)
    #         file.truncate(0)
    #         file.close()

    #         file=open('datasheet.txt','w')
    #         w=file.write(str(r))

    #         messagebox.showinfo('Sign Up','Successfully sign up')

    #     except:
    #         file=open('datasheet.txt','w')
    #         pp=str({'Username':'password'})
    #         file.write(pp)
    #         file.close()

    # else:
    #     messagebox.showerror('Invalid',"Both Password should match")
##############--------------------------
# Register/Sign up button:
Button(frame, width=39, pady=7, text='Register', bg='#917991', fg='white', border=0, command=signup).place(x=35, y=305)

# Aleready have an account text:
label=Label(frame, text="Already have an account?", fg='black', bg='white', font=('Officina',8))
label.place(x=100, y=344)

# Sign_in button:
sign_in=Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#917991', command=signin)
sign_in.place(x=231, y=344)

root.bind('<Return>',lambda event:signin())

root.mainloop()
