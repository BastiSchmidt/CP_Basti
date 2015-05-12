from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def odesys(phi, t, a, b, om):
    """
    phi ist Phasenraumvektor [x, p]
    """
    return np.array([phi[1], -4*phi[0]**3 + 2*phi[0] - (a + b*np.sin(om*t))])


def onclick(event):
    if event.button == 1 and event.inaxes:
        if fig.canvas.toolbar.mode == '':
            phi_0 = np.array([event.xdata, event.ydata])
            phi_t = odeint(odesys, phi_0, times, args=(A, B, omega))
            x_t = phi_t[:, 0]
            p_t = phi_t[:, 1]
            ax_p.plot(x_t, p_t, '.', ms=3)
            ax_s.plot(x_t[::steps], p_t[::steps], '.', ms=3)
            plt.draw()
    else:
        print "Bitte klicken Sie links auf einen der beiden Plotbereiche"

A = 0.1
B = 0.1
omega = 1
rotations = 200
steps = 10

times = np.linspace(0, 2 * np.pi * rotations, steps * rotations)

fig = plt.figure()

ax_p = fig.add_subplot(121)
ax_p.set_title('Phasenraum')
ax_p.set_xlim(-1.5, 1.5)
ax_p.set_ylim(-2, 2)
ax_p.set_xlabel('$x$')
ax_p.set_ylabel('$p$')

ax_s = fig.add_subplot(122)
ax_s.set_title('Stroboskopische Darstellung')
ax_s.set_xlim(-1.5, 1.5)
ax_s.set_ylim(-2, 2)
ax_s.set_xlabel('$x$')
ax_s.set_ylabel('$p$')

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
