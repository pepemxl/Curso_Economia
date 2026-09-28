# -*- coding: utf-8 -*-
"""Semana 3: familia de curvas de costos y optimo en competencia perfecta."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import numpy as np
from estilo_figuras import nueva_figura, limpiar, guardar, DEMANDA, OFERTA, EQUILIBRIO, ACENTO, NEUTRO


def main():
    # CT = 100 + 20q - 1.2q^2 + 0.06q^3  (forma en S del manual clasico)
    CF = 100.0
    q = np.linspace(1, 22, 500)
    CV = 20 * q - 1.2 * q ** 2 + 0.06 * q ** 3
    CT = CF + CV
    CMg = 20 - 2.4 * q + 0.18 * q ** 2
    CTMe = CT / q
    CVMe = CV / q

    fig, ax = nueva_figura(u'Costos de producción y equilibrio en competencia perfecta')
    ax.plot(q, CMg, color=OFERTA, lw=2.6, label=u'Costo Marginal (CMg)')
    ax.plot(q, CTMe, color=DEMANDA, lw=2.2, label=u'Costo Total Medio (CTMe)')
    ax.plot(q, CVMe, color=ACENTO, lw=2.0, ls='--', label=u'Costo Variable Medio (CVMe)')

    # El CMg corta al CTMe y al CVMe en sus minimos
    i_ctme, i_cvme = int(np.argmin(CTMe)), int(np.argmin(CVMe))
    ax.plot(q[i_ctme], CTMe[i_ctme], 'o', color=DEMANDA, ms=9, zorder=5)
    ax.plot(q[i_cvme], CVMe[i_cvme], 'o', color=ACENTO, ms=9, zorder=5)
    ax.annotate(u'Punto de cierre\n(mín. CVMe)', xy=(q[i_cvme], CVMe[i_cvme]),
                xytext=(q[i_cvme] - 4.2, CVMe[i_cvme] - 11), fontsize=9,
                arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.3))
    ax.annotate(u'Punto de equilibrio\na largo plazo (mín. CTMe)', xy=(q[i_ctme], CTMe[i_ctme]),
                xytext=(q[i_ctme] - 6.0, CTMe[i_ctme] + 30), fontsize=9,
                arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.3))

    # Precio de mercado y cantidad optima donde P = CMg
    P = 40.0
    ax.axhline(P, color=EQUILIBRIO, lw=2.2, ls='-.', label=u'Precio de mercado = IMg ($P=40$)')
    raices = np.roots([0.18, -2.4, 20 - P])
    q_opt = float(max(r.real for r in raices if abs(r.imag) < 1e-9))
    ax.plot(q_opt, P, '*', color=EQUILIBRIO, ms=20, zorder=6,
            label=u'Óptimo: $P = CMg$ (q≈%.1f)' % q_opt)

    ax.set_xlim(0, 22); ax.set_ylim(0, 90)
    limpiar(ax, u'Cantidad producida (q)', u'Costo / Precio por unidad ($)')
    guardar(fig, 'costos_produccion.png')


if __name__ == '__main__':
    main()
