from tkinter import *
import tkinter.messagebox as tmsg
import sqlite3 as sql

todolist = Tk()

tasks = []

def addtask():
    task_string = add_task.get().strip()  # Strip leading and trailing whitespaces
    if task_string:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        update_list()
        add_task.delete(0, 'end')
    else:
        tmsg.showinfo("Error", "Field is empty.")

def update_list():
    clear_list()
    for task in tasks:
        task_listbox.insert('end',task)

def deltask():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_task = task_listbox.get(selected_index)
        tasks.remove(selected_task)
        the_cursor.execute('delete from tasks where title = ?', (selected_task,))
        update_list()
    else:
        tmsg.showinfo('error', 'No task selected ')

def delalltask():
    message_box = tmsg.askyesno('Delete all', 'Are you sure?')
    if message_box:
        tasks.clear()
        the_cursor.execute('delete from tasks')
        update_list()

def clear_list():
    task_listbox.delete(0,'end')

def close():
    print(tasks)
    todolist.destroy()

def retrieve_database():
    tasks.clear()  # Clear the tasks list
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])



todolist.geometry("500x450+750+250")
todolist.title("TO DO LIST")
todolist.configure(bg = "#f8f1cd")
the_connection = sql.connect('listOfTasks.db')
the_cursor = the_connection.cursor()
the_cursor.execute('create table if not exists tasks(title text)')


header_label = Label(text = "The To Do List", font =("Brush Script MT","45"), background= "#f8f1cd", foreground = "#E8A317")
header_label.pack(side=TOP,pady=30)

task_label = Label(text="Enter the task:", font = ("Book Antiqua","30"), background= "#f8f1cd", foreground= "#000000")
task_label.pack( anchor="nw", padx=20, pady=20)

add_task = StringVar()
add_task = Entry(todolist,textvariable=add_task,font=("Arial Black",10),width=25)
add_task.pack(anchor="nw",padx=20,pady=10)

Button(text="Add Task", font=("Arial Black",10),width=24,command=addtask).pack(anchor="nw",padx=20)
Button(text="Delete Task", font=("Arial Black",10),width=24,command=deltask).pack(anchor="nw",padx=20,pady=5)
Button(text="Delete All Task", font=("Arial Black",10),width=24,command=delalltask).pack(anchor="nw",padx=20,pady=5)
Button(text="Exit", font=("Arial Black",10),width=24,command=exit).pack(anchor="nw",padx=20,pady=5)

task_listbox = Listbox(width=26,height=13,selectmode='SINGLE',background="#FFFFFF",foreground="#000000",selectbackground="#CD853F",selectforeground="#FFFFFF")
task_listbox.place(x=280,y=220)

retrieve_database()
update_list()
todolist.mainloop()
the_connection.commit()
the_cursor.close()
