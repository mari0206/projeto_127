from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
navegador = webdriver.Edge()
navegador.get(url)

scraped_data = []

def scrape():
    soup = BeautifulSoup(navegador.page_source, 'html.parser')

    table = soup.find('table', attrs= {'class', 'wikitable'})
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list = []
        #print(table_cols)

        for col in table_cols:
            #print(col.text)
            data = col.text.strip()
            temp_list.append(data)
            
        scraped_data.append(temp_list)

scrape()

stars_data = []

for i in range(0, len(scraped_data)):
    star_names = scraped_data[i][1]
    distance = scraped_data[i][3]
    mass = scraped_data[i, 5]
    radius = scraped_data[i, 6]
    lum = scraped_data[i, 7]

    required_data = [star_names, distance, mass, radius, lum]
    stars_data.append(required_data)

headers = ['star_names', 'distance', 'mass', 'radius', 'lum']
star_df = pd.DataFrame(stars_data, columns= headers)
star_df.to_csv('scraped_data.csv', index = True, index_label= 'id')


