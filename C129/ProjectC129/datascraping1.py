from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
import requests

star_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

headers = ["Star_name", "distance", "mass", "radius"]
star_data = []

def scrape():
    page = requests.get(star_url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    temp_list = []

    star_name = []
    radius = []
    mass = []
    distance = []

    for i in range(1, len(temp_list)):
        star_name.append(temp_list[i][0])
        distance.append(temp_list[i][5])
        mass.append((temp_list[i][8])*0.000954588)
        radius.append((temp_list[i][9])*0.102763)

    for tr_tag in soup.find("table").find_all("tr"):
        td = tr_tag.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
        for td in tr_tag:
            try: 
                temp_list.append(td.find_all("a")[0].contents[0])
            except:
                temp_list.append("")
    
    star_data.append(temp_list)

    df2 = pd.DataFrame(list(zip(star_name,radius,mass,distance)),columns=["Star Name", "Radius", "Mass", "Distance"])
    df2.to_csv("dwarf_stars.csv")

    with open("dwarf_stars.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(star_data)

scrape()
