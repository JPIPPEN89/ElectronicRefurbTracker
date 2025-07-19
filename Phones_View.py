# Laptop_View.py
from Base_Inventory_View import Base_Inventory_View
import Phone_Controller as pc

class Phones_View(Base_Inventory_View):
    def __init__(self, rootWindow):
        super().__init__(rootWindow, pc.Phone_Controller(), "Phone")