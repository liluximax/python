#!/usr/bin/python3
import sys
file_size = 43.1
time = float(sys.argv[1])
result = file_size / time * 8
print "\nfile: %sM, time: %ss, rate: %.2f\n" % (file_size, time, result)