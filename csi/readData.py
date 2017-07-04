#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import numpy as np
import matplotlib.pyplot as plt
import cal_std
from scipy.ndimage import filters


class Data(object):
    def __init__(self, timestamp_low, rssi, perm, noise, csi):
        self.timestamp_low = timestamp_low
        self.rssi = rssi
        self.perm = perm
        self.noise = noise
        self.csi = csi


def dict2Data(d):
    return Data(d['timestamp_low'], d['rssi'], d['perm'], d['noise'], d['csi'])


file_data = []

with open('/Users/luc/Desktop/csi/test_new.json', 'r') as f:
    for line in f.readlines():
        file_data.append(json.loads(line, object_hook=dict2Data))

csi_amp_a_list = []
csi_amp_b_list = []
csi_amp_c_list = []

csi_amp_1_a_list = []
csi_amp_1_b_list = []
csi_amp_1_c_list = []
csi_amp_2_a_list = []
csi_amp_2_b_list = []
csi_amp_2_c_list = []

csi_amp_2_a_var_list = []

rssi = []
time_start = file_data[0].timestamp_low
time = []

for data in file_data:
    csi_point = data.csi
    csi_amp_a = []
    csi_amp_b = []

    csi_amp_1_a = []
    csi_amp_1_b = []
    csi_amp_2_a = []
    csi_amp_2_b = []

    perm = data.perm
    hash = dict()
    for i in range(3):
        atenna = perm[i]
        if atenna == 1:
            hash['a'] = i
        elif atenna == 2:
            hash['b'] = i
        elif atenna == 3:
            hash['c'] = i

    for i in range(30):
        csi_bit = csi_point[i]
        if len(csi_bit) != 2:
            csi_amp_a.append(0)
            csi_amp_b.append(0)
        else:
            csi_amp_a.append(csi_bit[0][hash['a']] + csi_bit[1][hash['a']])
            csi_amp_b.append(csi_bit[0][hash['b']] + csi_bit[1][hash['b']])

            csi_amp_1_a.append(csi_bit[0][hash['a']])
            csi_amp_1_b.append(csi_bit[0][hash['b']])
            csi_amp_2_a.append(csi_bit[1][hash['a']])
            csi_amp_2_b.append(csi_bit[1][hash['b']])

    csi_amp_a_avg = np.mean(csi_amp_a)
    csi_amp_b_avg = np.mean(csi_amp_b)

    csi_amp_1_a_avg = np.mean(csi_amp_1_a)
    csi_amp_1_b_avg = np.mean(csi_amp_1_b)
    csi_amp_2_a_avg = np.mean(csi_amp_2_a)
    csi_amp_2_b_avg = np.mean(csi_amp_2_b)

    data.csi_amp_a_avg = csi_amp_a_avg
    data.csi_amp_b_avg = csi_amp_b_avg

    csi_amp_a_list.append(csi_amp_a_avg)
    csi_amp_b_list.append(csi_amp_b_avg)

    csi_amp_1_a_list.append(csi_amp_1_a_avg)
    csi_amp_1_b_list.append(csi_amp_1_b_avg)
    csi_amp_2_a_list.append(csi_amp_2_a_avg)
    csi_amp_2_b_list.append(csi_amp_2_b_avg)

    csi_amp_2_a_var_list.append(np.var(csi_amp_2_a))

    rssi.append(data.rssi)
    time.append(data.timestamp_low - time_start)

n = range(len(file_data))
# plt.plot(n, csi_amp_a_list, n, csi_amp_b_list, n, csi_amp_c_list, n, rssi)
# plt.plot(n, filters.gaussian_filter(csi_amp_a_list, 2), n, filters.gaussian_filter(csi_amp_b_list, 2))
# plt.plot(n, csi_amp_1_a_list, n, csi_amp_1_b_list, n, csi_amp_2_a_list, n, csi_amp_2_b_list)
# plt.show()


plt.subplot(221)
plt.plot(n, filters.gaussian_filter(csi_amp_1_a_list, 2))
# plt.xlabel("Data package index")
plt.ylabel("Amplitude/dB")
plt.title("Link 1")
plt.ylim(10, 25)
plt.subplot(222)
plt.plot(n, filters.gaussian_filter(csi_amp_1_b_list, 2))
# plt.xlabel("Data package index")
# plt.ylabel("Amplitude/dB")
plt.title("Link 2")
plt.ylim(10, 25)
plt.subplot(223)
plt.plot(n, filters.gaussian_filter(csi_amp_2_a_list, 2))
plt.xlabel("Data package index")
plt.ylabel("Amplitude/dB")
plt.title("Link 3")
plt.ylim(10, 25)
plt.subplot(224)
plt.plot(n, filters.gaussian_filter(csi_amp_2_b_list, 2))
plt.xlabel("Data package index")
# plt.ylabel("Amplitude/dB")
plt.title("Link 4")
plt.ylim(10, 25)
plt.show()

# plt.subplot(221)
# plt.plot(n, csi_amp_1_a_list)
# plt.ylim(5, 25)
# plt.subplot(222)
# plt.plot(n, csi_amp_1_b_list)
# plt.ylim(5, 25)
# plt.subplot(223)
# plt.plot(n, csi_amp_2_a_list)
# plt.ylim(5, 25)
# plt.subplot(224)
# plt.plot(n, csi_amp_2_b_list)
# plt.ylim(5, 25)
# plt.show()

# plt.subplot(235)
# plt.plot(n, rssi)

# plt.plot(n, filters.gaussian_filter(csi_amp_2_a_var_list, 2))
# plt.show()


# 使用滑动窗口 均值作为特征值来检测入侵行为
# length = len(file_data)
# window = 5
# csi_amp_1_a_list = filters.gaussian_filter(csi_amp_1_a_list, 1)
# csi_amp_1_b_list = filters.gaussian_filter(csi_amp_1_b_list, 1)
# csi_amp_2_a_list = filters.gaussian_filter(csi_amp_2_a_list, 1)
# csi_amp_2_b_list = filters.gaussian_filter(csi_amp_2_b_list, 1)
# cal_std.print_std(window, length, csi_amp_1_a_list, csi_amp_1_b_list, csi_amp_2_a_list, csi_amp_2_b_list)