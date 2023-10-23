import customtkinter
import tkinter.messagebox


root = customtkinter.CTk()
root.title("To-Do List")

font1 = ("Arial", 14, "bold")


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def completed_task():
    try:
        marked = listbox_tasks.curselection()
        temp = marked[0]
        temp_marked = listbox_tasks.get(marked)
        temp_marked = temp_marked + "✔"
        listbox_tasks.delete(temp)
        listbox_tasks.insert(temp, temp_marked)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def remove_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def delete_all_tasks():
    confirmed = tkinter.messagebox.showwarning(title="Delete All Tasks!", message="Are you sure you want delete all tasks?")
    if confirmed:
        listbox_tasks.delete(0, tkinter.END)


frame_tasks = customtkinter.CTkFrame(master=root, width=5, height=5, corner_radius=5)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=15, width=50)
listbox_tasks.pack(side=tkinter.LEFT, fill=tkinter.Y)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = customtkinter.CTkEntry(root, text_color="#050505", fg_color="#fff", width=280)
entry_task.pack()

button_add_task = customtkinter.CTkButton(root, font=font1, text_color="#fff", text="Add task", hover_color="#696969", command=add_task)
button_add_task.pack()

button_completed_task = customtkinter.CTkButton(root, font=font1, text_color="#fff", text="Completed", hover_color="#696969", command=completed_task)
button_completed_task.pack()

button_remove_task = customtkinter.CTkButton(root, font=font1, text_color="#fff", text="Remove task", hover_color="#696969", command=remove_task)
button_remove_task.pack()

button_delete_all_task = customtkinter.CTkButton(root, font=font1, text_color="#fff", text="Delete all tasks", hover_color="#696969", command=delete_all_tasks)
button_delete_all_task.pack()

root.mainloop()
