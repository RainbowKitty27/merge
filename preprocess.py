import csv
dataset1=[]
dataset2=[]
with open("stars.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open("datasorted1.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
    
headers1=dataset1[0]
stars_data1=dataset1[1:]
headers2=dataset2[0]
stars_data2=dataset2[1:]
headers=headers1+headers2
stardata=[]
for index, data_row in enumerate(stars_data1):
   stardata.append(stars_data1[index]+stars_data2[index])
with open("merge.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stardata)    