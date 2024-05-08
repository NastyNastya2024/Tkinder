import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task[0], bg="HotPink")

root = tk.Tk()
root.title('Task list')
root.configure(bg='HotPink')

text1 = tk.Label(root, text='Enter your task', bg='HotPink')
text1.pack(pady=10)

task_entry = tk.Entry(root, width=30, bg='LightPink')
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text='Add Task', bg='SkyBlue', command=add_task)
add_task_button.pack(pady=10)

delete_button = tk.Button(root, text='Delete Task', bg='SkyBlue', command=delete_task)
delete_button.pack(pady=10)

mark_button = tk.Button(root, text='Mark Task', bg='SkyBlue', command=mark_task)
mark_button.pack(pady=10)

text2 = tk.Label(root, text='Task Name', bg='HotPink')
text2.pack(pady=10)

task_listbox = tk.Listbox(root, height=10, width=50, bg='LightPink')
task_listbox.pack(pady=10)

root.mainloop()
