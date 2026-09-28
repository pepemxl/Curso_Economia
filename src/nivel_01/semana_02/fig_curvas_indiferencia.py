# -*- coding: utf-8 -*-
"""Semana 2: mapa de curvas de indiferencia, restriccion presupuestaria y optimo."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import numpy as np
from estilo_figuras import nueva_figura, limpiar, guardar, DEMANDA, OFERTA, EQUILIBRIO, NEUTRO


def main():
    # Cobb-Douglas U = x^0.5 * y^0.5; presupuesto I = 100, Px = 5, Py = 5
    I, Px, Py = 100.0, 5.0, 5.0
    fig, ax = nueva_figura(u'Teoría del consumidor: óptimo con restricción presupuestaria')

    x = np.linspace(1, 24, 400)
    # El optimo Cobb-Douglas simetrico: x* = I/(2Px), y* = I/(2Py)
    x_opt, y_opt = I / (2 * Px), I / (2 * Py)
    u_opt = np.sqrt(x_opt * y_opt)

    for u, estilo in [(u_opt * 0.7, ':'), (u_opt, '-'), (u_opt * 1.3, ':')]:
        y = u ** 2 / x                       # y = U^2 / x  para U = sqrt(xy)
        etiqueta = (u'Curva de indiferencia óptima (U=%.1f)' % u) if estilo == '-' \
                   else (u'U = %.1f (inalcanzable)' % u if u > u_opt else u'U = %.1f (subóptima)' % u)
        ax.plot(x, y, estilo, color=DEMANDA, linewidth=2.2 if estilo == '-' else 1.4,
                alpha=1.0 if estilo == '-' else 0.55, label=etiqueta)

    # Recta de presupuesto: I = Px*x + Py*y
    xb = np.linspace(0, I / Px, 100)
    ax.plot(xb, (I - Px * xb) / Py, color=OFERTA, linewidth=2.4,
            label=u'Restricción presupuestaria ($I=100$, $P_x=P_y=5$)')

    ax.plot(x_opt, y_opt, 'o', color=EQUILIBRIO, markersize=12, zorder=5,
            label=u'Óptimo del consumidor (10, 10)')
    ax.annotate(u'Tangencia:\n$TMS = P_x/P_y$', xy=(x_opt, y_opt),
                xytext=(x_opt + 4.5, y_opt + 5.5), fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.5))

    ax.set_xlim(0, 24); ax.set_ylim(0, 24)
    limpiar(ax, u'Cantidad del bien X', u'Cantidad del bien Y')
    guardar(fig, 'curvas_indiferencia.png')


if __name__ == '__main__':
    main()
