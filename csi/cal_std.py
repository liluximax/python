#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def cal_amp_std_window(window, n, l):
    res = []
    start = 0
    for i in range(1, n + 1):
        if i % window == 0:
            end = i
            csi_avg = np.mean(l[start:end])
            csi_std = np.var(l[start:end])
            ratio = csi_std / csi_avg
            res.append(ratio)
            start = i
    return res

def print_std(window, n, a_1, b_1, a_2, b_2):
    length = len(cal_amp_std_window(window, n, a_1))
    plt.subplot(221)
    plt.plot(range(length), cal_amp_std_window(window, n, a_1))
    plt.ylim(-0.05, 1)
    plt.subplot(222)
    plt.plot(range(length), cal_amp_std_window(window, n, b_1))
    plt.ylim(-0.05, 1)
    plt.subplot(223)
    plt.plot(range(length), cal_amp_std_window(window, n, a_2))
    plt.ylim(-0.05, 1)
    plt.subplot(224)
    plt.plot(range(length), cal_amp_std_window(window, n, b_2))
    plt.ylim(-0.05, 1)
    plt.show()

