import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Mark_As_Sold_View as sv


class Sold_Controller:
    def __init__(self):
        db.SalesDB().create_table()

    # in mark_as_sold functions save this as a variable and then sub it into add_sale function for parts_cost
    def parts_to_cost(self, id):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('''SELECT cost FROM parts WHERE id = ?''', (id,))

        cost = c.fetchone()

        conn.close()
        return cost[0] if cost else 0

    #Connect to db to get base_cost, brand, model, item_type
    def add_sale(self, item_type, brand, model, sold_for, parts_used, total_cost, total_profit, quantity):

        parts_cost = self.parts_to_cost(parts_used) #Scrap this it should go into the view
        total_cost = base_cost + parts_cost
        profit = sold_for - total_cost
        parts_used = ", ".join(parts_used)  # store part names for now

        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('''
            INSERT INTO sales (item_type, brand, model, sold_for, parts_used, total_cost, total_profit, quantity)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (item_type, brand, model, sold_for, parts_used, total_cost, total_profit, quantity))

        conn.commit()
        conn.close()

    def get_all_sales(self):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute("SELECT * FROM sales")
        rows = c.fetchall()
        conn.close()

        return rows