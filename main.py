import tkinter as tk

def add_task():
    task=entry.get()
    if task:
        task_listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def delete_task():
    selected_task=task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def check_task_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task = task_listbox.get(index)
        # Добавляем галочку к задаче, если её там ещё нет
        if not task.endswith(" ✓"):
            task_listbox.delete(index)
            task_listbox.insert(index, task + " ✓")

root=tk.Tk()
root.title("Task list")
root.configure(background="light steel blue")

text_for_entry=tk.Label(root, text="ВВЕДИТЕ ЗАДАЧУ", bg="light steel blue")
text_for_entry.place(x=45, y=5)

entry=tk.Entry(root, width=30, bg="honeydew1")
entry.place(x=5, y=30)

add_task_button=tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.place(x=45, y=60)

delete_button=tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.place(x=48, y=90)

check_button=tk.Button(root, text="Отметить выполненную задачу", bg="lawn green", command=check_task_completed)
check_button.place(x=5, y=120)

text_for_list=tk.Label(root, text="СПИСОК ЗАДАЧ", bg="light steel blue")
text_for_list.place(x=330, y=5)

task_listbox=tk.Listbox(root, height=15, width=60, bg="khaki1")
task_listbox.place(x=200, y=30)

root.mainloop()
