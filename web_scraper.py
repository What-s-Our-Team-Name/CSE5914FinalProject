from ctypes import cast
from sre_parse import State
from bs4 import BeautifulSoup, Tag
import requests
import csv
import re
from random import random
import time

from sqlalchemy import desc


def splitArray(cast_list):
    director_list = []
    star_list = []
    state_change = False
    for i in range(len(cast_list)):
        if(cast_list[i]=="|"):
            state_change = True
        else:
            if not state_change:
                director_list.append(cast_list[i])
            else:
                star_list.append(cast_list[i])
    return director_list,star_list


def randomSleep():
    time.sleep(random())

def scrape_page(writer):
    for movie in soup.findAll('div', class_='lister-item-content'):
        title_id = None
        title = None
        year = None
        runtime = None
        genres = None
        dir_list = None
        cast_list = None
        rating = None
        description = ''

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
            str_list = s.split('\n')
            mod_cast_list = []
            for string in str_list:
                mod_str = string.strip()
                if mod_str != '':
                    mod_cast_list.append(mod_str)
            dir_list, cast_list = splitArray(mod_cast_list)
        if movie.find('div', class_='inline-block ratings-imdb-rating'):
            s = movie.find('div', class_='inline-block ratings-imdb-rating').attrs
            rating = s['data-value']
        if movie.findAll('p', class_='text-muted'):
            p_tags = movie.findAll('p', class_='text-muted')
            if len(p_tags) >= 2:
                description_unclean = p_tags[1].contents
                description_unclean[0] = description_unclean[0][1:]
                for text in description_unclean:
                    if type(text) != Tag:
                        description += text
                    else:
                        for child in text.descendants:
                            if type(child) == str:
                                description += child

        writer.writerow((title_id, title, year, runtime, genres, dir_list, cast_list, rating, description))       

with open('movie_data_pop.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('title_id', 'title', 'year', 'runtime', 'genres', 'dir_list', 'cast_list', 'rating'))
    root = 'https://www.imdb.com'
    search_url = '/search/title/?title_type=feature&release_date=,2021-12-31&languages=en'
    response = requests.get(root+search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    i = 1
    while soup.find('a', class_='lister-page-next next-page'):
        try:
            scrape_page(writer)
            randomSleep() 
            search_url = soup.find('a', class_='lister-page-next next-page').attrs['href']
            response = requests.get(root+search_url)
            soup = BeautifulSoup(response.text, "html.parser")
            print('Page ' + str(i) + ' has been scraped')
            i += 1
        except:
            print(search_url)
            print(response)
    print("Scraping complete")