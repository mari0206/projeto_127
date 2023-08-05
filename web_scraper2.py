from bs4 import BeautifulSoup
import pandas as pd
import time
import requests


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)

scraped_data = []

def scrape():
    soup = BeautifulSoup(page.text, 'html.parser')

    tables = soup.find_all('table', attrs= {'class', 'wikitable', 'sortable'})
    table_rows = tables[1].find_all('tr')

    temp_list = []

    for row in table_rows:
        table_cols = row.find_all('td')
        data = [col.text.strip() for col in table_cols]

        temp_list.append(data)
            
    scraped_data.append(temp_list)

scrape()

stars_data = []

for i in range(0, len(scraped_data)):
    star_names = scraped_data[i][0]
    distance = scraped_data[i][5]
    mass = scraped_data[i, 7]
    radius = scraped_data[i, 8]

    required_data = [star_names, distance, mass, radius]
    stars_data.append(required_data)

headers = ['star_names', 'distance', 'mass', 'radius']
star_df = pd.DataFrame(stars_data, columns= headers)
star_df.to_csv('scraped_data.csv', index = True, index_label= 'id')
