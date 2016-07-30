
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)
class Student(object):

    def __init__(self, name, age, score):
        self._name = name
        self._age = age
        self._score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self._name, self._age, self._score)
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @property
    def score(self):
        return self._score
    
def Student2dict(std):
	return{
		'name': std._name,
		'age': std._age,
		'score': std._score
	}
s = Student('Bob', 20, 88)
'''
if do this
the json will be Dump Student: {"_score": 88, "_name": "Bob", "_age": 20}
contains '_'

std_data = json.dumps(s, default=lambda obj: obj.__dict__)
'''
std_data = json.dumps(s, default = Student2dict)
print('Dump Student:', std_data)
'''
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['_name'], d['_age'], d['_score']))
'''
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
print(rebuild.name)
print(rebuild.age)
print(rebuild.score)