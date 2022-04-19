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
                                                                           close=data_frame_needed['close'])]
                                            var config={responsive: true})


    # Volume Histogram
    volume_graph = pltly.histogram(data_frame_needed,
                                   x = 'date', y='volume',
                                   title='Volume of Coin',
                                   labels={'x': 'Date', 'y': 'Volume'}
                                   )

    # Updating plots here
    # candleStick_graph.update_layout(plot_bgcolor='black')
    candleStick_graph.update_layout(template='plotly_dark')
    volume_graph.update_layout(template='plotly_dark')



    graph_html_list.append(volume_graph.to_html(full_html=False, default_height=600, default_width=900))
    graph_html_list.append(candleStick_graph.to_html(full_html=False, default_height=600, default_width=900))
    return graph_html_list


def main(coin):
    # Opening database
    database = DBQ.ReadData('db.sqlite3')

    # Storing data frames
    jank_hash_table = database.query()

    # Closing database
    database.close_database()

    # TEST = input("Enter the coin you'd like to see")
    data_frame_needed = findTableNeeded(coin, jank_hash_table)

    return graphs(data_frame_needed)

