from __future__ import division
__author__ = 'Basti'

import numpy as np
import matplotlib.pyplot as plt

K = 2.6


class PSS(object):  # for Phase Space State
    def __init__(self, theta_0, p_0):
        self.theta[0] = theta_0
        self.p[0] = p_0

    def evolve(self):
        self.theta[len(self.theta)] = (self.theta[len(self.theta) - 1] +\
          self.p[len(self.p) - 1]) % (2 * np.pi)
        self.p[len(self.p)] = (self.p[len(self.p) - 1] + K *\
          np.sin(self.theta[len(self.theta) - 1]) + np.pi) % (2*np.pi) - np.pi


"""
def create_phase_space_diagram(theta_0, p_0):
    i = 0,

    while i < 1000 :


def mouse_click(event):
    create_phase_space_diagram(event.x, event.y)
"""


#Main
Start = PSS(1, 2)
print len(Start.theta)