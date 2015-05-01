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
    """
    Zu untersuchende Funktion gegeben in der Aufgabenstellung
    """
    return np.arctan(x**2)


def fprime(x):
    """
    Analytisch errechnete Ableitung der gegebenen Funktion
    """
    return 2*x/(x**4 + 1)


def forward(func, x_0, h):
    """
    Diese Funktion berechnet mittels Vorwartsdifferenzenmethode die numerisch
    genaeherte Ableitung der uebergebenen Funktion an der Stelle x_0 mit der
    Intervallbreite h
    """
    return (func(x_0 + h) - func(x_0))/h


def central(func, x_0, h):
    """
    Diese Funktion berechnet mittels Zentraldifferenzenmethode die numerisch
    genaeherte Ableitung der uebergebenen Funktion an der Stelle x_0 mit der
    Intervallbreite h
    """
    return (func(x_0 + h/2) - func(x_0 - h/2))/h


def extrapolate(func, x_0, h):
    """
    Diese Funktion berechnet mittels der extrapolierten Differenzenmethode
    die numerisch genaeherte Ableitung der uebergebenen Funktion an der Stelle
    x_0 mit der Intervallbreite h
    """
    return (8 * (func(x_0 + h/4) - func(x_0 - h/4)) -
            (func(x_0 + h/2) - func(x_0 - h/2)))/(3 * h)


h_list = 10**(np.linspace(-10.0, 0.0, 1001))
    # Anlegen eines arrrays von 1^(-10) bis 1 in gleichmaessig logarithmischen
    # Intervallen

error_forward = []
error_central = []
error_extrapolate = []
    # Anlegen der leeren Listen fuer die Fehler der DIfferentiationsverfahren
    # ion Abhaengigkeit der Intervallbreite h

for z in h_list:
    error_forward.append(abs((fprime(1/3) - forward(f, 1/3, z))/fprime(1/3)))
    error_central.append(abs((fprime(1/3) - central(f, 1/3, z))/fprime(1/3)))
    error_extrapolate.append(abs((fprime(1/3) - extrapolate(f, 1/3, z))\
                                 /fprime(1/3)))
    # Befuellen der Fehlerlisten mit dem Betrag des relativen Fehlers der
    # numerischen Methode zum analytisch exakten Ergebnis an der Stelle 1/3

print __doc__

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, yscale='log', xscale='log')
    # Anlegen eines Plotfensters mit logarithmischer Acheneinteilung

ax.plot(h_list, error_forward, 'r', label='Vorwaertsdifferenz')
ax.plot(h_list, abs(fprime(1/3) - forward(f, 1/3, h_list[-1])) * h_list,\
        'r--', label='erwartetes Verhalten: $O(h)$')
    # Plotten des Fehlers der Vorwaertsmethode und des erwarteten Verhaltens.
    # Fuer letzteres muss, damit der Achsenabschnitt passend auf dem des
    # relativen Fehlers liegt, noch mit dem letzten absoluten Fehler aus der
    # Liste multipliziert werden

ax.plot(h_list, error_central, 'g', label='Zentraldifferenz')
ax.plot(h_list, abs(fprime(1/3) - central(f, 1/3, h_list[-1])) * h_list**2,\
        'g--', label='erwartetes Verhalten: $O(h^2)$')
    # Plotten des Fehlers der Zentralmethode und des erwarteten Verhaltens.
    # Anpassen des Achsenabschnitts wie oben.

ax.plot(h_list, error_extrapolate, 'b', label='Extrapolierte Differenz')
ax.plot(h_list, abs(fprime(1/3) - extrapolate(f, 1/3, h_list[-1])) * h_list**4,\
        'b--', label='erwartetes Verhalten: $O(h^4)$')
    # Plotten des Fehlers der extrapolierten Differenzenmethode und des
    # erwarteten Verhaltens.
    # Anpassen des Achsenabschnitts wie oben.

ax.set_xlabel(r'$h$')
ax.set_ylabel('relativer Fehler')
ax.legend(loc=4)

plt.show()
