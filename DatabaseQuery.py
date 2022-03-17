import sqlite3
import pandas
import plotly.express as pltly
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import os



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
            data_query = 'SELECT date, high, low, volume FROM ' + index
            data_frame = pandas.read_sql_query(data_query, self.connection)
            table_list.append(data_frame)

        return table_list


    def close_database(self):
        self.connection.close()
        return



# Opening database
database = ReadData('db.sqlite3')


jank_hash_table = ReadData.query(database)
print(jank_hash_table)
ReadData.close_database(database)



# lineGraph = pltly.line(dataFrame, x='date', y='open', title='Bitcoin Opening Price')
# lineGraph.show() 
