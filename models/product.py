""" 
    Class definition for Product, as it is stored
    at DataBase.
"""

class Product:
    """
        Class that represents the Products stored at Database.
        Each table's atribute is converted to an property 
        from the class with its getter and setter methods.
    """

    def __init__(self):
        """
            Class constructor that inittialize
            the properties with valid values.
        """
        self.id = 0
        self.name = ''
        self.brand = ''
        self.price = 0.0

    @property
    def id(self):
        """ Getter to id. """
        return self.__id

    @id.setter
    def id(self, value):
        """ Setter to id. """
        self.__id = value

    @property
    def name(self):
        """ Getter to name. """
        return self.__name

    @name.setter
    def name(self, value):
        """ Setter to name. """
        self.__name = value

    @property
    def brand(self):
        """ Getter to brand. """
        return self.__brand

    @brand.setter
    def brand(self, value):
        """ Setter to brand. """
        self.__brand = value

    @property
    def price(self):
        """ Getter to price. """
        return self.__price

    @price.setter
    def price(self, value):
        """ Getter to price """
        self.__price = value
