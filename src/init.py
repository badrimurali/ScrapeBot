from bs4 import BeautifulSoup
from TagParser import getAll
import requests
import urllib
import os

url = "http://www.goal.com/en"
r = requests.get(url);
htmlData = r.text
soup = BeautifulSoup(htmlData, "html.parser")
imgs = getAll(soup, "img")
paragraphs = getAll(soup, "p")
divs = getAll(soup, "div")
for img in imgs:
	imgUrl = img["src"]
	print(imgUrl)
	# urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))

for p in paragraphs:
	for child in p.children:
		print(child)
		
for div in divs:
	print(len(list(div.children)))
	divList = list(div.children)
	for i in range(len(divList)):
		print("i", i, divList[i])


