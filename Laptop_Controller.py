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



    def item_sold_info(self, laptop_id):
        conn = db.Database().connect()
        c = conn.cursor()

        type = 'Laptop'
        c.execute('''SELECT * FROM laptops WHERE id = ?''', (laptop_id,))
        result = c.fetchone()
        conn.close()

        id, brand, model, cost, parts_used, quantity, purchase_date, sold = result

        return result


    def get_all_items(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT * FROM laptops")
        rows = c.fetchall()
        conn.close()

        return rows

    def laptop_cost(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(cost) FROM laptops")

        total_cost = c.fetchone()[0]
        if total_cost is None:
            return 0

        conn.close()
        return total_cost

    def disassembled_item(self,id):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''
                   UPDATE laptops
                   SET disassembled = 1
                   WHERE id = ?
               ''', (id))
        conn.commit()

        conn.close()



