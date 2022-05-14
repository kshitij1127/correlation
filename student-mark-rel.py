import numpy as np 
import csv 

def get_data_source(data_path):
    marks = []
    present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks']))
            present.append(float(row['Present']))

    return {
        "x": marks,
        "y": present,
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print("correlation between the marks of the students and the number of days that they are present is:", correlation[0,1])

def setup():
    data_path = "mark-rel.csv",
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()  