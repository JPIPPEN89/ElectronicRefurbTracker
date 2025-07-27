import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Laptop_View as lv
from Base_Inventory_Controller import Base_Inventory_Controller



class LaptopController(Base_Inventory_Controller):
    def __init__(self):
        db.LaptopDB().create_table()
        super().__init__('laptops')


    def laptop_cost(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(cost) FROM laptops")

        total_cost = c.fetchone()[0]
        if total_cost is None:
            return 0

        conn.close()
        return total_cost




