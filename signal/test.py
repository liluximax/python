#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import numpy as np

def getAbs(param):
    result = []
    for i in range(0, len(param)):
        result.append((int)(abs(param[i])))
    return result


def getConj(param):
    result = []
    for i in range(0, len(param)):
        result.append(param[i].conjugate())
    return result


def increase(a, num):
    b = []
    for i in range(num):
        for j in range(len(a)):
            b.append(a[j])
    return b


def print_every16(l):
    for i in range(len(l)):
        if i % 16 == 0:
            end = i + 16
            if end >= len(l):
                print (l[i:len(l)])
            else:
                print (l[i:end])


def change10To2(num):
    ms = []
    temp = abs(num) * 2
    count = 0
    while temp < 0.99 or temp > 1.0:
        count += 1
        if count > 8:
            break
        if temp > 1:
            ms.append(1)
            temp = (temp - 1) * 2
        else:
            ms.append(0)
            temp *= 2
    ms.append(1)

    if num >= 0:
        ms[0] = 0
    else:
        ms[0] = 1

    length = len(ms)
    while length < 8:
        ms.append(0)
        length += 1

    return ms[0:8]


def change2To10(l=[]):
    result = 0
    for i in range(0, 7):
        result += (l.pop() * math.pow(2, i))
    if l.pop() == 1:
        result = -result
    return result


def quantization(num):
    ms = change10To2(num)
    result = change2To10(ms)
    return result


def quanti_time_domain(l=[]):
    res = []
    for i in range(0, len(l)):
        real = l[i].real
        imag = l[i].imag
        res.append(complex(quantization(real), quantization(imag)))
    return res


lts = [0, 0, 0, 0, 0, 0, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 0, 1, -1,
       -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

sts = [0, 0, 0, 0, 0, 0, 0, 0, complex(1, 1), 0, 0, 0, complex(-1, -1), 0, 0, 0, complex(1, 1), 0, 0, 0,
       complex(-1, -1), 0, 0, 0,
       complex(-1, -1), 0, 0, 0, complex(1, 1), 0, 0, 0, 0, 0, 0, 0, complex(-1, -1), 0, 0, 0,
       complex(-1, -1), 0, 0, 0, complex(1, 1), 0, 0, 0, complex(1, 1), 0, 0, 0, complex(1, 1), 0, 0, 0,
       complex(1, 1), 0, 0, 0, 0, 0, 0, 0]

# 短训练序列生成
sts = math.sqrt(13. / 6.) * np.asarray(sts)
sts_shift = np.fft.fftshift(sts)
sts_ifft = np.fft.ifft(sts_shift)
sts_time_domain = sts_ifft[0:16]

lts_shift = np.fft.fftshift(lts)
lts_ifft = np.fft.ifft(lts_shift)
lts_time_domain = lts_ifft
