"""
    Python script that creates the database used by
    Products Registration app.
"""
import sqlite3 as sql


DROP_TABLE_PRODUCTS = "DROP TABLE IF EXISTS products;"

CREATE_TABLE_PRODUCTS = "CREATE TABLE products ("\
    "id INTEGER, name VARCHAR(80), brand VARCHAR(80), price REAL );"

INSERT_PRODUCTS = "INSERT INTO products (id, name, brand, price)"\
    "VALUES (1, 'Macarrão', 'Adria', 3.99);"


conn = sql.connect('database.db')
print("Database connected")

conn.execute(DROP_TABLE_PRODUCTS)
print("Table dropped")

conn.execute(CREATE_TABLE_PRODUCTS)
print("Table created")

# conn.execute(INSERT_PRODUCTS)
# print("Row inserted")

conn.close()
