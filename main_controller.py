import Laptop_Controller
import Mark_As_Sold_View
from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Phones_View as pv
import Laptop_View as lv
import Parts_View as pav
import Tools_View as tv
import Mark_As_Sold_View as masv
import Profit_Report_View as prv
import Base_Inventory_View as bv
import Other_Electronics_View as ov




def handle_category_selection(category, frame):
        # Clear previous menu widgets
        print("HANDLE FUNCTION CALLED:", category)
        for widget in frame.winfo_children():
            widget.destroy()

        if category == 'Phones':
            print("Phones Open")
            pv.Phones_View(Toplevel)

        elif category == 'Laptops':
            print("Laptops Open")
            lv.Laptop_View(Toplevel)

        elif category == 'Other Electronics':
            print("Other Electronics Open")
            ov.Other_Electronics_View(Toplevel)

        elif category == 'Parts':
            print("Parts Open")
            pav.Parts_View(Toplevel)
        elif category == 'Tools':
            print("Tools Open")
            tv.Tools_View(Toplevel)
        elif category == 'Sold Items':
            masv.Mark_As_Sold_View(Toplevel)

        elif category == 'Profit Report':
            print("Profit Report Open")
            prv.Profit_Report_View(Toplevel)



