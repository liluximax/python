#!/usr/bin/python3
def not_empty(s):
    return s and s.strip()

l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l)

def is_odd(n):
	return n % 2 == 1
l2 = list(filter(is_odd,list(range(20))))
print(l2)

def is_huishu(n):
	n_str = str(n)
	return n_str[::-1] == n_str

output = filter(is_huishu,range(100))
print(list(output))