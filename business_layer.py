#!/usr/bin/env python
# business_layer.py
"""
Author          :   Alexander Shelton
Date            :   October 2024
Name            :   Database Application
Description     :   An application for users to view data from a database based on their permissions.    
"""
import os
import logging
import psycopg2
from tkinter import messagebox
# Configure logging
logging.basicConfig(filename='app_errors.log', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s %(message)s')
# ----- BusinessLayer ----- #
class BusinessLayer:
    """
    Provides methods to interact with a PostgreSQL database, including fetching data
    and closing the database connection.

    Attributes:
        conn : psycopg2.connection
            The connection object to the PostgreSQL database.
        cursor : psycopg2.cursor
            The cursor object used for executing database queries.
    """
    def __init__(self, user, password):
        """
        Initializes a new instance of BusinessLayer.
        Attempts to connect to a PostgreSQL database using environment variables.
        Raises an exception if the connection fails.
        """
        self.user = user
        try:
            # Secure credentials using environment variables
            self.conn = psycopg2.connect(
                user=self.user,
                password=password,
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', '5432'),
                database=os.getenv('DB_NAME', 'postgres'),
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            logging.error(f"Error connecting to the database: {str(e)}")
            raise Exception("Database connection failed. Please check the logs.")

    def get_in450a_data(self):
        """
        Retrieves all records from the 'in450a' table.

        Returns:
            (list of tuple):
                All rows from the 'in450a' table.
        """
        try:
            self.cursor.execute("SELECT * FROM in450a;")
            return self.cursor.fetchall()
        except Exception as e:
            logging.error(f"Failed to get data from in450a: {e}")
            messagebox.showerror(
                "Error", 
                "An error occurred while fetching data. Please check the logs."
            )

    def get_in450b_data(self):
        """
        Retrieves records from the 'in450b' table specific to the current user.

        Returns:
            (list of tuple): All rows from the 'in450b' table for the current user.
        """
        try:
            self.cursor.execute("SELECT * FROM in450b;")
            return self.cursor.fetchall()
        except Exception as e:
            logging.error(f"Failed to get data from in450b: {e}")
            messagebox.showerror(
                "Error", 
                "An error occurred while fetching data. Please check the logs."
            )

    def get_in450c_data(self):
        """
        Retrieves records from the 'in450c' table specific to the current user.

        Returns:
            (list of tuple): 
                All rows from the 'in450c' table for the current user.
        """
        try:
            self.cursor.execute("SELECT * FROM in450c;")
            return self.cursor.fetchall()
        except Exception as e:
            logging.error(f"Failed to get data from in450c: {e}")
            messagebox.showerror(
                "Error", 
                "An error occurred while fetching data. Please check the logs."
            )

    def get_in450a_row_count(self):
        """
        Counts the number of rows in the 'in450a' table.

        Returns:
            (int): 
                The number of rows in the 'in450a' table.
        """
        try:
            self.cursor.execute("SELECT COUNT(*) FROM in450a;")
            return self.cursor.fetchone()[0]
        except Exception as e:
            logging.error(f"Failed to get row count for in450a: {e}")
            messagebox.showerror(
                "Error", 
                "An error occurred while fetching data. Please check the logs."
            )

    def get_in450b_names(self):
        """
        Retrieves first and last names from the 'in450b' table for the current user.

        Returns:
            (list of tuple):
                All first and last names from the 'in450b' table for the current user.
        """
        try:
            self.cursor.execute("SELECT first_name, last_name FROM in450b;")
            return self.cursor.fetchall()
        except Exception as e:
            logging.error(f"Failed to get names from in450b: {e}")
            messagebox.showerror(
                "Error", 
                "An error occurred while fetching data. Please check the logs."
            )

    def get_in450c_row_count(self):
        """
        Counts the number of rows in the 'in450c' table for the current user.

        Returns:
            (int):
                The number of rows in the 'in450c' table for the current user.
        """
        try:
            self.cursor.execute("SELECT COUNT(*) FROM in450c;")
            return self.cursor.fetchone()[0]
        except Exception as e:
            logging.error(f"Failed to get row count from in450c: {e}")
            messagebox.showerror(
                "Error", 
                "An error occurred while fetching data. Please check the logs."
            )

    def close_connection(self):
        """
        Closes the database connection and cursor.

        This method should be called when the database connection is no longer needed
        to ensure that resources are properly released.
        """
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            logging.error(f"Error closing the connection: {str(e)}")
            messagebox.showerror(
                "Error", 
                "An error occurred while closing the database connection. Please check the logs."
            )
