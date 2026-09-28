# -*- coding: utf-8 -*-
"""Semana 5: modelo DA-OA y cierre de una brecha recesiva con politica fiscal.

Calibracion coherente con el ejercicio de la Semana 5:
PIB inicial 5.000, PIB potencial 5.500, brecha de 500 cerrada con dG = 200 (k = 2,5).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import numpy as np
from estilo_figuras import (nueva_figura, limpiar, guardar,
                            DEMANDA, DEMANDA_NUEVA, OFERTA, EQUILIBRIO, NEUTRO)

BASE = 4200.0
PEND_OA, PEND_DA = 0.04, 0.04


def oa(Y):
    return 80.0 + PEND_OA * (Y - BASE)


def da(Y, intercepto):
    return intercepto - PEND_DA * (Y - BASE)


def equilibrio(intercepto):
    """Resuelve da(Y) = oa(Y) analiticamente en lugar de buscar el minimo."""
    Y = BASE + (intercepto - 80.0) / (PEND_OA + PEND_DA)
    return Y, oa(Y)


def main():
    fig, ax = nueva_figura(u'Modelo DA-OA: cierre de una brecha recesiva vía política fiscal')
    Y = np.linspace(4400, 6100, 400)

    INT1 = 144.0                      # DA inicial: equilibrio en PIB = 5.000
    INT2 = 184.0                      # DA tras el estimulo: equilibrio en PIB = 5.500

    ax.plot(Y, da(Y, INT1), color=DEMANDA, lw=2.5, label=u'$DA_1$ (demanda agregada inicial)')
    ax.plot(Y, da(Y, INT2), color=DEMANDA_NUEVA, lw=2.5, ls='--',
            label=u'$DA_2$ (tras $\\Delta G = 200$, con $k = 2{,}5$)')
    ax.plot(Y, oa(Y), color=OFERTA, lw=2.5, label=u'$OA$ (oferta agregada de corto plazo)')
    ax.axvline(5500, color=NEUTRO, lw=2.2, ls=':', label=u'$OA_{LP}$: PIB potencial = 5.500')

    y1, p1 = equilibrio(INT1)
    y2, p2 = equilibrio(INT2)
    for y, p in ((y1, p1), (y2, p2)):
        ax.plot(y, p, 'o', color=EQUILIBRIO, ms=13, zorder=6)

    ax.annotate(u'$E_1$: recesión\nPIB = %.0f' % y1, xy=(y1, p1), xytext=(y1 - 560, p1 - 22),
                fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.4))
    ax.annotate(u'$E_2$: pleno empleo\nPIB = %.0f' % y2, xy=(y2, p2), xytext=(y2 + 130, p2 - 30),
                fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.4))

    # Flecha que mide la brecha, apoyada sobre la curva OA
    ax.annotate('', xy=(y2, p2), xytext=(y1, p1),
                arrowprops=dict(arrowstyle='<->', color=EQUILIBRIO, lw=2.4))
    ax.text((y1 + y2) / 2, (p1 + p2) / 2 - 17, u'Brecha recesiva: 500', ha='center',
            fontsize=10.5, fontweight='bold', color=EQUILIBRIO)

    # El desplazamiento de la curva
    ax.annotate('', xy=(4700, da(4700, INT2)), xytext=(4700, da(4700, INT1)),
                arrowprops=dict(arrowstyle='->', color=DEMANDA, lw=2.0, ls='--'))
    ax.text(4640, (da(4700, INT1) + da(4700, INT2)) / 2, u'Desplazamiento\nde la DA',
            ha='right', fontsize=9.5, color=DEMANDA, fontweight='bold')

    ax.set_xlim(4400, 6100); ax.set_ylim(60, 195)
    limpiar(ax, u'PIB real (millones)', u'Nivel de precios')
    guardar(fig, 'da_oa_brecha_recesiva.png')


if __name__ == '__main__':
    main()
