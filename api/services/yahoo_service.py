import requests

def get_stock_quote(symbol: str):
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()
