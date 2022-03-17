import sqlite3
import pandas


class ReadData:
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def query(self):
        # List of table names with the word home in the name
        table_name_list = []

        # List of tables with their data
        table_list = []

        # Query to get all tables with the 'home_' in their name
        table_query = """SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%home_%'"""

        # Executing the query
        self.cursor.execute(table_query)
        table_names = self.cursor.fetchall()

        # Finding tables with "home_" in their name
        for index in range(len(table_names)):
            table_name_list.append(table_names[index][0])

        for index in table_name_list:
            # Query to grab data needed
            data_query = 'SELECT * FROM ' + index

            # Creating data frame from the sql table
            data_frame = pandas.read_sql_query(data_query, self.connection)

            # Adding the name of the database table to the dataframe
            data_frame.insert(0, 'name', index[5:])

            # Appending the dataframe to the table_list
            table_list.append(data_frame)

        return table_list


    def close_database(self):
        self.connection.close()
        return

