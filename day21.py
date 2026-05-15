import requests
from bs4 import BeautifulSoup
response=requests.get("https://news.ycombinator.com/")
soup=BeautifulSoup(response.text,"html.parser")
article_tag=soup.find_all("span",class_="titleline")
titles=[]
for i in article_tag:
    links=i.find("a")
    titles.append({
        "title":links.text,
        "link":links["href"] if links else None
    })
for item in titles:
    print(item)
with open("hackernews.txt","w") as file:
    for item in titles:
        file.write(str(item)+"\n")