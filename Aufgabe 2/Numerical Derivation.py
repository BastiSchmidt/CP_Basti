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


X_0 = 1/3
    # Zu untersuchender Punkt als Parameter

h_list = 10**(np.linspace(-10.0, 0.0, 1001))
    # Anlegen eines arrrays von 1^(-10) bis 1 in gleichmaessig logarithmischen
    # Intervallen

error_forward = []
error_central = []
error_extrapolate = []
    # Anlegen der leeren Listen fuer die Fehler der DIfferentiationsverfahren
    # ion Abhaengigkeit der Intervallbreite h

for z in h_list:
    error_forward.append(abs((fprime(X_0) - forward(f, X_0, z))/fprime(X_0)))
    error_central.append(abs((fprime(X_0) - central(f, X_0, z))/fprime(X_0)))
    error_extrapolate.append(abs((fprime(X_0) - extrapolate(f, X_0, z))\
                                 /fprime(X_0)))
    # Befuellen der Fehlerlisten mit dem Betrag des relativen Fehlers der
    # numerischen Methode zum analytisch exakten Ergebnis an der Stelle 1/3

print __doc__

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, yscale='log', xscale='log')
    # Anlegen eines Plotfensters mit logarithmischer Acheneinteilung

ax.plot(h_list, error_forward, 'r', label='Vorwaertsdifferenz')
ax.plot(h_list, abs(fprime(X_0) - forward(f, X_0, h_list[-1])) * h_list,\
        'r--', label='erwartetes Verhalten: $O(h)$')
    # Plotten des Fehlers der Vorwaertsmethode und des erwarteten Verhaltens.
    # Fuer letzteres muss, damit der Achsenabschnitt passend auf dem des
    # relativen Fehlers liegt, noch mit dem letzten absoluten Fehler aus der
    # Liste multipliziert werden

ax.plot(h_list, error_central, 'g', label='Zentraldifferenz')
ax.plot(h_list, abs(fprime(X_0) - central(f, X_0, h_list[-1])) * h_list**2,\
        'g--', label='erwartetes Verhalten: $O(h^2)$')
    # Plotten des Fehlers der Zentralmethode und des erwarteten Verhaltens.
    # Anpassen des Achsenabschnitts wie oben.

ax.plot(h_list, error_extrapolate, 'b', label='Extrapolierte Differenz')
ax.plot(h_list, abs(fprime(X_0) - extrapolate(f, X_0, h_list[-1])) *\
        h_list**4, 'b--', label='erwartetes Verhalten: $O(h^4)$')
    # Plotten des Fehlers der extrapolierten Differenzenmethode und des
    # erwarteten Verhaltens.
    # Anpassen des Achsenabschnitts wie oben. Die Abhaengigkeit des Fehlers von
    # h als h^4 konnt eich mittels Taylor-Entwicklung pruefen, man haette es
    # aber auch mit einer grafischen Anpassung des Anstieges durch Probieren
    # herausfinden koennen

ax.set_xlabel(r'$h$')
ax.set_ylabel('relativer Fehler')
ax.legend(loc=4)

plt.show()

"""
Beobachtung

Wenn man die Intervallbreite h immer kleiner waehlt wird das Ableitungsergebnis
nur bis zu einem bestimmten Punkt besser, naemlich genau bis zum Gleichgewicht
zwischen Diskretisierungs- und Rundungsfehler. Am Beispiel der Vorwaerts-
differenz ist das ungefaehr bei h = 10^-8 der Fall. Macht man h darueber hinaus
noch kleiner passiert folgendes: Da h als Gleitkommazahl (float) mit 52 nur
eine begrenzte Anzahl von Bits fuer seine Mantisse zur Verfuegung hat, wird bei
allzu grossem Abstand von kleinster und groesster Dezimalstelle das Ende
abgeschnitten. Dadurch kommt es dazu, dass der Fehler durch dieses Abschneiden
groesser wird als der durch die Groesse von h, was auch immer weiter zunimmt,
wenn h kleiner wird. Das gleiche Verhalten ist auch bei den anderen Methoden zu
sehen, durch die geringere Gewichtung von h tritt dies jedoch erst spaeter auf.

Die optimale Wahl fuer h fuer die Vorwaertsmethode liegt daher im Bereich um
10^-8. Der daraus resultierende minimale Fehler liegt dann ebenfalls in dem
Bereich um 1.4*10^-8. Etwas besser ist die Zentraldifferenzenmethode, wo
der kleinste Fehler von 6*10-12 bei einem h um 10^-5 liegt. Als beste unter den
untersuchten Methoden erwies sich Methode der extrapolierten Differenz, welche
ihren kleinsten Fehler von 1.3*10-13 bei einem h von 0.0019 hat.
(Bei allen Methoden gibt es zwar noch geringere Fehler, diese liegen aber schon
im irregulaeren Bereich des ueberwiegenden Rundungsfehlers. Dieser ist aber
unkontrollierbar, da er von der Funktion und der zu untersuchenden Stelle
abhaengt, was man sehen kann, wenn man z.B. X_0 auf 1.0 aendert)

Bei allen Methoden bewegt sich der Rundungsfehler ab einem gewissen Wert fuer
h in dem gleichen 'Kanal', da irgendwann bei der Zahl die Stellen gleich
weit auseinander sind um abgeschnitten zu werden. Dies tritt durch die
Wichtunf bei der extrapolierten Methode frueher ein und bei der Vorwaerts-
methode als letztes.

Auch interessant ist, dass fuer sehr grosse h in Abhaengigkeit von X_0 noch
nicht einmal das erwartete Verhalten erreicht wird sondern zu Beginn der Fehler
fuer einen kleinen Bereich auch konstant sein kann. (siehe Vorwaerts im
angezeigten Beispiel)
"""
