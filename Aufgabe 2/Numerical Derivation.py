from __future__ import division
__author__ = 'Sebastian'

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.arctan(x**2)


def fprime(x):
    return 2*x/(x**4 + 1)


class Function(object):
    def __init__(self, function):
        self.defn = function

    def forward(self, x_0, h):
        return (self.defn(x_0 + h) - self.defn(x_0))/h

    def central(self, x_0, h):
        return (self.defn(x_0 + h/2) - self.defn(x_0 - h/2))/h

    def extrapolate(self, x_0, h):
        return (8 * (self.defn(x_0 + h/4) - self.defn(x_0 - h/4)) -
               (self.defn(x_0 + h/2) - self.defn(x_0 - h/2)))/(3 * h)


F = Function(f)

h_list = 10**(np.linspace(-10.0, 0.0, 1001))
error_forward = []
error_central = []
error_extrapolate = []

for z in h_list:
    error_forward.append(abs((fprime(1/3) - F.forward(1/3, z))/fprime(1/3)))
    error_central.append(abs((fprime(1/3) - F.central(1/3, z))/fprime(1/3)))
    error_extrapolate.append(abs((fprime(1/3) - F.extrapolate(1/3, z))/fprime(1/3)))

plt.subplot(111, yscale='log', xscale='log')
plt.plot(h_list, error_forward, 'r')
plt.plot(h_list, abs(fprime(1/3) - F.forward(1/3, h_list[-1])) * h_list, 'r--')
plt.plot(h_list, error_central, 'g')
plt.plot(h_list, abs(fprime(1/3) - F.central(1/3, h_list[-1])) * h_list**2, 'g--')
plt.plot(h_list, error_extrapolate, 'b')
plt.plot(h_list, abs(fprime(1/3) - F.extrapolate(1/3, h_list[-1])) * h_list**4, 'b--')
plt.show()
