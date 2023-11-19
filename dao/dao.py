"""
    Data Access Object - DAO
    Class responsible for execute SQL instructions
    and handle connections with DataBase.
"""

import sqlite3 as sql

class DAO:
    """ Generic DAO """

    def __init__(self, db_file):
        self.__db_file = db_file
        self.__connection = None

    def __enter__(self):
        self.__connection = sql.connect(self.__db_file)
        return self

    def __exit__(self, *args):
        self.__connection.close()

    def select_one(self, sql_query):
        """
            Performs a SELECT sql query and
            returns only one row.
        """
        self.__connection.row_factory = sql.Row
        cursor = self.__connection.cursor()
        cursor.execute(sql_query)

        return cursor.fetchone()

    def select_many(self, sql_query):
        """
            Performs a SELECT sql query and
            returns many rows.
        """
        self.__connection.row_factory = sql.Row
        cursor = self.__connection.cursor()
        cursor.execute(sql_query)

        return cursor.fetchall()

    def __data_change(self, sql_query):
        """
            Performs SQL commands that make changes on data
            and them persists the changes through a commit.
            Used to perform INSERT, UPDATE and DELETE.
            NOTE: for a better readability, use its aliases,
            dependending on the SQL instruction it's being 
            executed
        """
        cur = self.__connection.cursor()
        cur.execute(sql_query)
        self.__connection.commit()

    # Different aliases for data_change()
    # to make the code more readable.
    insert = update = delete = __data_change
