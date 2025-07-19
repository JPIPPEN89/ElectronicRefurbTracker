# Laptop_View.py
from Base_Inventory_View import Base_Inventory_View
import Other_Electronics_Controller as oc

class Other_Electronics_View(Base_Inventory_View):
    def __init__(self, rootWindow):
        super().__init__(rootWindow, oc.Other_Electronics_Controller(), "Other")