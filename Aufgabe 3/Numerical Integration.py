from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def fa(x):
    return np.sin(2*x)
Int_a = -0.25


def fb(x):
    return np.exp(-100 * x**2)
Int_b = 0.177245

def fc(x):
    return (1.0 + np.sign(x))/2
Int_c = np.pi/3

def middle(func, a, b, n):
    width = float((b - a)/n)
    x_i = np.linspace(a, b, n, endpoint=False)
    f_i = func(x_i + width/2)
    return sum(f_i) * width


def trapez(func, a, b, n):
    width = float(b - a)/n
    x_i = np.linspace(a, b, n + 1)
    int_i = func(x_i[:-1]) + func(x_i[1:])
    return sum(int_i) * width/2


def simpson(func, a, b, n):
    return 4/3 * trapez(func, a, b, 2*n) - 1/3 * trapez(func, a, b, n)

A = -np.pi/2
B = np.pi/3
number = 1000
N_list = np.int32(np.logspace(0, 5, number))
h_list = (B - A)/N_list
error_middle = np.zeros(number)
error_trapez = np.zeros(number)
error_simpson = np.zeros(number)

for z in range(number):
    error_middle[z] = abs((middle(fa, A, B, N_list[z]) - Int_a) / Int_a)
    error_trapez[z] = abs((trapez(fa, A, B, N_list[z]) - Int_a) / Int_a)
    error_simpson[z] = abs((simpson(fa, A, B, N_list[z]) - Int_a) / Int_a)


fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, xscale='log', yscale='log')
ax.plot(h_list, error_middle, 'g.', label='Mittelwertmethode')
ax.plot(h_list, error_trapez, 'b.', label='Trapezmethode')
ax.plot(h_list, error_simpson, 'r.', label='Simpson-Methode')
plt.legend(loc='best')
plt.show()
