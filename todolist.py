import tkinter as tk  
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql                 

def add_task():  
      
    task_string = task_field.get()  
      
    if len(task_string) == 0:  

        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
          
        tasks.append(task_string)  
         
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
         
        list_update()  
          
        task_field.delete(0, 'end')  
  
  
def list_update():  
     
    clear_list()  
    
    for task in tasks:  
          
        task_listbox.insert('end', task)  
  
 
def delete_task():  
      
    try:  
          
        the_value = task_listbox.get(task_listbox.curselection())  
          
        if the_value in tasks:  
              
            tasks.remove(the_value)  
              
            list_update()  
              
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
          
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
  
def delete_all_tasks():  
      
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
      
    if message_box == True:  
          
        while(len(tasks) != 0):  
             
            tasks.pop()  
          
        the_cursor.execute('delete from tasks')  
          
        list_update() 
            
def cross_off_tasks():
      task_listbox.itemconfig(
            task_listbox.curselection(),
            fg="#dedede")
      
def uncross_tasks():
    task_listbox.itemconfig(
        task_listbox.curselection(),
        fg="#464646")
  
def clear_list():  
    
    task_listbox.delete(0, 'end')  
  
  
def close():  
    
    print(tasks)  
     
    guiWindow.destroy()  
  
 
def retrieve_database():  
    
    while(len(tasks) != 0):  
        
        tasks.pop()  
      
    for row in the_cursor.execute('select title from tasks'):  
          
        tasks.append(row[0])  
  
# main function  
if __name__ == "__main__":  
      
    guiWindow = tk.Tk()  
    
    guiWindow.title("To-Do List Manager")  
     
    guiWindow.iconbitmap("to do list.ico")
      
    guiWindow.geometry("800x400+200+200")  
      
    guiWindow.resizable(0, 1)  
      
    guiWindow.configure(bg = "#917991")  
  
    
    the_connection = sql.connect('listOfTasks.db')  
    
    the_cursor = the_connection.cursor()  
      
    the_cursor.execute('create table if not exists tasks (title text)')  
  
     
    tasks = []  
      
    
    header_frame = tk.Frame(guiWindow, bg = "#ffffff")  
    functions_frame = tk.Frame(guiWindow, bg = "#ffffff")  
    listbox_frame = tk.Frame(guiWindow, bg = "#ffffff")  
  
    
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "bottom", expand = True, fill = "both")  
    listbox_frame.pack(side = "top", expand = True, fill = "both")  
      
     
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("officina", "35"),  
        background = "#917991",  
        foreground = "#000000" ,
    )  
     
    header_label.pack(padx = 20, pady = 20)  
  
     
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#917991",  
        foreground = "#000000"  
    )  
    
    task_label.place(x = 240, y = 10)  
      
     
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    
    task_field.place(x = 390, y = 9)  
  
     
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    ) 
    cross_button = ttk.Button(
        functions_frame,
        text = "Cross Off Task",
        width = 24,
        command = cross_off_tasks 
    )
    uncross_button = ttk.Button(
        functions_frame,
        text = "Uncross Task",
        width = 24,
        command = uncross_tasks
    )    
    add_button.place(x = 225, y = 50)  
    del_button.place(x = 400, y = 50)  
    del_all_button.place(x = 225, y = 90)  
    exit_button.place(x = 400, y = 90) 
    cross_button.place(x=225,y =125)
    uncross_button.place(x=400, y=125)
  
    
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 128,  
        height = 8,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
     
    task_listbox.place(x = 10, y = 20)  
  
     
    retrieve_database()  
    list_update()  
      
    guiWindow.mainloop()  
   
    the_connection.commit()  
    the_cursor.close()  
