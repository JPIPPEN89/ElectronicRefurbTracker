from database import LaptopDB, SalesDB, PhonesDB, PartsDB
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Main_Controller as mc
import Phone_Controller as pc

class Phone_View(Toplevel):
    def __init__(self, rootWindow):
        Toplevel.__init__(self)
        self.controller = pc.Phone_Controller()

        self.title("Linked List Demo")
        self.geometry("900x800")

        frameLeft = Frame(self, width=30, height=40, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=LEFT, padx=20, pady=20)

        frameRight = Frame(self, width=70, height=40, highlightbackground="black", highlightthickness=2)
        frameRight.pack(side=RIGHT, padx=20, pady=20)


        self.lblPhoneList = ttk.Label(frameLeft, text="Phones List").grid(row=1, column=0, padx=10, pady=0)
        self.tboxData = tk.Text(frameLeft, width=30, height=20)
        self.tboxData.grid(row=2, column=0)

        # Phone information data entry
        self.lblBrand = ttk.Label(frameRight, text="Phone Brand:").grid(row=1, column=0, padx=10, pady=0)
        self.entBrand = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBrand.grid(row=1, column=1, padx=10, pady=10)

        self.lblModel = ttk.Label(frameRight, text="Phone Model:").grid(row=2, column=0, padx=10, pady=0)
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


        # Buttons
####WE ARE STOPPPING HERE############################################################################################################
        #######################################################
        self.btnAppend = ttk.Button(frameRight, text="Add Phone",
                                    command=lambda: [
                                        self.controller.add_item(self.entBrand.get(), self.entModel.get(), self.entCost.get(),
                                                               self.entQuantity.get(), self.entBadParts.get(),
                                                            ),
                                        self.updateDisplay()
                                    ])
        self.btnAppend.grid(row=7, column=0, padx=10, pady=10)


############### ADDING PARTS TO SOLD AFTER GETTING FUNCTIONAL ########################
        self.btnPrepend = ttk.Button(frameRight, text="Mark as Sold",
                                     command=lambda: [
                                         self.controller.prepend(self.entFirstName.get(), self.entLastName.get(),
                                                                 self.entSSN.get(), self.entPhone.get(),
                                                                 self.entEmail.get()), self.updateDisplay()])

        self.btnPrepend.grid(row=7, column=1, padx=10, pady=10)

        self.btnDisplay = ttk.Button(frameRight, text="Display All", command=self.updateDisplay)
        self.btnDisplay.grid(row=8, column=0, padx=10, pady=10)

        self.btnClear = ttk.Button(frameRight, text="Clear the Data",
                                   command=lambda: [self.tboxData.delete("1.0", tk.END)])
        self.btnClear.grid(row=8, column=1, padx=10, pady=1)

        self.btnLoadFile = ttk.Button(frameRight, text="Open", command=lambda: [self.getFile()])
        self.btnLoadFile.grid(row=9, column=0, padx=10, pady=10)

        self.lblStatus = ttk.Label(frameLeft, text="")
        self.lblStatus.grid(row=5, column=0, padx=10, pady=10)

        self.lblInstruction = ttk.Label(frameRight, text="Enter SSN above to delete or search")
        self.lblInstruction.grid(row=10, column=0, columnspan=2, padx=0, pady=0)

        self.btnDelete = ttk.Button(frameRight, text="Delete",
                                    command=lambda: [
                                        self.controller.delete(self.entSSN.get()),
                                        self.updateDisplay()])
        self.btnDelete.grid(row=11, column=0, pady=10, padx=10)

        self.btnSearch = ttk.Button(frameRight, text="Search",
                                    command=lambda: [
                                        self.tboxData.delete("1.0", tk.END),
                                        self.tboxData.insert(INSERT, self.controller.search(self.entSSN.get()))
                                    ])
        self.btnSearch.grid(row=11, column=1, padx=10, pady=10)
        # View Methods

    def updateDisplay(self):
        self.tboxData.delete("1.0", tk.END)

        rows = self.controller.get_all_phones()
        if not rows:
            self.tboxData.insert(tk.END, "No phones found.\n")
            return

        # Optional: add a header
        header = f"{'ID':<3} {'Brand':<10} {'Model':<20} {'Cost':<7} {'Quantity':<8} {'Parts':<25} {'Sold':<5} {'Date Added'}\n"
        self.tboxData.insert(tk.END, header)
        self.tboxData.insert(tk.END, "-" * 100 + "\n")

        for row in rows:
            id, brand, model, cost, parts_used, quantity, purchase_date, sold = row
            formatted = f"{id:<3} {brand:<10} {model:<20} ${cost:<6.2f} {quantity:<8} {parts_used:<25} {sold:<5} {purchase_date}\n"
            self.tboxData.insert(tk.END, formatted)

    def getFile(self):
        fileName = filedialog.askopenfile(title="", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
        row_count = self.controller.load(fileName)
        self.lblStatus.config(text="Students Loaded: " + str(row_count))
        self.updateDisplay()

    def Choose_Sold(self):
        pass
