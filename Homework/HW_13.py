import csv
import json
import os
import glob
import datetime

from DataEntry import DataEntry

folder_path = "C:\\Users\\Professional\\Downloads\\SKU\\SKU"
all_list = []

csv_paths = glob.glob(os.path.join(folder_path, '*.csv'))
for csv_path in csv_paths:
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            date = datetime.datetime.strptime(row[0], '%d-%b-%Y')
            time = datetime.datetime.strptime(row[1], '%H:%M:%S')
            expiration_date = datetime.datetime.strptime(row[7], '%d-%b-%Y')
            data_entry = DataEntry(date.date(), time.time(), row[2], row[3], int(row[4]), row[5], row[6],
                                   expiration_date.date(), float(row[8]), row[9])

            all_list.append(data_entry)

json_paths = glob.glob(os.path.join(folder_path, '*.json'))
for json_path in json_paths:
    with open(json_path, 'r') as file:
        json_reader = json.load(file)
        for json_row in json_reader["data"]:
            data_entry = DataEntry(**json_row)
            all_list.append(data_entry)


print(len(all_list))


