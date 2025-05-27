from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Phones_View as pv


def handle_category_selection(category, frame):
    # Clear previous menu widgets
    for widget in frame.winfo_children():
        widget.destroy()

    if category == 'Phones':
        pv.Phone_View(Toplevel)
    elif category == 'Laptops':
        _show_laptop_menu(frame)
    elif category == 'Parts':
        _show_parts_menu(frame)
    elif category == 'Tools':
        _show_tools_menu(frame)


def _show_phone_menu(frame):
    option = tk.StringVar()
    option.set("Select a Phone Option")
    actions = ['Add Phone', 'Delete Phone', 'Mark as Sold', 'Update Phone Info', 'Display All Phones']
    dropdown = tk.OptionMenu(frame, option, *actions)
    dropdown.pack()


def _show_laptop_menu(frame):
    option = tk.StringVar()
    option.set("Select a Laptop Option")
    actions = ['Add Laptop', 'Delete Laptop', 'Mark as Sold', 'Update Laptop Info', 'Display All Laptops']
    dropdown = tk.OptionMenu(frame, option, *actions)
    dropdown.pack()


def _show_parts_menu(frame):
    option = tk.StringVar()
    option.set("Select a Part Option")
    actions = ['Add Part', 'Delete Part', 'Update Part Info', 'Display All Parts']  # You can modify this
    dropdown = tk.OptionMenu(frame, option, *actions)
    dropdown.pack()


def _show_tools_menu(frame):
    option = tk.StringVar()
    option.set("Select a Tool Option")
    actions = ['Add Tool', 'Delete Tool', 'Update Tool Info', 'Display All Tools']  # You can modify this
    dropdown = tk.OptionMenu(frame, option, *actions)
    dropdown.pack()


class DBController:
    def __init__(self):
        self.laptop_db = LaptopDB()
        self.phones_db = PhonesDB()
        self.parts_db = PartsDB()
        self.sales_db = SalesDB()

class ViewController:

    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.show_main_view()


    def Phone_View(self):
        self._clear_view()
        self.current_view = pv.Phone_View(self.root, self)
        self.current_view.pack(fill="both", expand=True)

    #def Phon
    # def selected(self, selected_option):
    #
    #     if selected_option == 'Phones':
    #         phone_option = StringVar()
    #         phone_option.set("Select an Option")
    #
    #         options = ['Add Phone', 'Delete Phone', 'Mark as Sold', 'Update Phone Info']
    #         dropdown = OptionMenu(main_frame, phone_option, *options)
    #         dropdown.grid(row=4, column=1, padx=10, pady=10, sticky=W)