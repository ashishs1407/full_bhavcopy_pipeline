import requests
import pandas as pd
import time

symbol = 'NIFTY'
url = f'https://www.nseindia.com/api/option-chain-indices?symbol={symbol}'

headers = {"accept-encoding":"gzip, deflate, br, zstd" ,
           "accept-language":"en-US,en;q=0.9",
           "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
           }

session = requests.Session()

data = session.get(url , headers= headers).json()["records"]["data"]

