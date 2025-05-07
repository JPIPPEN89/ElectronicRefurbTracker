import sqlite3
from tkinter import *
from tkinter import ttk
from database import init_db
from AddView import Add_View

init_db()

root = Tk()
root.geometry("600x800")
root.title("Electronic Refurb Tracker")

#Main Screen Buttons For Functions

btnAdd = (Button(root, text="Add Item", command= lambda:Add_View(root)).grid(row=4, column=2, padx=10, pady=10))

root.mainloop()