url = "https://www.ncei.noaa.gov/data/storm-events/access/original/2020/StormEvents_details_s20200201_e20200228_c20200515.csv"
import requests

res = requests.get(url)
from os import path

if path.isfile(res.text):
    import pandas as pd
    df = pd.read_csv(res.text)
    print(df.columns)