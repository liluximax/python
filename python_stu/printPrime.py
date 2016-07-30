#!/usr/bin/python3
'''
判断是否为质数
'''
import math
def isPrime(num):
	flag = True
	if num < 2:
		flag = False
	else:
		for i in range(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				flag = False
				break
	return flag
'''
for i in range(101):
	if isPrime(i):
		print(i)
'''
l = [x for x in range(101) if isPrime(x)]
print(l)