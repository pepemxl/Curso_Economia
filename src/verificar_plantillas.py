# -*- coding: utf-8 -*-
"""Evalua las formulas de las plantillas .xlsx y comprueba sus invariantes.

openpyxl escribe formulas pero no las calcula: sin esta verificacion, una
plantilla con referencias mal escritas se publicaria rota y en silencio.
Se ejecuta con `make plantillas`.
"""
import math as _math
import os
import re
import sys

from openpyxl import load_workbook
from openpyxl.utils import range_boundaries, get_column_letter

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'assets', 'plantillas')

RE_RANGO = re.compile(r"(?:('[^']+'|[A-Za-z_][A-Za-z0-9_ .&]*)!)?(\$?[A-Z]{1,3}\$?\d+:\$?[A-Z]{1,3}\$?\d+)")
RE_CELDA = re.compile(r"(?:('[^']+'|[A-Za-z_][A-Za-z0-9_ .&]*)!)?(\$?[A-Z]{1,3}\$?\d+)(?![\w(])")
RE_FUNC = re.compile(r"\b([A-Z][A-Z0-9._]*)\(")

FUNCS = {
    'SUM': lambda *a: sum(_planos(a)),
    'MAX': lambda *a: max(_planos(a)),
    'MIN': lambda *a: min(_planos(a)),
    'ABS': lambda x: abs(x),
    'AVERAGE': lambda *a: (lambda v: sum(v) / len(v))(_planos(a)),
    'ROUND': lambda x, n=0: round(x, int(n)),
    'SQRT': lambda x: x ** 0.5,
    'IFERROR': lambda v, alt: alt if isinstance(v, Exception) else v,
    'CHOOSE': lambda i, *o: o[int(i) - 1],
    'IF': lambda c, a, b=0: a if c else b,
    'NPV': lambda r, *a: sum(v / (1 + r) ** (i + 1) for i, v in enumerate(_planos(a))),
    'PMT': lambda r, n, pv: -pv * r / (1 - (1 + r) ** -n),
    'COUNT': lambda *a: len(_planos(a)),
    'SUMPRODUCT': lambda *a: sum(x * y for x, y in zip(*[list(v) for v in a])),
    # Estadisticas. RAND() se fija en 0,5 para que la verificacion sea
    # determinista: NORM.INV(0,5; mu; s) = mu, asi la simulacion debe caer
    # exactamente sobre su valor teorico.
    'RAND': lambda: 0.5,
    'SQRT': lambda x: x ** 0.5,
    'STDEV.S': lambda *a: _stdev(_planos(a)),
    'NORM.S.INV': lambda p: _probit(p),
    'NORM.INV': lambda p, mu, s: mu + s * _probit(p),
    'NORM.DIST': lambda x, mu, s, acum: (_cdf((x - mu) / s) if acum
                                         else _pdf((x - mu) / s) / s),
    'NORM.S.DIST': lambda z, acum: _cdf(z) if acum else _pdf(z),
    'COUNTIF': lambda rango, crit: _countif(rango, crit),
    'PERCENTILE.INC': lambda rango, p: _percentil(_planos([rango]), p),
    'MEDIAN': lambda *a: _percentil(_planos(a), 0.5),
}


def _pdf(z):
    return _math.exp(-z * z / 2.0) / _math.sqrt(2 * _math.pi)


def _cdf(z):
    return 0.5 * (1 + _math.erf(z / _math.sqrt(2)))


def _probit(p):
    """Inversa de la normal estandar por biseccion (precision de sobra aqui)."""
    lo, hi = -12.0, 12.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if _cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _stdev(v):
    n = len(v)
    m = sum(v) / n
    return (sum((x - m) ** 2 for x in v) / (n - 1)) ** 0.5


def _countif(rango, crit):
    vals = _planos([rango])
    crit = str(crit).strip('"')
    for op in ('>=', '<=', '<>', '>', '<', '='):
        if crit.startswith(op):
            u = float(crit[len(op):])
            cmp = {'>': lambda x: x > u, '<': lambda x: x < u,
                   '>=': lambda x: x >= u, '<=': lambda x: x <= u,
                   '=': lambda x: x == u, '<>': lambda x: x != u}[op]
            return sum(1 for x in vals if cmp(x))
    return sum(1 for x in vals if x == float(crit))


def _percentil(v, p):
    v = sorted(v)
    k = (len(v) - 1) * p
    lo = int(k)
    hi = min(lo + 1, len(v) - 1)
    return v[lo] + (k - lo) * (v[hi] - v[lo])


def _planos(args):
    out = []
    for a in args:
        if isinstance(a, (list, tuple)):
            out.extend(_planos(a))
        elif isinstance(a, (int, float)):
            out.append(a)
    return out


class Libro(object):
    def __init__(self, ruta):
        self.wb = load_workbook(ruta, data_only=False)
        self.cache = {}
        self.pila = set()

    def valor(self, hoja, coord):
        coord = coord.replace('$', '')
        clave = (hoja, coord)
        if clave in self.cache:
            return self.cache[clave]
        if clave in self.pila:
            raise ValueError('referencia circular en %s!%s' % clave)
        self.pila.add(clave)
        try:
            bruto = self.wb[hoja][coord].value
            if bruto is None or bruto == '':
                v = 0
            elif isinstance(bruto, str) and bruto.startswith('='):
                v = self._evaluar(hoja, bruto[1:])
            elif isinstance(bruto, (int, float)):
                v = bruto
            else:
                v = bruto
            self.cache[clave] = v
            return v
        finally:
            self.pila.discard(clave)

    def rango(self, hoja, ref):
        c1, f1, c2, f2 = range_boundaries(ref.replace('$', ''))
        return [self.valor(hoja, '%s%d' % (get_column_letter(c), f))
                for f in range(f1, f2 + 1) for c in range(c1, c2 + 1)]

    def _evaluar(self, hoja, expr):
        ctx = {'_V': [], '_R': []}

        def sub_rango(m):
            h = (m.group(1) or hoja).strip("'")
            ctx['_R'].append(self.rango(h, m.group(2)))
            return '_R[%d]' % (len(ctx['_R']) - 1)

        def sub_celda(m):
            h = (m.group(1) or hoja).strip("'")
            ctx['_V'].append(self.valor(h, m.group(2)))
            return '_V[%d]' % (len(ctx['_V']) - 1)

        # Proteger nombres de funcion antes de sustituir referencias
        funcs_vistas = []

        def sub_func(m):
            funcs_vistas.append(m.group(1))
            return '_F%d(' % (len(funcs_vistas) - 1)

        e = RE_FUNC.sub(sub_func, expr)
        e = RE_RANGO.sub(sub_rango, e)
        e = RE_CELDA.sub(sub_celda, e)
        e = e.replace('^', '**').replace('<>', '!=')
        e = re.sub(r'\bTRUE\b', 'True', e)
        e = re.sub(r'\bFALSE\b', 'False', e)
        entorno = {'_V': ctx['_V'], '_R': ctx['_R']}
        for i, nombre in enumerate(funcs_vistas):
            if nombre not in FUNCS:
                raise ValueError('funcion no soportada por el verificador: %s' % nombre)
            entorno['_F%d' % i] = FUNCS[nombre]
        try:
            return eval(e, {'__builtins__': {}}, entorno)
        except Exception as exc:                       # se propaga a IFERROR
            raise ValueError('no se pudo evaluar "%s" -> "%s": %s' % (expr, e, exc))


def comprobar(nombre, pruebas):
    ruta = os.path.join(DIR, nombre)
    lb = Libro(ruta)
    fallos = []
    for descripcion, hoja, coord, esperado, tol in pruebas:
        try:
            obtenido = lb.valor(hoja, coord)
        except Exception as exc:
            fallos.append('  [ERROR] %s: %s' % (descripcion, exc)); continue
        if not isinstance(obtenido, (int, float)):
            fallos.append('  [FALLO] %s: no es numero (%r)' % (descripcion, obtenido)); continue
        if abs(obtenido - esperado) > tol:
            fallos.append('  [FALLO] %s: esperado %.4f, obtenido %.4f'
                          % (descripcion, esperado, obtenido))
        else:
            print('  ok  %-52s %12.2f' % (descripcion, obtenido))
    return fallos


# ---------------------------------------------------------------------------
# Suite de comprobaciones: cada plantilla debe reproducir el ejercicio del curso
# ---------------------------------------------------------------------------

def _suite():
    fallos = []

    print('modelo_3_estados.xlsx  (Semanas 18-19)')
    lb = Libro(os.path.join(DIR, 'modelo_3_estados.xlsx'))
    for etiqueta, coord, esperado in [
            ('Ventas Ano 1', 'C4', 1100.0), ('EBITDA Ano 1', 'C5', 220.0),
            ('EBIT Ano 1', 'C7', 200.0), ('EBT Ano 1', 'C9', 170.0),
            ('Utilidad neta Ano 1', 'C11', 127.5)]:
        v = lb.valor('P&L', coord)
        ok = abs(v - esperado) < 0.01
        print('  %s %-28s %10.2f (esperado %.2f)' % ('ok ' if ok else 'FALLO', etiqueta, v, esperado))
        if not ok:
            fallos.append('modelo_3_estados: %s' % etiqueta)
    fila_chk = None
    for fila in lb.wb['Balance'].iter_rows(min_col=1, max_col=1):
        if fila[0].value and 'Activo - (Pasivo' in str(fila[0].value):
            fila_chk = fila[0].row
    for i in range(6):
        v = lb.valor('Balance', '%s%d' % (get_column_letter(2 + i), fila_chk))
        if abs(v) > 1e-6:
            fallos.append('modelo_3_estados: el balance NO cuadra en el Ano %d (%.4f)' % (i, v))
    print('  %s balance cuadra en los 6 anos' % ('ok ' if not fallos else 'FALLO'))

    print('dcf_wacc.xlsx  (Semanas 24 y 37)')
    lb = Libro(os.path.join(DIR, 'dcf_wacc.xlsx'))
    fallos += comprobar_hoja(lb, [
        ('WACC de GoldRush = 8,00%', 'WACC', None, 'WACC', 0.08, 1e-6),
        ('Suma de VP explicitos', 'DCF', None, 'Suma de VP explicitos', 142.2991, 0.001),
        ('VP del valor terminal', 'DCF', None, 'VP del valor terminal', 481.6380, 0.001),
        ('Enterprise Value', 'DCF', None, 'Enterprise Value', 623.9371, 0.001),
        ('Valor por accion de LogiTrans', 'DCF', None, 'VALOR INTRINSECO', 116.7874, 0.001),
    ])

    print('var_montecarlo.xlsx  (Semanas 20 y 32)')
    lb = Libro(os.path.join(DIR, 'var_montecarlo.xlsx'))
    fallos += comprobar_hoja(lb, [
        ('Contratos de cobertura', 'VaR parametrico', None, 'CONTRATOS A VENDER', 24.0, 1e-9),
        ('VaR a 1 dia', 'VaR parametrico', None, 'VaR a 1 dia  =', 232634.79, 1.0),
        ('VAN esperado teorico', 'Monte Carlo', None, 'VAN esperado', 37037.037, 0.01),
        ('Sigma del flujo', 'Monte Carlo', None, 'Sigma del flujo', 304138.13, 0.01),
        ('P(VAN>0) teorica', 'Monte Carlo', None, 'P(VAN > 0) teorica', 0.5523, 0.0005),
    ])

    print('plantilla_reporte_final.xlsx  (Semana 40)')
    lb = Libro(os.path.join(DIR, 'plantilla_reporte_final.xlsx'))
    fallos += comprobar_hoja(lb, [
        ('EBITDA Ano 1 = EBIT + D&A', '4 Comparables', None, 'EBITDA del Ano 1', 2376.0, 0.01),
        ('Target price por DCF', '3 Valuacion DCF', None, 'TARGET PRICE POR DCF', 47.1238, 0.001),
        ('Target price por Comps', '4 Comparables', None, 'TARGET PRICE POR COMPS', 47.3244, 0.001),
        ('Precio objetivo mezclado', '4 Comparables', None, 'PRECIO OBJETIVO FINAL', 47.2040, 0.001),
    ])
    return fallos


def comprobar_hoja(lb, pruebas):
    """Localiza cada fila por su etiqueta en la columna A, para no fijar numeros de fila."""
    fallos = []
    for descripcion, hoja, _, etiqueta, esperado, tol in pruebas:
        fila = None
        for f in lb.wb[hoja].iter_rows(min_col=1, max_col=1):
            if f[0].value and str(f[0].value).startswith(etiqueta):
                fila = f[0].row
                break
        if fila is None:
            fallos.append('%s: no se encontro la fila "%s"' % (hoja, etiqueta))
            print('  FALLO %-40s (fila no encontrada)' % descripcion)
            continue
        v = lb.valor(hoja, 'B%d' % fila)
        ok = isinstance(v, (int, float)) and abs(v - esperado) < tol
        print('  %s %-40s %14.4f (esperado %.4f)'
              % ('ok ' if ok else 'FALLO', descripcion, v if isinstance(v, (int, float)) else -1, esperado))
        if not ok:
            fallos.append('%s: %s' % (hoja, descripcion))
    return fallos


if __name__ == '__main__':
    problemas = _suite()
    if problemas:
        print('\n%d COMPROBACION(ES) FALLIDA(S):' % len(problemas))
        for p in problemas:
            print('  - %s' % p)
        sys.exit(1)
    print('\nTodas las plantillas reproducen los ejercicios del curso.')
