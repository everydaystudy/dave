import csv
import json


def return_column_names(fname):

    with open(fname, newline='') as f:
        reader = csv.reader(f)
        lst = list(reader)

    columns = lst[0]

    return columns
    

def return_data_by_column(fname, cname):

    with open(fname, newline='') as f:
        reader = csv.reader(f)
        lst = list(reader)

    idx = lst[0].index(cname)
    data = [x[idx] for x in lst[1:]]

    return data

