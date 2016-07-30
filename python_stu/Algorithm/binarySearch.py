#!/usr/bin/python3

def search(target, *list):
	left = 0
	right = len(list) - 1
	while left <= right:
		mid = (left + right) >> 1
		if target > list[mid]:
			left = mid + 1
		elif target < list[mid]:
			right = mid - 1
		else:
			return mid
	return -1

def pow(x, n = 2):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s

def fact(n):
	if n == 1:
		return n
	return n * fact(n - 1)