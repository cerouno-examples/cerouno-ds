import requests
import pandas as pd

def ethereum():
    r = requests.get("https://graphs2.coinmarketcap.com/currencies/ethereum/")
    return r.json() 