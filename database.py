import sqlite3

class Database:
    def __init__(self, db_name="refurb.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

#Laptop Database Logic
class LaptopDB(Database):

    def create_table(self):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()
        # Laptops table

        c.execute('''
            CREATE TABLE IF NOT EXISTS laptops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT,
                model TEXT,
                cost REAL,
                quantity INTEGER,
                bad_parts TEXT,
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
                sold INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()



class PhonesDB(Database):

    def create_table(self):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()

        # Phones table
        c.execute('''
            CREATE TABLE IF NOT EXISTS phones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT,
                model TEXT,
                cost REAL,
                bad_parts TEXT,
                quantity INTEGER,
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
                sold INTEGER DEFAULT 0
            )
        ''')

        conn.commit()
        conn.close()





class PartsDB(Database):

    def create_table(self):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()


        # Parts table
        c.execute('''
            CREATE TABLE IF NOT EXISTS parts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT,
                model TEXT,
                part_type TEXT,
                cost REAL,
                quantity INTEGER,
                used_part INTEGER DEFAULT 0,
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()



class ToolsDB(Database):

    def create_table(self):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()

        # Tools table
        c.execute('''
            CREATE TABLE IF NOT EXISTS tools (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cost REAL NOT NULL,
                quantity INTEGER,
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()



class SalesDB(Database):
    def create_table(self):
        conn = self.connect()
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_type TEXT NOT NULL,       -- 'laptop' or 'phone'
                item_id INTEGER NOT NULL,
                sold_for REAL NOT NULL,
                parts_used TEXT,               -- (simplified for now)
                total_cost REAL NOT NULL,
                total_profit REAL NOT NULL,
                quantity INTEGER,
                sale_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()

    def add_sale(self, item_type, item_id, sold_for, parts_used_list, base_cost, parts_cost):
        total_cost = base_cost + parts_cost
        profit = sold_for - total_cost
        parts_used = ", ".join(parts_used_list)  # store part names for now

        conn = self.connect()
        c = conn.cursor()

        c.execute('''
            INSERT INTO sales (item_type, item_id, sold_for, parts_used, total_cost, total_profit)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (item_type, item_id, sold_for, parts_used, total_cost, profit))

        conn.commit()
        conn.close()