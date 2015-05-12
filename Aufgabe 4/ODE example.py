import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def abl(y, t, C, A):
    return np.array([y[1], C * np.sin(y[0] + A)])

c = 1.0
a = 2.0
y0 = np.array([1.0, 0.9])
zeiten = np.linspace(0.0, 20.0, 200)
y_t = odeint(abl, y0, zeiten, args=(c, a))
phi_t =  y_t[:, 0]
v_t = y_t[:, 1]

plt.figure()
plt.subplot(111)
plt.plot(phi_t, v_t, ms=1, ls="-")
plt.show()