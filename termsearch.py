#!/usr/bin/env python
# Name
# Date
# Description


import mincemeat
import os, sys

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~”“'''

# We'll send each mapper a book with the key it's title.
data = {}
incr = 0
for filename in os.listdir("."):
    if ".txt" == filename[-4:]:
        with open(filename) as file:
            line = file.readline()
            line_count = 0
            while line:
                data[incr] = (filename, line_count, line.lower().translate(str.maketrans(dict(map( lambda c: (c,' '), punctuations)))))
                line = file.readline()
                line_count += 1
                incr += 1
            print(f"{filename} read.")

#print(data)  # Uncomment these lines to see what data looks like
#print(len(data))
#sys.exit(1)

def mapfn(k, v):
    (filename, line_num, line) = v
    for w in line.split():
        yield w, (filename, line_num)

def reducefn(k, vs):
    files = {}
    for (filename, line) in vs:
        if filename not in files.keys():
            files[filename] = []
        files[filename].append(line)
    ret = []
    for k in files:
        ret.append( (k, min(files[k]), len(files[k])))
    return ret

s = mincemeat.Server()

# The data source can be any dictionary-like object
s.datasource = data
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

while True:
    print()
    word = input("What word to lookup?")
    if word in results.keys():
        for r in results[word]:
            print(f"   First line: {r[1]} Occurrences: {r[2]}  {r[0]}")
    else:
        print(f"{word} not in the texts read.")