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
from backend_oop import Database

database = Database("bookstore.db")

class Window(tk.Frame):
    """It is a class that contains GUI interface for a book store"""
    def __init__(self, window):
        self.window = window
        print(id(self.window), "i")
        self.window.wm_title("Bookstore")

        self.label_1 = tk.Label(self.window, text="Title")
        self.label_1.grid(row=0, column=0)

        self.label_2 = tk.Label(self.window, text="Author")
        self.label_2.grid(row=0, column=2)

        self.label_3 = tk.Label(self.window, text="Year")
        self.label_3.grid(row=1, column=0)

        self.label_4 = tk.Label(self.window, text="ISBN")
        self.label_4.grid(row=1, column=2)

        self.title_text = tk.StringVar()
        self.entry_1 = tk.Entry(self.window, textvariable=self.title_text)
        self.entry_1.grid(row=0, column=1)

        self.author_text = tk.StringVar()
        self.entry_2 = tk.Entry(self.window, textvariable=self.author_text)
        self.entry_2.grid(row=0, column=3)

        self.year_text = tk.StringVar()
        self.entry_3 = tk.Entry(self.window, textvariable=self.year_text)
        self.entry_3.grid(row=1, column=1)

        self.isbn_text = tk.StringVar()
        self.entry_4 = tk.Entry(self.window, textvariable=self.isbn_text)
        self.entry_4.grid(row=1, column=3)

        self.listbox_1 = tk.Listbox(self.window, height=6, width=35)
        self.listbox_1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.scrollbar_1 = tk.Scrollbar(self.window)
        self.scrollbar_1.grid(row=2, column=2, rowspan=6, sticky=tk.N+tk.S+tk.E+tk.W)

        self.listbox_1.configure(yscrollcommand=self.scrollbar_1.set)
        self.scrollbar_1.configure(command=self.listbox_1.yview)

        self.listbox_1.bind('<<ListboxSelect>>', self.get_selected_row)

        self.button_1 = tk.Button(self.window, text="View all", width=12, command=self.view_command)
        self.button_1.grid(row=2, column=3)

        self.button_2 = tk.Button(self.window, text="Search entry", width=12, command=self.search_command)
        self.button_2.grid(row=3, column=3)

        self.button_3 = tk.Button(self.window, text="Add entry", width=12, command=self.add_command)
        self.button_3.grid(row=4, column=3)

        self.button_4 = tk.Button(self.window, text="Update", width=12, command=self.update_command)
        self.button_4.grid(row=5, column=3)

        self.button_5 = tk.Button(self.window, text="Delete", width=12, command=self.delete_command)
        self.button_5.grid(row=6, column=3)

        self.button_6 = tk.Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.button_6.grid(row=7, column=3)

    def get_selected_row(self, event):
        if self.listbox_1.size():    
            global selected_tuple
            index = self.listbox_1.curselection()[0]
            selected_tuple = self.listbox_1.get(index)
            self.entry_1.delete(0, tk.END)
            self.entry_1.insert(tk.END, selected_tuple[1])
            self.entry_2.delete(0, tk.END)
            self.entry_2.insert(tk.END, selected_tuple[2])
            self.entry_3.delete(0, tk.END)
            self.entry_3.insert(tk.END, selected_tuple[3])
            self.entry_4.delete(0, tk.END)
            self.entry_4.insert(tk.END, selected_tuple[4])


    def view_command(self):
        self.listbox_1.delete(0, tk.END)
        for row in database.view():
            self.listbox_1.insert(tk.END, row)

    def search_command(self):
        self.listbox_1.delete(0, tk.END)
        for row in database.search(self.title_text.get(), self.author_text.get(), 
                                    self.year_text.get(), self.isbn_text.get()):
            self.listbox_1.insert(tk.END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.listbox_1.delete(0, tk.END)
        self.listbox_1.insert(tk.END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(selected_tuple[0])

    def update_command(self):
        database.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

root = tk.Tk()
root.title("My Bookstore App")
print(id(root))
window = Window(root)
root.mainloop()