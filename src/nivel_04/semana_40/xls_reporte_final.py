# -*- coding: utf-8 -*-
"""Semana 40: andamiaje del modelo de Excel que acompana al reporte de inversion.

Viene con datos de ejemplo coherentes para que el modelo funcione desde el
primer momento; el alumno los sustituye por los de la empresa que elija.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.formatting.rule import CellIsRule
from estilo_excel import (titulo, seccion, cabecera, fila_datos, nota, anchos, guardar,
                          NUM_MILES, NUM_DEC, NUM_PCT, NUM_PCT2, R_INPUT, R_TOTAL,
                          F_SECCION, F_TOTAL, F_NOTA, BORDE, AZUL, VERDE, ROJO)

N = 5
col = lambda i: chr(ord('B') + i)


def hoja_supuestos(wb):
    ws = wb.create_sheet('1 Supuestos')
    anchos(ws, 46, 14, 7)
    f = titulo(ws, 'SUPUESTOS  ·  sustituye los datos de ejemplo por los de tu empresa', 7)
    f = nota(ws, f, 'Regla de oro: ningun numero escrito a mano fuera de esta hoja. Todo lo demas son formulas.')
    f += 1

    f = seccion(ws, f, 'Escenario')
    f = fila_datos(ws, f, 'Escenario (1=Base  2=Optimista  3=Pesimista)', [1], fmt='0', input_=True)
    r_esc = 'B%d' % (f - 1)
    f += 1
    f = cabecera(ws, f, ['Supuesto', 'Base', 'Optimista', 'Pesimista'])
    tabla = f
    escenarios = [('Crecimiento de ventas', 0.08, 0.14, 0.02, NUM_PCT),
                  ('Margen EBIT', 0.18, 0.22, 0.13, NUM_PCT),
                  ('CapEx como % de ventas', 0.06, 0.05, 0.08, NUM_PCT),
                  ('Cambio en capital de trabajo como % de ventas', 0.02, 0.015, 0.035, NUM_PCT)]
    for etiqueta, b, o, p, fmt in escenarios:
        f = fila_datos(ws, f, etiqueta, [b, o, p], fmt=fmt, input_=True)
    f += 1

    f = seccion(ws, f, 'Supuestos activos')
    activos = []
    for i, (etiqueta, _, _, _, fmt) in enumerate(escenarios):
        fo = tabla + i
        f = fila_datos(ws, f, etiqueta,
                       ['=IFERROR(CHOOSE($%s,B%d,C%d,D%d),"Escenario invalido")'
                        % (r_esc, fo, fo, fo)], fmt=fmt)
        activos.append('\'1 Supuestos\'!$B$%d' % (f - 1))
    f += 1

    f = seccion(ws, f, 'Datos historicos y financieros')
    fijos = [('Ventas del ultimo ano reportado', 10000, NUM_MILES),
             ('Depreciacion como % de ventas', 0.04, NUM_PCT),
             ('Tasa impositiva efectiva', 0.25, NUM_PCT),
             ('Deuda financiera total', 3000, NUM_MILES),
             ('Efectivo y equivalentes', 800, NUM_MILES),
             ('Acciones en circulacion (millones)', 315, NUM_DEC),
             ('Precio actual de mercado por accion', 42.0, NUM_DEC)]
    refs = []
    for etiqueta, v, fmt in fijos:
        f = fila_datos(ws, f, etiqueta, [v], fmt=fmt, input_=True)
        refs.append('\'1 Supuestos\'!$B$%d' % (f - 1))
    f += 1

    f = seccion(ws, f, 'Costo de capital (WACC)')
    wacc_in = [('Tasa libre de riesgo', 0.04, NUM_PCT2),
               ('Beta', 1.15, NUM_DEC),
               ('Prima por riesgo de mercado', 0.055, NUM_PCT2),
               ('Costo de la deuda antes de impuestos', 0.065, NUM_PCT2)]
    rw = []
    for etiqueta, v, fmt in wacc_in:
        f = fila_datos(ws, f, etiqueta, [v], fmt=fmt, input_=True)
        rw.append('B%d' % (f - 1))
    f = fila_datos(ws, f, 'Costo del patrimonio (CAPM)',
                   ['=%s+%s*%s' % (rw[0], rw[1], rw[2])], fmt=NUM_PCT2)
    r_re = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'Valor de mercado del patrimonio  (precio x acciones)',
                   ['=%s*%s' % (refs[6], refs[5])], fmt=NUM_MILES)
    r_E = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'WACC',
                   ['=(%s/(%s+%s))*%s+(%s/(%s+%s))*%s*(1-%s)'
                    % (r_E, r_E, refs[3], r_re, refs[3], r_E, refs[3], rw[3], refs[2])],
                   fmt=NUM_PCT2, total=True)
    r_wacc = '\'1 Supuestos\'!$B$%d' % (f - 1)
    ws['B%d' % (f - 1)].font = Font(bold=True, size=13)
    f = fila_datos(ws, f, 'Crecimiento perpetuo (g)', [0.02], fmt=NUM_PCT2, input_=True)
    r_g = '\'1 Supuestos\'!$B$%d' % (f - 1)
    f = nota(ws, f, 'g nunca debe superar el crecimiento nominal de la economia (2-3%). Y jamas al WACC.')

    return dict(crec=activos[0], margen=activos[1], capex=activos[2], nwc=activos[3],
                ventas0=refs[0], dep=refs[1], tax=refs[2], deuda=refs[3],
                caja=refs[4], acciones=refs[5], precio=refs[6],
                wacc=r_wacc, g=r_g)


def hoja_proyeccion(wb, r):
    ws = wb.create_sheet('2 Proyeccion')
    anchos(ws, 46, 14, 7)
    f = titulo(ws, 'PROYECCION DE FLUJOS A %d ANOS' % N, 7)
    f = cabecera(ws, f, ['Concepto'] + ['Ano %d' % i for i in range(N + 1)])

    f = fila_datos(ws, f, 'Ventas',
                   ['=%s' % r['ventas0']] +
                   ['=%s%d*(1+%s)' % (col(i - 1), f, r['crec']) for i in range(1, N + 1)])
    r_v = f - 1
    f = fila_datos(ws, f, 'EBIT',
                   ['=%s%d*%s' % (col(i), r_v, r['margen']) for i in range(N + 1)], total=True)
    r_ebit = f - 1
    f = fila_datos(ws, f, 'NOPAT  =  EBIT x (1 - t)',
                   ['=%s%d*(1-%s)' % (col(i), r_ebit, r['tax']) for i in range(N + 1)], total=True)
    r_nopat = f - 1
    f = fila_datos(ws, f, '(+) Depreciacion y amortizacion',
                   ['=%s%d*%s' % (col(i), r_v, r['dep']) for i in range(N + 1)])
    r_dep = f - 1
    f = fila_datos(ws, f, '(-) CapEx',
                   ['=-%s%d*%s' % (col(i), r_v, r['capex']) for i in range(N + 1)])
    r_capex = f - 1
    f = fila_datos(ws, f, '(-) Cambio en capital de trabajo',
                   ['=-%s%d*%s' % (col(i), r_v, r['nwc']) for i in range(N + 1)])
    r_nwc = f - 1
    f = fila_datos(ws, f, 'FCFF',
                   ['=%s%d+%s%d+%s%d+%s%d' % (col(i), r_nopat, col(i), r_dep,
                                              col(i), r_capex, col(i), r_nwc)
                    for i in range(N + 1)], total=True)
    r_fcff = f - 1
    f += 1
    f = nota(ws, f, 'El FCFF no resta intereses: pertenece a accionistas Y acreedores, y el financiamiento ya esta en el WACC.')
    return dict(fcff=r_fcff, ventas=r_v, ebit=r_ebit, dep=r_dep)


def hoja_dcf(wb, r, p):
    ws = wb.create_sheet('3 Valuacion DCF')
    anchos(ws, 46, 16, 6)
    f = titulo(ws, 'VALUACION POR DCF', 6)
    f = cabecera(ws, f, ['Concepto'] + ['Ano %d' % i for i in range(1, N + 1)])
    f = fila_datos(ws, f, 'FCFF proyectado',
                   ["='2 Proyeccion'!%s%d" % (col(i), p['fcff']) for i in range(1, N + 1)])
    r_f = f - 1
    f = fila_datos(ws, f, 'Factor de descuento',
                   ['=1/(1+%s)^%d' % (r['wacc'], i) for i in range(1, N + 1)], fmt='0.0000')
    r_fd = f - 1
    f = fila_datos(ws, f, 'Valor presente',
                   ['=%s%d*%s%d' % (col(i - 1), r_f, col(i - 1), r_fd) for i in range(1, N + 1)],
                   fmt=NUM_DEC)
    r_vp = f - 1
    f += 1
    f = fila_datos(ws, f, 'Suma de VP explicitos',
                   ['=SUM(B%d:%s%d)' % (r_vp, col(N - 1), r_vp)], fmt=NUM_DEC, total=True)
    r_suma = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'Valor terminal (Gordon) al final del Ano %d' % N,
                   ['=IFERROR(%s%d*(1+%s)/(%s-%s),"g >= WACC: revisa los supuestos")'
                    % (col(N - 1), r_f, r['g'], r['wacc'], r['g'])], fmt=NUM_DEC)
    r_tv = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'VP del valor terminal',
                   ['=%s*%s%d' % (r_tv, col(N - 1), r_fd)], fmt=NUM_DEC, total=True)
    r_vptv = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'Peso del valor terminal sobre el EV',
                   ['=%s/(%s+%s)' % (r_vptv, r_suma, r_vptv)], fmt=NUM_PCT)
    f += 1
    f = seccion(ws, f, 'Puente al valor por accion')
    f = fila_datos(ws, f, 'ENTERPRISE VALUE', ['=%s+%s' % (r_suma, r_vptv)],
                   fmt=NUM_DEC, total=True)
    r_ev = 'B%d' % (f - 1)
    f = fila_datos(ws, f, '(-) Deuda financiera', ['=-%s' % r['deuda']], fmt=NUM_DEC)
    f = fila_datos(ws, f, '(+) Efectivo y equivalentes', ['=%s' % r['caja']], fmt=NUM_DEC)
    f = fila_datos(ws, f, 'EQUITY VALUE', ['=%s-%s+%s' % (r_ev, r['deuda'], r['caja'])],
                   fmt=NUM_DEC, total=True)
    r_eq = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'TARGET PRICE POR DCF',
                   ['=IFERROR(%s/%s,"Revisa las acciones")' % (r_eq, r['acciones'])],
                   fmt=NUM_DEC, total=True)
    r_tp = '\'3 Valuacion DCF\'!$B$%d' % (f - 1)
    ws['B%d' % (f - 1)].font = Font(bold=True, size=14)
    return dict(tp=r_tp)


def hoja_comps(wb, r, p, d):
    ws = wb.create_sheet('4 Comparables')
    anchos(ws, 34, 15, 6)
    f = titulo(ws, 'VALUACION RELATIVA POR MULTIPLOS (COMPS)', 6)
    f = cabecera(ws, f, ['Empresa comparable', 'EV/EBITDA', 'P/E', 'P/S', 'Crecimiento'])
    prim = f
    ejemplo = [('Comparable 1', 6.8, 14.2, 1.1, 0.07),
               ('Comparable 2', 7.6, 16.4, 1.4, 0.11),
               ('Comparable 3', 6.2, 12.9, 0.9, 0.04),
               ('Comparable 4', 7.9, 17.1, 1.5, 0.09)]
    for nombre, ev, pe, ps, g in ejemplo:
        f = fila_datos(ws, f, nombre, [ev, pe, ps, g], fmt=NUM_DEC, input_=True)
    ult = f - 1
    f = fila_datos(ws, f, 'MEDIANA del sector',
                   ['=MEDIAN(%s%d:%s%d)' % (c, prim, c, ult) for c in 'BCDE'],
                   fmt=NUM_DEC, total=True)
    r_med = f - 1
    f = nota(ws, f, 'Usa la MEDIANA, no la media: un solo comparable atipico distorsiona el promedio.')
    f += 1

    f = seccion(ws, f, 'Aplicacion del multiplo a tu empresa')
    f = fila_datos(ws, f, 'EBITDA del Ano 1 (EBIT + D&A)',
                   ["='2 Proyeccion'!C%d+'2 Proyeccion'!C%d" % (p['ebit'], p['dep'])],
                   fmt=NUM_DEC)
    r_ebitda = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'Enterprise Value implicito  (mediana EV/EBITDA x EBITDA)',
                   ['=B%d*%s' % (r_med, r_ebitda)], fmt=NUM_DEC)
    r_evi = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'Equity Value implicito',
                   ['=%s-%s+%s' % (r_evi, r['deuda'], r['caja'])], fmt=NUM_DEC)
    r_eqi = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'TARGET PRICE POR COMPS',
                   ['=IFERROR(%s/%s,"Revisa las acciones")' % (r_eqi, r['acciones'])],
                   fmt=NUM_DEC, total=True)
    r_tpc = '\'4 Comparables\'!$B$%d' % (f - 1)
    f += 1

    f = seccion(ws, f, 'Precio objetivo mezclado (Blended)')
    f = fila_datos(ws, f, 'Peso del DCF', [0.60], fmt=NUM_PCT, input_=True)
    r_w = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'Peso de los Comps', ['=1-%s' % r_w], fmt=NUM_PCT)
    r_w2 = 'B%d' % (f - 1)
    f = fila_datos(ws, f, 'Target price DCF', ['=%s' % d['tp']], fmt=NUM_DEC)
    f = fila_datos(ws, f, 'Target price Comps', ['=%s' % r_tpc], fmt=NUM_DEC)
    f = fila_datos(ws, f, 'PRECIO OBJETIVO FINAL',
                   ['=%s*%s+%s*%s' % (r_w, d['tp'], r_w2, r_tpc)], fmt=NUM_DEC, total=True)
    r_tpf = 'B%d' % (f - 1)
    ws['B%d' % (f - 1)].font = Font(bold=True, size=14)
    f = fila_datos(ws, f, 'Precio actual de mercado', ['=%s' % r['precio']], fmt=NUM_DEC)
    f = fila_datos(ws, f, 'UPSIDE / DOWNSIDE',
                   ['=IFERROR(%s/%s-1,"")' % (r_tpf, r['precio'])], fmt=NUM_PCT, total=True)
    r_up = f - 1
    f = fila_datos(ws, f, 'RECOMENDACION',
                   ['=IF(B%d>0.15,"COMPRAR",IF(B%d<-0.10,"VENDER","MANTENER"))' % (r_up, r_up)],
                   fmt='General', total=True)
    ws['B%d' % (f - 1)].font = Font(bold=True, size=14)
    ws['B%d' % (f - 1)].alignment = Alignment(horizontal='center')
    f = nota(ws, f, 'Los umbrales (+15% / -10%) son convencion habitual de research; ajustalos y justificalos.')


def hoja_rubrica(wb):
    ws = wb.create_sheet('5 Rubrica')
    anchos(ws, 76, 12, 3)
    f = titulo(ws, 'AUTOEVALUACION CONTRA LA RUBRICA (100 puntos)', 3)
    f = nota(ws, f, 'Puntuate antes de entregar. Escribe tu puntaje en la columna amarilla.')
    f += 1
    f = cabecera(ws, f, ['Criterio', 'Maximo', 'Tu puntaje'])
    prim = f
    criterios = [
        ('Correctitud matematica: DCF y WACC bien calculados, FCFF pasa la prueba, Excel sin loops rotos', 30),
        ('Profundidad de analisis: explica el POR QUE de los numeros, identifica banderas rojas o ventajas reales', 30),
        ('Coherencia macroeconomica: los supuestos son consistentes con el ciclo y las tasas actuales', 15),
        ('Presentacion y comunicacion: reporte claro, profesional, recomendacion coherente con los numeros', 15),
        ('Gestion de riesgos: riesgos logicos identificados, con coberturas o puntos de salida', 10),
    ]
    for texto, maximo in criterios:
        f = fila_datos(ws, f, texto, [maximo, 0], fmt='0')
        ws.cell(f - 1, 3).fill = R_INPUT
    ult = f - 1
    f = fila_datos(ws, f, 'TOTAL',
                   ['=SUM(B%d:B%d)' % (prim, ult), '=SUM(C%d:C%d)' % (prim, ult)],
                   fmt='0', total=True)
    r_tot = f - 1
    ws.conditional_formatting.add('C%d' % r_tot, CellIsRule(
        operator='greaterThanOrEqual', formula=['70'],
        fill=PatternFill('solid', fgColor='C6EFCE'), font=Font(color='006100', bold=True)))
    ws.conditional_formatting.add('C%d' % r_tot, CellIsRule(
        operator='lessThan', formula=['70'],
        fill=PatternFill('solid', fgColor='FFC7CE'), font=Font(color='9C0006', bold=True)))
    f += 1
    f = seccion(ws, f, 'Comprobaciones tecnicas antes de entregar')
    for chk in ['El balance del modelo cuadra en TODOS los anos proyectados',
                'El valor terminal no supera el 85% del Enterprise Value',
                'g es menor que el WACC y no supera el 3%',
                'Los tres escenarios (base, optimista, pesimista) funcionan sin errores',
                'Ninguna celda de calculo tiene numeros escritos a mano',
                'Las fuentes de los datos historicos estan citadas']:
        ws.cell(f, 1, u'☐  ' + chk)
        f += 1


def main():
    wb = Workbook(); wb.remove(wb.active)
    r = hoja_supuestos(wb)
    p = hoja_proyeccion(wb, r)
    d = hoja_dcf(wb, r, p)
    hoja_comps(wb, r, p, d)
    hoja_rubrica(wb)
    wb.active = 0
    guardar(wb, 'plantilla_reporte_final.xlsx')


if __name__ == '__main__':
    main()
