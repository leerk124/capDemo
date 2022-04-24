import DatabaseQuery as DBQ
import plotly.graph_objects as graph_object
import plotly.express as pltly



def findTableNeeded(coin, jank_hash_table):
    coin_wanted = None
    for index in jank_hash_table:
        if coin == index['name'][0]:
            coin_wanted = index
            break
    return coin_wanted


def graphs(data_frame_needed, coin):
    graph_html_list = []

    # Candlestick Graph
    candleStick_graph = graph_object.Figure(data=[graph_object.Candlestick(x=data_frame_needed['date'],
                                                                           open=data_frame_needed['open'],
                                                                           high=data_frame_needed['high'],
                                                                           low=data_frame_needed['low'],
                                                                           close=data_frame_needed['close'])])


    # Volume Histogram
    volume_graph = pltly.histogram(data_frame_needed,
                                   x='date', y='volume',
                                   title='Amount of ' + coin.capitalize() + ' In Circulation',
                                   labels={'x': 'Date', 'y': 'Volume'})

    # Updating plots here
    # candleStick_graph.update_layout(plot_bgcolor='black')
    candleStick_graph.update_layout(template='plotly_dark',
                                    title='Price History of ' + coin.capitalize(),
                                    xaxis_title_text='Date',
                                    yaxis_title_text='Price ($)')

    volume_graph.update_layout(template='plotly_dark',
                               bargap=0.1,
                               xaxis_title_text='Date',
                               yaxis_title_text='Volume')



    graph_html_list.append(volume_graph.to_html(full_html=False, default_height=600, default_width=1100))
    graph_html_list.append(candleStick_graph.to_html(full_html=False, default_height=600, default_width=1100))
    return graph_html_list

def tableToHTML(data_frame_needed):
    data_frame = data_frame_needed
    columns_to_be_formatted = ['open', 'high', 'low', 'close', 'adj_close']
    data_frame.pop('name')  # Removing name column because it is not needed for printing

    # Formatting numbers to two decimal places
    for column in columns_to_be_formatted:
        data_frame.loc[:, column] = data_frame[column].map('{:.2f}'.format)

    # Converting entire dataframe to type string
    data_frame = data_frame.astype(str)

    # Trying to format text in data frame for better table
    for column in data_frame:
        for index in range(len(column)):
            data_frame[column][index] = '%.10000s' % (data_frame[column][index])


    data_frame = data_frame.sort_values(by=['date'], ascending=False)   # Sorting tables by newest date
    data_frame = data_frame.reset_index(drop=True)  # Resetting the index of the data frame to be in new order
    table_as_html = data_frame.to_html      # Getting html version of data frame to print on webpage

    return table_as_html

def main(coin):
    # Opening database
    database = DBQ.ReadData('db.sqlite3')

    # Storing data frames
    jank_hash_table = database.query()

    # Closing database
    database.close_database()

    # Finding table for wanted coin
    data_frame_needed = findTableNeeded(coin, jank_hash_table)

    # Converting data to html for webpage
    table_as_html = tableToHTML(data_frame_needed)
    html_list = graphs(data_frame_needed, coin)

    html_list.append(table_as_html)

    return html_list
