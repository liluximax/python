#!/usr/bin/python3
lines = list()
with open('/Users/luc/Desktop/TC_header.txt', 'r') as f:
    for line in f.readlines():
        single = list()
        line = line.strip("\n").strip(" ")
        for num in line.split(" "):
            single.append(int(num))
        lines.append(single)

for line in lines:
    print (line)