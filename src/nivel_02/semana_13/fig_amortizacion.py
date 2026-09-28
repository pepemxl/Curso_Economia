# -*- coding: utf-8 -*-
"""Semana 13: comparativa de los tres sistemas de amortizacion."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import numpy as np
import matplotlib.pyplot as plt
from estilo_figuras import DEMANDA, OFERTA, ACENTO, NEUTRO, guardar, DIR_IMAGENES

CAPITAL, TASA, N = 100000.0, 0.08, 10


def frances():
    """Cuota constante: C = P * i / (1 - (1+i)^-n)."""
    cuota = CAPITAL * TASA / (1 - (1 + TASA) ** -N)
    saldo, filas = CAPITAL, []
    for _ in range(N):
        interes = saldo * TASA
        amort = cuota - interes
        saldo -= amort
        filas.append((cuota, interes, amort))
    return filas


def aleman():
    """Amortizacion a capital constante; la cuota decrece."""
    amort, saldo, filas = CAPITAL / N, CAPITAL, []
    for _ in range(N):
        interes = saldo * TASA
        saldo -= amort
        filas.append((amort + interes, interes, amort))
    return filas


def americano():
    """Solo intereses; el capital se devuelve integro al final."""
    filas = []
    for t in range(N):
        interes = CAPITAL * TASA
        amort = CAPITAL if t == N - 1 else 0.0
        filas.append((interes + amort, interes, amort))
    return filas


def main():
    sistemas = [(u'Francés (cuota constante)', frances(), DEMANDA),
                (u'Alemán (capital constante)', aleman(), OFERTA),
                (u'Americano (bullet)', americano(), ACENTO)]
    anios = np.arange(1, N + 1)

    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(u'Sistemas de amortización: préstamo de $100.000 al 8%% a %d años' % N,
                 fontsize=15, fontweight='bold')

    for nombre, filas, color in sistemas:
        cuotas = [f[0] for f in filas]
        intereses_ac = np.cumsum([f[1] for f in filas])
        total_int = intereses_ac[-1]
        axes[0].plot(anios, cuotas, 'o-', color=color, lw=2.3, ms=6, label=nombre)
        axes[1].plot(anios, intereses_ac, 'o-', color=color, lw=2.3, ms=6,
                     label=u'%s — total: $%s' % (nombre.split(' (')[0], format(int(round(total_int)), ',d')))

    # Escala logaritmica: el pago bullet del ultimo anio (108.000) aplastaria
    # las curvas francesa y alemana en escala lineal.
    axes[0].set_yscale('log')
    axes[0].set_yticks([8000, 10000, 15000, 20000, 40000, 100000])
    axes[0].get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda v, _: '%s' % format(int(v), ',d')))
    axes[0].set_title(u'Cuota total pagada cada año (escala log)', fontweight='bold')
    axes[0].set_xlabel(u'Año', fontweight='bold')
    axes[0].set_ylabel(u'Cuota ($)', fontweight='bold')
    axes[1].set_title(u'Intereses acumulados', fontweight='bold')
    axes[1].set_xlabel(u'Año', fontweight='bold')
    axes[1].set_ylabel(u'Intereses acumulados ($)', fontweight='bold')

    for ax in axes:
        for lado in ('top', 'right'):
            ax.spines[lado].set_visible(False)
        ax.grid(True, linestyle='--', alpha=0.35)
        ax.legend(loc='best', fontsize=9.5, framealpha=0.95)
        ax.set_xticks(anios)

    axes[0].annotate(u'El Alemán exige más\nesfuerzo de caja al inicio…',
                     xy=(1, aleman()[0][0]), xytext=(3.0, 30000), fontsize=9,
                     arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.3))
    axes[1].annotate(u'…y por eso paga\nmenos intereses en total',
                     xy=(N, np.cumsum([f[1] for f in aleman()])[-1]), xytext=(3.4, 62000),
                     fontsize=9, arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.3))

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    guardar(fig, 'sistemas_amortizacion.png')


if __name__ == '__main__':
    main()
