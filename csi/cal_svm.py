#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
from math import *
import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.ndimage import filters
import copy


class Data(object):
    def __init__(self, timestamp_low, rssi, perm, noise, csi, phase, SNR):
        self.timestamp_low = timestamp_low
        self.rssi = rssi
        self.perm = perm
        self.noise = noise
        self.csi = csi
        self.phase = phase
        self.SNR = SNR


def dict2Data(d):
    return Data(d['timestamp_low'], d['rssi'], d['perm'], d['noise'], d['csi'], d['phase'], d['SNR'])


file_data = []

with open('/Users/luc/Desktop/csi/test_new.json', 'r') as f:
    for line in f.readlines():
        file_data.append(json.loads(line, object_hook=dict2Data))


def preprocessingPhase(phases, tphases):
    index = range(-28, 0, 2) + [-1, 1] + range(3, 28, 2) + [28]
    for l in range(10):
        clear = True
        base = 0
        tphases[0] = phases[0]

        for i in range(1, 30):
            if phases[i] - phases[i - 1] > pi:
                base += 1
                clear = False
            elif phases[i] - phases[i - 1] < -pi:
                base -= 1
                clear = False
            tphases[i] = phases[i] - 2 * pi * base

        if clear == True:
            break
        else:
            for i in range(30):
                phases[i] = tphases[i] - (tphases[29] - tphases[0]) * 1.0 / (28 - (-28)) * (
                    index[i]) - 1.0 / 30 * sum([tphases[j] for j in range(30)])
    return phases

rssi = []
csi_list = []
time_start = file_data[0].timestamp_low
time = []

# 滑动窗口取静态标准值
def get_normal_eigen(channel):
    point_start = 10
    point_end = 50
    csi_amp_normal = [0 for i in range(30)]
    csi_phase_normal = [0 for i in range(30)]
    for point in range(point_start, point_end + 1):
        csi_amp, csi_phase = __get_normal_eigen(channel, point)
        for index in range(30):
            csi_amp_normal[index] += csi_amp[index]
            csi_phase_normal[index] += csi_phase[index]
    for i in range(30):
        csi_amp_normal[i] /= (point_end - point_start + 1)
        csi_phase_normal[i] /= (point_end - point_start + 1)

    csi_amp_normal = get_normal_amp(csi_amp_normal)
    return csi_amp_normal, csi_phase_normal

# 取标准特征值,暂时取第20个采样点
def __get_normal_eigen(channel, point):
    data = file_data[point]
    csi_point = data.csi
    csi_point_phase = data.phase
    amp_normal = []
    phase = []
    tphase = list(range(30))

    perm = data.perm
    rx_atenna_combine = ['a', 'b']
    rx_atenna = rx_atenna_combine[(channel - 1) % 2]
    tx_atenna = 0
    if channel == 3 or channel == 4:
        tx_atenna = 1
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
        csi_phase_bit = csi_point_phase[i]
        amp_normal.append(csi_bit[tx_atenna][hash[rx_atenna]])
        phase.append(csi_phase_bit[tx_atenna][hash[rx_atenna]])

    phase_normal = preprocessingPhase(phase, tphase)
    return amp_normal, phase_normal

# 协方差取最大值作为特征值
def get_max_eigen(cov):
    temp = [];
    temp.append(cov[0][0])
    temp.append(cov[0][1])
    temp.append(cov[1][0])
    temp.append(cov[1][1])
    temp.sort()
    return temp[3]

def get_top2_eigen(cov):
    temp = [];
    temp.append(cov[0][0])
    temp.append(cov[0][1])
    temp.append(cov[1][0])
    temp.append(cov[1][1])
    temp.sort()
    return temp[3], temp[2]

def do_amp_by_mean(amp):
    amp_mean = np.mean(amp)
    res = list(range(30))
    for i in range(30):
        res[i] = amp[i] / 30
    return res

def get_normal_amp(amp):
    amp_copy = copy.copy(amp)
    amp_copy.sort()
    max = amp_copy[29]
    min = amp_copy[0]
    amp_normal = [0 for i in range(30)]
    for i in range(30):
        gap = max - min
        if gap == 0:
            gap = -1
        amp_normal[i] = (amp[i] - min) / float(gap)
    return amp_normal

def plot_carrier(channel, start, end):
    x_list = []
    y_list = []

    amp_normal, phase_normal = get_normal_eigen(channel)
    csi_amp_list = []
    rx_atenna_combine = ['a', 'b']
    rx_atenna = rx_atenna_combine[(channel - 1) % 2]
    tx_atenna = 0
    if channel == 3 or channel == 4:
        tx_atenna = 1
    print (tx_atenna)
    n_30 = range(1,31)
    n_12 = range(12)
    for data in file_data[start:end]:
        csi_point = data.csi
        csi_point_phase = data.phase
        snr = data.SNR
        # 第i个采样点中30个幅值的集合
        csi_amp_carrier = []
        # 第i个采样点中30个相位的集合
        csi_phase_carrier = []
        tphases = []

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
            csi_phase_bit = csi_point_phase[i]
            if len(csi_bit) != 2:
                csi_amp_carrier.append(0)
                csi_phase_carrier.append(0)
                tphases.append(0)
            else:
                csi_amp_carrier.append(csi_bit[tx_atenna][hash[rx_atenna]])
                csi_phase_carrier.append(csi_phase_bit[tx_atenna][hash[rx_atenna]])
                tphases.append(0)

        # plt.plot(n_30, csi_phase_carrier)
        phases = preprocessingPhase(csi_phase_carrier, tphases)

        csi_amp_delata = get_normal_amp(csi_amp_carrier)
        amp_cov = np.cov(csi_amp_delata, amp_normal)
        phase_cov = np.cov(phases, phase_normal)

        x_list.append(get_max_eigen(amp_cov))
        # x_list.append(np.mean(csi_amp_delata))
        y_list.append(get_max_eigen(phase_cov))
        # y_list.append(np.mean(csi_phase_carrier))
        csi_amp_list.append(np.mean(csi_amp_carrier))

        # if flag == 1:
        #     plt.plot(n_30, csi_amp_carrier)
        # if flag == 2:
        #     plt.plot(n_30, phases)

        # plt.plot(n_12, snr)
        # plt.plot(n_30, amp_cov)
        csi_list.append(np.mean(phases))
    return x_list, y_list


# 选取特征值,在整个时域中查看特征值变化
# start = 0
# end = 900
# channel = 1
# x, y = plot_carrier(channel, start, end)
# plt.subplot(211)
# x = filters.gaussian_filter(x, 1)
# xa, xd = pywt.dwt(x, 'db2')
# plt.plot(range(len(xa)), xa)
# plt.title(channel)
# plt.grid(True)
# # plt.plot(range(len(x)), x)
# plt.subplot(212)
# plt.plot(range(len(y)), y, 'r')
# ya, yd = pywt.dwt(y, 'coif2')
# plt.plot(range(len(ya)), ya)
# plt.plot(range(len(yd)), yd)
# plt.title(channel)
# plt.grid(True)
# plt.show()

start = 0
end = 900
x, y = plot_carrier(4, start, end)
ya, yd = pywt.dwt(y, 'coif2')
for i in ya:
    print i
    print ","
plt.plot(range(len(ya)), ya)

plt.show()


# 剔除bad stream
# start = 0
# end = len(file_data)
# plot_carrier(3, start, end)
# plt.plot(range(end), csi_list)
# plt.show()

# 绘制30个子载波分布代码
# start = 450
# end = 550
# plt.subplot(221)
# plot_carrier(1, start, end)
# plt.ylim(0, 40)
# plt.subplot(222)
# plot_carrier(2, start, end)
# plt.ylim(0, 40)
# plt.subplot(223)
# plot_carrier(3, start, end)
# plt.ylim(0, 40)
# plt.subplot(224)
# plot_carrier(4, start, end)
# plt.ylim(0, 40)
# plt.show()

# 绘制经过线性变换前后相位对比代码
# start = 700
# end = 800
# plt.figure(1)
# plt.subplot(211)
# plt.xlabel("Subcarrier index")
# plt.ylabel("Phase [random]")
# plot_carrier(1, start, end, 1)
# plt.subplot(212)
# plt.xlabel("Subcarrier index")
# plt.ylabel("Phase [processed]")
# plot_carrier(1, start, end, 2)
# plt.ylim(-3, 3)

# 绘制相位 静态与入侵场景的对比
# start = 750
# end = 800
# plt.subplot(221)
# plot_carrier(1, start, end, 2)
# plt.title("Static Stage")
# plt.ylabel("Phase [processed]")
# plt.ylim(-3, 3)
#
# start = 450
# end = 550
# plt.subplot(222)
# plot_carrier(1, start, end, 2)
# plt.title("Intrusion Stage")
# plt.ylabel("Phase [processed]")
# plt.ylim(-3, 3)
#
# start = 20
# end = 70
# plt.subplot(223)
# plt.title("Static Stage")
# plot_carrier(1, start, end, 1)
# plt.xlabel("Subcarrier index")
# plt.ylabel("Amplitude/dB")
# plt.ylim(0, 40)
#
# start = 450
# end = 550
# plt.subplot(224)
# plt.title("Intrusion Stage")
# plot_carrier(2, start, end, 1)
# plt.xlabel("Subcarrier index")
# plt.ylabel("Amplitude/dB")
# plt.ylim(0, 40)
# plt.show()