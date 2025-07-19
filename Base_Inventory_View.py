from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import main_controller as mc
import Laptop_Controller as lc
import Mark_As_Sold_Controller as masc
import Mark_As_Sold_View as masv


class Base_Inventory_View(Toplevel):

    def __init__(self, rootWindow, controller, item_type):
        Toplevel.__init__(self)
        #item_type = "Laptop"
        self.controller = controller


        self.title(f"{item_type}")
        self.geometry("900x800")

        frameLeft = Frame(self, width=100, height=200, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=LEFT, padx=20, pady=20)

        frameRight = Frame(self, width=70, height=40, highlightbackground="black", highlightthickness=2)
        frameRight.pack(side=RIGHT, padx=20, pady=20)

        self.lblPhoneList = ttk.Label(frameLeft, text=f"{item_type} List").grid(row=1, column=0, padx=10, pady=0)
        self.tboxData = tk.Text(frameLeft, width=50, height=40)
        self.tboxData.grid(row=2, column=0)

        # item information data entry
        self.lblBrand = ttk.Label(frameRight, text=f"{item_type} Brand:").grid(row=1, column=0, padx=10, pady=0)
        self.entBrand = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBrand.grid(row=1, column=1, padx=10, pady=10)

        self.lblModel = ttk.Label(frameRight, text=f"{item_type} Model:").grid(row=2, column=0, padx=10, pady=0)
        self.entModel = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entModel.grid(row=2, column=1, padx=10, pady=10)

        self.lblCost = ttk.Label(frameRight, text="Cost:").grid(row=3, column=0, padx=10, pady=0)
        self.entCost = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entCost.grid(row=3, column=1, padx=10, pady=10)

        self.lblBadParts = ttk.Label(frameRight, text="Bad Parts:").grid(row=4, column=0, padx=10, pady=0)
        self.entBadParts = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBadParts.grid(row=4, column=1, padx=10, pady=10)

        self.lblQuantity = ttk.Label(frameRight, text="Quantity:").grid(row=5, column=0, padx=10, pady=0)
        self.entQuantity = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entQuantity.grid(row=5, column=1, padx=10, pady=10)

        self.lblID = ttk.Label(frameRight, text="ID (Used for Updates):").grid(row=6, column=0, padx=10, pady=0)
        self.entID = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entID.grid(row=6, column=1, padx=10, pady=10)

        # Add Button
        self.btnAdd = ttk.Button(frameRight, text=f"Add {item_type}",
                                 command=lambda: [
                                     self.controller.add_item(self.entBrand.get(), self.entModel.get(),
                                                              self.entCost.get(),
                                                              self.entQuantity.get(), self.entBadParts.get(),
                                                              ),
                                     self.updateDisplay(item_type)
                                 ])
        self.btnAdd.grid(row=7, column=0, padx=10, pady=10)

        # Mark as sold button
        self.btnSold = ttk.Button(frameRight, text="Mark as Sold",
                                  command=lambda: [
                                      self.controller.mark_as_sold(self.entID.get()),
                                      masv.Mark_As_Sold_View(Toplevel, item_type,
                                                             self.controller.item_sold_info(self.entID.get())),
                                  ])

        self.btnSold.grid(row=7, column=1, padx=10, pady=10)

        # Display all phones button
        self.btnDisplay = ttk.Button(frameRight, text="Display All", command=lambda: self.updateDisplay(item_type))
        self.btnDisplay.grid(row=8, column=0, padx=10, pady=10)

        # Clear the data button
        self.btnClear = ttk.Button(frameRight, text="Clear the Data",
                                   command=lambda: [self.tboxData.delete("1.0", tk.END)])
        self.btnClear.grid(row=8, column=1, padx=10, pady=1)

        self.lblInstruction = ttk.Label(frameRight, text="Enter ID above to delete or search")
        self.lblInstruction.grid(row=10, column=0, columnspan=2, padx=0, pady=0)

        # Delete Button NEEDS FUNCTIONALITY
        self.btnDelete = ttk.Button(frameRight, text="Delete",
                                    command=lambda: [
                                        self.controller.delete(self.entID.get()),
                                        self.updateDisplay(item_type)])
        self.btnDelete.grid(row=11, column=0, pady=10, padx=10)

        # Search Button NEEDS FUNCTIONALITY
        self.btnSearch = ttk.Button(frameRight, text="Search",
                                    command=lambda: [
                                        self.tboxData.delete("1.0", tk.END),
                                        self.tboxData.insert(INSERT, self.controller.search(self.entSSN.get()))
                                    ])
        self.btnSearch.grid(row=11, column=1, padx=10, pady=10)
        # View Methods

        self.btnDisassembled = ttk.Button(frameRight, text="Disassembled", command=lambda:
        [self.controller.disassembled_item(self.entID.get())])
        self.btnDisassembled.grid(row=12, column=0, pady=10, padx=10)

    def updateDisplay(self,item_type):
        self.tboxData.delete("1.0", tk.END)

        rows = self.controller.get_all_items() ##### FIX IN CONTROLLER
        if not rows:
            self.tboxData.insert(tk.END, f"No {item_type} found.\n")
            return

        # Optional: add a header
        header = (f"{'ID':<3} {'Brand':<10} {'Model':<20} {'Cost':<7} {'Quantity':<8} {'Bad Parts':<25} {'Date Added'} "
                  f"{'Sold':<5} {'Fully Functional':<5}\n {'Notes'}")
        self.tboxData.insert(tk.END, header)
        self.tboxData.insert(tk.END, "-" * 100 + "\n")

        for row in rows:
            id, brand, model, cost, parts_used, quantity, purchase_date, disassembled, sold, fully_functional, notes = row
            formatted = (f"{id:<3} {brand:<10} {model:<20} ${cost:<6.2f} {parts_used:<25} {quantity:<8} {purchase_date}"
                         f" {sold:<5} {fully_functional:<5}\n {notes}\n")
            self.tboxData.insert(tk.END, formatted)


