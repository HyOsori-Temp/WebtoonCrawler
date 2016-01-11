__author__ = 'yongeun'

import requests
from bs4 import BeautifulSoup

response = requests.get("http://comic.naver.com")
parser = BeautifulSoup(response.text, 'lxml')

pageElements = parser.find_all(name='a', attrs={'class':'title'})

for pageElement in pageElements:
    print pageElement

print response

