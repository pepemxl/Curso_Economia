# -*- coding: utf-8 -*-
"""Semana 39: frontera eficiente de Markowitz y Linea de Asignacion de Capital."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import numpy as np
from estilo_figuras import nueva_figura, limpiar, guardar, DEMANDA, OFERTA, EQUILIBRIO, ACENTO, NEUTRO

RF = 3.0                                   # tasa libre de riesgo del ejercicio


def main():
    # Dos activos con correlacion parcial: generan la tipica frontera en forma de bala
    r1, s1 = 12.0, 15.0                    # Fondo Alfa
    r2, s2 = 8.0, 5.0                      # Fondo Beta
    rho = 0.25

    w = np.linspace(-0.35, 1.35, 400)
    rp = w * r1 + (1 - w) * r2
    sp = np.sqrt((w * s1) ** 2 + ((1 - w) * s2) ** 2 + 2 * w * (1 - w) * rho * s1 * s2)

    fig, ax = nueva_figura(u'Frontera eficiente de Markowitz y Línea de Asignación de Capital')

    i_min = int(np.argmin(sp))
    eficiente = np.arange(len(w)) >= i_min
    ax.plot(sp[~eficiente], rp[~eficiente], color=NEUTRO, lw=2.0, ls=':',
            label=u'Tramo ineficiente (mismo riesgo, menos retorno)')
    ax.plot(sp[eficiente], rp[eficiente], color=DEMANDA, lw=3.0,
            label=u'Frontera eficiente')
    ax.plot(sp[i_min], rp[i_min], 'D', color=ACENTO, ms=11, zorder=6,
            label=u'Cartera de mínima varianza ($\\sigma = %.1f\\%%$)' % sp[i_min])

    # Los dos fondos del ejercicio
    ax.plot(s1, r1, 'o', color=OFERTA, ms=13, zorder=6)
    ax.annotate(u'Fondo Alfa\n$R=12\\%$, $\\sigma=15\\%$\nSharpe = 0,60',
                xy=(s1, r1), xytext=(s1 - 1.0, r1 - 4.2), fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.3))
    ax.plot(s2, r2, 'o', color=EQUILIBRIO, ms=13, zorder=6)
    ax.annotate(u'Fondo Beta\n$R=8\\%$, $\\sigma=5\\%$\nSharpe = 1,00',
                xy=(s2, r2), xytext=(s2 - 3.6, r2 + 4.0), fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.3))

    # CAL apoyada en el Fondo Beta: R = Rf + Sharpe * sigma
    sharpe_beta = (r2 - RF) / s2
    sx = np.linspace(0, 19, 100)
    ax.plot(sx, RF + sharpe_beta * sx, color=EQUILIBRIO, lw=2.4, ls='--',
            label=u'CAL sobre el Fondo Beta ($R = 3\\%% + %.2f\\sigma$)' % sharpe_beta)
    ax.plot(0, RF, '*', color=NEUTRO, ms=17, zorder=6, label=u'Activo libre de riesgo (3%)')

    # El punto clave del ejercicio: Beta apalancado 3x iguala el riesgo de Alfa
    ax.plot(15.0, 18.0, 'P', color=EQUILIBRIO, ms=15, zorder=7)
    ax.annotate(u'Fondo Beta apalancado 3×\n$\\sigma=15\\%$ igual que Alfa,\npero $R=18\\%$',
                xy=(15.0, 18.0), xytext=(8.4, 19.6), fontsize=10, fontweight='bold',
                color=EQUILIBRIO,
                arrowprops=dict(arrowstyle='->', color=EQUILIBRIO, lw=1.6))
    ax.annotate('', xy=(15.0, 17.6), xytext=(15.0, 12.4),
                arrowprops=dict(arrowstyle='<->', color=OFERTA, lw=2.2))
    ax.text(15.45, 15.0, u'+600 pb\nal mismo\nriesgo', fontsize=9.5,
            color=OFERTA, fontweight='bold')

    ax.set_xlim(0, 19); ax.set_ylim(2, 22)
    limpiar(ax, u'Riesgo — desviación estándar $\\sigma$ (%)', u'Retorno esperado (%)')
    ax.legend(loc='lower right', fontsize=9, framealpha=0.95)
    guardar(fig, 'frontera_eficiente.png')


if __name__ == '__main__':
    main()
