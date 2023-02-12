# REGISTRATION PAGE:

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import ast

root=Tk()
root.title('Sign Up')
root.geometry('800x400+200+200')
root.configure(bg="white")
root.resizable(False, False)

def signin():
    first_name=fname.get()
    last_name=lname.get()
    email=email.get()
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()

    if password==confirm_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo('Sign Up','Successfully sign up')

        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid',"Both Password should match")


############-------------------
frame1=Frame(root,width=350, height=300, bg="blue")
frame1.place(x=400, y=10)
image=(Image.open("reg.jpg"))
resize_image=image.resize((400,350))
imagess=ImageTk.PhotoImage(resize_image)
lbl=Label(frame1, image=imagess, width=400, height=400)
lbl.pack()

frame=Frame(root, width=370, height=380, bg='white')
frame.place(x=50, y=10)

heading=Label(frame, text='Registration', fg="#917991", font=('Officina',23,'bold'))
heading.place(x=130, y=1)

############-------------------
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

############-------------------
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

############-------------------
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

############-------------------
def on_enter(e):
    email.delete(0, 'end')

def on_leave(e):
    name=email.get()
    if name=='':
        email.insert(0, 'Email address')

email=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
email.place(x=30, y=166)
email.insert(0, 'Email address')
email.bind('<FocusIn>', on_enter)
email.bind('<FocusOut>', on_leave)

Frame(frame, width=310, height=2, bg='black').place(x=25, y=191)

############--------------------
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

Frame(frame, width=310, height=2, bg='black').place(x=25, y=233)

##------------------------------
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

Frame(frame, width=310, height=2, bg='black').place(x=25, y=275)

############--------------------
check_value=IntVar
check_box=Checkbutton(text="I read and agree to Terms & Conditions?",fg='black',font=('Officina',7), variable=check_value)
check_box.place(x=90, y=290)

############--------------------
Button(frame, width=39, pady=7, text='Register', bg='#917991', fg='white', border=0, command=signin).place(x=35, y=305)
label=Label(frame, text="Already have an account?", fg='black', bg='white', font=('Officina',8))
label.place(x=100, y=344)

def signin():
    root.destroy()
    import Login

sign_up=Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#917991', command=signin)
sign_up.place(x=231, y=344)

root.bind('<Return>',lambda event:signin())

root.mainloop()
