from __future__ import division
__author__ = 'Sebastian'

import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return x**3

def Fprime(x):
    return 2*x


class Function(object):
    def __init__(self, function):
        self.defn = function

    def forward(self, x_0, h):
        return (self.defn(x_0 + h) - self.defn(x_0))/h

    def central(self, x_0, h):
        return (self.defn(x_0 + h/2) - self.defn(x_0 - h/2))/h

    def extrapolate(self, x_0, h):
        return (8 * (self.defn(x_0 + h/4) - self.defn(x_0 - h/4)) -\
               (self.defn(x_0 + h/2) - self.defn(x_0 - h/2)))/(3 * h)


f = Function(F)

p = np.linspace(-10, 0, 1000)
h_list = 10**p

error_forward = []
error_central = []
error_extrapolate = []


for z in h_list:
    error_forward.append(abs(Fprime(z) - f.forward(1/3,z))/Fprime(z))

plt.plot(h_list, error_forward, c='k')
plt.subplot(111, xscale="log", yscale="log")

plt.show()

