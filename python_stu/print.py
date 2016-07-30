#!/usr/bin/python3
x = input("x: ")
y = input("y: ")
print(int(x) - int(y))
print("sss")
nums = [1,2,3,4,5]
nums.pop()
print(nums)

def my_abs(x):
	if (x>0):
		return x
	else:
		return -x

print(my_abs(int(x))