import pandas
import matplotlib.pyplot as plt
import csv

data = []
with open('dataset_Facebook.csv') as csvfile:
    reader1 = csv.reader(csvfile,delimiter=';')
    for row in reader1:
        try:
            data.append(int(row[5]))
        except ValueError:
            print("ignoring the column title")
print(data)


plt.hist(data, bins=40)

plt.title("Histogram for Facebook Metrics : Binning")
plt.xlabel("Post Hour")
plt.ylabel("Frequency")
plt.show()