"""
Aufgabe 2.1

Dieses Programm dient dem Kennenlernen elementarer numerischer
Differentiationsmethoden und dem Illustrieren der Fehlerquellen ebenjener
Methoden in Abhaengigkeit vom Differentiationsparameter h.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.arctan(x**2)


def fprime(x):
    return 2*x/(x**4 + 1)


def forward(func, x_0, h):
    return (func(x_0 + h) - func(x_0))/h


def central(func, x_0, h):
    return (func(x_0 + h/2) - func(x_0 - h/2))/h


def extrapolate(func, x_0, h):
    return (8 * (func(x_0 + h/4) - func(x_0 - h/4)) -
            (func(x_0 + h/2) - func(x_0 - h/2)))/(3 * h)


h_list = 10**(np.linspace(-10.0, 0.0, 1001))
error_forward = []
error_central = []
error_extrapolate = []

for z in h_list:
    error_forward.append(abs((fprime(1/3) - forward(f, 1/3, z))/fprime(1/3)))
    error_central.append(abs((fprime(1/3) - central(f, 1/3, z))/fprime(1/3)))
    error_extrapolate.append(abs((fprime(1/3) - extrapolate(f, 1/3, z))/fprime(1/3)))

print __doc__

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, yscale='log', xscale='log')
ax.plot(h_list, error_forward, 'r', label='Vorwaertsdifferenz')
ax.plot(h_list, abs(fprime(1/3) - forward(f, 1/3, h_list[-1])) * h_list, 'r--', label='erwartetes Verhalten: $O(h)$')
ax.plot(h_list, error_central, 'g', label='Zentraldifferenz')
ax.plot(h_list, abs(fprime(1/3) - central(f, 1/3, h_list[-1])) * h_list**2, 'g--', label='erwartetes Verhalten: $O(h^2)$')
ax.plot(h_list, error_extrapolate, 'b', label='Extrapolierte Differenz')
ax.plot(h_list, abs(fprime(1/3) - extrapolate(f, 1/3, h_list[-1])) * h_list**4, 'b--', label='erwartetes Verhalten: $O(h^4)$')
ax.set_xlabel(r'$h$')
ax.set_ylabel('relativer Fehler')
ax.legend(loc='best')
plt.show()
