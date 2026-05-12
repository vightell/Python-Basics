import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.cats.com/cat-breeds')
soup = BeautifulSoup(response.text, 'html.parser')
links=soup.find_all('a')
for link in links:
    print(link.text)
    print(link.get('href'))