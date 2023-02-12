# LOG IN PAGE:

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3 as sql
import os


# creating a window:
root=Tk()

# window title:
root.title('Login')
root.geometry('800x400+200+200')
root.configure(bg="white")
root.resizable(False, False)


############----------------------
# to open another window(registration):
def sign_up():
    root.destroy()
    os.system("python Registration.py")

def login():
    def opensignup():
        root.destroy()

############----------------------
# image frame:
frame1=Frame(root,width=350, height=300, bg="blue")
frame1.place(x=60, y=40)
image=(Image.open("Log.png"))
resize_image=image.resize((310,330))
imagess=ImageTk.PhotoImage(resize_image)
lbl=Label(frame1, image=imagess, width=300, height=300)
lbl.pack()


############-----------------------
# login frame:  
frame=Frame(root, width=350, height=390, bg='white')
frame.place(x=400, y=50)

# login text
heading=Label(frame, text='Log In', fg="#917991", font=('Officina',23,'bold'))
heading.place(x=130, y=1)


###########------------------------
# authorization check:
def check():
        a=user.get()
        b=code.get()
        try:
            conn=sql.connect('admins.db')
            c=conn.cursor()
            
            c.execute("SELECT * from users")
            records=c.fetchall()
            i=len(records)-1
            while i>=0:
                if records[i][2]!=a or records[i][4]!=b:
                    i=i-1
                    if i==-1:
                        messagebox.showerror("Login","Invalid credentials")
                        break
                else:
                    # to change user status to active after login and set other users as inactive
                    c.execute("""UPDATE users SET
                    status=:inactive
                    WHERE status=:active""",
                    {'inactive':False,
                    'active':True})
                    conn.commit()
                    
                    c.execute("""UPDATE users SET
                    status= :val
                    WHERE mail = :a""",
                    {
                        'val':True,
                        'a':a
                    })
                    conn.commit()
                    messagebox.showinfo("Login","Logged in Successfully")
                    # openstatus()
                    break
            conn.commit()
            conn.close()
        except:
            messagebox.showerror("Invalid Info","Sign Up First")
            

############-----------------------
# username input:
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
user.place(x=30, y=80)
user.insert(0,'Username')
# bind function
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


############-----------------------
# password input:
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')

code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
code.place(x=30, y=150)
code.insert(0, 'Password')
# bind function is used to know the mouse movement hovering over or clicking
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
showw=IntVar(value=1)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# to show password, checkbutton:
def show():
    if(showw.get()==1):
        code.config(show='')
    else:
        code.config(show='*')

Checkbutton(text='Show password', offvalue=0, variable=showw, bg='white', command=show).place(x=600, y=230)    


###########----------------------
# verification check(signin):
def signin():
    username=user.get()
    password=code.get()

    if (username=="" or username=="Enter Your Username") or (password=="" or password=="Enter Your Password"):
        messagebox.showerror("Error","One or More Fields Empty.")
    elif len(password)<8:
        messagebox.showerror("Error", "Password must be 8 characters")
    else:
        check()

############---------------------
# Login button:
Button(frame, width=39, pady=7, text='Login', bg='#917991', fg='white', border=0, command=signin).place(x=35, y=230)
label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Officina',8))
label.place(x=100, y=270)

# Forgot password button:
forgot_password=Button(frame, width=15, text='Forgot password?', font=('Officina', 8, 'underline'), border=0, bg='white', cursor='hand2', fg='#917991')
forgot_password.place(x=30, y=190)

# Sign_up button:
sign_up=Button(frame, width=6, text='Sign Up', border=0, bg='white', command=sign_up , cursor='hand2', fg='#917991')
sign_up.place(x=220, y=270)
root.bind('<Return>',lambda event:signin())

root.mainloop()


