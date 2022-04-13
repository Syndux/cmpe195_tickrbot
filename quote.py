import os
import finnhub
import requests


finnhub_client = finnhub.Client(api_key=os.environ['finnhub'])

def not_found():
    not_found_dict = dict()
    not_found_dict['color'] = 'red'
    not_found_dict['title'] = "Stock symbol does not exist."
    return not_found_dict

def get_quote(symbol):
    stock_quote = finnhub_client.quote(symbol={symbol.upper()})

    if stock_quote['c'] == 0:
        return not_found()
