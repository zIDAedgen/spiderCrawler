from bs4 import BeautifulSoup
import urllib.request
import requests
import lxml
import csv

title = ['name', 'price', 'location', 'id']

name_array = ['a', 'b', 'c', 'd', 'e']
price_array = [100, 200, 300, 400, 500]
location_array = ['brisban', 'Sydney', 'Molben', 'Adlade', 'Perth']
id_array = [1001, 1002, 2003, 2004, 1005]
write_in = []
list = len(name_array)
while list > 0:

    write_in.append([name_array[list - 1], price_array[list - 1], location_array[list - 1], id_array[list - 1]])
    list = list - 1

print(write_in)
file = open('houses.csv', 'w')
writer = csv.writer(file)

writer.writerow(title)
for i in range(5):
    writer.writerow(write_in[i])

file.close()
