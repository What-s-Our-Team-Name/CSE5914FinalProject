import requests
import browsercookie
import bs4
url = 'https://www.imdb.com/user/k_z9p2w7dy/lists?ref_=nv_usr_lst_3'
cj = browsercookie.chrome()
res = requests.get(url, cookies=cj)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")