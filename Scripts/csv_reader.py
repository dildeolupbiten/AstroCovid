# -*- coding: utf-8 -*-

from .modules import csv, array


def read_csv_file(filename: str = ""):
    data = {}
    result = []
    for index, row in enumerate(csv.reader(open(filename))):
        if index == 0:
            result.append(row[1:])
        else:
            row[1] = row[1].replace(" ", "\ ")
            if row[1] in data:
                data[row[1]] += array(
                    [int(i) if str(i).isnumeric() else 0 for i in row[2:]]
                )
            else:
                data[row[1]] = array(
                    [
                        int(i) if str(i).isnumeric() else float(i)
                        for i in row[2:]
                    ]
                )
    return result + [
        [k] + [
            int(i) if str(i).isnumeric() else float(i) for i in v
        ] for k, v in data.items()
    ]
