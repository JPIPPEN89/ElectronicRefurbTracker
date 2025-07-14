import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Mark_As_Sold_View as sv
import Parts_Controller as pc



class Sold_Controller:
    def __init__(self):
        db.SalesDB().create_table()


    def sold_view(self, category, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        sv.Sold_View(Toplevel)

    # in mark_as_sold functions save this as a variable and then sub it into add_sale function for parts_cost
    def parts_to_cost(self, id):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('''SELECT cost FROM parts WHERE id = ?''', (id,))

        cost = c.fetchone()

        conn.close()
        return cost[0] if cost else 0

    def part_type(self, id):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('''SELECT part_type FROM parts WHERE id = ?''', (id,))

        part = c.fetchone()
        if part:
            pc.Parts_Controller().used_part(id)
            return str(part)
        else:
            return "None"

    #Connect to db to get base_cost, brand, model, item_type
    def add_sale(self, item_type, brand, model, sold_for, parts_used, parts_cost, quantity, entCost):

        total_cost = entCost + parts_cost
        profit = float(sold_for) - total_cost
        parts_used = parts_used  # store part names for now

        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('''
            INSERT INTO sales (item_type, item_brand, item_model, sold_for, parts_used, parts_cost, total_cost, total_profit, quantity)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (item_type, brand, model, sold_for, parts_used, parts_cost, total_cost, profit, quantity))

        conn.commit()
        conn.close()

    def get_all_sales(self):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute("SELECT * FROM sales")
        rows = c.fetchall()
        conn.close()

        return rows

    def sold_total(self):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute("SELECT SUM(sold_for) FROM sales")
        total = c.fetchone()[0]
        conn.close()

        return total

    def laptop_sold_total(self):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute("SELECT SUM(sold_for) FROM sales WHERE item_type = 'Laptop'")
        total = c.fetchone()[0]
        conn.close()

        return total if total is not None else 0

    def phone_sold_total(self):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute("SELECT SUM(sold_for) FROM sales WHERE item_type = 'Phone'")
        total = c.fetchone()[0]
        conn.close()

        return total if total is not None else 0

    def parts_sold_total(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(sold_for) FROM sales WHERE item_type = 'Parts'")

        total = c.fetchone()[0]
        conn.close()

        return total if total is not None else 0