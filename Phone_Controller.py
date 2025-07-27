import Phones_View as pv
import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
from Base_Inventory_Controller import Base_Inventory_Controller

class Phone_Controller(Base_Inventory_Controller):
    def __init__(self):
        super().__init__('phones')
        db.PhonesDB().create_table()


    def phone_cost(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(cost) FROM phones")
        total_cost = c.fetchone()[0]
        conn.close()

        if total_cost is None:
            return 0

        return total_cost
#