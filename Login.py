# LOG IN PAGE:

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3 as sql
import random



# creating a window:
root=Tk()


# window title:
root.title('Login')
root.geometry('800x400+200+200')
root.configure(bg="white")
root.iconbitmap("window.ico")   
root.resizable(False, False)


############----------------------
# image frame:
frame1=Frame(root,width=350, height=300, bg="blue")
frame1.place(x=60, y=40)
image=(Image.open("Log.png"))
resize_image=image.resize((310,330))
imagess=ImageTk.PhotoImage(resize_image)
lbl=Label(frame1, image=imagess, width=300, height=300)
lbl.pack()

############----------------------
# to open another window(registration):
# login function:
def login():

    def sign_up():
        root.destroy()
        import Registration


############-----------------------
# login frame:  
    frame=Frame(root, width=350, height=390, bg='white')
    frame.place(x=400, y=50)

# login text
    heading=Label(frame, text='Log In', bg='white', fg="#917991", font=('Officina',23,'bold'))
    heading.place(x=130, y=1)


###########------------------------
# authorization check:
    # def check():
    #         a=user.get()
    #         b=code.get()
    #         try:
    #             conn=sql.connect('admin.db')
    #             c=conn.cursor()
                
    #             c.execute("SELECT * from users")
    #             records=c.fetchall()
    #             i=len(records)-1
    #             while i>=0:
    #                 if records[i][2]!=a or records[i][4]!=b:
    #                     i=i-1
    #                     if i==-1:
    #                         messagebox.showerror("Login","Invalid credentials")
    #                         break
    #                 else:
    #                     # to change user status to active after login and set other users as inactive
    #                     c.execute("""UPDATE users SET
    #                     status=:inactive
    #                     WHERE status=:active""",
    #                     {'inactive':False,
    #                     'active':True})
    #                     conn.commit()
                        
    #                     c.execute("""UPDATE users SET
    #                     status= :val
    #                     WHERE user = :a""",
    #                     {
    #                         'val':True,
    #                         'a':a
    #                     })
    #                     conn.commit()
    #                     messagebox.showinfo("Login","Logged in Successfully")
    #                     # openstatus()
    #                     #Login connection

    #                     # def lis():
    #                     #     import list
    #                     break
    #             conn.commit()
    #             conn.close()
    #         except:
    #             messagebox.showerror("Invalid","Sign Up First")
            

############-----------------------
# username input:
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0, 'Username')
    global user
    user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
    user.place(x=30, y=80)
    user.insert(0,'Username')
    # bind function is used to know the movement of mouse hovering over or clicking
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
# bind function
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
    

        def todlist():
            root.destroy()
            import todolist 
               
           

        if user.get()=='' or code.get()=='':
            messagebox.showinfo("error","one or more fields are empty")
        
        else:            
            conn = sql.connect("admin.db")
            c = conn.cursor()

            u = 'SELECT * FROM users WHERE mail = ? and pwd = ?'
            c.execute(u,[(user.get()),(code.get())])
            un=user.get()
            result = c.fetchall()
            if result:
                messagebox.showinfo("Success", 'Logged in Successfully.')
                conn.commit()
                c.execute("""UPDATE users SET
                            status= :condition
                            WHERE mail = :un""",
                            {
                                'condition':True,
                                'un':un
                            })
                
                conn.commit()
                conn.close()
                todlist()
                
            else:
                messagebox.showinfo("error","Invalid credentials")
                
        # if (username=="" or username=="Enter Your Username") or (password=="" or password=="Enter Your Password"):
        #     messagebox.showerror("Error","One or More Fields Empty.")
        # elif len(password)<6:
        #     messagebox.showerror("Error", "Password must be more than 6 characters")
        # else:
        #     check()


############---------------------
# Login button:
    # Button(frame, width=39, pady=7, text='Login', bg='#917991', fg='white', border=0, command=signin).place(x=35, y=230)
    # label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Officina',8))
    # label.place(x=100, y=270)

    Button(frame, width=39, pady=7, text='Login', bg='#917991', fg='white', border=0, command=signin).place(x=35, y=230)
    label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Officina',8))
    label.place(x=100, y=270)
    

# data input function with 'enter key'
    root.bind('<Return>',lambda event:signin())


############-----------------------
# Sign_up button:
    signup=Button(frame, width=6, text='Sign Up', border=0, bg='white', command=sign_up , cursor='hand2', fg='#917991')
    signup.place(x=220, y=270)


############-----------------------
# Forgot password text:
    forgot_password=Button(frame, width=15, text='Forgot password?', font=('Officina', 8, 'underline'), border=0, bg='white', cursor='hand2', command=pwd, fg='#917991')
    forgot_password.place(x=30, y=190)


# Forgot password function:
def pwd():

    # creating a window
    win=Toplevel()
    win.geometry('400x350+150+150')
    win.title('Forgot Password')
    win.resizable(False, False)

    frame2=Frame(win, bg='white', width=500, height=400).place(x=0, y=0)
    label=Label(win, text='Reset Password', bg='white',fg='#917991' , font=('Officina', 23, 'bold')).place(x=60, y=10)


############-----------------------
# User input:
    # remove functionalities(placeholders)
    def on_enter(e):
            mail.delete(0, 'end')

    def on_leave(e):
        name=mail.get()
        if name=='':
            mail.insert(0, 'Enter Your Email')

    mail=Entry(win)
    mail.insert(0, 'Enter Your Email')
    mail.place(x=40, y=75,width=290, height=35)
    # bind function:
    mail.bind('<FocusIn>', on_enter)
    mail.bind('<FocusOut>', on_leave)


############-----------------------
# Security questions:
    ans=StringVar()

    a="Q1: What is your favourite food?"
    b="Q2: What is the name of your first pet?"
    c="Q3: What is the name of your childhood best friend?"
    list=[a,b,c]
    ques=random.choice(list)
    num=int(ques[1])-1
    Label(win,text=ques, bg='white', fg='#917991').place(x=40,y=118)
    Entry(win,textvariable=ans).place(x=40,y=140,width=290,height=35)


############-----------------------
# function to show password:
    def show():
        if (showw.get()==1):
            new_pwd.config(show='')
        else:
            new_pwd.config(show='*')

    def show2():
        if (showww.get()==1):
            c_pwd.config(show='')
        else:
            c_pwd.config(show='*')
# New password:
    def on_enter(e):
            new_pwd.delete(0, 'end')

    def on_leave(e):
        name=new_pwd.get()
        if name=='':
            new_pwd.insert(0, 'New Password')

    new_pwd=Entry(win)
    new_pwd.insert(0, 'New Password') 
    new_pwd.place(x=40, y=190, width=250, height=35)
    # bind function
    new_pwd.bind('<FocusIn>', on_enter)
    new_pwd.bind('<FocusOut>', on_leave)

    showw=IntVar(value=1)
    Checkbutton(win,text='Show',offvalue=0,variable=showw,bg='white',command=show).place(x=300,y=193)


# Confirm Password:
    def on_enter(e):
            c_pwd.delete(0, 'end')

    def on_leave(e):
        name=c_pwd.get()
        if name=='':
            c_pwd.insert(0, 'Confirm Password')

    c_pwd=Entry(win)
    c_pwd.insert(0, 'Confirm Password') 
    c_pwd.place(x=40, y=240, width=250, height=35)
    # bind function
    c_pwd.bind('<FocusIn>', on_enter) 
    c_pwd.bind('<FocusOut>', on_leave)

    showww=IntVar(value=1)
    Checkbutton(win,text='Show',offvalue=0,variable=showww,bg='white',command=show2).place(x=300,y=233)


   


############-----------------------
# update function for new password
    def update():
        a=mail.get()
        b=ans.get()
        
        #database connection for password update
        conn=sql.connect('admin.db')
        c=conn.cursor()
        c.execute("SELECT * from users")
        records=c.fetchall()
        i=len(records)-1
        while i>=0:
            if records[i][2]!=a or records[i][(6+num)]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Password Reset","Invalid Credentials")
                    break
            else:
                pw_upd=new_pwd.get()
                cpw_upd=c_pwd.get()
                c.execute("""UPDATE users SET
                pwd= :new_pwd,
                cpwd= :c_pwd
                WHERE username = :a""",
                {
                    'new_pwd':pw_upd,
                    'c_pwd':cpw_upd,
                    'a':a
                })
                conn.commit()
                conn.close()

                messagebox.showinfo("Password Reset","Password Changed Successfully")
                # to destroy previous password after successful new password update
                win.destroy()
                break             
       

############-----------------------
# Password verification for forgot functionality:
    def verify():
        w=mail.get()
        x=ans.get()
        y=new_pwd.get()
        z=c_pwd.get()

        if w=="" or w=="Enter Your Email" or x=="" or y=="" or y=="New Password" or z=="" or z=="Confirm New Password":
            messagebox.showerror("Error","One or More Fields Empty")
        else:
            if "@" and ".com" not in w:
                messagebox.showerror("Error","Invalid Email")
            elif len(y)<6 or len(z)<6:
                messagebox.showerror("Error","Password must be more than 6 characters")
            elif y!=z:
                messagebox.showerror("Error","Passwords Mismatch")
            else:
                update()
    Button(win,text="Confirm",font=('Officina',10,'bold'),fg='white',bg='#917991',width=18,height=1,cursor='hand2',command= verify).place(x=110, y=300)

login()



root.mainloop()
