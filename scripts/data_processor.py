import csv
import json


def csv_reader(file_location):
    with open(file_location, mode='r') as csv_file:
        data = [line for line in csv.DictReader(csv_file)]
        for row in data:
            try:
                row['Lat'] = float(row['Lat'])
                row['Long'] = float(row['Long'])
                row['Altitude'] = float(row['Altitude'])
            except Exception as exp:
                raise ValueError(str(exp))

        return data

def json_reader(file_location):
    with open(file_location) as f:
        parent = json.load(f)
        for child in parent:
            try:
                child['id'] = int(child['id'])
                child['name'] = str(child['name'])
            except Exception as exp:
                raise ValueError(str(exp))
        return parent
