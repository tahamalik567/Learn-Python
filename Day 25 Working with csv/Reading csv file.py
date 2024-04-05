file_path = "/Users/tahamalik/Learn Python/Learn-Python/Day 25 Working with csv/weather_data.csv"

# with open(file_path) as datafile:
#     data = datafile.readlines()
#     print(data)

import csv 
with open(file_path) as datafile:
    data = csv.reader(datafile)
    # print(type(data)) #<class '_csv.reader'>
    print(data)
    for row in data:
        print(row)