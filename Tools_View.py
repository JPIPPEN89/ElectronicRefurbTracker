from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import main_controller as mc
import Tools_Controller as tc


class Tools_View(Toplevel):
    def __init__(self, rootWindow):
        Toplevel.__init__(self)
        self.controller = tc.Tools_Controller()

        self.title("Laptops")
        self.geometry("900x800")

        frameLeft = Frame(self, width=100, height=200, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=LEFT, padx=20, pady=20)

        frameRight = Frame(self, width=70, height=40, highlightbackground="black", highlightthickness=2)
        frameRight.pack(side=RIGHT, padx=20, pady=20)

        self.lblPhoneList = ttk.Label(frameLeft, text="Tools List").grid(row=1, column=0, padx=10, pady=0)
        self.tboxData = tk.Text(frameLeft, width=50, height=40)
        self.tboxData.grid(row=2, column=0)

        # Phone information data entry
        self.lblName = ttk.Label(frameRight, text="Tools Name:").grid(row=1, column=0, padx=10, pady=0)
        self.entName = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entName.grid(row=1, column=1, padx=10, pady=10)



        self.lblCost = ttk.Label(frameRight, text="Cost:").grid(row=3, column=0, padx=10, pady=0)
        self.entCost = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entCost.grid(row=3, column=1, padx=10, pady=10)


        self.lblQuantity = ttk.Label(frameRight, text="Quantity:").grid(row=5, column=0, padx=10, pady=0)
        self.entQuantity = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entQuantity.grid(row=5, column=1, padx=10, pady=10)

        # Add Phone Button
        self.btnAdd = ttk.Button(frameRight, text="Add Tools",
                                 command=lambda: [
                                     self.controller.add_item(self.entName.get(),
                                                              self.entCost.get(),
                                                              self.entQuantity.get()
                                                              ),
                                     self.updateDisplay()
                                 ])
        self.btnAdd.grid(row=7, column=0, padx=10, pady=10)

        # Display all tools button
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

        rows = self.controller.get_all_tools()
        if not rows:
            self.tboxData.insert(tk.END, "No laptops found.\n")
            return

        # Optional: add a header
        header = f"{'ID':<3} {'Tool':<10} {'Cost':<7} {'Quantity':<8} {'Date Added'}\n"
        self.tboxData.insert(tk.END, header)
        self.tboxData.insert(tk.END, "-" * 100 + "\n")

        for row in rows:
            id, tool, cost, quantity, purchase_date = row
            formatted = f"{id:<3} {tool:<10} ${cost:<6.2f} {quantity:<8} {purchase_date}\n"
            self.tboxData.insert(tk.END, formatted)

    # def getFile(self):
    #     fileName = filedialog.askopenfile(title="", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    #     row_count = self.controller.load(fileName)
    #     self.lblStatus.config(text="Students Loaded: " + str(row_count))
    #     self.updateDisplay()

    def Choose_Sold(self):
        pass
