import csv
dataset_1=[]
dataset_2=[]

with open('dwarf_stars.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open('bright_stars.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers1 = dataset_1[0]
stardata1 = dataset_1[1:]

headers2 = dataset_2[0]
stardata2 = dataset_2[1:]

headers = headers1 + headers2
stardata = []

for index,datarow in enumerate(planetdata1):
    stardata.append(stardata1[index]+stardata2[index])

with open('merged_data.csv','a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stardata)