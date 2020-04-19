import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Penetration-Tester&where=Austin-TX'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

#print(results.prettify())

#job_elems = results.find_all('section', class_='card-content')
pen_jobs = results.find_all('h2', string=lambda text: 'penetration' in text.lower())
for job in pen_jobs:
    # title_elem = job.find('h2', class_='title')
    # company_elem = job.find('div', class_='company')
    # location_elem = job.find('div', class_='location')
    # if None in (title_elem, company_elem, location_elem):
    #     continue
    # print(title_elem.text.strip())
    # print(company_elem.text.strip())
    # print(location_elem.text.strip())
    # print()
    link = job.find('a')['href']
    print(job.text.strip())
    print(f"Apply here: {link}\n")