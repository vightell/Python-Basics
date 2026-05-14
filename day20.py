import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.hackathon.com/2024/schedule")
soup=BeautifulSoup(response.text,"html.parser")
links=soup.find_all("a")
stored_links=[]
for link in links:
    stored_links.append({
    "text":link.text,
    "url":link.get("href")
})
with open("day20_links_messy.txt","w") as file:
 file.write(str(stored_links))