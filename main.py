import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from database import Database, LaptopDB, PhonesDB
#from AddView import Add_View
import Main_Controller as mc

# Initialize main window
root = Tk()
root.geometry("600x800")
root.title("Electronic Refurb Tracker")

# Main Frame
main_frame = Frame(root)
main_frame.pack(padx=20, pady=20)

# Label
main_label = ttk.Label(main_frame, text="Choose From Drop Down Menu:")
main_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Dropdown setup
selected_option = StringVar()
selected_option.set("Select an Option")  # Default value

options = ['Phones', 'Laptops', 'Parts', 'Tools', 'All Items', 'Profit Report']
dropdown = OptionMenu(main_frame, selected_option, *options)
dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=W)

#Secondary Frame Holder
secondary_frame= Frame(main_frame)
secondary_frame.grid(row=4, column=0, columnspan=2, pady=10)


selected_option.trace("w", lambda *args: mc.handle_category_selection(selected_option.get(),secondary_frame))

root.mainloop()

