"""
    Data Access Object - DAO
    A generic class for others DAO
"""

import sqlite3 as sql

class DAO:
    """ Generic DAO """

    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        self.connection = sql.connect(self.db_file)
        return self

    def __exit__(self, *args):
        self.connection.close()

    def select_one(self, sql_query):
        """
            Performs a SELECT sql query and
            returns only one row.
        """
        self.connection.row_factory = sql.Row
        cursor = self.connection.cursor()
        cursor.execute(sql_query)

        return cursor.fetchone()

    def select_many(self, sql_query):
        """
            Performs a SELECT sql query and
            returns many rows.
        """
        self.connection.row_factory = sql.Row
        cursor = self.connection.cursor()
        cursor.execute(sql_query)

        return cursor.fetchall()

    def data_change(self, sql_query):
        """
            Performs SQL commands that make changes on data
            and them persists the changes through a commit.
            Used to perform INSERT, UPDATE and DELETE.
        """
        cur = self.connection.cursor()
        cur.execute(sql_query)
        self.connection.commit()

    # Different aliases for data_change()
    # to make code more readable.
    insert = update = delete = data_change
