from bs4 import BeautifulSoup
import requests
import urllib
import os

url = "http://www.goal.com/en"
r = requests.get(url);
htmlData = r.text
soup = BeautifulSoup(htmlData, "html.parser")
imgs = soup.findAll("img");
i = 0
for img in imgs:
	imgUrl = img["src"]
	print(imgUrl)
	urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))


