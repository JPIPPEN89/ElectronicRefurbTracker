import sqlite3
import database as db

def get_current_version(conn):
    c = conn.cursor()
    c.execute("SELECT version FROM schema_version")
    return c.fetchone()[0]

def set_new_version(conn, version):
    c = conn.cursor()
    c.execute("UPDATE schema_version SET version = ?", (version,))
    conn.commit()

def apply_migrations():
    conn = sqlite3.connect("refurb.db")
    c = conn.cursor()
    #c.execute('''INSERT INTO schema_version (version) VALUES (1)''')
    conn.commit()
    current_version = get_current_version(conn)

    conn.close()
    print("All migrations applied.")
    print(f"Current Version is {current_version}")

if __name__ == "__main__":
    db.Schema_Version().create_table()
    apply_migrations()