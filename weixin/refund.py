#!/usr/bin/python3
lines = list()
with open('/Users/luc/Desktop/refound.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line)

for i in range(5):
    lines.pop(0)


def filter(l):
    data = l.split('\t')
    order = data[2].strip('`')
    pay = data[11]
    commit = 'refund'
    return order + ',' + pay + ',' + commit + ',' + order


lout = list(map(filter, lines))

with open('/Users/luc/Desktop/result.txt', 'w') as out:
    for i in range(len(lout) - 1):
        out.write(lout[i])
        out.write('\n')
    out.write(lout[len(lout) - 1])

print('success')
