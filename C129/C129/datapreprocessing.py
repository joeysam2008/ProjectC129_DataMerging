import csv
dataset_1=[]
dataset_2=[]

with open('final.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open('archive_sorted_dataset1.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers1 = dataset_1[0]
planetdata1 = dataset_1[1:]

headers2 = dataset_2[0]
planetdata2 = dataset_2[1:]

headers = headers1 + headers2
planetdata = []

for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open('mergeddata.csv','a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)
    