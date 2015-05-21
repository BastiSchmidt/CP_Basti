"""
Spass, Spass, Spass
"""

import numpy as np
import matplotlib.pyplot as plt


def V(x, a):
    """
    Definition des gegebenen Potentials aus der Aufgabenstellung.
    Uebernimmt den Parameter A und die Stelle x; uebergibt den Wert des
    Potentials an der Stelle x
    """
    return x**4 - x**2 + a*x


def OneD_Schroedinger(v, args, l, dx, h):
    """
    Diese Routine loest numerisch die eindimensionale Schroedinger-
    Gleichung (SG) fuer ein gegebenes Potential v. Sie stellt dazu
    zunaechst die nach endlicher Groesse abgebrochene Matrix des zur SG
    gehoerenden Gleichungssystems auf, diagonalisiert diese und bestimmt
    die Eigenwerte (~energien) und Eigenvektoren (~funktionen)l.
    Letztere werden noch normalisiert.

    Uebernimmt:

    -    v: beliebiges eindimensionales Potential, welches als Funktion
            in dem Programm definiert sein sollte
    - args: zusaetzliche Parameter des Potentials
    -    l: halbe Laenge des zu untersuchenden Intervalls, welches
            dann als [-l, l] gewaehlt wird. An den Stellen x = +-l
            sollte die Wellenfunktion psi schon verschwunden sein
    -   dx: Diskretisierungsschrittweite
    -    h: effektives Wirkungsquantum der einheitenlosen SG

    Uebergibt:

    -        E_n: Eigenenergien zu den Eigenfunktionen psi der SG als
                  1-dim. nd.array.
    - psi_n_norm: normierte Eigenfunktionen der SG auf [-l, l] als
                  2-dim nd.array. Die psi_n_norm[i,:] gehoert dabei zu
                  E_n[i].
    -  x_n[1:-1]: Array von x-Werten zu den psi_n_norm, entspricht
                  [-l, l] ohne die beiden auesseren Werte, da
                  psi_n_norm(+-l) = 0 sein sollte.
    -        V_n: Array der Potentialwerte zu den x_n[1:-1]
    """
    x_n = np.arange(-l, l , dx)
    V_n = v(x_n[1:-1], args)
    z = h**2/(2 * dx**2)
    matrix = np.diag(V_n + 2*z) +\
             np.diag(np.ones(len(V_n)-1) * (-z), +1) +\
             np.diag(np.ones(len(V_n)-1) * (-z), -1)
    E_n, psi_n = np.linalg.eigh(matrix)
    psi_n_norm = psi_n/np.sqrt(dx)
    return E_n, psi_n_norm, x_n[1:-1], V_n


def plot_eigenfunctions(ax, scalefactor=0.01):
    """
    Diese Funktion plottet Eigenfunktionen in Hoehe ihrer Eigenenergien in ein
    Potential V, welche alle aus dem Aufruf der Funktion OneD_Schroedinger()
    gewonnen werden
    """
    ev, ef, xi, Vi = OneD_Schroedinger(V, L, Delta_x, h_eff, A)
    ax.plot(xi, Vi, lw=3, color='k')
    ax.plot(xi, ev + scalefactor*ef)


# globale Parameter
A = 0.04
L = 2.5  # must be positive
Delta_x = 0.0025
h_eff = 0.05

ax1 = plt.subplot()
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-0.3, 0.11)
ax1.set_xlabel('$x$')
ax1.set_title('Asymmetrisches Doppelmuldenpotential')

if __name__ == "__main__":
    print __doc__
    plot_eigenfunctions(ax1)
    plt.show()
