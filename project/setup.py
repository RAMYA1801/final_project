import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    item TEXT,
                    FOREIGN KEY(customer_id) REFERENCES customers(id))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
