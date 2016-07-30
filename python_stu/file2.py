#!/usr/bin/python3
with open('/home/liluxi/python/out','r') as f1:
	l = f1.readlines()
	def substr(s):
		s = s.strip()
		s = s.strip(',')
		return s
	lout = map(substr,l)

with open('/home/liluxi/python/newout','w') as f2:
	for line in lout:
		f2.write(line)
		f2.write('\n')