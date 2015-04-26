from __future__ import division
__author__ = 'Basti'


import numpy as np
import matplotlib.pyplot as plt


"""
Umrechnung von Polar- in kartesische Koordinaten:
    x = r * cos(phi)
    y = r * sin(phi)
"""

t = np.linspace(0.0, 5.0, 500)


def build_plot(x_0, y_0):
    """
    Diese Funktion erzeugt aus den gegebenen Anfangskoordinaten die Punkte der
    Spirale,  welche sich von dort aus bilden soll
    """
    x_new = 0.5**t * np.cos(2*np.pi*t) + x_0
    y_new = 0.5**t * np.sin(2*np.pi*t) + y_0
    return x_new, y_new


def mouse_click(event):
    """
    wird aufgerufen wenn auf den Plotbereich geklickt wird und zeichnet die
    dort entstehende Spirale
    """
    x, y = build_plot(event.xdata, event.ydata)
    plt.plot(x, y)
    plt.draw()

fig1 = plt.figure(0)
plt.subplot(111, aspect=1.0)  #fester quadratischer Plotbereich
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.title('Spirale')
plt.xlabel('x')
plt.ylabel('y')

plt.connect('button_press_event', mouse_click)  #verbindet Mausklick mit Fkt
plt.show()