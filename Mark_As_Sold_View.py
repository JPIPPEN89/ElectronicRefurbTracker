from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import main_controller as mc
import Mark_As_Sold_Controller as sc
from main import options
import Parts_Controller as pc



class Sold_View(Toplevel):
    def __init__(self, rootWindow):
        Toplevel.__init__(self)
        self.controller = sc.Sold_Controller()

        self.title("Sales")
        self.geometry("900x800")

        frameLeft = Frame(self, width=100, height=200, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=LEFT, padx=20, pady=20)

        frameRight = Frame(self, width=70, height=40, highlightbackground="black", highlightthickness=2)
        frameRight.pack(side=RIGHT, padx=20, pady=20)

        self.lblSoldList = ttk.Label(frameLeft, text="Sales List").grid(row=1, column=0, padx=10, pady=0)
        self.tboxData = tk.Text(frameLeft, width=50, height=40)
        self.tboxData.grid(row=2, column=0)

        self.lblSoldFor = ttk.Label(frameRight, text="Sold For:").grid(row=1, column=0, padx=10, pady=10)
        self.entSoldFor = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entSoldFor.grid(row=1, column=1, padx=10,pady=10)

        self.lblPartsUsed = ttk.Label(frameRight, text="Parts Used (Ent ID):").grid(row=1, column=0, padx=10, pady=10)
        self.entPartsUsed = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entPartsUsed.grid(row=2, column=1, padx=10, pady=10)


        # Add Phone Button
        self.btnShowParts = ttk.Button(frameRight, text="Show Parts",
                                 command=lambda: self.Parts_Display())
        self.btnShowParts.grid(row=7, column=0, padx=10, pady=10)

        # Mark as sold button
        self.btnSold = ttk.Button(frameRight, text="Done",
                                  command=lambda: [
                                      self.controller.mark_as_sold(self.entID.get()), self.updateDisplay()])

        self.btnSold.grid(row=7, column=1, padx=10, pady=10)

        # Display all phones button
        # self.btnDisplay = ttk.Button(frameRight, text="Display All Sold", command=self.updateDisplay)
        # self.btnDisplay.grid(row=8, column=0, padx=10, pady=10)

        # Clear the data button
        self.btnClear = ttk.Button(frameRight, text="Clear the Data",
                                   command=lambda: [self.tboxData.delete("1.0", tk.END)])
        self.btnClear.grid(row=8, column=1, padx=10, pady=1)

        # self.lblInstruction = ttk.Label(frameRight, text="Enter ID above to delete or search")
        # self.lblInstruction.grid(row=10, column=0, columnspan=2, padx=0, pady=0)
        #
        # # Delete Button NEEDS FUNCTIONALITY
        # self.btnDelete = ttk.Button(frameRight, text="Delete",
        #                             command=lambda: [
        #                                 self.controller.delete(self.entID.get()),
        #                                 self.updateDisplay()])
        # self.btnDelete.grid(row=11, column=0, pady=10, padx=10)
        #
        # # Search Button NEEDS FUNCTIONALITY
        # self.btnSearch = ttk.Button(frameRight, text="Search",
        #                             command=lambda: [
        #                                 self.tboxData.delete("1.0", tk.END),
        #                                 self.tboxData.insert(INSERT, self.controller.search(self.entSSN.get()))
        #                             ])
        # self.btnSearch.grid(row=11, column=1, padx=10, pady=10)
        # # View Methods

    def updateDisplay(self):
        self.tboxData.delete("1.0", tk.END)

        rows = sc.Sold_Controller().get_all_sales()
        if not rows:
            self.tboxData.insert(tk.END, "No sales found.\n")
            return

        header = f"{'ID':<3} {'Brand':<10} {'Model':<20} {'Cost':<7} {'Quantity':<8} {'Parts Used':<25} {'Sold':<5} {'Date Added'}\n"
        self.tboxData.insert(tk.END, header)
        self.tboxData.insert(tk.END, "-" * 100 + "\n")

        for row in rows:
            id, item_type, brand, model, sold_for, parts_used, total_cost, total_profit, quantity, sale_date, sold = row
            formatted = (f"{id:<3} {brand:<10} {model:<20} ${sold_for:<6.2f} "
                         f"{parts_used:<25} {total_cost:<6.2f} {total_profit:<6.2f} {quantity:<8} {sale_date}\n")
            self.tboxData.insert(tk.END, formatted)

    def Parts_Display(self):
        self.tboxData.delete("1.0", tk.END)
        rows = pc.Parts_Controller().get_all_parts()

        if not rows:
            self.tboxData.insert(tk.END, "No Parts Found.\n")
            return

        header = f"{'ID':<3} {'Brand':<10} {'Model':<20} {'Part Type':<25} {'Cost':<7} {'Quantity':<8} {'Used':<5} {'Date Added'}\n"
        self.tboxData.insert(tk.END, header)
        self.tboxData.insert(tk.END, "-" * 100 + "\n")

        for row in rows:
            id, brand, model, part_type, cost, quantity, used_part, purchase_date, = row
            formatted = f"{id:<3} {brand:<10} {model:<20} {part_type:<25} ${cost:<6.2f} {quantity:<8} {used_part:<5} {purchase_date}\n"
            self.tboxData.insert(tk.END, formatted)











