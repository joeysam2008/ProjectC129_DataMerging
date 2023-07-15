from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
import requests

bright_star_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome()
browser.get(bright_star_url)
time.sleep(10)

headers = ["Star_names", "Distance", "Mass", "Radius"]
bright_star_data = []

def scrape():
    page = requests.get(bright_star_url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    temp_list = []

    Star_names = []
    Radius = []
    Mass = []
    Distance = []

    for i in range(1, len(temp_list)):
        Star_names.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][8])
        Radius.append(temp_list[i][9])

    for tr_tag in soup.find("table").find_all("tr"):
        td = tr_tag.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
        for td in tr_tag:
            try: 
                temp_list.append(td.find_all("a")[0].contents[0])
            except:
                temp_list.append("")
    
    bright_star_data.append(temp_list)

    df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
    print(df2)

    df2.to_csv('bright_stars.csv')

scrape()
