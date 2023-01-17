# LOG IN PAGE:

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import ast

root=Tk()
root.title('Login')
root.geometry('800x400+200+200')
root.configure(bg="white")
root.resizable(False, False)

############-------------------
def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text="Hello Everyone!", bg='white', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()

    elif username!='admin' and password!='1234':
        messagebox.showerror("Error","Invalid username and password")

    elif password!="1234":
        messagebox.showerror("Error","Invalid password")

    elif username!="admin":
        messagebox.showerror("Error","Invalid Username")


############--------------------
frame1=Frame(root,width=350, height=300, bg="blue")
frame1.place(x=60, y=40)
image=(Image.open("task.png"))
resize_image=image.resize((310,330))
imagess=ImageTk.PhotoImage(resize_image)
lbl=Label(frame1, image=imagess, width=300, height=300)
lbl.pack()
  
frame=Frame(root, width=350, height=390, bg='white')
frame.place(x=400, y=50)

heading=Label(frame, text='Log In', fg="#917991", font=('Officina',23,'bold'))
heading.place(x=130, y=1)

############--------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

############--------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')

code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

############---------------------
Button(frame, width=39, pady=7, text='Login', bg='#917991', fg='white', border=0, command=signin).place(x=35, y=204)
label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Officina',8))
label.place(x=100, y=270)

sign_up=Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#917991')
sign_up.place(x=220, y=270)

root.bind('<Return>',lambda event:signin())

root.mainloop()

