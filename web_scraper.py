from bs4 import BeautifulSoup
import requests
import csv
import re
from random import random
import time


def randomSleep():
    time.sleep(random())

def scrape_page(writer):
    for movie in soup.findAll('div', class_='lister-item-content'):
        if movie.find(href=re.compile('title')):
            s = str(movie.find(href=re.compile('title')))
            ss1 = 'tt'
            ss2 = '/">'
            title_id = s[s.find(ss1):s.find(ss2)]
            title = movie.find(href=re.compile('title')).get_text()
        if movie.find('span', class_='lister-item-year text-muted unbold'):
            year = movie.find('span', class_='lister-item-year text-muted unbold').get_text()
        if movie.find('span', class_='runtime'):
            runtime = movie.find('span', class_='runtime').get_text()
        if movie.find('span', class_='genre'):
            genres = movie.find('span', class_='genre').get_text()
        if movie.find('p', class_=''):
            s = movie.find('p', class_='').get_text()
            print(s)
            str_list = s.split()
            print(str_list)
            # start = s.find('Director:') + len('Director:')
            # end = s.find('|')
            # director = s[start:end].strip()
            # start = s.find('Stars:') + len('Stars:')
            # end = s.find('|')
            # stars = s[start:].strip()
        writer.writerow((title_id, title, year, runtime, genres, director, stars))       

with open('movie_data.csv', 'w') as f:
    writer = csv.writer(f)
    root = 'https://www.imdb.com'
    search_url = '/search/title/?title_type=feature&sort=alpha,asc'
    response = requests.get(root+search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    #while soup.find('a', class_='lister-page-next next-page'):
    scrape_page(writer)
    randomSleep() 
    # search_url = soup.find('a', class_='lister-page-next next-page').attrs['href']
    # response = requests.get(root+search_url)
    # soup = BeautifulSoup(response.text, "html.parser")