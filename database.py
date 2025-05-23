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

        c.execute('DROP TABLE IF EXISTS laptops')
        c.execute('''
            CREATE TABLE laptops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT,
                model TEXT,
                cost REAL,
                quantity INTEGER,
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
                sold INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()

    def add_item(self, brand, model, cost, quantity):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''INSERT INTO laptops (brand, model, cost, quantity)
                VALUES (?,?,?,?)    
        ''',(brand, model, cost, quantity))
        conn.commit()
        conn.close()

    def mark_as_sold(self, laptop_id):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''
                UPDATE laptops
                SET sold = 1
                WHERE id = ?
            ''', (laptop_id))
        conn.commit()
        conn.close()


    def get_all_laptops(self):
        conn = self.connect()
        c = conn.cursor()
        c.execute("SELECT * FROM laptops")
        rows = c.fetchall()
        conn.close()

        print('Laptops:')
        for row in rows:
            print(row)

class PhonesDB(Database):

    def create_table(self):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()

        c.execute('DROP TABLE IF EXISTS phones')

        # Phones table
        c.execute('''
            CREATE TABLE phones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT,
                model TEXT,
                cost REAL,
                quantity INTEGER,
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
                sold INTEGER DEFAULT 0
            )
        ''')

        conn.commit()
        conn.close()


    def add_item(self,brand, model, cost, quantity):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''INSERT INTO phones (brand, model, cost, quantity)
                        VALUES (?,?,?,?)    
                ''', (brand, model, cost, quantity))
        conn.commit()
        conn.close()

    def mark_as_sold(self, phone_id):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()

        c.execute('''UPDATE phones
                    SET sold = 1
                    WHERE id = ?''',(phone_id))

        conn.commit()
        conn.close()

    def get_all_phones(self):
        conn = self.connect()
        c = conn.cursor()
        c.execute("SELECT * FROM phones")
        rows = c.fetchall()
        conn.close()

        print('Phones:')
        for row in rows:
            print(row)


class PartsDB(Database):
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

    def add_item(self, brand, model, part_type, cost, quantity):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''INSERT INTO parts (brand, model, part_type, cost, quantity)
                               VALUES (?,?,?,?,?)    
                       ''', (brand, model, part_type, cost, quantity))
        conn.commit()
        conn.close()

    def used_part(self,part_id):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()

        c.execute('''UPDATE phones
                    SET used_part = 1
                    WHERE id = ?''',(part_id))

        conn.commit()
        conn.close()

class ToolsDB(Database):
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

    def add_item(self,name, cost, quantity):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()

        c.execute('''INSERT INTO tools(name, cost, quantity),
                    VALUES (?,?,?)''',(name, cost, quantity))

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