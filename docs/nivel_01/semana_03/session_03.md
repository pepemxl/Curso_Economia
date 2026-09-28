# Semana 3 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Costos y Toma de Decisiones
Imagina que eres el gerente de una fábrica de zapatos. Tienes los siguientes costos a corto plazo:
* Costo Fijo Total (CFT) = $1,000 (alquiler de la nave industrial)
* Costo Variable Total (CVT) = $5 por unidad producida
* El zapato se vende en el mercado a un precio (P) de $10.

**Análisis paso a paso:**
Si actualmente produces 100 zapatos:
1. Costo Total (CT) = $1,000 (CFT) + $500 (CVT: 100x5) = $1,500
2. Costo Total Medio (CTMe) = $1,500 / 100 = $15 por zapato.
3. Costo Marginal (CMg) = Como el CVT es lineal, producir una unidad más siempre cuesta $5 más. CMg = $5.

**Decisión Gerencial:**
* Si Produces 100 unidades: Ingresos = $10x100 = $1,000. Costos = $1,500. **Pérdida de $500.**
* ¿Deberías cerrar la fábrica a corto plazo? **NO.** 
* Siguiendo la regla $IMg = CMg$. Tu IMg es $10 (el precio de venta). Tu CMg es $5. Como $10 > $5, **cada zapato adicional que produces te aporta $5 de margen de contribución** para ayudar a pagar el alquiler fijo.
* Producción óptima: Debes producir hasta que $CMg = P$, es decir, donde el costo marginal llegue a $10. Supongamos que esto ocurre en la unidad 200.
* A 200 unidades: Ingresos = $2,000. CT = $1,000 (Fijo) + $1,000 (Variable: 200x5) = $2,000. ¡Punto de equilibrio (Break-even) logrado! 

---

## Cuándo cerrar: la regla del corto y del largo plazo

El ejercicio anterior deja una pregunta abierta: la fábrica pierde dinero, ¿hasta cuándo hay
que aguantar? La respuesta depende del horizonte, y es una de las decisiones gerenciales más
mal tomadas en la práctica.

**A corto plazo** los costos fijos son **hundidos**: el alquiler de la nave se paga aunque no
produzcas ni un zapato. Entonces la única pregunta relevante es si cada unidad aporta algo para
cubrirlos:

$$\text{Producir si } P \ge CVMe \qquad \text{Cerrar si } P < CVMe$$

En el ejemplo: $P = 10$ y $CVMe = 5$. Cada zapato deja **$5 de margen de contribución**. Cerrar
significaría perder los $1,000 completos del alquiler; producir 100 unidades reduce la pérdida a
$500. **Producir es la decisión correcta aunque haya pérdidas contables.**

**A largo plazo** todos los costos son evitables: se puede no renovar el alquiler. La regla se
endurece:

$$\text{Permanecer si } P \ge CTMe \qquad \text{Salir si } P < CTMe$$

| Situación | Corto plazo | Largo plazo |
|---|---|---|
| $P \ge CTMe$ | Producir (con beneficio) | Permanecer |
| $CVMe \le P < CTMe$ | **Producir** (minimiza la pérdida) | **Salir** |
| $P < CVMe$ | **Cerrar** | Salir |

!!! danger "La falacia del costo hundido"
    El error inverso es igual de común: *"ya invertimos $2 millones en este proyecto, no podemos
    abandonarlo ahora"*. Ese dinero **ya no existe**: gastado está, se continúe o no. La única
    pregunta válida es si los flujos **futuros** justifican los costos **futuros**.

    Es exactamente el mismo razonamiento del VAN (Semana 25): en el análisis solo entran los
    **flujos incrementales**. Un proyecto en marcha se evalúa desde hoy hacia adelante, nunca
    mirando lo ya invertido.

---

## Segundo ejercicio: monopolio frente a competencia

La misma fábrica de zapatos, pero ahora es la **única** del país (tiene una patente). Enfrenta
la curva de demanda del mercado completo:

$$P = 20 - 0.05Q$$

Sus costos: $CFT = 1{,}000$ y $CMg = CVMe = 5$ (constante).

**Paso 1 — El ingreso marginal del monopolista**

$$IT = P \times Q = (20 - 0.05Q)Q = 20Q - 0.05Q^2$$

$$IMg = \frac{d\,IT}{dQ} = 20 - 0.1Q$$

Fíjate en el resultado: la curva de $IMg$ tiene **el doble de pendiente** que la de demanda.
Es una regularidad general de las demandas lineales, y la razón es la que vimos en la sesión
anterior: para vender una unidad más, el monopolista debe bajar el precio de **todas** las
unidades.

**Paso 2 — Cantidad y precio de monopolio**

$$IMg = CMg \Longrightarrow 20 - 0.1Q = 5 \Longrightarrow Q_M = 150$$

$$P_M = 20 - 0.05(150) = \$12.50$$

$$\pi_M = (12.50 - 5) \times 150 - 1{,}000 = 1{,}125 - 1{,}000 = \mathbf{\$125}$$

**Paso 3 — Comparación con competencia perfecta**

En competencia el precio se iguala al costo marginal, $P_C = CMg = 5$:

$$5 = 20 - 0.05Q \Longrightarrow Q_C = 300$$

| | Monopolio | Competencia |
|---|---|---|
| Precio | **$12.50** | $5.00 |
| Cantidad | **150** | 300 |
| Beneficio económico | +$125 | −$1,000 (no cubre el fijo) |

**El monopolista produce la mitad y cobra dos veces y media más.** Esa restricción deliberada
de la cantidad es el origen de la **pérdida de eficiencia** del monopolio, y la justificación
económica de las leyes antimonopolio.

Nota además el detalle incómodo: en competencia perfecta pura, con este costo fijo, **nadie
podría operar de forma rentable**. Cuando existen costos fijos grandes e indivisibles, la
competencia perfecta no es un equilibrio sostenible — es el caso del **monopolio natural**
(redes eléctricas, agua, ferrocarril), donde la respuesta no es prohibir el monopolio sino
regular su tarifa.

---

## Errores frecuentes en costos y estructuras de mercado

1. **Igualar $P = CMg$ cuando hay poder de mercado.** Esa condición solo vale en competencia
   perfecta, donde $P = IMg$. El monopolista iguala $IMg = CMg$ y **luego** lee el precio en la
   curva de demanda. Confundirlas es el error más caro del tema.
2. **Confundir beneficio contable con beneficio económico.** El económico descuenta también el
   **costo de oportunidad** del capital y del tiempo del dueño. Una empresa con beneficio
   contable positivo puede estar destruyendo valor si rinde menos que su WACC (Semana 24).
3. **Creer que el CMg siempre es constante.** En el primer ejercicio lo era porque el CVT era
   lineal. En la realidad tiene forma de U: primero baja por especialización, luego sube por
   rendimientos marginales decrecientes.
4. **Olvidar que el CMg corta al CTMe en su mínimo.** No es casualidad ni un dibujo bonito: si
   la unidad adicional cuesta menos que el promedio, el promedio baja; si cuesta más, sube. Por
   tanto se cruzan justo donde el promedio deja de bajar.
5. **Tratar el largo plazo como "muchos años".** En microeconomía el largo plazo se define por
   la **flexibilidad de los factores**, no por el calendario: es el horizonte en el que *todos*
   los costos se vuelven variables.

---
