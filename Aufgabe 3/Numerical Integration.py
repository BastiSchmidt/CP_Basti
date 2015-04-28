from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return x


def F1(x):
    return 1/2 * x**2


class Function(object):
    def __init__(self, function):
        self.defn = function

    def middle(self, a, b, n):
        width = (a - b)/n
        x_i = np.linspace(a, b, n, endpoint=False)
        f_i = self.defn(x_i + width/2)
        return sum(f_i)*width

    def trapez(self, a, b, n):
        width = (a - b)/n
        return

    def simpson(self, a, b, n):
        return n


Int1 = Function(f1)

print np.linspace(0, 10, 10)
print np.linspace(0, 10, 10, endpoint=False)
print np.linspace(0, 10, 11)