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
        # c.execute('''DROP TABLE IF EXISTS laptops''')
        # conn.commit()
        c.execute('''
            CREATE TABLE IF NOT EXISTS laptops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT,
                model TEXT,
                cost REAL,
                quantity INTEGER,
                bad_parts TEXT,
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
                disassembled INTEGER DEFAULT 0,
                sold INTEGER DEFAULT 0,
                fully_functional DEFAULT 0,
                notes TEXT
            )
        ''')
        conn.commit()
        conn.close()



class PhonesDB(Database):

    def create_table(self):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()
        # c.execute('''DROP TABLE IF EXISTS phones''')
        # conn.commit()
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
                disassembled INTEGER DEFAULT 0,
                sold INTEGER DEFAULT 0,
                fully_functional DEFAULT 0,
                notes TEXT
            )
        ''')



        conn.commit()
        conn.close()





class PartsDB(Database):

    def create_table(self):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()
        # c.execute('''DROP TABLE IF EXISTS parts''')
        # conn.commit()

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
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
                fully_functional DEFAULT 0,
                notes TEXT
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

        # c.execute('''DROP TABLE IF EXISTS sales''')
        # conn.commit()

        c.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_type TEXT NOT NULL,       -- 'laptop' or 'phone'
                item_brand TEXT NOT NULL,
                item_model TEXT NOT NULL,
                -- item_id INTEGER NOT NULL,
                sold_for REAL NOT NULL,
                parts_used INTEGER DEFAULT 0, -- (simplified for now)
                parts_cost REAL DEFAULT 0,   -- (simplified for now)
                total_cost REAL NOT NULL,
                total_profit REAL NOT NULL,
                quantity INTEGER,
                sale_date TEXT DEFAULT CURRENT_TIMESTAMP,
                notes
            )
        ''')

        conn.commit()
        conn.close()

class Schema_Version(Database):
    def create_table(self):
        conn = self.connect()
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS schema_version (
                        version INTEGER
                    )''')
        conn.commit()
        conn.close()


class Other_Electronics(Database):
    def create_table(self):
        conn = sqlite3.connect("refurb.db")
        c = conn.cursor()
        # c.execute('''DROP TABLE IF EXISTS laptops''')
        # conn.commit()
        # Phones table
        c.execute('''
                    CREATE TABLE IF NOT EXISTS other_electronics (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        brand TEXT,
                        model TEXT,
                        cost REAL,
                        bad_parts TEXT,
                        quantity INTEGER,
                        purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
                        disassembled INTEGER DEFAULT 0,
                        sold INTEGER DEFAULT 0,
                        fully_functional DEFAULT 0,
                        notes TEXT
                    )
                ''')

        conn.commit()
        conn.close()
