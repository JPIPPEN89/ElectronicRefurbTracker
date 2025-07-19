import database as db

class Other_Electronics_Controller:
    def __init__(self):
        db.Other_Electronics().create_table()

    def add_item(self, brand, model, cost, quantity, bad_parts):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''INSERT INTO other_electronics (brand, model, cost, quantity, bad_parts)
                   VALUES (?,?,?,?,?)    
           ''', (brand, model, cost, quantity, bad_parts))
        conn.commit()
        conn.close()

    def mark_as_sold(self, id):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''
                   UPDATE other_electronics
                   SET sold = 1
                   WHERE id = ?
               ''', (id))
        conn.commit()

        conn.close()



    def item_sold_info(self, id):
        conn = db.Database().connect()
        c = conn.cursor()

        type = 'Other'
        c.execute('''SELECT * FROM other_electronics WHERE id = ?''', (id,))
        result = c.fetchone()
        conn.close()

        id, brand, model, cost, parts_used, quantity, purchase_date, sold = result

        return result


    def get_all_items(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT * FROM other_electronics")
        rows = c.fetchall()
        conn.close()

        return rows

    def other_cost(self):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute("SELECT SUM(cost) FROM other_electronics")
        total_cost = c.fetchone()[0]

        if total_cost is None:
            return 0
        conn.close()
        return total_cost

    def disassembled_item(self,id):
        conn = db.Database().connect()
        c = conn.cursor()
        c.execute('''
                   UPDATE other_electronics
                   SET disassembled = 1
                   WHERE id = ?
               ''', (id))
        conn.commit()

        conn.close()

