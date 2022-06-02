from bs4 import BeautifulSoup
import requests
import csv
import re

root = 'https://www.imdb.com'
search_url = '/search/title/?title_type=feature&sort=alpha,asc'
response = requests.get(root+search_url)
soup = BeautifulSoup(response.text, "html.parser")

with open('test_data.csv', 'w') as f:
    print(soup.find('div', class_='lister-item-content').prettify())
    for movie in soup.findAll('div', class_='lister-item-content'):
        if movie.find(href=re.compile('title')):
            s = str(movie.find(href=re.compile('title')))
            ss1 = 'tt'
            ss2 = '/">'
            print(s[s.find(ss1):s.find(ss2)])
            print(movie.find(href=re.compile('title')).get_text())
        if movie.find('span', class_='lister-item-year text-muted unbold'):
            print(movie.find('span', class_='lister-item-year text-muted unbold').get_text())
        if movie.find('span', class_='runtime'):
            print(movie.find('span', class_='runtime').get_text())
        if movie.find('span', class_='genre'):
            print(movie.find('span', class_='genre').get_text())
        if movie.find('p', class_=''):
            s = movie.find('p', class_='').get_text()
            start = s.find('    Director:') + len('    Director:')
            end = s.find('|')
            director = s[start:end].strip()
            start = s.find('    Stars:') + len('    Stars:')
            end = s.find('|')
            stars = s[start:].strip()
            print(director)
            print(stars)
        print('--------------------------------------------------------------------------------')

    # search_url = soup.find('a', class_="lister-page-next next-page").get('href')
    # response = requests.get(root+search_url)
    # soup = BeautifulSoup(response.text, "html.parser")