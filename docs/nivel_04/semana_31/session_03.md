# Semana 31 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: Calculando la Pérdida Esperada (Riesgo de Crédito)
Eres el Director de Riesgos de un Banco Comercial. Tienes una cartera de 1,000 préstamos hipotecarios, cada uno por **$200,000**. El banco ha calculado estos parámetros basándose en su historial pasado y en el modelo de scoring de crédito:

* **EAD (Exposure at Default):** $200,000 ( saldo promedio del préstamo)
* **PD (Probability of Default):** 3% anual ( Hay un 97% de probabilidad de que el cliente pague la hipoteca sin problemas).
* **LGD (Loss Given Default):** 40% (Que la casa, en caso de ejecución de la hipoteca, solo cubra el 60% de la deuda debido a la caída de los precios inmobiliarios y comisiones legales).

**Cálculo Matemático (Pérdida Esperada de un Solo Préstamo):**
$$ EL = 0.03 \text{ (PD)} \times 0.40 \text{ (LGD)} \times \$200,000 \text{ (EAD)} $$

$$ EL = 0.012 \times \$200,000 = \mathbf{\$2,400} $$

**Cálculo para Toda la Cartera (1,000 clientes):**
$$ EL_{total} = 1,000 \times \$2,400 = \mathbf{\$2,400,000} $$

**Veredicto Financiero:**
El banco *sabe* matemáticamente que perderá $2.4 millones este año en su cartera hipotecaria. No es una sorpresa, es la estadística promedio. Por lo tanto, el banco cobra a todos los clientes un "spread" (ej. 1% extra de interés) para cubrir esos $2.4M. Si la recaudación de ese spread supera los $2.4M, el riesgo ha sido rentable y el banco gana dinero de forma segura.

---

## Segundo ejercicio: pérdida esperada frente a pérdida inesperada

El banco sabe que perderá $\$2,4$ millones. Lo que le puede matar **no es eso**, sino lo que no
espera. Cuantifiquémoslo.

**Paso 1 — La distribución de pérdidas si los impagos fueran independientes**

Con $n = 1{,}000$ préstamos y $PD = 3\%$, el número de impagos sigue una binomial:

$$\mu = np = 1{,}000 \times 0.03 = 30 \text{ impagos}$$

$$\sigma = \sqrt{np(1-p)} = \sqrt{1{,}000 \times 0.03 \times 0.97} = \sqrt{29.1} = 5.39$$

Cada impago cuesta $LGD \times EAD = 0.40 \times 200{,}000 = \$80{,}000$:

$$\sigma_{pérdida} = 5.39 \times 80{,}000 = \mathbf{\$431{,}400}$$

**Paso 2 — Capital económico al 99,9 % (el estándar de Basilea)**

$$UL = z_{99.9\%} \times \sigma = 3.09 \times 431{,}400 = \mathbf{\$1.33 \text{ millones}}$$

El banco necesitaría **$\$1,33$ M de capital** además de los $\$2,4$ M de provisiones. Pérdida
total en el peor escenario: $\$3,73$ M.

**Paso 3 — Y ahora, la corrección que lo cambia todo: la correlación**

El cálculo anterior asume que los impagos son **independientes**: que Juan deje de pagar su
hipoteca no dice nada sobre María. **Eso es falso.** Ambos pierden el empleo en la misma
recesión, y el valor de ambas casas cae a la vez.

Si introducimos una correlación de impago $\rho = 0.15$ (el valor que Basilea prescribe para
hipotecas), la desviación de la cartera crece drásticamente. Una aproximación:

$$\sigma_{corr} \approx \sigma_{indep}\sqrt{1 + (n-1)\rho} = 431{,}400 \times \sqrt{1 + 999(0.15)}$$

$$\sigma_{corr} \approx 431{,}400 \times 12.25 = \mathbf{\$5.28 \text{ millones}}$$

**La desviación se multiplica por 12.** El capital necesario pasa de $\$1,33$ M a más de
$\$16$ M.

!!! danger "La correlación es el riesgo que de verdad importa"
    Este es, en una fórmula, el error que provocó la crisis de 2008.

    Los modelos de las agencias de calificación asumían correlaciones bajas entre impagos
    hipotecarios de distintas regiones de Estados Unidos. Con ese supuesto, empaquetar miles de
    hipotecas *subprime* diversificaba el riesgo: las probabilidades de que fallaran todas a la
    vez eran ínfimas, y los tramos superiores merecían calificación AAA.

    **Cuando los precios de la vivienda cayeron a nivel nacional, la correlación saltó hacia 1.**
    La diversificación se evaporó exactamente cuando se la necesitaba, y los tramos "AAA"
    perdieron el 80 % de su valor.

    Es el mismo fenómeno que hundió a LTCM en 1998 (Semana 39) y el mismo que invalida una
    simulación Monte Carlo que ignore correlaciones (Semana 20). **En las crisis, todo
    correlaciona.**

---

## Los tres tipos de riesgo y cómo se miden

| Riesgo | Definición | Métrica principal | Capital según Basilea |
|---|---|---|---|
| **De mercado** | Pérdidas por movimientos de precios (tasas, divisas, acciones, materias primas) | VaR, Expected Shortfall | Modelo interno o estándar |
| **De crédito** | La contraparte no paga | $EL = PD \times LGD \times EAD$ | IRB o estándar por ponderaciones |
| **Operativo** | Fallos de procesos, personas, sistemas o eventos externos | Base de datos de pérdidas internas | Indicador de negocio |

**El riesgo operativo es el más subestimado**, precisamente porque no tiene una fórmula elegante.
Incluye fraude interno, errores de ejecución, ciberataques, fallos legales y desastres. Su
distribución tiene **colas extremadamente gordas**: muchísimos eventos pequeños y unos pocos
catastróficos.

Ejemplos que costaron más que cualquier pérdida de mercado de sus entidades:

* **Barings Bank (1995):** un solo operador, Nick Leeson, con controles inexistentes. El banco,
  de 233 años, quebró.
* **Société Générale (2008):** Jérôme Kerviel, $\$7.200$ millones.
* **Knight Capital (2012):** un despliegue de software defectuoso perdió $\$440$ millones **en
  45 minutos**.

A ellos se añaden dos riesgos que las tres categorías clásicas no capturan bien y que Basilea
III incorporó tras 2008:

* **Riesgo de liquidez:** ser solvente pero no poder convertir activos en efectivo a tiempo. Es
  lo que mide el LCR de la Semana 34, y lo que mató a Lehman y a Northern Rock.
* **Riesgo sistémico:** que el fallo de una entidad contagie al sistema entero por
  interconexión. Es la razón de que existan las entidades "demasiado grandes para caer" y los
  colchones de capital adicionales que se les exigen.

---
