
# New chalenge
# 1) Create a code that conect pull earnings data from the Alpha Vantage capital
# 2) Give the user the choice of chosing teh ticker. and the period of earnings requested
# 3) Plot the chart 

# Path shortcut: /Users/mateussfeir/Desktop/Python/GPT\ Project\ stock\ market
# File name: python Earnings_chart.py

'''Solution:'''

# 1) Create a function to push the data from the API (Aplication Programming Interface)

import requests
import matplotlib.pyplot as plt

chosen_stock = input('Which company do you want to get data? ').upper()

def get_period_data():
    period = input('Do you want to see annual or quarterly report? (a/q) ').lower()
    if period == 'a' or period == 'annual':
        period = 'annual'
    elif period == 'q' or period == 'quarterly':
        period = 'quarterly'
    return period

def information_requested():
    information = input('Do you want to request the net income or revenue for the chosen company? (ni/r) ').lower()
    if information == 'net income' or information == 'ni':
        information = 'netIncome'
    elif information == 'revenue' or information == 'r':
        information = 'totalRevenue'
    return information

period = get_period_data()

information = information_requested()

def get_API():
    url = 'https://www.alphavantage.co/query'
    params = {'function': 'INCOME_STATEMENT',
            'symbol': chosen_stock,
            'apikey': 'TE1E1KD330UYLRHQ'}
    response = requests.get(url, params=params)
    return response

# url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=TE1E1KD330UYLRHQ'

# 2) Call the function and convert the data to JSON format

response = get_API()
data = response.json()
# print(data)

# 3) Create a list to storage the date and the net income data.

earnings_list = []

for earnings in data[f'{period}Reports']:

    chosen_data = float(earnings[information])
    fiscal_date = earnings['fiscalDateEnding']
    earnings_list.append((fiscal_date, chosen_data))

# 3.1) Separate the informations in the list 

earnings_list.reverse()
dates = [inf[0] for inf in earnings_list]
chosen_data = [inf[1] for inf in earnings_list]
chosen_data_billion = [x/1000000000 for x in chosen_data]
# print(chosen_data_billion)


# 4) Plot the chart

plt.style.use('dark_background')
plt.bar(dates, chosen_data)
plt.xlabel('Date')
plt.ylabel('Earnings (Billion)')
plt.title(f"{chosen_stock}'s {information}")
plt.show()






