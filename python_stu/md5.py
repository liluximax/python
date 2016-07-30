#!/usr/bin/python3
import hashlib
import json
from urllib import request
'''
add salt
'''
def calc_md5(password):
	md5 = hashlib.md5()
	salt = password + 'the-salt'
	md5.update(salt.encode('utf-8'))
	return md5.hexdigest()

password = '1234'
print(calc_md5(password))
url = 'http://weather.yahooapis.com/forecastrss?u=c&w=2151330'
with request.urlopen('http://app1.u-coupon.cn:8000/weixin/get_city_list.php') as f:
		data = f.read()
		data = data.decode('utf-8')
		d = json.loads(data)
		citylist = d['city_list']
		for city in citylist:
			print('%s: %s' % (city['cityname'],city['city_id']))
