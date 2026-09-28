# -*- coding: utf-8 -*-
"""Semana 24: Linea del Mercado de Valores (SML) y el CAPM de GoldRush Inc."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import numpy as np
from estilo_figuras import nueva_figura, limpiar, guardar, DEMANDA, OFERTA, EQUILIBRIO, ACENTO, NEUTRO

RF, MRP = 3.5, 5.5          # datos del ejercicio de la Semana 24


def main():
    fig, ax = nueva_figura(u'CAPM: Línea del Mercado de Valores (SML)')
    beta = np.linspace(0, 2.0, 200)
    ax.plot(beta, RF + beta * MRP, color=DEMANDA, lw=2.8,
            label=u'SML: $r_e = %.1f\\%% + \\beta \\times %.1f\\%%$' % (RF, MRP))

    # Cada etiqueta lleva su posicion explicita para que no se solapen
    puntos = [
        (0.0, RF, u'Activo libre de riesgo\n($\\beta = 0$)', NEUTRO, (0.12, 1.9)),
        (1.0, RF + MRP, u'Cartera de mercado\n($\\beta = 1$)', ACENTO, (0.42, 7.3)),
        (1.1, RF + 1.1 * MRP, u'GoldRush Inc.\n$\\beta = 1{,}1 \\Rightarrow r_e = 9{,}55\\%$',
         EQUILIBRIO, (1.30, 12.2)),
    ]
    for b, r, etiqueta, color, destino in puntos:
        ax.plot(b, r, 'o', color=color, ms=13, zorder=6)
        ax.annotate(etiqueta, xy=(b, r), xytext=destino,
                    fontsize=10, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=NEUTRO, lw=1.3))

    # Activos mal valorados: fuera de la recta
    ax.plot(0.8, 10.5, 's', color=EQUILIBRIO, ms=11, zorder=6)
    ax.annotate(u'Infravalorada\n(rinde más de lo exigido)', xy=(0.8, 10.5),
                xytext=(0.16, 8.6), fontsize=9.5, color=EQUILIBRIO,
                arrowprops=dict(arrowstyle='->', color=EQUILIBRIO, lw=1.3))
    ax.plot(1.5, 8.0, 's', color=OFERTA, ms=11, zorder=6)
    ax.annotate(u'Sobrevalorada\n(rinde menos de lo exigido)', xy=(1.5, 8.0),
                xytext=(1.30, 4.4), fontsize=9.5, color=OFERTA,
                arrowprops=dict(arrowstyle='->', color=OFERTA, lw=1.3))

    # La prima por riesgo de mercado como segmento vertical
    ax.annotate('', xy=(1.0, RF + MRP), xytext=(1.0, RF),
                arrowprops=dict(arrowstyle='<->', color=ACENTO, lw=2.0))
    ax.text(1.05, RF + MRP / 2, u'$MRP = 5{,}5\\%$', ha='left', fontsize=10,
            color=ACENTO, fontweight='bold')
    ax.axhline(RF, color=NEUTRO, lw=1.2, ls=':')

    ax.set_xlim(0, 2.0); ax.set_ylim(0, 15)
    limpiar(ax, u'Beta ($\\beta$) — riesgo sistemático', u'Rendimiento exigido (%)')
    guardar(fig, 'capm_sml.png')


if __name__ == '__main__':
    main()
