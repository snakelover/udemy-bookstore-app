"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

import tkinter as tk
import backend

def get_selected_row(event):
    if listbox_1.size():    
        global selected_tuple
        index = listbox_1.curselection()[0]
        selected_tuple = listbox_1.get(index)
        entry_1.delete(0, tk.END)
        entry_1.insert(tk.END, selected_tuple[1])
        entry_2.delete(0, tk.END)
        entry_2.insert(tk.END, selected_tuple[2])
        entry_3.delete(0, tk.END)
        entry_3.insert(tk.END, selected_tuple[3])
        entry_4.delete(0, tk.END)
        entry_4.insert(tk.END, selected_tuple[4])


def view_command():
    listbox_1.delete(0, tk.END)
    for row in backend.view():
        listbox_1.insert(tk.END, row)

def search_command():
    listbox_1.delete(0, tk.END)
    for row in backend.search(title_text.get(), author_text.get(), 
                                year_text.get(), isbn_text.get()):
        listbox_1.insert(tk.END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listbox_1.delete(0, tk.END)
    listbox_1.insert(tk.END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = tk.Tk()
window.wm_title("Book Store")

label_1 = tk.Label(window, text="Title")
label_1.grid(row=0, column=0)

label_2 = tk.Label(window, text="Author")
label_2.grid(row=0, column=2)

label_3 = tk.Label(window, text="Year")
label_3.grid(row=1, column=0)

label_4 = tk.Label(window, text="ISBN")
label_4.grid(row=1, column=2)

title_text = tk.StringVar()
entry_1 = tk.Entry(window, textvariable=title_text)
entry_1.grid(row=0, column=1)

author_text = tk.StringVar()
entry_2 = tk.Entry(window, textvariable=author_text)
entry_2.grid(row=0, column=3)

year_text = tk.StringVar()
entry_3 = tk.Entry(window, textvariable=year_text)
entry_3.grid(row=1, column=1)

isbn_text = tk.StringVar()
entry_4 = tk.Entry(window, textvariable=isbn_text)
entry_4.grid(row=1, column=3)

listbox_1 = tk.Listbox(window, height=6, width=35)
listbox_1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar_1 = tk.Scrollbar(window)
scrollbar_1.grid(row=2, column=2, rowspan=6, sticky=tk.N+tk.S+tk.E+tk.W)

listbox_1.configure(yscrollcommand=scrollbar_1.set)
scrollbar_1.configure(command=listbox_1.yview)

listbox_1.bind('<<ListboxSelect>>', get_selected_row)

button_1 = tk.Button(window, text="View all", width=12, command=view_command)
button_1.grid(row=2, column=3)

button_2 = tk.Button(window, text="Search entry", width=12, command=search_command)
button_2.grid(row=3, column=3)

button_3 = tk.Button(window, text="Add entry", width=12, command=add_command)
button_3.grid(row=4, column=3)

button_4 = tk.Button(window, text="Update", width=12, command=update_command)
button_4.grid(row=5, column=3)

button_5 = tk.Button(window, text="Delete", width=12, command=delete_command)
button_5.grid(row=6, column=3)

button_6 = tk.Button(window, text="Close", width=12, command=window.destroy)
button_6.grid(row=7, column=3)


window.mainloop()
