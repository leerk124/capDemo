import DatabaseQuery as DBQ
import plotly.graph_objects as graph_object
import plotly.express as pltly
import plotly.offline
import os

# TODO: Possibly want to reuse the graphs method by creating a list of the graphs' html to return to views to print
#       multiple graphs at once


def findTableNeeded(TEST, jank_hash_table):
    TEST2 = None
    for index in jank_hash_table:
        if TEST == index['name'][0]:
            TEST2 = index
            break
    return TEST2


def graphs(data_frame_needed):

    # Simple line graph
    lineGraph = pltly.line(data_frame_needed,
                           x='date', y=['high', 'low'],
                           title='Bitcoin High and Low Price',
                           labels={'x': 'Date', 'y': 'High and Low'},
                           )

    # Candlestick Graph
    figure = graph_object.Figure(data=[graph_object.Candlestick(x=data_frame_needed['date'],
                                                                open=data_frame_needed['open'],
                                                                high=data_frame_needed['high'],
                                                                low=data_frame_needed['low'],
                                                                close=data_frame_needed['close'])])

    return figure.to_html(full_html=False, default_height=500, default_width=700)


def main(coin):
    # Opening database
    database = DBQ.ReadData('db.sqlite3')

    # Storing data frames
    jank_hash_table = DBQ.ReadData.query(database)

    # Closing database
    DBQ.ReadData.close_database(database)

    # TEST = input("Enter the coin you'd like to see")
    data_frame_needed = findTableNeeded(coin, jank_hash_table)

    return graphs(data_frame_needed)


# main('bitcoin')

