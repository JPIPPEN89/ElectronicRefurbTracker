import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Tools_View as tv

class Tools_Controller:
    def __init__(self):
        db.ToolsDB().create_table()

    def add_item(self,name, cost, quantity):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('''INSERT INTO tools(name, cost, quantity)
                    VALUES (?,?,?)''',(name, cost, quantity))

        conn.commit()
        conn.close()

    def get_all_tools(self):
        conn = db.Database().connect()
        c = conn.cursor()

        c.execute('SELECT * FROM tools')
        rows =c.fetchall()
        conn.close()

        return rows