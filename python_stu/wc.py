#!/usr/bin/python3
'''
wordcount
interview of xiaomi band
'''
from collections import Counter
with open('/Users/luc/Documents/python/python_stu/file/wordcount','r') as f:
	l = f.readlines()
	ll = list(map(lambda s : s.strip(),l))
	c = Counter()
	for word in ll:
		c[word] = c[word] + 1
	d = dict()
	for word in ll:
		d[word] = 0
	for word in ll:
		d[word] = d[word] + 1
print(d)
print(c)
print(len(c))
#按大小排序，选出top3
print(c.most_common()[-1:-3:-1])
out = list()
for k,v in c.items():
	'''
	(k,v) tuple cannot modify
	'''
	out.append([k,v])
print(out)
'''
Counter 2 list
insert sort 
'''
def sort_top(*out):
	for i in range(len(out)):
		for j in range(i,len(out)):
			if out[i][1] <= out[j][1]:
				temp = out[i][1]
				out[i][1] = out[j][1]
				out[j][1] = temp
	return out
print(sort_top(*out))
with open('/Users/luc/Documents/python/python_stu/file/wc_top','w') as f2:
	for word in out:
		f2.write(word[0])
		f2.write(':')
		f2.write(str(word[1]))
		f2.write('\n')
