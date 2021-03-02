#!/usr/bin/env python
import mincemeat
import os, sys

'''data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again",
        ]'''

'''
# Reads all the .txt files
data = []
incr = 0
for filename in os.listdir("."):
    if ".txt" == filename[-4:]:
        with open(filename) as file:
            line = file.readline()
            line_count = 0
            while line:
                data.append(line.lower())
                line = file.readline()
                line_count += 1
                incr += 1
            print(filename, " read.")
'''

# Reads all the .nums files
data = []
incr = 0
for filename in os.listdir("."):
    if ".nums" == filename[-5:]:
        with open(filename) as file:
            line = file.readline()
            line_count = 0
            while line:
                data.append(int(line.lower()))
                line = file.readline()
                line_count += 1
                incr += 1
            print(filename, " read.")

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

print(datasource)

def mapfn(k, v):
    for w in v.split():
        yield w, 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
