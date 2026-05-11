import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.github.com")
soup=BeautifulSoup(response.text,"html.parser")
title=soup.find("h1")
paragraph=soup.find("p")
print(title.text)
print(paragraph.text)