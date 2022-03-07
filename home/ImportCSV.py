import pandas
import webbrowser
import time
from models import *

BTC_url = 'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD'
webbrowser.open(BTC_url)
time.sleep(.5)
BTC_dataFrame = pandas.read_csv('/Users/austincarreno/Downloads/BTC-USD.csv')

BTC_Object = [
    Bitcoin(
        name='Bitcoin',
        date=BTC_dataFrame[['Date']],
        open=BTC_dataFrame[['Open']],
        high=BTC_dataFrame[['High']],
        low=BTC_dataFrame[['Low']],
        close=BTC_dataFrame[['Close']],
        adj_close=BTC_dataFrame[['Adj Close']],
        volume=BTC_dataFrame[['Volume']]
    )
]

Bitcoin.objects.bulk_create(BTC_Object)
