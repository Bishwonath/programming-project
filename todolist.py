# TO DO LIST:      

from tkinter import *
from tkinter import messagebox
import sqlite3 as sql


# creating a window:
root=Tk()

# window title:
root.title("To-Do List")  
root.geometry("800x650+300+100") 
# root.configure(bg = "white")   
root.resizable(False, False)  
  

################---------------------
# add task function:
def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0: 
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        tasks.append(task_string)  
        cursor.execute('insert into tasks values (?)', (task_string ,))  
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
            cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        


################---------------------
# delete all function:  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:  
        while(len(tasks) != 0):  
            tasks.pop()  
        cursor.execute('delete from tasks')  
        list_update()  
  
  
def clear_list():  
    task_listbox.delete(0, 'end')  
  

################---------------------
# exit function:              
def close():  
    print(tasks)
    msb=messagebox.askquestion("Logout","Are you sure you want to exit?")
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
# function:
def retrieve_database():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in cursor.execute('select title from tasks'):  
        tasks.append(row[0])  
  

################---------------------
# edit function:
def editTask():
        editor = Tk()
        editor.title("Edit task")
        editor.geometry("300x200+100+355")
        editor.resizable(False,False)
        global new_task

        new_task =Entry(editor,width=20,font=("Officina",14))
        new_task.place(x=45, y=20)
    

    # from delete function
        delt = task_listbox.get("active") 
        print(delt)

        if "'" in delt:
            ourIndex = delt.index("'")
            letters = list(delt)   
            letters.insert(ourIndex,"\\")
            delt = "".join(letters)

        def save():
            newValue = new_task.get()
            conn = sql.connect("listOfTasks.db")
            
            print(newValue)
            c = conn.cursor()
            records=c.fetchone()

            c.execute("""UPDATE tasks SET
            title=:edit_ed
             
             """,
            {"edit_ed":newValue}
                
            )

            conn.commit()
            conn.close()
            list_update()
            editor.destroy()
            
        save_button = Button(editor, text="Save", bg="#917991", fg="white",width=12,height=1, command=save)
        save_button.place(x=110, y=60)
        

        


################---------------------
# main function  
  
connection = sql.connect('listOfTasks.db')    
cursor = connection.cursor()  
cursor.execute('create table if not exists tasks (title text)')  
     
tasks = []  
      
################---------------------
# creating frame:
header_frame = Frame(root, bg = "white")  
functions_frame = Frame(root, bg = "white")  
listbox_frame = Frame(root, bg = "white") 
global taskinput_frame 
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
        width = 11, 
        height = 2,
        bg="#917991",
        fg="white",
        font=("Officina", 12), 
        command = close  
    ) 
    
def refresh():
    root.destroy()
    import todolist
    
            
    
refresh_button = Button(functions_frame, text="Refresh",font=("Officina", 12), bg="#917991", fg="white",width=11,height=2, command=refresh)
refresh_button.place(x=410, y=100)


# Edit button:
edit_button = Button(
        functions_frame,  
        text = "Edit",  
        width = 25, 
        height = 2,
        bg="#917991",
        fg="white",
        font=("Officina", 12),
        command = editTask   
    )

      
# Positioning the above buttons:
add_button.place(x = 140, y = 100) 
sort_button.place(x = 410, y = 100)
del_button.place(x = 140, y = 10)  
del_all_button.place(x = 410, y = 10)  
exit_button.place(x = 540, y = 100)  
edit_button.place(x = 140, y = 100)

    
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
      
      
connection.commit()  
cursor.close()
