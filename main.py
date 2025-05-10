import sqlite3
from tkinter import *
from tkinter import ttk
from database import Database, LaptopDB, PhonesDB

from AddView import Add_View

#init_db()

root = Tk()
root.geometry("600x800")
root.title("Electronic Refurb Tracker")

#Main Screen Buttons For Functions

btnAdd = (Button(root, text="Add Item", command= lambda:Add_View(root)).grid(row=4, column=2, padx=10, pady=10))

root.mainloop()

LTdb = LaptopDB()
LTdb.create_table()
LTdb.add_item("Dell", "Latitude 7400", 130, 1)

LTdb.get_all_laptops()

PhoneDB = PhonesDB()
PhoneDB.create_table()
PhoneDB.add_item("Apple", "iPhone xr", 44.36, 1)
PhoneDB.get_all_phones()
