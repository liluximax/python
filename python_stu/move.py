#!/usr/bin/python3
import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny


try:
	10 / 0
except Exception as e:
	print(e)
finally:
	print('finally')
print('goon')

