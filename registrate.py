import tkinter as tk

class RegisterForm(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Registration Form")

        # create the form elements
        self.label_name = tk.Label(self, text="Name")
        self.entry_name = tk.Entry(self)
        self.label_email = tk.Label(self, text="Email")
        self.entry_email = tk.Entry(self)
        self.label_password = tk.Label(self, text="Password")
        self.entry_password = tk.Entry(self, show="*")
        self.button_register = tk.Button(self, text="Register", command=self.register)

        # layout the form elements
        self.label_name.pack()
        self.entry_name.pack()
        self.label_email.pack()
        self.entry_email.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_register.pack()

    def register(self):
        # get the values from the form
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        # do something with the values here (e.g. save to database)
        print(f"Name: {name}, Email: {email}, Password: {password}")

# create and run the form
form = RegisterForm()
form.mainloop()
