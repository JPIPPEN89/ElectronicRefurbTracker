# Laptop_View.py
from Base_Inventory_View import Base_Inventory_View
import Laptop_Controller as lc

class Laptop_View(Base_Inventory_View):
    def __init__(self, rootWindow):
        super().__init__(rootWindow, lc.LaptopController(), "Laptop")