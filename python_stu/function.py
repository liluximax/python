#!/usr/bin/python3
from functools import reduce
def fact(n):
	if n == 1:
		return n
	return n * fact(n - 1)

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)
def fib2(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b,a+b
		n = n + 1
	print('done')		

fib2(6)

def jumpStep(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	return jumpStep(n - 1) + jumpStep(n - 2)

l = []
for x in range(1,11):
	if x % 2 == 0:
		l.append(x*x)

#print(l)

l = [x for x in range(1,11)]
#print(l)

def fib2(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n +1
	return 'done'

def add2(x,y,f):
	return f(x)+f(y)

def add(x,y):
	return x + y

def f(x):
	return x*x

'''
str to int
map reduce
'''
def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(fn, map(char2num,s))

print(str2int('1233'))

r = map(f, range(10))
print(list(r))

sum = reduce(add,[1,2,3,4,5])
print(sum)

'''
to lower
'''
def normalize(name):
    return name.lower().capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''
get accumulate
'''
def prod(L):
	def acc(x,y):
		return x * y
	return reduce(acc, L)
print(prod([3, 5, 7, 9]))

'''
'123.456' to 123.456
'''
def str2float(s):
	high,low = s.split('.')
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	def fn(x,y):
		return x * 10 + y
	return reduce(fn, map(char2num, high + low)) / 10 ** len(low)

'''
is even
'''
def is_even(n):
	return n % 2 == 0
print(list(filter(is_even,[1,2,3,4,5,6])))
