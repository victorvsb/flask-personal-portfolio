"""
    Python script that creates the database used by
    Products Registration app.
"""
import sqlite3 as sql


DROP_TABLE_PRODUCTS = "DROP TABLE IF EXISTS products;"

CREATE_TABLE_PRODUCTS = """
    CREATE TABLE products (
        id INTEGER, 
        name VARCHAR(80), 
        brand VARCHAR(80), 
        price REAL 
    );"""

INSERT_PRODUCTS = """
    INSERT INTO products (id, name, brand, price)
    VALUES 
    (1, 'Sparkling water', 'S. Pellegrino', 3.99),
    (2, 'Weath flour', 'Caputo', 1.99),
    (3, 'Olive', 'Olivere', 5.99),
    (4, 'Cheddar', 'Joseph Heler', 2.99),
    (5, 'Pringles Original', 'Pringles', 2.49);
    """

conn = sql.connect('database.db')
print("Database connected.")

conn.execute(DROP_TABLE_PRODUCTS)
print("Table dropped.")

conn.execute(CREATE_TABLE_PRODUCTS)
print("Table created.")

with sql.connect("database.db") as con:
    cur = con.cursor()
    cur.execute(INSERT_PRODUCTS)

    con.commit()
    print("Rows inserted.")

conn.close()
