from selenium.webdriver.common.by import By
import pandas
import DatabaseQuery as DBQ
from selenium import webdriver
import time
import os


def main():
    coin_list = ['BTC-USD', 'ADA-USD', 'DOGE-USD', 'ETH-USD', 'HNT-USD',
                 'LTC-USD', 'DOT-USD', 'SHIB-USD', 'USDT-USD']  # List of names of coins to update db

    database = DBQ.ReadData('db.sqlite3')  # Open database connection

    table_list = database.query()  # Grab tables needed
    table_list = sorted(table_list, key=lambda dataframe: dataframe.name[0])  # Sorting list of tables by name

    # Sorting tables by date
    for table in table_list:
        table.sort_values(by=['date'], ascending=False)

    downloadCSV(coin_list)  # Downloading the csv's needed to update the database
    new_data_list = store_from_csv(coin_list)  # Storing new data in dataframes
    data_to_add_list = compare_data(table_list, new_data_list)  # Comparing data

    database.updateDatabase(data_to_add_list)
    database.close_database()  # Close database connection after we're done
    # pushToGitHub()

# Downloading the CSV for each coin to insert into database
def downloadCSV(coin_list):
    executable_path = "/Users/austincarreno/SoftwareEngineeringProject/capDemo/driver/geckodriver"
    driver = webdriver.Firefox(executable_path=executable_path)
    for coin in coin_list:
        driver.get('https://finance.yahoo.com/quote/' + coin + '/history?p=' + coin)
        time.sleep(5)
        # driver.find_element_by_link_text('Download').click()
        driver.find_element(by=By.LINK_TEXT, value='Download').click()
        # time.sleep(10)


# Storing the new data from the CSV to a data frame
def store_from_csv(coin_list):
    updated_data_df_list = []
    for coin in coin_list:
        temp_df = pandas.read_csv('/Users/austincarreno/Downloads/' + coin + '.csv')

        match coin:
            case 'BTC-USD':
                temp_df.insert(0, 'name', 'bitcoin')
            case 'ADA-USD':
                temp_df.insert(0, 'name', 'cardano')
            case 'DOGE-USD':
                temp_df.insert(0, 'name', 'doge')
            case 'ETH-USD':
                temp_df.insert(0, 'name', 'ethereum')
            case 'HNT-USD':
                temp_df.insert(0, 'name', 'helium')
            case 'LTC-USD':
                temp_df.insert(0, 'name', 'litecoin')
            case 'DOT-USD':
                temp_df.insert(0, 'name', 'polkadot')
            case 'SHIB-USD':
                temp_df.insert(0, 'name', 'shibainu')
            case 'USDT-USD':
                temp_df.insert(0, 'name', 'tether')

        temp_df.sort_values(by=['Date'], ascending=False)
        temp_df.rename(columns={'Date': 'date', 'Adj Close': 'adj_close'}, inplace=True)
        updated_data_df_list.append(temp_df)
        os.remove('/Users/austincarreno/Downloads/' + coin + '.csv')

    updated_data_df_list = sorted(updated_data_df_list, key=lambda dataframe: dataframe.name[0])
    return updated_data_df_list


# Comparing new data to old data to find data needed to be added to the database
def compare_data(table_list, new_data_list):
    for outer_index in range(len(new_data_list)):
        for inner_index in range(len(new_data_list[outer_index].date)):
            if new_data_list[outer_index].date[inner_index] == \
                    table_list[outer_index].date[len(table_list[outer_index]) - 1]:
                new_data_list[outer_index] = new_data_list[outer_index][inner_index + 1:]
                break

    return new_data_list


# Pushing updated database to GitHub
# def pushToGitHub():
#     # TODO: TESTING
#     os.system("git commit -m 'Updating Database' db.sqlite3"
#               "git checkout --patch Austin db.sqlite3")

# ----------------------------------------------------------------------------------------------------------------------
main()
