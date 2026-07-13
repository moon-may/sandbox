import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup)