# read csv file from an url

import requests
from io import StringIO
import pandas as pd

url = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

df = pd.read_csv(data)
print(df)