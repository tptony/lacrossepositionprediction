"""
A simple utility to connect to psql database and query data. Created in Milestone II by Matt
"""

import psycopg2
import dotenv
import os
import pandas as pd


class LaxDB(object):
    """
    A simple utility to connect to psql database and query data.
    """

    def __init__(self):

        # Load environment variables from .env file
        dotenv.load_dotenv()

        db_params = {
            'host': os.getenv('LAX_DB_HOST'),
            'port': os.getenv('LAX_DB_PORT'),
            'user': os.getenv('LAX_DB_USER'),
            'password': os.getenv('LAX_DB_PASSWORD'),
            'dbname': os.getenv('LAX_DB_NAME'),
        }
        self.db_params = db_params
        self.conn = None
        self.cur = None

        self.connect()

    def connect(self):
        """
        Connect to the database.
        """
        try:
            self.conn = psycopg2.connect(**self.db_params)
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close(self):
        """
        Close the database connection.
        """
        if self.conn is not None:
            self.conn.close()

    def query(self, query):
        """
        Execute a query and return the results as a pandas dataframe.
        """
        self.cur.execute(query)
        columns = [desc[0] for desc in self.cur.description]
        data = self.cur.fetchall()
        df = pd.DataFrame(data, columns=columns)
        return df

    def query_with_params(self, query, params):
        """
        Execute a query with parameters and return the results as a pandas dataframe.
        """
        self.cur.execute(query, params)
        columns = [desc[0] for desc in self.cur.description]
        data = self.cur.fetchall()
        df = pd.DataFrame(data, columns=columns)
        return df
