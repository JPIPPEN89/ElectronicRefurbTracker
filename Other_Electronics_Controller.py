import database as db
from Base_Inventory_Controller import Base_Inventory_Controller

class Other_Electronics_Controller(Base_Inventory_Controller):
    def __init__(self):
        super().__init__('other_electronics')
        db.Other_Electronics().create_table()

