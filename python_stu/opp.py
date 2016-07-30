#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
class Student(object):
	"""docstring for Student"""
	def __init__(self, name = 'stu', score = 60):
		self.__name = name
		self.__score = score
	def get_name(self):
		return self.__name
	def get_grade(self):
		return self.__score
	def set_name(self, name):
		self.__name = name
	def set_score(self, score):
		self.__score = score
	def print_score(self):
		print('%s:%s' % (self.__name, self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

a = Student('a',67)
b = Student('b',98)

'''c = Student()
c.print_score()
a.print_score()
print(a.get_grade())
b.print_score()
print(b.get_grade())
'''
class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal run')
class Dog(Animal):
	def run(self):
		print('Dog run')
class Cat(Animal):
	def run(self):
		print('cat run')

def run_twice(param):
	param.run()
	param.run()
		
run_twice(Dog())
run_twice(Cat())

class Staff(object):
	"""docstring for Staff"""
	def __init__(self, birth, age = 0):
		super(Staff, self).__init__()
		self._birth = birth
		self._age = age
	@property
	def age(self):
	    return 2016 - self._birth
	@property
	def birth(self):
	    return self._birth
	@birth.setter
	def birth(self, value):
		self._birth = value

'''
object 2 json
json 2 object
'''
class Shop(object):
	"""docstring for Shop"""
	def __init__(self, price, time):
		self._price = price
		self._time = time
	@property
	def price(self):
	    return self._price
	@property
	def time(self):
	    return self._time
	@price.setter
	def price():
		return self._price
	@time.setter
	def time():
		return self._time
def Shop2dict(std):
	return {
		'price': std._price,
		'time': std._time
			}
def dict2Shop(d):
	return Shop(d['price'], d['time'])
s = Shop(10,1000)
json_str = json.dumps(s,default = Shop2dict)
print(json_str)
'''ss = json.loads(json_str, object_hook = dict2Shop)'''
ss = json.loads(json_str,object_hook = lambda d : Shop(d['price'],d['time']))
print(ss.time)