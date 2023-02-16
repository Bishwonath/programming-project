# TO DO LIST:      

from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

# creating a window:
root=Tk()

# window title:
root.title("To-Do List")  
root.geometry("800x600+300+100") 
root.configure(bg = "white")   
root.resizable(False, False)  
  

################---------------------
# add task function:
def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0: 
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        tasks.append(task_string)  
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        list_update()  
        task_field.delete(0, 'end')  


################---------------------
# Prioritize function:
def sort_listbox():
        selected_index = task_listbox.curselection()
        if selected_index:
            # selected_index = selected_index[0]
            selected_item = task_listbox.get(selected_index)
        items = list(task_listbox.get(0, END))
        items.sort()
        items.insert(0, selected_item)
        task_listbox.delete(0, END)
        for item in items:
            task_listbox.insert(END, item)
        # items.sort.mainloop()


################---------------------
# update function:
def list_update():  
    clear_list()  
    for task in tasks:  
        task_listbox.insert('end', task)  
  
 
################---------------------
# delete function:
def delete_task():        
    try: 
        the_value = task_listbox.get(task_listbox.curselection())   
        if the_value in tasks:  
            tasks.remove(the_value)  
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        


################---------------------
# delete all function:  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:  
        while(len(tasks) != 0):  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  
  
  
def clear_list():  
    task_listbox.delete(0, 'end')  
  

################---------------------
# exit function:
def close():  
    print(tasks)  
    root.destroy()  
  

################---------------------
# function:
def retrieve_database():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  
  

################---------------------
# logout function:
def logout():
    msb=messagebox.askquestion("Logout","Are you sure you want to logout?")
    if msb=='yes':
#set user status to inactive
        conn=sql.connect('admin.db')
        c=conn.cursor()
        c.execute("""UPDATE users SET
        status= :off
        WHERE status= :on""",
        {
            'off':False,
            'on':True
        })
        conn.commit()
        conn.close()

        try:
#destroy window and import logout
            root.destroy()
            import Login
        except:
            pass


################---------------------
# main function  
if __name__ == "__main__":  
    the_connection = sql.connect('listOfTasks.db')    
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  
     
    tasks = []  
      
################---------------------
# creating frame:
    header_frame = Frame(root, bg = "white")  
    functions_frame = Frame(root, bg = "white")  
    listbox_frame = Frame(root, bg = "white")  
    taskinput_frame = Frame(root, bg = "white")
  
    
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "bottom", expand = True, fill = "both")  
    listbox_frame.pack(side = "top", expand = True, fill = "both") 
    taskinput_frame.pack(expand = True, fill = "both") 
      
# creating title:
    header_label = Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Officina", "35", "bold"),  
        background = "white",  
        foreground = "#917991" ,
    )  
     
    header_label.pack(padx = 50, pady = 5)  
  

# Enter task text:
    task_label = Label(  
        taskinput_frame,
        text = "Enter the task:",  
        font = ("Officina", 14),  
        background = "white",  
        foreground = "#917991"  
    )  
# position:
    task_label.place(x = 160, y = 22)  
      
# entry gap:
    task_field = Entry(  
        taskinput_frame,  
        font = ("Officina", "14"),  
        width = 30,  
        background = "white",  
        foreground = "black"  
    )  
    task_field.place(x = 290, y = 25)  
  
# Add button:
    add_button = Button(  
        taskinput_frame,  
        text = "Add Task",  
        width = 25,
        height = 2, 
        bg="#917991",
        fg="white",
        font=("Officina", 12),
        command = add_task  
    )  

# Prioritize button:
    sort_button = Button(
        taskinput_frame,
        text= "Prioritize",
        width = 25, 
        height = 2,
        bg= "#917991",
        fg= "white",
        font= ("Officina", 12), 
        command= sort_listbox,
    )
    
# Delete button:
    del_button = Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 25, 
        height = 2,
        bg="#917991",
        fg="white",
        font=("Officina", 12),
        command = delete_task  
    )  

# Delete all button:
    del_all_button = Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 25,  
        height = 2,
        bg="#917991",
        fg="white",
        font=("Officina", 12),
        command = delete_all_tasks  
    )  

# Exit button:
    exit_button = Button(  
        functions_frame,  
        text = "Exit",  
        width = 25, 
        height = 2,
        bg="#917991",
        fg="white",
        font=("Officina", 12), 
        command = close  
    ) 

# Logout button:
    logout_button = Button(
    functions_frame,  
        text = "Logout",  
        width = 25, 
        height = 2,
        bg="#917991",
        fg="white",
        font=("Officina", 12),
        command = logout   
    )

      
# Positioning the above buttons:
    add_button.place(x = 140, y = 100) 
    sort_button.place(x = 410, y = 100)
    del_button.place(x = 140, y = 10)  
    del_all_button.place(x = 410, y = 10)  
    exit_button.place(x = 410, y = 100)  
    logout_button.place(x = 140, y = 100)

    
################---------------------
# list box:
    task_listbox = Listbox(  
        listbox_frame,  
        width = 55,  
        height = 5, 
        font=('Officina',18), 
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )

    task_listbox.place(x = 40, y = 10)  
     
    retrieve_database()  
    list_update()  
      
    root.mainloop()  
   
    the_connection.commit()  
    the_cursor.close()  