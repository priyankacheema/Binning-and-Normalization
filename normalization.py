import pandas
import matplotlib.pyplot as plt
import csv

data = []
with open('dataset_Facebook.csv') as csvfile:
    reader1 = csv.reader(csvfile,delimiter=';')
    for row in reader1:
        try:
            newrange = (0,1)
            oldrange = (1,23)
            olddiff = oldrange[1] - oldrange[0]
            newdiff = newrange[1] - newrange[0] 
            currentval = int(row[5])
            newval = (((currentval - oldrange[0]) * newdiff)/olddiff) + newrange[0]
            data.append(newval)
        except ValueError:
            print("ignoring the column title")
print(data)
plt.hist(data, normed=True)
plt.title("Histogram for Facebook Metrics : Normalization")
plt.xlabel("Post Hour")
plt.ylabel("Frequency")
plt.show()