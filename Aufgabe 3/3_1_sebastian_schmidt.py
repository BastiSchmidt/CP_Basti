"""
Aufgabe 2.1

Dieses Programm dient dem Kennenlernen elementarer numerischer Integrations-
methoden: der Mittelpunktsmethode, der Trapezmethode und der Simpson-Methode.
Zudem sollen die numerischen Fehler ebenjener Methoden in Abhaengigkeit von der
Intervallbreite der Integration dargestellt werden.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def fa(x):
    """
    Gegebene Funktion aus Aufgabenstellung a)
    """
    return np.sin(2*x)
# Analytische Loesung des bestimmten Integrals aus a)
Inta = -0.25


def fb(x):
    """
    Gegebene Funktion aus Aufgabenstellung b)
    """
    return np.exp(-100 * x**2)
# Genaeherte Loesung des bestimmten Integrals aus b)
Intb = 0.177245


def fc(x):
    """
    Gegebene Funktion aus Aufgabenstellung c)
    """
    return (1.0 + np.sign(x))/2
# Analytische Loesung des bestimmten Integrals aus c)
Intc = np.pi/3


def middle(func, a, b, n):
    """
    Berechnet numerisch mittels der Mittelwertmethode das bestimmte Integral
    der Funktion func von a bis b mit der Intervallanzahl n
    """
    width = float((b - a)/n)                    # Intervallbreite
    x_i = np.linspace(a, b, n, endpoint=False)  # Erzeugung eines Arrays linker
    f_i = func(x_i + width/2)                   # Grenzen, Funktionswerte
    return sum(f_i) * width                     # werden in der Mitte genommen


def trapez(func, a, b, n):
    """
    Berechnet numerisch mittels der Trapezmethode das bestimmte Integral
    der Funktion func von a bis b mit der Intervallanzahl n
    """
    width = float(b - a)/n
    x_i = np.linspace(a, b, n + 1)              # Erzeugung eines Arrays linker
    f_i = (func(x_i[:-1]) + func(x_i[1:]))/2    # und rechter Grenzen, Fktwerte
    return sum(f_i) * width                     # zwischen beiden gemittelt


def simpson(func, a, b, n):
    """
    Berechnet numerisch mittels der Simpson-Methode das bestimmte Integral
    der Funktion func von a bis b mit der Intervallanzahl n
    """
    width = float(b - a)/(2*n)                  # halbe Breite
    x = np.linspace(a, b, 2*n + 1)              # Fktwerte wie Trapezmethode,
    f_i = (func(x[:-1]) + func(x[1:]))/2        # einmal halbe und ganze Breite
    f_j = (func(x[:-2:2]) + func(x[2::2]))/2    # mit entspr. Wichtung
    return 4/3 * sum(f_i) * width - 1/3 * sum(f_j) * width * 2

# feste obere und untere Integrationsgrenze als Parameter
A = -np.pi/2
B = np.pi/3

# Anzahl der verschiedenen Intervallanzahlen (int32) in logarithmischen Abstand
# allerdings Doppelung durch Rundung, mit np.unique() herausgefiltert
number = 1000
N_list = np.unique(np.int32(np.logspace(0, 5, number)))

# Intervallbreiten aus der Anzahl der Intervalle
h_list = (B - A)/N_list

# Arrays fuer die Betraege der relativen Fehler der drei Methoden
error_middle = np.zeros(len(N_list))
error_trapez = np.zeros(len(N_list))
error_simpson = np.zeros(len(N_list))

# Befuellen der Fehlerlisten innerhalb einer Schleife. Dies ist noetig, da
# innerhalb der Funktionen nicht ohne grossen Aufwand der Typ ndarray in den
# Aufruf von np.linspace() einzubetten ist
for z in range(len(N_list)):
    error_middle[z] = np.absolute((middle(fa, A, B, N_list[z]) - Inta)/Inta)
    error_trapez[z] = np.absolute((trapez(fa, A, B, N_list[z]) - Inta)/Inta)
    error_simpson[z] = np.absolute((simpson(fa, A, B, N_list[z]) - Inta)/Inta)


# Anlegen eines Plotfensters mit logarithmischer Achseneinteilung
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, xscale='log', yscale='log')

# Plotten der Fehler der verschiedenen Methoden als Punktplot
ax.plot(h_list, error_middle, 'g.', ms=2, label='Mittelwertmethode')
ax.plot(h_list, error_trapez, 'r.', ms=2, label='Trapezmethode')
ax.plot(h_list, error_simpson, 'b.', ms=2, label='Simpson-Methode')

# Plotten des Skalierungsverhaltens fuer die Methoden. Damit dadurch nicht der
# Plotbereich verzerrt wird, wird nur eine kuerzere Linie mittels des
# angelegten Arrays x gezeichnet
x = np.logspace(-3, -1, 100)
ax.plot(x, x**2, 'k--', label='Skalierungsverhalten: $h^2$')
ax.plot(x, x**4, 'b--', label='Skalierungsverhalten: $h^4$')

# Anzeigen der Legende an der bestmoeglichen Position
ax.legend(loc='best')
ax.set_xlabel('$h$', fontsize=18)
ax.set_ylabel(r"$\frac{\Delta I}{I}$", fontsize=18)
ax.set_title('Numerische Integration', fontsize=20)

plt.show()