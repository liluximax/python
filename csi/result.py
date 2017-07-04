#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# n_groups = 5
# men = (20, 35, 30, 35, 27)
# women = (25, 32, 34, 20, 25)
#
# # fig, ax = plt.subplot()
# index = np.arange(n_groups)
# print index
# bar_width = 0.35
#
# rects1 = plt.bar(index, men, bar_width, None, None, color='b', label='Men')
# rects2 = plt.bar(index + bar_width, women, bar_width, None, None, color='r', label='Women')
#
# plt.xticks(index + bar_width, ('a', 'b', 'c', 'd', 'e'))
# plt.legend()
# plt.ylim(0, 40)
# plt.show()

# MIMO准确性对比
n_groups = 4
mimo1 = (89, 88, 92, 90)
mimo2 = (94, 90, 95, 93)
mimo3 = (96, 97, 95, 96)

index = np.arange(n_groups)
bar_width = 0.2
gap = 0.03

rects1 = plt.bar(index, mimo1, bar_width, None, None, color='w', label='1*1 antennas')
rects2 = plt.bar(index + bar_width + gap, mimo2, bar_width, None, None, color='gray', label='1*2 antennas')
rects3 = plt.bar(index + 2 * bar_width + 2 * gap, mimo3, bar_width, None, None, color='w', hatch='\\', label='2*2 antennas')

plt.xlabel("Measurement Case")
plt.ylabel("Correct Rate (%)")
plt.xticks(index + (1.5 * bar_width + gap), ('1', '2', '3', '4'))
plt.legend(loc=4)
plt.ylim(0, 100)
plt.show()

# FP/FN对比
# n_groups = 5
# fp = (1.4, 2.4, 3.8, 4.6, 4.4)
# fn = (8.6, 6, 2.2, 1.6, 0.8)
#
# index = np.arange(n_groups)
# bar_width = 0.2
# gap = 0.03
#
# rects1 = plt.bar(index, fp, bar_width, None, None, color='w', label='FP')
# rects2 = plt.bar(index + bar_width + gap, fn, bar_width, None, None, color='gray', label='FN')
#
# plt.xlabel("Window Size (ms)")
# plt.ylabel("FP/FN (%)")
# plt.xticks(index + (bar_width + 0.5*gap), ('500', '1000', '1500', '2000', '2500'))
# plt.legend()
# plt.ylim(0, 10)
# plt.show()


# my FIMD RSSI 准确率对比    HPMD
# High Precision Human Motion Detection System
# HPMD

# hpdp = [88, 91, 93, 96, 95, 96, 92, 81, 79, 74]
# fimd = [86, 86, 89, 91, 92, 84, 79, 69, 65, 67]
# rssi = [63, 72, 74, 81, 82, 75, 72, 51, 46, 42]
# n = range(10)
# plt.plot(n, hpdp, color='black', linewidth=2, marker='o', ms=8, label='HPMD')
# plt.plot(n, fimd, color='black', linewidth=2, marker='d', ms=8, label='FIMD')
# plt.plot(n, rssi, color='black', linewidth=2, marker='^', ms=8, label='RSSI')
# plt.grid()
# plt.ylim(20, 100)
# plt.legend(loc=4)
# plt.xlabel("Window Size (ms)")
# plt.ylabel("Correct Rate (%)")
# plt.xticks(n, ('500', '1000', '1500', '2000', '2500', '3000', '3500', '4000', '4500', '5000'))
# plt.show()
