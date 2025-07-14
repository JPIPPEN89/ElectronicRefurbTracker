import Phones_View as pv
import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk


class Phone_Controller:
    def __init__(self):
        db.PhonesDB().create_table()  # Added () to instantiate the class

    def add_item(self, brand, model, cost, quantity, bad_parts):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''INSERT INTO phones (brand, model, cost, bad_parts, quantity)
                     VALUES (?, ?, ?, ?,?)''', (brand, model, cost, bad_parts, quantity))
        conn.commit()
        conn.close()

    #####NEEDS FUNCTIONALITY FOR SOLD#############
    def mark_as_sold(self, phone_id):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''UPDATE phones
                     SET sold = 1
                     WHERE id = ?''', (phone_id,))
        conn.commit()
        conn.close()

################FIXING#####################
    def phone_sold_info(self, phone_id):
        conn = db.Database().connect()
        c = conn.cursor()

        type = 'Phone'
        c.execute('''SELECT * FROM phones WHERE id = ?''', (phone_id,))
        result = c.fetchone()
        conn.close()

        id, brand, model, cost, parts_used, quantity, purchase_date, sold = result

        return result



    def get_all_phones(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT * FROM phones")
        rows = c.fetchall()
        conn.close()

        return rows

    def delete(self):
        pass

    def phone_cost(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(cost) FROM phones")
        total_cost = c.fetchone()[0]
        conn.close()

        return total_cost