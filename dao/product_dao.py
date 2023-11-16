"""
    Data Access Object - DAO's Products.
    Class responsable for accessing the Database and
    make CRUD operations on Products table.
"""

import sqlite3 as sql
from models.product import Product

class ProductDAO:
    """ ProductDAO"""

    def __init__(self, **kwargs):
        if 'product' in kwargs:
            self.product = kwargs['product']
        self.__connection= None

    @property
    def product(self):
        """ Getter to product. """
        return self.__product

    @product.setter
    def product(self, product):
        """ Setter to product. """
        self.__product = product

    def __connect(self):
        self.__connection = sql.connect('database.db')

    def __disconnect(self):
        self.__connection.close()

    def select_all(self):
        """ 
            Selects all rows in Products table.
        """
        self.__connect()
        self.__connection.row_factory = sql.Row
        cursor = self.__connection.cursor()

        query = "SELECT * FROM products ORDER BY name;"

        cursor.execute(query)

        products = cursor.fetchall()

        self.__disconnect()

        return products

    def select(self):
        """ 
            Performs a SELECT in Products table, filtering by id.
        """
        select_product_query = f"""
            SELECT * 
            FROM products 
            WHERE id={self.product.id};
        """
        self.__connect()
        self.__connection.row_factory = sql.Row
        cursor = self.__connection.cursor()
        cursor.execute(select_product_query)

        row = cursor.fetchone()
        product = Product()
        product.id = row['id']
        product.name = row['name']
        product.brand = row['brand']
        product.price = row['price']

        self.__disconnect()
        return product

    def insert(self):
        """
            Performs an INSERT in Products table.
        """
        insert_product_query = f"""
            INSERT INTO products (id, name, brand, price )
            VALUES (
                {self.product.id}, 
                '{self.product.name}',
                '{self.product.brand}', 
                {self.product.price} 
            );
        """
        self.__connect()
        cursor = self.__connection.cursor()
        cursor.execute(insert_product_query)
        self.__connection.commit()
        self.__disconnect()

    def update(self):
        """
            Performs an UPDATE in Products table,
            filtering by id.
        """
        update_product_query = f"""
            UPDATE products 
            SET 
                name='{self.product.name}', 
                brand='{self.product.brand}', 
                price={self.product.price}
            WHERE 
                id={self.product.id}
            ;
        """
        self.__connect()
        cur = self.__connection.cursor()
        cur.execute(update_product_query)
        self.__connection.commit()
        self.__disconnect()

    def delete(self):
        """
            Perform a DELETE in Products table,
            filtering by id.
        """
        update_product_query = f"""
            DELETE FROM products 
            WHERE id={self.product.id};
        """
        self.__connect()
        cur = self.__connection.cursor()
        cur.execute(update_product_query)
        self.__connection.commit()
        self.__disconnect()
