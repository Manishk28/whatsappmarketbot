import os
import requests
import json

API_KEY = "3a7f7041eb9e07d2b78ccc88093fd26e"
BASE_URL = "http://api.marketstack.com/v1/"

def get_stock_price(stock_symbol):
    param = {
        'access_key' : API_KEY
    }
    end_point = ''.join([BASE_URL,"tickers/", stock_symbol,"/intraday/latest"])
    api_result = requests.get(end_point,param)
    print(api_result)
    json_result = json.loads(api_result.text)
    return {
        'last_price' : json_result['last']
    }

result = get_stock_price("HDFC")
print(result)