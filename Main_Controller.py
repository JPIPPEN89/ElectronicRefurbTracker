from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Phones_View as pv
import Laptop_View as lv
import Parts_View as pav
import Tools_View as tv

def handle_category_selection(category, frame):
    # Clear previous menu widgets
    for widget in frame.winfo_children():
        widget.destroy()

    if category == 'Phones':
        pv.Phone_View(Toplevel)
    elif category == 'Laptops':
        lv.Laptop_View(Toplevel)
    elif category == 'Parts':
        pav.Parts_View(Toplevel)
    elif category == 'Tools':
        tv.Tools_View(Toplevel)


