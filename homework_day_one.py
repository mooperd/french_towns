import csv 

with open(r"short.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for town in reader:
        if int(town["E14TS500"]) > 0:
            print((town["LIBGEO"]) + " has " + (town["E14TS500"]) + " firm/s with more than 500 employees in the town")