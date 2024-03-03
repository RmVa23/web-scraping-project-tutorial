import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request

# load the .env file variables
#load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine functio

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"


def scrape_Web(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f'Error al acceder a la URL: {url, response.status_code}')
    soup = BeautifulSoup(response.text, 'html.parser')

print(scrape_Web(url))