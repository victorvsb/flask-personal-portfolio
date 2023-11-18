"""
    Data Access Object - DAO's Products.
    Class responsable for accessing the Database and
    make CRUD operations on Products table.
"""
from models.product import Product
from dao.dao import DAO

class ProductDAO:
    """ ProductDAO"""

    def __init__(self, **kwargs):
        if 'product' in kwargs:
            self.product = kwargs['product']
        else:
            self.product = Product()

        if 'id' in kwargs:
            self.product.id = kwargs['id']

        if 'name' in kwargs:
            self.product.name = kwargs['name']

        if 'brand' in kwargs:
            self.product.brand = kwargs['brand']

        if 'price' in kwargs:
            self.product.price = kwargs['price']

    @property
    def product(self):
        """ Getter to product. """
        return self.__product

    @product.setter
    def product(self, product):
        """ Setter to product. """
        self.__product = product

    def select_all(self):
        """ 
            Selects all rows in Products table.
        """
        select_product = "SELECT * FROM products ORDER BY name;"

        with DAO('database.db') as dao:
            return dao.select_many(select_product)

    def select(self):
        """ 
            Performs a SELECT in Products table, filtering by id.
        """
        select_products = f"""
            SELECT * 
            FROM products 
            WHERE id={self.product.id};
        """

        with DAO('database.db') as dao:
            return dao.select_one(select_products)

    def insert(self):
        """
            Performs an INSERT in Products table.
        """
        insert_product = f"""
            INSERT INTO products (id, name, brand, price )
            VALUES (
                {self.product.id}, 
                '{self.product.name}',
                '{self.product.brand}', 
                {self.product.price} 
            );
        """
        with DAO('database.db') as dao:
            return dao.insert(insert_product)

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
        with DAO('database.db') as dao:
            return dao.update(update_product_query)

    def delete(self):
        """
            Perform a DELETE in Products table,
            filtering by id.
        """
        delete_product_query = f"""
            DELETE FROM products 
            WHERE id={self.product.id};
        """
        with DAO('database.db') as dao:
            return dao.delete(delete_product_query)
