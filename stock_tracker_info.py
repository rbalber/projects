import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import time as tm


print('For this program to run smoothly please have a stable internet connection. This program was inspired by Alan')

tm.sleep(3)
print('\nEnjoy!')
    
tm.sleep(10)
print('\nPlease type in the stock symbol you\'d like information about?')
stock = str(input())

name = yf.Ticker(stock)
name_1 = stock.upper()
info = name.info
log_name = info['longName']
sector = info['sector']

print(f'\nYou typed {name_1}, and the name of the organization is the {log_name}, this firm is in the {sector} sector')

tm.sleep(5)

print('\nI will also grab you some of the company\'s info, as well')

summary = info['longBusinessSummary']
num_employees = info['fullTimeEmployees']
num_employees = "{:,}".format(num_employees)
num_employees = str(num_employees)

tm.sleep(10)
print('\n'+ summary)

tm.sleep(30)
print('\nAlso the company has about ' + num_employees + ' full time employees')


tm.sleep(3)

print(f'\nHere is some of the stock history for {log_name}')

days_back = input(f'\nHow many days would back would you like to look at {log_name}?\n')


days_back = str(days_back)

days = days_back + 'd'

history = name.history(days)

history = history.values.tolist()

tm.sleep(5)

print('Which would you like information for? (Open, High, Low, Close, Volume)')

option = str(input())

if option == 'Open':
    _option = 0
    _option = int(_option)
elif option == 'High':
    _option = 1
    _option = int(_option)
elif option == 'Low':
    _option = 2
    _option = int(_option)
elif option == 'Close':
    _option = 3
    _option = int(_option)
elif option == 'Volume':
    _option = 4
    _option = int(_option)


option_item = history[-1][_option]

tm.sleep(5)
option_item = "{:,}".format(option_item)
option_item = str(option_item)
print(f'\nThe {option} for {log_name} the previous business day, is {option_item}')


print('\nWould you like to a see the recommendation Yahoo has for this stock?')

answer_1 = input()

if answer_1 == 'yes':
    rec = info['recommendationKey']
    tm.sleep(5)
    rec = rec.upper()
    print('\n' + rec)
else:
    tm.sleep(5)
    rec = info['recommendationKey']
    rec = rec.upper()
    print('\n' + rec)

tm.sleep(7)
print(f'\nLastly to end this program I will present you some of the important financials for {log_name}')

current_price = info['currentPrice']
current_price = round(current_price)
current_price = "{:,}".format(current_price)


profit_margin = info['profitMargins']
profit_margin = profit_margin * 100
profit_margin = round(profit_margin)
profit_margin = str(profit_margin)

gross_profits = info['grossProfits']
gross_profits = round(gross_profits)
gross_profits = "{:,}".format(gross_profits)
gross_profits = str(gross_profits)

ebitda_margins = info['ebitdaMargins']
ebitda_margins = ebitda_margins * 100
ebitda_margins = round(ebitda_margins)
ebitda_margins = str(ebitda_margins)

operatig_cash_flow = info['operatingCashflow']
operatig_cash_flow = round(operatig_cash_flow)
operatig_cash_flow = "{:,}".format(operatig_cash_flow)
operatig_cash_flow = str(operatig_cash_flow)

roa = info['returnOnAssets']
roa = roa * 100
roa = round(roa)
roa = str(roa)

roe = info['returnOnEquity']
roe = roe * 100
roe = round(roe)
roe = str(roe)


rev_growth = info['revenueGrowth']
rev_growth = rev_growth * 100
rev_growth = round(rev_growth)
rev_growth = str(rev_growth)


tm.sleep(7)
print('\nSorry this is taking so long to recieve, it should only take a few more seconds')

tm.sleep(3)
print(f'\nBelow are some of the important financials, that I thought you\'d would like to look at: \n\nCurrent Price is ${current_price} \nProfit Margins is {profit_margin}% \nGross Profits is ${gross_profits} \nEarnings Before Interest, Taxes, Depreciation and Amortization margins is {ebitda_margins}% \nOperating Cash Flow is ${operatig_cash_flow}')
print(f'\nReturn on Assets is {roa}% \nReturn on Equity is {roe}% \nRevenue Growth is {rev_growth}%')


tm.sleep(10)

print('\nIf you enjoyed or wanted to suggest something to this code, please donate or reach out to me')


tm.sleep(30)

done = input('\nPlease type close to end this program. \n')

if done == 'close':
    print(f'You typed {done}')
else:
    print('You did not type close')

##style.use('ggplot')
##graph = history[_option].plot()
##plt.show()




#This is not investment adivce, this should only be used for educational purposes
# Created by Rance Albert 2021 










