#!/usr/bin/python3
'''
ip 地址转 int
'''
ip_str = '115.29.51.206'
print(ip_str)
def ip2int(ip_str):
	ip = ip_str.split('.')
	ip_int = list(map(int, ip))
	return (ip_int[0] << 24) + (ip_int[1] << 16) + (ip_int[2] << 8) + ip_int[3]

ip_int = ip2int(ip_str)
print(ip_int)

def ip2str(ip_int):
	ip_str = str((ip_int >> 24) & 0xff)
	ip_str += '.'
	ip_str += str((ip_int >> 16) & 0xff)
	ip_str += '.'
	ip_str += str((ip_int >> 8) & 0xff)
	ip_str += '.'
	ip_str += str(ip_int & 0xff)
	return ip_str

ip_str2 = ip2str(ip_int)
print(ip_str2)
print(type(ip_str2))