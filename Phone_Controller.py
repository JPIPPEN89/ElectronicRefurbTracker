import Phones_View as pv
import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk

class Phone_Controller:
    def __init__(self):
        db.PhonesDB().create_table()  # Added () to instantiate the class

    def add_item(self, brand, model, cost, quantity, diagnosis):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''INSERT INTO phones (brand, model, cost, quantity, diagnosis)
                     VALUES (?, ?, ?, ?,?)''', (brand, model, cost, quantity, diagnosis))
        conn.commit()
        conn.close()

    def mark_as_sold(self, phone_id):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''UPDATE phones
                     SET sold = 1
                     WHERE id = ?''', (phone_id,))
        conn.commit()
        conn.close()

    def get_all_phones(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT * FROM phones")
        rows = c.fetchall()
        conn.close()

        return rows