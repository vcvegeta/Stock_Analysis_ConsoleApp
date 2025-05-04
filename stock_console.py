# stock_console.py 
import os
from datetime import datetime
from stock_class import Stock, DailyData
from utilities import clear_screen, display_stock_chart, sortStocks
from os import path
import stock_data

# Main entry point
def main():
    # Create the database if it doesn't exist
    if not path.exists('stocks.db'):
        stock_data.create_database()
    stock_list = []
    main_menu(stock_list)

# Our Main Menu 
def main_menu(stock_list):
    while True:
        #clear_screen()
        print()
        sortStocks(stock_list)
        print('---Welcome to the Stock Analyzer Main Menu by VIRAAT---')
        print('1 - Manage Stocks (Add, Update, Delete, List)')
        print('2 - Add Daily Stock Data (Date, Price, Volume)')
        print('3 - Show Report')
        print('4 - Show Matplotlib Chart')
        print('5 - Manage Data (Save, Load, Retrieve)')
        print('0 - Exit from Program')
        choice = input('Enter Menu Option: ')
        if choice == '1':
            manage_stocks(stock_list)
        elif choice == '2':
            add_stock_data(stock_list)
        elif choice == '3':
            show_report(stock_list)
        elif choice == '4':
            show_chart(stock_list)
        elif choice == '5':
            manage_data(stock_list)
        elif choice == '0':
            #clear_screen()
            print()
            print('Goodbye')
            break
        else:
            input('Invalid option. Press Enter to continue...')

# Manage Stocks Menu
def manage_stocks(stock_list):
    while True:
        #clear_screen()
        print()
        sortStocks(stock_list)
        print('### Manage Stocks ### by VIRAAT') 
        print('1 - Add Stock')
        print('2 - Update Shares')
        print('3 - Delete Stock')
        print('4 - List Stocks')
        print('0 - Return to Main Menu')
        choice = input('Enter Menu Option: ')
        if choice == '1':
            add_stock(stock_list)
        elif choice == '2':
            update_shares(stock_list)
        elif choice == '3':
            delete_stock(stock_list)
        elif choice == '4':
            list_stocks(stock_list)
        elif choice == '0':
            break
        else:
            input('Invalid option. Press Enter to continue...')

# Add new stock
def add_stock(stock_list):
    #clear_screen()
    print()
    while True:
        print('###  Add Stock  ### by Viraat')
        symbol = input('Enter Ticker Symbol (or 0 to cancel): ').upper()
        if symbol == '0' or not symbol:
            break
        name = input('Enter Company Name: ')
        try:
            shares = float(input('Enter Number of Shares: '))
        except ValueError:
            shares = 0.0
        stock_list.append(Stock(symbol, name, shares))
        cont = input('Stock Added. Press Enter to add another or 0 to stop: ')
        if cont == '0':
            break

# Update shares menu
def update_shares(stock_list):
    while True:
        #clear_screen()
        print()
        sortStocks(stock_list)
        print('### Update Shares ### by Viraat') 
        print('1 - Buy Shares')
        print('2 - Sell Shares')
        print('0 - Return')
        choice = input('Enter Menu Option: ')
        if choice == '1':
            buy_shares(stock_list)
        elif choice == '2':
            sell_shares(stock_list)
        elif choice == '0':
            break
        else:
            input('Invalid option. Press Enter to continue...')

# Buy shares
def buy_shares(stock_list):
    #clear_screen()
    print()
    print('Buy Shares ---')
    symbols = ' '.join(s.symbol for s in stock_list)
    print(f'Stock List: [{symbols}]')
    sym = input('Which stock?: ').upper()
    try:
        cnt = float(input('Shares to buy: '))
        for s in stock_list:
            if s.symbol == sym:
                s.buy(cnt)
                print(f'Bought {cnt} shares of {sym}.')
                break
    except ValueError:
        print('Invalid number.')
    input('Press Enter to continue...')

# Sell shares
def sell_shares(stock_list):
    #clear_screen()
    print()
    print('Sell Shares ---')
    symbols = ' '.join(s.symbol for s in stock_list)
    print(f'Stock List: [{symbols}]')
    sym = input('Which stock?: ').upper()
    try:
        cnt = float(input('Shares to sell: '))
        for s in stock_list:
            if s.symbol == sym:
                s.sell(cnt)
                print(f'Sold {cnt} shares of {sym}.')
                break
    except ValueError:
        print('Invalid number.')
    input('Press Enter to continue...')

# Delete a stock
def delete_stock(stock_list):
    #clear_screen()
    print()
    print('Delete Stock ---')
    symbols = ' '.join(s.symbol for s in stock_list)
    print(f'Stock List: [{symbols}]')
    sym = input('Which stock to delete?: ').upper()
    stock_list[:] = [s for s in stock_list if s.symbol != sym]
    print(f'Deleted {sym} if existed.')
    input('Press Enter to continue...')

# List all tracked stocks
def list_stocks(stock_list):
    #clear_screen()
    print()
    sortStocks(stock_list)
    print('Stock List ---')
    print('SYMBOL    NAME    SHARES')
    print('=========================')
    for s in stock_list:
        print(f"{s.symbol}    {s.name}    {s.shares}")
    input('Press Enter to continue...')

# Add daily stock data
def add_stock_data(stock_list): 
    #clear_screen()
    print()
    sortStocks(stock_list)
    print('Add Daily Stock Data ---')
    symbols = ' '.join(s.symbol for s in stock_list)
    print(f'Stock List: [{symbols}]')
    sym = input('Stock symbol?: ').upper()
    print('Enter date,price,volume (blank to quit)')
    while True:
        entry = input('> ')
        if not entry:
            break
        try:
            d_str,p_str,v_str = entry.split(',')
            dt = datetime.strptime(d_str,'%m/%d/%y')
            price,vol = float(p_str),int(v_str)
            for s in stock_list:
                if s.symbol==sym:
                    s.add_data(DailyData(dt,price,vol))
                    print(f'Added {dt.strftime("%m/%d/%y")}')
                    break
        except Exception:
            print('Invalid entry.')
    input('Press Enter to continue...')

# Show report
def show_report(stock_list):
    #clear_screen()
    print()
    for s in stock_list:
        print('Stock Report ---')
        print(f'Report for: {s.symbol} {s.name}')
        print(f'Shares: {s.shares}')
        if not s.DataList:
            print('No history.')
        else:
            print('Date       Price      Volume')
            print('-----------------------------')
            for d in sorted(s.DataList,key=lambda x:x.date):
                print(f'{d.date.strftime("%m/%d/%y")}   ${d.close:,.2f}   {d.volume}')
        input('Press Enter...')

# Show chart interaction
def show_chart(stock_list):
    #clear_screen()
    print()
    sortStocks(stock_list)
    print('Show Chart ---')
    symbols=' '.join(s.symbol for s in stock_list)
    print(f'Stock List: [{symbols}]')
    sym=input('Symbol?: ').upper()
    display_stock_chart(stock_list,sym)
    input('Press Enter to continue...')

# Manage Data Menu
def manage_data(stock_list):
    while True:
        #clear_screen()
        print()
        print('Manage Data ---')
        print('1 - Save Data to Database')
        print('2 - Load Data from Database')
        print('3 - Retrieve Data from Web')
        print('4 - Import from CSV File')
        print('0 - Return')
        choice=input('Enter Menu Option: ')
        if choice=='1':
            stock_data.save_stock_data(stock_list)
            print('Data saved.')
            input('Press Enter to continue...')
        elif choice=='2':
            stock_data.load_stock_data(stock_list)
            print('Data loaded.')
            input('Press Enter to continue...')
        elif choice=='3':
            retrieve_from_web(stock_list)
        elif choice=='4':
            import_csv(stock_list)
        elif choice=='0':
            break

# Retrieve via web
def retrieve_from_web(stock_list):
    #clear_screen()
    print()
    print('Retrieving from web...')
    start=input('Start (MM/DD/YY): ')
    end=input('End   (MM/DD/YY): ')
    cnt=stock_data.retrieve_stock_web(start,end,stock_list)
    print(f'Records: {cnt}')
    input('Press Enter...')

# Import CSV
def import_csv(stock_list):
    #clear_screen()
    print()
    sym=input('Symbol: ').upper()
    filename=input('CSV file: ')
    stock_data.import_stock_web_csv(stock_list,sym,filename)
    print('CSV import complete.')
    input('Press Enter...')

if __name__=='__main__':
    main()         
