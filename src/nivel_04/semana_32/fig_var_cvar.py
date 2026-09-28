# -*- coding: utf-8 -*-
"""Semana 32: VaR parametrico y Expected Shortfall (CVaR) sobre el portafolio del ejercicio."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from math import exp, pi, sqrt
import numpy as np
from estilo_figuras import nueva_figura, limpiar, guardar, DEMANDA, OFERTA, EQUILIBRIO, RIESGO, NEUTRO

VALOR, SIGMA_D, Z99 = 5_000_000.0, 0.02, 2.326


def main():
    sigma = VALOR * SIGMA_D                       # desviacion en dolares: 100.000
    var99 = Z99 * sigma                           # 232.600
    # Para la normal, ES = sigma * phi(z) / (1 - c)
    phi = exp(-Z99 ** 2 / 2) / sqrt(2 * pi)
    es99 = sigma * phi / 0.01

    x = np.linspace(-4.2 * sigma, 3.2 * sigma, 900)
    dens = np.exp(-(x ** 2) / (2 * sigma ** 2)) / (sigma * sqrt(2 * pi))

    fig, ax = nueva_figura(u'VaR y Expected Shortfall al 99%: portafolio de $5.000.000')
    ax.plot(x, dens, color=DEMANDA, lw=2.6, label=u'Distribución de P&L diario ($\\sigma = \\$100.000$)')
    ax.fill_between(x, dens, where=(x <= -var99), color=OFERTA, alpha=0.65,
                    label=u'Cola del 1% peor')

    # Verticales acotadas a la altura de la densidad: de suelo a techo dominarian la figura
    def altura(v):
        return exp(-(v ** 2) / (2 * sigma ** 2)) / (sigma * sqrt(2 * pi))

    ax.vlines(-var99, 0, altura(var99) * 4.2, color=EQUILIBRIO, lw=2.6, ls='--',
              label=u'VaR 99% = \\$232.600 (donde empieza la cola)')
    ax.vlines(-es99, 0, altura(es99) * 6.0, color=RIESGO, lw=2.6, ls='-.',
              label=u'Expected Shortfall = \\$%s (pérdida media EN la cola)'
                    % format(int(round(es99)), ',d').replace(',', '.'))

    ax.annotate(u'El VaR dice dónde\nempieza la cola…', xy=(-var99, altura(var99) * 4.2),
                xytext=(-2.0 * sigma, 2.1e-6), fontsize=10, fontweight='bold', color=EQUILIBRIO,
                ha='left', arrowprops=dict(arrowstyle='->', color=EQUILIBRIO, lw=1.5))
    ax.annotate(u'…pero el ES mide\nqué tan profunda es', xy=(-es99, altura(es99) * 6.0),
                xytext=(-4.15 * sigma, 1.5e-6), fontsize=10, fontweight='bold', color=RIESGO,
                ha='left', arrowprops=dict(arrowstyle='->', color=RIESGO, lw=1.5))

    ax.set_xticks([-4e5, -3e5, -2e5, -1e5, 0, 1e5, 2e5, 3e5])
    ax.set_xticklabels([u'-400k', u'-300k', u'-200k', u'-100k', u'0', u'+100k', u'+200k', u'+300k'])
    ax.set_ylim(0, 4.6e-6)
    limpiar(ax, u'Pérdida / ganancia diaria ($)', u'Densidad de probabilidad')
    ax.legend(loc='upper right', fontsize=9.5, framealpha=0.95)
    guardar(fig, 'var_cvar.png')
    print('     VaR99 = %.0f | ES99 = %.0f' % (var99, es99))


if __name__ == '__main__':
    main()
