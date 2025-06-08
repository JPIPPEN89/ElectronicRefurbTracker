import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Laptop_View as lv


class LaptopController:
    def __init__(self):
        db.LaptopDB().create_table()

    def add_item(self, brand, model, cost, quantity, bad_parts):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''INSERT INTO laptops (brand, model, cost, quantity, bad_parts)
                   VALUES (?,?,?,?,?)    
           ''', (brand, model, cost, quantity, bad_parts))
        conn.commit()
        conn.close()

    def mark_as_sold(self, laptop_id):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''
                   UPDATE laptops
                   SET sold = 1
                   WHERE id = ?
               ''', (laptop_id))
        conn.commit()
        conn.close()



    def get_all_laptops(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT * FROM laptops")
        rows = c.fetchall()
        conn.close()

        return rows