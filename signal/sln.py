#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import numpy as np

# 短训练序列频域标准值
# 注意初始位置从0开始 一个64个点
sts = [0, 0, 0, 0, 0, 0, 0, 0, complex(1, 1), 0, 0, 0, complex(-1, -1), 0, 0, 0, complex(1, 1), 0, 0, 0,
       complex(-1, -1), 0, 0, 0,
       complex(-1, -1), 0, 0, 0, complex(1, 1), 0, 0, 0, 0, 0, 0, 0, complex(-1, -1), 0, 0, 0,
       complex(-1, -1), 0, 0, 0, complex(1, 1), 0, 0, 0, complex(1, 1), 0, 0, 0, complex(1, 1), 0, 0, 0,
       complex(1, 1), 0, 0, 0, 0, 0, 0, 0]

# 长训练序列频域标准值
# 注意初始位置从0开始 一个64个点
lts = [0, 0, 0, 0, 0, 0, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 0, 1, -1,
       -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# 量化信号为1 -1
def getsmallsln(x):
    result = []
    for i in range(0, len(x)):
        real = x[i].real
        imag = x[i].imag
        temp = 0
        if real >= 0 and imag >= 0:
            temp = complex(1, 1)
        elif real >= 0 and imag < 0:
            temp = complex(1, -1)
        elif real < 0 and imag >= 0:
            temp = complex(-1, 1)
        elif real < 0 and imag < 0:
            temp = complex(-1, -1)
        result.append(temp)
    return result

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
# 将ifft小数计算结果量化为2进制,再转化为10进制
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

def getabs(x):
    result = []
    for i in range(0, len(x)):
        result.append(int(abs(x[i])))
    return result

def getconj(x):
    result = []
    for i in range(0, len(x)):
        result.append(x[i].conjugate())
    return result
# 扩容函数
def increase(a, num):
    b = []
    for i in range(num):
        for j in range(len(a)):
            b.append(a[j])
    return b
# 每16个点取一次
def selectMaxPoint(l):
    return [l[x] for x in range(len(l)) if (x + 1) % 16 == 0]
# 每16个点打印一个\n
def print_every16(l):
    for i in range(len(l)):
        if i % 16 == 0:
            end = i + 16
            if end >= len(l):
                print (l[i:len(l)])
            else:
                print (l[i:end])


sts = math.sqrt(13. / 6.) * np.asarray(sts)
sts_shift = np.fft.fftshift(sts)
sts_ifft = np.fft.ifft(sts_shift)
sts_time_domain = sts_ifft[0:16]
print('短训练序列ifft:')
print(sts_time_domain)
print('\n短训练符号量化为10进制:')
sts_time_domain_quanti = quanti_time_domain(sts_time_domain)
print(sts_time_domain_quanti)
print('\n短训练符号扩容10倍,生成短训练序列:')
sts_final = increase(sts_time_domain_quanti, 10)
print_every16(sts_final)

print('\n长训练序列ifft:')
lts_shift = np.fft.fftshift(lts)
lts_ifft = np.fft.ifft(lts_shift)
lts_time_domain = lts_ifft
print_every16(lts_time_domain)
print('\n长训练符号量化为10进制:')
lts_time_domain_quanti = quanti_time_domain(lts_time_domain)
print_every16(lts_time_domain_quanti)
print('\nG1间隔:')
g1 = lts_time_domain_quanti[32:64]
print_every16(g1)
print('\n长训练符号扩容2倍,生成长训练序列:')
lts_final = increase(lts_time_domain_quanti, 2)
print_every16(lts_final)

print('\n本地存储训练序列')
local_signal = sts_time_domain_quanti
print(local_signal)
print('\n对输入信号进行量化:')
signal = sts_final + g1 + lts_final
input_signal = getsmallsln(signal)
print_every16(input_signal)

print('\n卷积运算:')
cov = np.convolve(input_signal, getconj(local_signal)[::-1])
cov_abs = getabs(cov)
print_every16(cov_abs)
