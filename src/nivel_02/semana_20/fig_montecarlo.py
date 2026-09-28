# -*- coding: utf-8 -*-
"""Semana 20: simulacion Monte Carlo del VAN del proyecto inmobiliario.

Reproduce en Python el mismo ejercicio que la sesion 4 resuelve en Excel.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import numpy as np
from estilo_figuras import nueva_figura, limpiar, guardar, DEMANDA, OFERTA, EQUILIBRIO, NEUTRO

INVERSION, TASA = 2_000_000.0, 0.08
MU_VENTA, SD_VENTA = 2_500_000.0, 300_000.0
MU_COSTO, SD_COSTO = 300_000.0, 50_000.0
N = 100_000


def miles(v):
    """Formato de miles a la espanola: 1.234.567"""
    return format(int(round(v)), ',d').replace(',', '.')


def main():
    rng = np.random.default_rng(42)          # semilla fija: figura reproducible
    venta = rng.normal(MU_VENTA, SD_VENTA, N)
    costo = rng.normal(MU_COSTO, SD_COSTO, N)
    van = -INVERSION + (venta - costo) / (1 + TASA)

    p_exito = float((van > 0).mean())
    van_medio = float(van.mean())
    # Valor teorico: la resta de dos normales independientes suma varianzas
    sd_flujo = (SD_VENTA ** 2 + SD_COSTO ** 2) ** 0.5
    van_teorico = -INVERSION + (MU_VENTA - MU_COSTO) / (1 + TASA)

    fig, ax = nueva_figura(u'Simulación Monte Carlo: distribución del VAN (%s iteraciones)'
                           % miles(N))
    n, bins, parches = ax.hist(van, bins=90, color=DEMANDA, alpha=0.55, edgecolor='white')
    for b, parche in zip(bins[:-1], parches):
        if b < 0:
            parche.set_facecolor(OFERTA)

    ax.axvline(0, color='black', lw=2.0, ls='-')
    # El signo $ debe escaparse: matplotlib lo interpretaria como inicio de mathtext
    ax.axvline(van_medio, color=EQUILIBRIO, lw=2.4, ls='--',
               label=u'VAN medio simulado = \\$%s   (teórico: \\$%s)'
                     % (miles(van_medio), miles(van_teorico)))

    ax.text(0.02, 0.95, u'$P(VAN > 0) = %.1f\\%%$\n$P(VAN < 0) = %.1f\\%%$'
            % (p_exito * 100, (1 - p_exito) * 100),
            transform=ax.transAxes, fontsize=13, fontweight='bold', va='top',
            bbox=dict(boxstyle='round,pad=0.6', facecolor='white', edgecolor=NEUTRO))
    ax.text(0.02, 0.74,
            u'$\\sigma_{flujo} = \\sqrt{300.000^2 + 50.000^2} = %s$' % miles(sd_flujo),
            transform=ax.transAxes, fontsize=10.5, va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f5f5f5', edgecolor=NEUTRO))

    ax.annotate(u'Zona de pérdida', xy=(-250_000, max(n) * 0.35),
                fontsize=11, fontweight='bold', color=OFERTA, ha='center')
    limpiar(ax, u'VAN del proyecto ($)', u'Frecuencia (nº de iteraciones)')
    guardar(fig, 'montecarlo_van.png')
    print('     P(exito) = %.2f%%  |  VAN medio = %.0f' % (p_exito * 100, van_medio))


if __name__ == '__main__':
    main()
