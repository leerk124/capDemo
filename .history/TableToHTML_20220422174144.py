import DatabaseQuery as DBQ
import PlotlyTest as PT


def findTableNeeded(coin):
    coin




def main(coin):
    database = DBQ.ReadData('db.sqlite3')
    table = database.query()
    table_wanted = PT.findTableNeeded(coin, table)

    table_as_html = table_wanted.to_html
    print(table)
    print(table_as_html)



main('bitcoin')