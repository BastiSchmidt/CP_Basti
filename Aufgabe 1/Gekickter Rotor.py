from __future__ import division
__author__ = 'Sebastian'

from numpy import *
import matplotlib.pyplot as plt


K = 6.0


class PSS(object):  # for Phase Space State
    def __init__(self, theta_0, p_0):
        self.theta = [theta_0 % (2*pi)]
        self.p = [(p_0 + pi) % (2*pi) - pi]

    def evolve(self):
        self.theta.append((self.theta[-1] + self.p[-1]) % (2 * pi))
        self.p.append((self.p[-1] + K * sin(self.theta[-1])+pi) % (2*pi) - pi)


def mouse_click(event):
    start = PSS(event.xdata, event.ydata)
    for i in range(1, 1000):
        start.evolve()
    plt.plot(start.theta, start.p, '.')
    plt.draw()


fig1 = plt.figure(0)
plt.subplot(111, aspect=1.0)  #fester quadratischer Plotbereich
plt.xlim(0, 2*pi)
plt.ylim(-pi, pi)
plt.title('gekickter Rotor')
plt.xlabel('Theta')
plt.ylabel('p')

plt.connect('button_press_event', mouse_click)  #verbindet Mausklick mit Fkt
plt.show()


"""
Textgelaber
"""
