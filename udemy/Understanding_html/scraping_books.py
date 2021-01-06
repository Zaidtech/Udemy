import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.example.com')
print(page.content)

