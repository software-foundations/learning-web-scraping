import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.gilenofilho.com.br')

print(response.status_code)

print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find('title'))

link = soup.find('h3', attrs={'class': 'ctitle'})

links = soup.find_all('h3', attrs={'class': 'ctitle'})

print(link)

print(links)

for li in links:
	print(li)
