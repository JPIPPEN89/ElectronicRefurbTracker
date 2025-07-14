import database as db
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Phone_Controller as phc
import Laptop_Controller as lpc
import Parts_Controller as ptc
import Tools_Controller as ttc
import Mark_As_Sold_Controller as masc
import Profit_Report_View as prv

class Profit_Report_Controller:
    def total_cost(self):
        phones = phc.Phone_Controller().phone_cost()
        laptops = lpc.LaptopController().laptop_cost()
        parts = ptc.Parts_Controller().parts_cost()
        tools = ttc.Tools_Controller().tools_cost()

        total = phones + laptops + parts + tools
        return total

    def total_profit(self):
        cost = self.total_cost()
        sold = masc.Sold_Controller().sold_total()
        profit = sold - cost

        return profit

    def total_sold(self):
        sold = masc.Sold_Controller().sold_total()
        return sold

    #### LAPTOPS ####
    def laptop_cost(self):
        laptops = lpc.LaptopController().laptop_cost()
        return laptops

    def laptops_sold(self):
        laptops = masc.Sold_Controller().laptop_sold_total()
        return laptops

    def laptop_profit(self):
        laptops_sold = self.laptops_sold()
        laptops_cost = self.laptop_cost()
        return laptops_sold - laptops_cost

    def total_laptops(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM laptops")
        rows = c.fetchone()[0]
        conn.close()

        return rows

    def laptops_sold_count(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(sold) FROM laptops")
        rows = c.fetchone()[0]
        conn.close()

        return rows

    def laptops_in_stock(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM laptops WHERE sold = 0")
        rows = c.fetchone()[0]
        conn.close()

        return rows

    # Phones
    def phone_cost(self):
        phones = phc.Phone_Controller().phone_cost()
        return phones

    def phones_sold(self):
        phones = masc.Sold_Controller().phone_sold_total()
        return phones

    def phone_profit(self):
        phones_sold = self.phones_sold()
        phone_cost = self.laptop_cost()
        return phones_sold - phone_cost

    def total_phones(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM phones")
        rows = c.fetchone()[0]
        conn.close()

        return rows

    def phones_sold_count(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(sold) FROM phones")
        rows = c.fetchone()[0]
        conn.close()

        return rows

    def phones_in_stock(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM phones WHERE sold = 0")
        rows = c.fetchone()[0]
        conn.close()

        return rows

    # Parts
    def parts_cost(self):
        parts = ptc.Parts_Controller().parts_cost()
        return parts

    def parts_sold(self):
        return masc.Sold_Controller().parts_sold_total()


    def parts_profit(self):
        pass

    def parts_used(self):
        pass

    def total_parts(self):
        pass

    def parts_sold_count(self):
        pass

    def parts_in_stock(self):
        pass

    # Tools
    def tools_cost(self):
        tools = ttc.Tools_Controller().tools_cost()
        return tools