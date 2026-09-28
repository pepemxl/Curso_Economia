# Semana 21 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: Diagnosticando a "TechCorp"
Tienes los siguientes extractos de los estados financieros de TechCorp al cierre de año:
* Ventas: $1,000,000
* COGS: $600,000
* Utilidad Neta: $80,000
* Activo Corriente: $300,000 (de los cuales $50,000 es Inventario)
* Pasivo Corriente: $150,000
* Activos Totales: $1,000,000
* Patrimonio: $400,000 (lo demás es deuda)
* EBIT: $130,000; Gasto Financiero: $30,000

**Tu Diagnóstico de Ratios:**
1. **Liquidez:** Razón Corriente = 300k / 150k = **2.0**. (Muy sano, tiene $2 en activos por cada $1 de deuda a corto plazo). Prueba Ácida = (300k - 50k) / 150k = **1.66**. (Excelente, aún sin vender inventario, cubre sus deudas).
2. **Solvencia:** Cobertura de Intereses = 130k / 30k = **4.33x**. (Cubre los intereses 4.3 veces. Estructura de capital segura).
3. **Rentabilidad:** Margen Neto = 80k / 1,000k = **8%**. ROE = 80k / 400k = **20%**. (La empresa gana un 20% sobre el dinero de los accionistas. ¡Es una excelente inversión!)

---

## Por qué el diagnóstico anterior está incompleto

La conclusión *"ROE del 20 %, ¡excelente inversión!"* es exactamente el tipo de análisis
superficial que un ratio aislado invita a hacer. Descompongamos ese 20 % antes de celebrarlo.

**Dupont sobre los mismos datos:**

$$ROE = \underbrace{\frac{80}{1{,}000}}_{\text{Margen } 8\%} \times \underbrace{\frac{1{,}000}{1{,}000}}_{\text{Rotación } 1.0} \times \underbrace{\frac{1{,}000}{400}}_{\text{Apalancamiento } 2.5}$$

$$ROE = 8\% \times 1.0 \times 2.5 = \mathbf{20\%}$$

**El ROA es del 8 %** ($80/1{,}000$). El salto del 8 % al 20 % **lo produce íntegramente el
apalancamiento**: TechCorp tiene $\$600,000$ de deuda frente a $\$400,000$ de patrimonio.

Sin deuda, esta empresa rendiría un 8 %, no un 20 %. Eso no la invalida —el apalancamiento es
una herramienta legítima— pero cambia por completo la lectura: **lo que parecía calidad
operativa es en buena parte riesgo financiero**.

---

## Segundo ejercicio: el mismo diagnóstico bajo estrés

Un analista de crédito nunca evalúa una empresa en su mejor año. Somete a TechCorp a un
escenario adverso: **las ventas caen un 20 %** y, por apalancamiento operativo, **el EBIT cae un
40 %** (de 130 a 78).

| Ratio | Escenario base | Escenario adverso |
|---|---|---|
| Ventas | 1,000,000 | 800,000 |
| EBIT | 130,000 | **78,000** |
| Gasto financiero | 30,000 | 30,000 |
| EBT | 100,000 | **48,000** |
| Utilidad neta (20 % impuestos) | 80,000 | **38,400** |
| **Cobertura de intereses** | 4.33× | **2.60×** |
| **Margen neto** | 8.0 % | **4.8 %** |
| **ROE** | 20.0 % | **9.6 %** |

**El ROE se desploma a la mitad ante una caída del 20 % en ventas.** Esa es la contrapartida del
apalancamiento: amplifica en las dos direcciones.

Y si las tasas subieran, duplicando el gasto financiero a $\$60,000$ en el mismo escenario
adverso:

$$\text{Cobertura} = \frac{78{,}000}{60{,}000} = \mathbf{1.30\times}$$

Por debajo del *covenant* habitual de 2,0×. **TechCorp entraría en incumplimiento técnico.**

---

## El análisis que ningún ratio individual da: la comparación

Los ratios **no tienen significado absoluto**. Un margen del 8 % es magnífico en un supermercado
y catastrófico en una farmacéutica. Solo dicen algo en tres comparaciones:

**1. Contra la propia historia (análisis de tendencia).** ¿El margen mejora o se deteriora en
los últimos 3-5 años? Un ratio bueno en caída es peor señal que uno mediocre estable.

**2. Contra el sector.** Órdenes de magnitud típicos:

| Sector | Margen neto | Rotación de activos | ROE |
|---|---|---|---|
| Supermercados | 1-3 % | 2.5-3.5 | 12-18 % |
| Software | 15-30 % | 0.5-0.8 | 15-25 % |
| Bancos | 20-25 % | 0.05-0.1 | 8-15 % |
| Utilities | 8-12 % | 0.3-0.4 | 8-12 % |
| Farmacéutica | 15-25 % | 0.5-0.7 | 15-25 % |

Fíjate en la regularidad: **margen alto y rotación baja, o margen bajo y rotación alta.** Son
dos estrategias competitivas distintas —diferenciación o costos— y el Dupont las hace visibles
de inmediato.

**3. Contra los *covenants*.** Los contratos de deuda fijan umbrales concretos (cobertura
mínima, Deuda/EBITDA máximo). Un ratio que se acerca a su límite contractual es una alarma
inmediata, aunque en abstracto parezca aceptable.

!!! danger "Las trampas técnicas del cálculo de ratios"
    1. **Saldos puntuales frente a promedios.** El ROA usa una utilidad **de todo el año** sobre
       activos **de un solo día**. Lo correcto es usar el promedio del saldo inicial y final,
       sobre todo si hubo una adquisición.
    2. **Maquillaje de cierre (*window dressing*).** Una empresa puede pagar deuda de corto
       plazo justo antes del cierre para mejorar su razón corriente, y volver a endeudarse en
       enero. Compara varios trimestres, no solo el anual.
    3. **Deuda fuera de balance.** Arrendamientos operativos, garantías y compromisos con
       proveedores pueden ocultar apalancamiento real. Están en las **notas**, no en el balance.
    4. **Sectores donde los ratios estándar no aplican.** En un banco, el "inventario" no existe
       y la deuda **es** su materia prima: un D/E de 10 es normal. Los ratios bancarios son
       otros (margen de intermediación, ratio de capital, morosidad).

---
