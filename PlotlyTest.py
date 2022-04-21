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


def graphs(data_frame_needed):
    graph_html_list = []
    # Candlestick Graph
    candleStick_graph = graph_object.Figure(data=[graph_object.Candlestick(x=data_frame_needed['date'],
                                                                           open=data_frame_needed['open'],
                                                                           high=data_frame_needed['high'],
                                                                           low=data_frame_needed['low'],
                                                                           close=data_frame_needed['close'])])


    # Volume Histogram
    volume_graph = pltly.histogram(data_frame_needed,
                                   x = 'date', y='volume',
                                   title='Volume of Coin',
                                   labels={'x': 'Date', 'y': 'Volume'})

    # Updating plots here
    # candleStick_graph.update_layout(plot_bgcolor='black')
    candleStick_graph.update_layout(template='plotly_dark')
    volume_graph.update_layout(template='plotly_dark')



    graph_html_list.append(volume_graph.to_html(full_html=False, default_height=600, default_width=1100))
    graph_html_list.append(candleStick_graph.to_html(full_html=False, default_height=600, default_width=1100))
    return graph_html_list

def tableToHTML(data_frame_needed):
    data_frame = data_frame_needed
    columns_to_be_formatted = ['open', 'high', 'low', 'close', 'adj_close']
    data_frame.pop('name')

    for column in columns_to_be_formatted:
        data_frame.loc[:, column] = data_frame[column].map('{:.2f}'.format)

    data_frame = data_frame.sort_values(by=['date'], ascending=False)
    data_frame = data_frame.reset_index(drop=True)
    table_as_html = data_frame.to_html

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
    html_list = graphs(data_frame_needed)

    html_list.append(table_as_html)

    return html_list
