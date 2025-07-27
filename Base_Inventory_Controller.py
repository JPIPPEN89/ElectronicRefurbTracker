import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Base_Inventory_View as bv
from datetime import date



class Base_Inventory_Controller:
    def __init__(self, item_type):
        # if item_type == 'Laptop':
        #     self.item_type = 'laptops'
        # elif item_type == 'Phone':
        #     self.item_type ='phones'
        # elif item_type == 'Other':
        #     self.item_type = 'other_electronics'
        self.item_type = item_type




    def add_item(self, brand, model, cost, quantity, bad_parts, ram, ssd, notes):
        conn = db.Database().connect()
        c = conn.cursor()

        new_id = self.ID_Generator()

        command = f'INSERT INTO {self.item_type} (custom_id ,brand, model, cost, quantity, bad_parts, ram, ssd, notes) VALUES (?,?,?,?,?,?,?,?,?)'

        c.execute(command, (new_id, brand,model, cost, quantity, bad_parts, ram, ssd, notes))
        conn.commit()
        conn.close()

    def mark_as_sold(self, _id):
        conn = db.Database().connect()
        c = conn.cursor()

        command = f'UPDATE {self.item_type} SET sold = 1 WHERE custom_id = ?'
        c.execute(command, (_id,))
        conn.commit()

        conn.close()



    def item_sold_info(self, _id):
        conn = db.Database().connect()
        c = conn.cursor()

        command = f"SELECT * FROM {self.item_type} WHERE custom_id = ?"
        c.execute(command, (_id,))
        result = c.fetchone()
        conn.close()

        (id, custom_id, brand, model, cost, parts_used, quantity, ram, ssd,
         purchase_date, disassembled, sold, fully_functional, notes) = result

        return result


    def get_all_items(self):
        conn = db.Database().connect()
        c = conn.cursor()

        command = f"SELECT * FROM {self.item_type}"
        c.execute(command)
        rows = c.fetchall()
        conn.close()

        return rows

    def items_total_cost(self):
        conn = db.Database().connect()
        c = conn.cursor()

        command = f"SELECT SUM(cost) FROM {self.item_type}"
        c.execute(command)

        total_cost = c.fetchone()[0]
        if total_cost is None:
            return 0

        conn.close()
        return total_cost

    def disassembled_item(self,id):
        conn = db.Database().connect()
        c = conn.cursor()

        command = f"UPDATE {self.item_type} SET disassembled = 1 WHERE custom_id = ?"
        c.execute(command, (id))
        conn.commit()

        conn.close()

    def ID_Generator(self):
        conn = db.Database().connect()
        c = conn.cursor()

        prefix = str(self.item_type[:3]).upper()  # e.g., LAP for Laptop
        today = date.today()
        mid = f"{today.month:02}{today.day:02}"  # e.g., 0716

        # This assumes your ID field is stored as a string like LAP07160001
        c.execute(f"SELECT id FROM {self.item_type} WHERE id LIKE ? ORDER BY id DESC LIMIT 1", (f"{prefix}{mid}%",))
        last_id_row = c.fetchone()

        if last_id_row:
            last_id = last_id_row[0]
            # Get numeric part at the end and increment it
            suffix = int(last_id[-3:]) + 1
        else:
            suffix = 1

        conn.close()

        new_id = f"{prefix}{mid}{suffix:04}"
        return new_id


    def update_item(self, id):
        conn = db.Database().connect()
        c = conn.cursor()

        command = f'UPDATE {self.item_type} WHERE custom_id = ?'

        pass

    def delete_item(self, id):
        conn = db.Database().connect()
        c = conn.cursor()

        command= f"DELETE FROM {self.item_type} WHERE custom_id = ?"
        c.execute(command, (id,))

        conn.commit()
        conn.close()


