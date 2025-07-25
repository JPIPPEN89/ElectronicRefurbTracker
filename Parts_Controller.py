import Parts_View as pv
import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
import main_controller as mc


class Parts_Controller:
    def __init__(self):
        db.PartsDB().create_table()

    def add_item(self, brand, model, part_type, cost, quantity):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''INSERT INTO parts (brand, model, part_type, cost, quantity)
                               VALUES (?,?,?,?,?)    
                       ''', (brand, model, part_type, cost, quantity))
        conn.commit()
        conn.close()

    def used_part(self,part_id):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('''UPDATE parts
                    SET used_part = 1
                    WHERE id = ?''',(part_id))

        conn.commit()
        conn.close()

    def get_all_parts(self):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('SELECT * FROM parts')
        rows = c.fetchall()
        conn.close()

        return rows

    def parts_cost(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(cost) FROM parts")
        total_cost = c.fetchone()[0]

        if total_cost is None:
            return 0

        conn.close()
        return total_cost