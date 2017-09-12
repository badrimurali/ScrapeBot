"""this is a scrapebot for scraping any website"""
from bs4 import BeautifulSoup
from TagParser import getAll
import requests

URL = "http://www.goal.com/en"
R = requests.get(URL)
HTML_DATA = R.text
SOUP = BeautifulSoup(HTML_DATA, "html.parser")
IMGS = getAll(SOUP, "img")
PARA = getAll(SOUP, "p")
DIVS = getAll(SOUP, "div")
for img in IMGS:
    imgUrl = img["src"]
    print imgUrl

for p in PARA:
    for child in p.children:
        print child

for div in DIVS:
    print len(list(div.children))
    divList = list(div.children)
    for count, divItem in enumerate(divList):
        print("i", count, divItem)
