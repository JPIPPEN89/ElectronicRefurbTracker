import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import AddController as ac

class Add_View(Toplevel):

    def __init__(self, rootWindow):
        Toplevel.__init__(self)
        self.controller = ac.AddController()

        self.title("Add Item to Inventory")
        self.geometry("900x1100")

        frameLeft = Frame(self, width=30, height=40, highlightbackground="black", highlightthickness=2)
        frameLeft.pack(side=LEFT, padx=20, pady=20)

        frameRight = Frame(self, width=70, height=40, highlightbackground="black", highlightthickness=2)
        frameRight.pack(side=RIGHT, padx=20, pady=20)