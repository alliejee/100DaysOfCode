import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Penetration-Tester&where=Austin-TX'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(div='summary')

print(soup.prettify())