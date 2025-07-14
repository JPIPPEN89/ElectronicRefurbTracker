
import tkinter as tk
from tkinter import *
from tkinter import ttk
import main_controller as mc
import Profit_Report_Controller as prc

class Profit_Report_View(Toplevel):

    def __init__(self, rootWindow):
        Toplevel.__init__(self)

        self.controller = prc.Profit_Report_Controller()

        self.title("Profit Report")
        self.geometry("900x800")

        # Scrollable canvas setup
        canvas = Canvas(self, borderwidth=0, background="#ffffff")
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, background="#ffffff")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack them
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Replace 'frameLeft' with 'scrollable_frame' below
        frameLeft = scrollable_frame

        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        self.lblProfitReport = (Label(frameLeft, text="Profit Report", font=('Helvetica', 16, 'bold'))
                                .grid(row=0, column=0, padx=10, pady=10))

        self.lblTotalSpent = (Label(frameLeft, text=f"Total Spent: $ {float(self.controller.total_cost())}", font=('Helvetica', 12))
                              .grid(row=1, column=0, padx=10, pady=10))

        self.lblTotalSold = (Label(frameLeft, text=f"Total Sold: $ {float(self.controller.total_sold())}", font=('Helvetica', 12))
                             .grid(row=2, column=0, padx=10, pady=10))

        self.lblTotalProfit = (Label(frameLeft, text=f"Total Profit: $ {float(self.controller.total_profit())}", font=('Helvetica', 12))
                               .grid(row=3, column=0, padx=10, pady=10))

        self.lblSep = (Label(frameLeft, text="-----------------------------------------------", font=('Helvetica', 12))
                       .grid(row=4, column=0, padx=10, pady=10))

        #LAPTOPS
        self.lblLaptops = (Label(frameLeft, text="Laptops", font=('Helvetica', 12, 'bold'))
                           .grid(row=5, column=0, padx=10, pady=10))

        self.lblLaptopsCost = (Label(frameLeft, text=f"Total Cost of Laptops: ${self.controller.laptop_cost()}", font=('Helvetica', 12))
                               .grid(row=6, column=0, padx=10, pady=10))

        self.lblSoldLaptops = (Label(frameLeft, text=f"Total Sold Laptops: ${self.controller.laptops_sold()}", font=('Helvetica', 12))
                               .grid(row=7, column=0, padx=10, pady=10))

        self.lblLaptopProfit = (
            Label(frameLeft, text=f"Laptop Profit: ${self.controller.laptop_profit()}", font=('Helvetica', 12))
            .grid(row=8, column=0, padx=10, pady=10))

        self.lblTotalLaptops = (
            Label(frameLeft, text=f"Total Laptops: {self.controller.total_laptops()}", font=('Helvetica', 12))
            .grid(row=9, column=0, padx=10, pady=10))

        self.lblLaptopsSoldCount = (
            Label(frameLeft, text=f"Total Laptops Sold: {self.controller.laptops_sold_count()}", font=('Helvetica', 12))
            .grid(row=10, column=0, padx=10, pady=10))

        self.lblLaptopsInStock = (
            Label(frameLeft, text=f"Laptops in Stock: {self.controller.laptops_in_stock()}", font=('Helvetica', 12))
            .grid(row=11, column=0, padx=10, pady=10))

        self.lblSep2 = (Label(frameLeft, text="-----------------------------------------------", font=('Helvetica', 12))
                        .grid(row=12, column=0, padx=10, pady=10))

        # Phones
        self.lblPhones = (Label(frameLeft, text="Phones", font=('Helvetica', 12, 'bold'))
                          .grid(row=13, column=0, padx=10, pady=10))

        self.lblPhonesCost = (
            Label(frameLeft, text=f"Spend on Phones: ${self.controller.phone_cost()}", font=('Helvetica', 12))
            .grid(row=14, column=0, padx=10, pady=10))

        self.lblPhonesSold = (
            Label(frameLeft, text=f"Sold Phones: ${self.controller.phones_sold()}", font=('Helvetica', 12))
            .grid(row=15, column=0, padx=10, pady=10))

        self.lblPhonesProfit = (
            Label(frameLeft, text=f"Phones Profit: ${self.controller.phone_profit()}", font=('Helvetica', 12))
            .grid(row=16, column=0, padx=10, pady=10))

        self.lblTotalPhones = (
            Label(frameLeft, text=f"Total Phones: {self.controller.total_phones()}", font=('Helvetica', 12))
            .grid(row=17, column=0, padx=10, pady=10))

        self.lblPhonesSoldCount = (
            Label(frameLeft, text=f"Total Phones Sold: {self.controller.phones_sold_count()}", font=('Helvetica', 12))
            .grid(row=18, column=0, padx=10, pady=10))

        self.lblPhonesInStock = (
            Label(frameLeft, text=f"Phones in Stock: {self.controller.phones_in_stock()}", font=('Helvetica', 12))
            .grid(row=19, column=0, padx=10, pady=10))

        self.lblSep3 = (Label(frameLeft, text="-----------------------------------------------", font=('Helvetica', 12))
                        .grid(row=20, column=0, padx=10, pady=10))

        # Parts
        self.lblParts = (Label(frameLeft, text="Parts", font=('Helvetica', 12, 'bold'))
                         .grid(row=21, column=0, padx=10, pady=10))

        self.lblPartsCost = (
            Label(frameLeft, text=f"Spend on Parts: ${self.controller.parts_cost()}", font=('Helvetica', 12))
            .grid(row=22, column=0, padx=10, pady=10))

        self.lblPartsSold = (
            Label(frameLeft, text=f"Sold Parts: ${self.controller.parts_sold()}", font=('Helvetica', 12))
            .grid(row=23, column=0, padx=10, pady=10))

        self.lblPartsProfit = (
            Label(frameLeft, text=f"Parts Profit: ${self.controller.parts_profit()}", font=('Helvetica', 12))
            .grid(row=24, column=0, padx=10, pady=10))

        self.lblPartsUsed = (
            Label(frameLeft, text=f"Total Parts Used: {self.controller.parts_used()}", font=('Helvetica', 12))
            .grid(row=25, column=0, padx=10, pady=10))

        self.lblTotalParts = (
            Label(frameLeft, text=f"Total Parts: {self.controller.total_parts()}", font=('Helvetica', 12))
            .grid(row=26, column=0, padx=10, pady=10))

        self.lblPartsSoldCount = (
            Label(frameLeft, text=f"Total Parts Sold: {self.controller.parts_sold_count()}", font=('Helvetica', 12))
            .grid(row=27, column=0, padx=10, pady=10))

        self.lblPartsInStock = (
            Label(frameLeft, text=f"Parts in Stock: {self.controller.parts_in_stock()}", font=('Helvetica', 12))
            .grid(row=28, column=0, padx=10, pady=10))

        self.lblSep4 = (Label(frameLeft, text="-----------------------------------------------", font=('Helvetica', 12))
                        .grid(row=29, column=0, padx=10, pady=10))

        # Tools
        self.lblToolsCost = (Label(frameLeft, text=f"Total Spent on Tools: ${self.controller.tools_cost()}",
                                   font=('Helvetica', 12, 'bold'))
                             .grid(row=30, column=0, padx=10, pady=10))

        # Spend on Laptops:
        # Sold Laptops:
        # Laptop Profit:
        # Total Laptops:
        # Total Laptops Sold:
        # Total Laptops in Stock:
        #
        # Spend on Phones:
        # Sold Phones:
        # Phones Profit:
        # Total Phones:
        # Total Phones Sold:
        # Phones in Stock:
        #
        # Spend on Parts:
        # Sold Parts:
        # Parts Profit:
        # Total Parts Used
        # Total Parts:
        # Total Parts Sold:
        # Parts in Stock:
        #
        # Total Spent on Tools:
