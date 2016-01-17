__author__ = 'yongeun, hyeonseok'

import requests
from bs4 import BeautifulSoup

response = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
parser = BeautifulSoup(response.text, "lxml")

titles = parser.find_all("a", "title")

#print all titles of webtoon
#for elem in titles:
#    print 'title:{0} link:{1}\n'.format(elem['title'].encode('utf-8'), elem['href'].encode('utf-8'))
#
today_webtoon = parser.findAll("div", { "class" : "col col_selected" })

for elem in today_webtoon:
    titles = elem.find_all("a", "title")
    for elem2 in titles:
        print 'title:{0} link:{1}\n'.format(elem2['title'].encode('utf-8'), elem2['href'].encode('utf-8'))

print response
