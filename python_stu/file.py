#!/usr/bin/python3
try:
	f1 = open('/home/liluxi/python/test','r')
	l = f1.readlines()
finally:
	f1.close()
def addstr(s):
	s = s.strip()
	s += ','
	return s
lout = map(addstr, l)

with open('/home/liluxi/python/out','w') as f2:
	for line in lout:
		f2.write(line)
		f2.write('\n')
