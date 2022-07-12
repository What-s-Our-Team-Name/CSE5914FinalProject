#@author: What is our team name?

import requests

import csv
"""
URL = "https://imdb-api.com/en/API/Top250Movies/k_z9p2w7dy"
r = requests.get(url = URL)
data = r.json()
ids = []
i = 0
row = []
col = [""]
for titleID in range(len(data['items'])):
    #ids[i] = data['items'][titleID]['id']
    col.append(data['items'][titleID]['id'])
    row.append([data['items'][titleID]['id']])
    i += 1
print(col)
print(row)

with open('data.csv','w') as f:
    write = csv.writer(f)
    write.writerow(col)
    write.writerows(row)
"""
URL = "https://imdb-api.com/en/API/IMDbList/k_z9p2w7dy/ls004285275"
r = requests.get(url = URL)
data = r.json()
print(data)