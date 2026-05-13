import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.friv.com/")
soup=BeautifulSoup(response.text,"html.parser")
links=soup.find_all("a")
stored_links=[]
for link in links:
    stored_links.append({
        "text": link.text,
        "url": link.get("href")
    })
print(stored_links)