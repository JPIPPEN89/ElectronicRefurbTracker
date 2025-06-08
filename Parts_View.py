from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import main_controller as mc
import Parts_Controller as pc


class Parts_View(Toplevel):
    def __init__(self, rootWindow):
        Toplevel.__init__(self)
        self.controller = pc.Parts_Controller()

        self.title("Parts")
        self.geometry("900x800")

        frameLeft = Frame(self, width=100, height=200, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=LEFT, padx=20, pady=20)

        frameRight = Frame(self, width=70, height=40, highlightbackground="black", highlightthickness=2)
        frameRight.pack(side=RIGHT, padx=20, pady=20)

        self.lblPartsList = ttk.Label(frameLeft, text="Parts List").grid(row=1, column=0, padx=10, pady=0)
        self.tboxData = tk.Text(frameLeft, width=50, height=40)
        self.tboxData.grid(row=2, column=0)

        # Parts information data entry
        self.lblBrand = ttk.Label(frameRight, text="Parts Brand:").grid(row=1, column=0, padx=10, pady=0)
        self.entBrand = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBrand.grid(row=1, column=1, padx=10, pady=10)

        self.lblModel = ttk.Label(frameRight, text="Parts Model:").grid(row=2, column=0, padx=10, pady=0)
        self.entModel = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entModel.grid(row=2, column=1, padx=10, pady=10)

        self.lblCost = ttk.Label(frameRight, text="Cost:").grid(row=3, column=0, padx=10, pady=0)
        self.entCost = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entCost.grid(row=3, column=1, padx=10, pady=10)

        self.lblPartType = ttk.Label(frameRight, text="Part Type:").grid(row=4, column=0, padx=10, pady=0)
        self.entPartType = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entPartType.grid(row=4, column=1, padx=10, pady=10)

        self.lblQuantity = ttk.Label(frameRight, text="Quantity:").grid(row=5, column=0, padx=10, pady=0)
        self.entQuantity = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entQuantity.grid(row=5, column=1, padx=10, pady=10)

        self.lblID = ttk.Label(frameRight, text="ID (Used for Updates):").grid(row=6, column=0, padx=10, pady=0)
        self.entID = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entID.grid(row=6, column=1, padx=10, pady=10)

        # Add Parts Button
        self.btnAdd = ttk.Button(frameRight, text="Add Part",
                                 command=lambda: [
                                     self.controller.add_item(self.entBrand.get(), self.entModel.get(),
                                                              self.entPartType.get(), self.entCost.get(),
                                                              self.entQuantity.get()
                                                              ),
                                     self.updateDisplay()
                                 ])
        self.btnAdd.grid(row=7, column=0, padx=10, pady=10)

        # Mark as sold button
        self.btnUsed = ttk.Button(frameRight, text="Mark as Used",
                                  command=lambda: [
                                      self.controller.used_part(self.entID.get()), self.updateDisplay()])

        self.btnUsed.grid(row=7, column=1, padx=10, pady=10)

        # Display all phones button
        self.btnDisplay = ttk.Button(frameRight, text="Display All", command=self.updateDisplay)
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
                                        self.updateDisplay()])
        self.btnDelete.grid(row=11, column=0, pady=10, padx=10)

        # Search Button NEEDS FUNCTIONALITY
        self.btnSearch = ttk.Button(frameRight, text="Search",
                                    command=lambda: [
                                        self.tboxData.delete("1.0", tk.END),
                                        self.tboxData.insert(INSERT, self.controller.search(self.entSSN.get()))
                                    ])
        self.btnSearch.grid(row=11, column=1, padx=10, pady=10)
        # View Methods

    def updateDisplay(self):
        self.tboxData.delete("1.0", tk.END)

        rows = self.controller.get_all_parts()
        if not rows:
            self.tboxData.insert(tk.END, "No laptops found.\n")
            return

        # Optional: add a header
        header = f"{'ID':<3} {'Brand':<10} {'Model':<20} {'Part Type':<25} {'Cost':<7} {'Quantity':<8} {'Used':<5} {'Date Added'}\n"
        self.tboxData.insert(tk.END, header)
        self.tboxData.insert(tk.END, "-" * 100 + "\n")

        for row in rows:
            id, brand, model, part_type, cost, quantity, used_part, purchase_date,  = row
            formatted = f"{id:<3} {brand:<10} {model:<20} {part_type:<25} ${cost:<6.2f} {quantity:<8} {used_part:<5} {purchase_date}\n"
            self.tboxData.insert(tk.END, formatted)

    # def getFile(self):
    #     fileName = filedialog.askopenfile(title="", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    #     row_count = self.controller.load(fileName)
    #     self.lblStatus.config(text="Students Loaded: " + str(row_count))
    #     self.updateDisplay()

    def Choose_Sold(self):
        pass
