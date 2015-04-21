"""
Exercise 1.1, Sebastian Schmidt

This program illustrates phase space paths of a kicked rotor. You can set
different starting conditions for the rotor in order to generate and study
different regions of the phase space.
In order to start click left on the plotting area.
"""

from __future__ import division
from numpy import *
import matplotlib.pyplot as plt


class PSS(object):                                 # for Phase Space State

    """
    This class contains information about the Phase State of the rotor. Also it
    includes a method to generate the next state from the latest state
    information using the given formulas.
    """

    def __init__(self, theta_0, p_0, k=2.6):
        self.theta = [theta_0 % (2*pi)]            # list of theta values
        self.p = [(p_0 + pi) % (2*pi) - pi]        # list of p values
        self.K = k

    def evolve(self):
        self.theta.append((self.theta[-1] + self.p[-1]) % (2 * pi))
        self.p.append((self.p[-1] + self.K * sin(self.theta[-1])+pi)%(2*pi)-pi)


def onclick(event):

    """
    This function creates a PSS class, initializes it with the xdata- and
    ydata-values of the lift-click-event and plots the next 1000 Phase Space
    States using the PSS.evolve function. It also filters out wrong user input
    and handles the case of zooming into the picture.
    """

    # Check first, if the user left-clicked on the plotting area and then if he
    # is not in zooming mode

    if event.inaxes and event.button == 1:
        if plt.get_current_fig_manager().toolbar.mode == '':
            start = PSS(event.xdata, event.ydata)  # initializing PSS class
            for i in range(1, 1000):               # with clicked on coords,
                start.evolve()                     # creating the next 1000
            ax.plot(start.theta, start.p, '.')     # Phase Space States and
            plt.draw()                             # plotting them
    else:
        print "Please click left on the Plotting Area."

print __doc__

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect(1.0)
ax.set_xlim(0, 2*pi)
ax.set_ylim(-pi, pi)
ax.set_title('Kicked Rotor')
ax.set_xlabel(r'$\theta$')
ax.set_ylabel('$p$')
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()                                        


"""
Textgelaber
"""