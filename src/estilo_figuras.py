# -*- coding: utf-8 -*-
"""Estilo y utilidades comunes para las figuras del curso.

Todas las figuras se generan con `make figures`, que ejecuta cada
`src/**/fig_*.py` y deja los PNG en `docs/images/`.
"""
import os
import matplotlib
matplotlib.use('Agg')          # sin display: funciona en CI y en Docker
import matplotlib.pyplot as plt

# Paleta unica del curso (misma que src/nivel_01/semana_01)
DEMANDA        = '#1f77b4'   # azul
DEMANDA_NUEVA  = '#aec7e8'   # azul claro
OFERTA         = '#d62728'   # rojo
OFERTA_NUEVA   = '#ff9896'   # rojo claro
EQUILIBRIO     = '#2ca02c'   # verde
ACENTO         = '#ff7f0e'   # naranja
NEUTRO         = '#7f7f7f'   # gris
RIESGO         = '#9467bd'   # morado

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_IMAGENES = os.path.join(RAIZ, 'docs', 'images')


def nueva_figura(titulo, figsize=(10, 6.5)):
    """Crea figura y ejes con el estilo comun del curso."""
    plt.rcParams.update({
        'font.size': 11,
        'axes.titlesize': 13,
        'axes.labelsize': 11,
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
    })
    fig, ax = plt.subplots(figsize=figsize)
    fig.suptitle(titulo, fontsize=15, fontweight='bold')
    return fig, ax


def limpiar(ax, xlabel=None, ylabel=None, leyenda=True):
    """Quita el marco superior/derecho y aplica rejilla suave."""
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    if xlabel:
        ax.set_xlabel(xlabel, fontweight='bold')
    if ylabel:
        ax.set_ylabel(ylabel, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.35)
    if leyenda:
        ax.legend(loc='best', framealpha=0.95)


def guardar(fig, nombre):
    """Guarda siempre en docs/images/, sin depender del directorio actual."""
    if not os.path.isdir(DIR_IMAGENES):
        os.makedirs(DIR_IMAGENES)
    destino = os.path.join(DIR_IMAGENES, nombre)
    fig.savefig(destino, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('  -> %s' % os.path.relpath(destino, RAIZ))
