# -*- coding: utf-8 -*-
"""Semana 15: las tres distribuciones de probabilidad clave en finanzas."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from math import comb, exp, factorial, pi, sqrt
import numpy as np
import matplotlib.pyplot as plt
from estilo_figuras import DEMANDA, OFERTA, ACENTO, EQUILIBRIO, guardar


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2))
    fig.suptitle(u'Distribuciones de probabilidad aplicadas a finanzas',
                 fontsize=15, fontweight='bold')

    # --- Binomial: el fondo de VC del ejercicio (n=5, p=0.2) ---
    n, p = 5, 0.20
    k = np.arange(0, n + 1)
    pmf = [comb(n, i) * p ** i * (1 - p) ** (n - i) for i in k]
    barras = axes[0].bar(k, pmf, color=DEMANDA, alpha=0.85, edgecolor='white')
    barras[2].set_color(EQUILIBRIO)
    axes[0].set_title(u'Binomial: 5 startups, éxito 20%%\n$P(X=2) = %.4f$' % pmf[2],
                      fontweight='bold')
    axes[0].set_xlabel(u'Número de startups exitosas', fontweight='bold')
    axes[0].set_ylabel(u'Probabilidad', fontweight='bold')
    for i, v in zip(k, pmf):
        axes[0].text(i, v + 0.012, '%.3f' % v, ha='center', fontsize=9)

    # --- Normal: retornos diarios de Amazon (mu=0.05%, sigma=2%) ---
    mu, sigma = 0.05, 2.0
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 500)
    dens = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * sqrt(2 * pi))
    axes[1].plot(x, dens, color=OFERTA, lw=2.4)
    corte = -3.95
    axes[1].fill_between(x, dens, where=(x <= corte), color=OFERTA, alpha=0.45)
    axes[1].axvline(corte, color=EQUILIBRIO, lw=2.0, ls='--')
    axes[1].annotate(u'$Z = -2{,}00$\n$P = 2{,}28\\%$', xy=(corte - 1.0, 0.018),
                     fontsize=10, fontweight='bold', color=EQUILIBRIO, ha='center')
    axes[1].set_title(u'Normal: retorno diario de una acción\n$\\mu = 0{,}05\\%$, $\\sigma = 2\\%$',
                      fontweight='bold')
    axes[1].set_xlabel(u'Retorno diario (%)', fontweight='bold')
    axes[1].set_ylabel(u'Densidad', fontweight='bold')

    # --- Poisson: eventos raros (impagos por trimestre) ---
    lam = 3.0
    kk = np.arange(0, 12)
    pois = [exp(-lam) * lam ** i / factorial(i) for i in kk]
    axes[2].bar(kk, pois, color=ACENTO, alpha=0.85, edgecolor='white')
    axes[2].set_title(u'Poisson: nº de impagos por trimestre\n$\\lambda = 3$',
                      fontweight='bold')
    axes[2].set_xlabel(u'Número de eventos', fontweight='bold')
    axes[2].set_ylabel(u'Probabilidad', fontweight='bold')

    for ax in axes:
        for lado in ('top', 'right'):
            ax.spines[lado].set_visible(False)
        ax.grid(True, linestyle='--', alpha=0.3)

    fig.tight_layout(rect=(0, 0, 1, 0.92))
    guardar(fig, 'distribuciones_probabilidad.png')


if __name__ == '__main__':
    main()
