import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import sqlite3

# Function to add a new task
def add_task():
    task = entry_task.get()
    if task:
        conn.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, 0))
        conn.commit()
        update_treeview()
        entry_task.delete(0, tk.END)

# Function to mark a task as completed
def mark_task():
    selected_item = treeview.selection()
    if selected_item:
        item_id = treeview.item(selected_item[0], 'text')
        conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (item_id,))
        conn.commit()
        update_treeview()

# Function to unmark a task as not completed
def unmark_task():
    selected_item = treeview.selection()
    if selected_item:
        item_id = treeview.item(selected_item[0], 'text')
        conn.execute("UPDATE tasks SET completed = 0 WHERE id = ?", (item_id,))
        conn.commit()
        update_treeview()

# Function to toggle task completion status (for double-click event)
def toggle_task(event):
    selected_item = treeview.selection()
    if selected_item:
        item_id = treeview.item(selected_item[0], 'text')
        current_status = conn.execute("SELECT completed FROM tasks WHERE id = ?", (item_id,)).fetchone()[0]
        new_status = 1 if current_status == 0 else 0
        conn.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_status, item_id))
        conn.commit()
        update_treeview()

# Function to delete a task
def delete_task():
    selected_item = treeview.selection()
    if selected_item:
        item_id = treeview.item(selected_item[0], 'text')
        conn.execute("DELETE FROM tasks WHERE id = ?", (item_id,))
        conn.commit()
        update_treeview()

# Function to update the treeview with tasks
def update_treeview():
    for item in treeview.get_children():
        treeview.delete(item)
    cursor = conn.execute("SELECT id, task, completed FROM tasks")
    for row in cursor:
        task_display = row[1]
        if row[2] == 1:
            treeview.insert("", tk.END, text=row[0], values=(f"✔ {task_display}",))
        else:
            treeview.insert("", tk.END, text=row[0], values=(task_display,))

# Creating the main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="#FCE4EC")  # Set background color to pale pink
root.geometry("500x350")  # Decrease the window size

# Creating a custom font
custom_font = font.Font(family="Helvetica", size=12)

# Creating the database
conn = sqlite3.connect('tasks.db')
conn.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             task TEXT NOT NULL,
             completed INTEGER NOT NULL)''')

# Creating GUI elements
entry_task = tk.Entry(root, width=60, bg="#E8EAF6", font=custom_font)  # Adjust width, set background color to pale lavender, and font
entry_task.grid(row=0, column=0, padx=10, pady=10)

btn_add_task = tk.Button(root, text="Add Task", width=56, command=add_task, bg="#E1F5FE", fg="#AD1457", font=custom_font)  # Adjust width, set background color to light aqua, text color to dark pink, and font
btn_add_task.grid(row=1, column=0, padx=10, pady=10)

# Creating Treeview widget
treeview = ttk.Treeview(root, columns=("Task",), show="headings")
treeview.heading("#1", text="Task : ", anchor="w")  # Align the heading to the left
treeview.column("#1", anchor="w", width=450)  # Adjust column width
treeview.grid(row=2, column=0, padx=10, pady=10)
treeview.bind("<Double-1>", toggle_task)

# Applying custom font to Treeview items
style = ttk.Style()
style.configure("Treeview.Heading", font=custom_font)
style.configure("Treeview", font=custom_font, rowheight=25, background="#E3F2FD")  # Set Treeview background to pale blue

# Creating a frame to hold the mark and unmark buttons
frame_mark_unmark = tk.Frame(root, bg="#FCE4EC")  # Set background color to pale pink
frame_mark_unmark.grid(row=3, column=0, padx=10, pady=10)

# Creating buttons for mark and unmark tasks and placing them in the frame
btn_mark_task = tk.Button(frame_mark_unmark, text="Mark Task", width=26, command=mark_task, bg="#E1F5FE", fg="#AD1457", font=custom_font)  # Adjust width, set background color to light aqua, text color to dark pink, and font
btn_mark_task.grid(row=0, column=0, padx=5)

btn_unmark_task = tk.Button(frame_mark_unmark, text="Unmark Task", width=26, command=unmark_task, bg="#E1F5FE", fg="#AD1457", font=custom_font)  # Adjust width, set background color to light aqua, text color to dark pink, and font
btn_unmark_task.grid(row=0, column=1, padx=5)

btn_delete_task = tk.Button(root, text="Delete Task", width=56, command=delete_task, bg="#E1F5FE", fg="#AD1457", font=custom_font)  # Adjust width, set background color to light aqua, text color to dark pink, and font
btn_delete_task.grid(row=4, column=0, padx=10, pady=10)

# Populate treeview with existing tasks
update_treeview()

root.mainloop()
