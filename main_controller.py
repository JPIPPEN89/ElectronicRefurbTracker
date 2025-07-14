from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Phones_View as pv
import Laptop_View as lv
import Parts_View as pav
import Tools_View as tv
import Mark_As_Sold_View as sv
import Profit_Report_View as prv



def handle_category_selection(category, frame):
        # Clear previous menu widgets
        print("HANDLE FUNCTION CALLED:", category)
        for widget in frame.winfo_children():
            widget.destroy()

        if category == 'Phones':
            print("Phones Open")
            pv.Phone_View(Toplevel)
        elif category == 'Laptops':
            print("Laptops Open")
            lv.Laptop_View(Toplevel)
        elif category == 'Parts':
            print("Parts Open")
            pav.Parts_View(Toplevel)
        elif category == 'Tools':
            print("Tools Open")
            tv.Tools_View(Toplevel)
       #elif category == 'Sold Items':
           # sv.Sold_View(Toplevel)
        elif category == 'Profit Report':
            print("Profit Report Open")
            prv.Profit_Report_View(Toplevel)



