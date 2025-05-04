# utilities.py
import matplotlib.pyplot as plt
import matplotlib.dates as mdates   
from os import system, name

# Function to clear the screen
def clear_screen():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

# Sort the stock list alphabetically by symbol
def sortStocks(stock_list):
    stock_list.sort(key=lambda s: s.symbol)

# Sort each stock's daily data oldest-to-newest
def sortDailyData(stock_list):
    for stock in stock_list:
        stock.DataList.sort(key=lambda d: d.date)

# Display a closing-price chart for the given symbol
def display_stock_chart(stock_list, symbol):
    # Find the matching stock in the portfolio
    selected = next((s for s in stock_list if s.symbol == symbol), None)
    if not selected or not selected.DataList:
        print(f"No data available for {symbol}.")
        return

    # Prepare data lists
    dates = [d.date for d in selected.DataList]
    prices = [d.close for d in selected.DataList]

    # Plot using matplotlib with explicit Axes object
    fig, ax = plt.subplots()
    ax.plot(dates, prices)
    ax.set_title(selected.name.upper())                    # uppercase title
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    # Format x-axis dates exactly as MM/DD/YY
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    fig.autofmt_xdate()
    plt.show()    