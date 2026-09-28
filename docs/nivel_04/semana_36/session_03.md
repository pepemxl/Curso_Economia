# Semana 36 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Calculando el DTL en Excel
La empresa "MaqTec" compra una máquina de $10,000. 
* **Contablemente:** Depreciación lineal en 5 años = $2,000 / año.
* **Fiscalmente:** El gobierno permite depreciación acelerada = $4,000 en el Año 1.
* **EBIT antes de depreciación:** $10,000.
* **Tasa de Impuestos:** 25%.

**Cálculo del Año 1:**
1. **Ingreso Contable:** EBIT = $10,000 - $2,000 (Dep. Contable) = $8,000. Impuesto Contable = $8,000 × 25% = **$2,000**. (Esto aparece en el Estado de Resultados).
2. **Ingreso Fiscal:** EBIT Fiscal = $10,000 - $4,000 (Dep. Acelerada) = $6,000. Impuesto Pagado en Efectivo = $6,000 × 25% = **$1,500**. (Esto sale de la caja del banco).
3. **Diferencia Temporaria:** Pagaste $500 menos hoy de lo que la contabilidad dice que debes.
4. **DTL (Año 1):** Registramos un Pasivo por Impuesto Diferido (DTL) de **$500**. 
* **Asiento Contable:**
  * Débito: Gasto por Impuestos (P&L) $2,000
  * Crédito: Efectivo (Balance) $1,500
  * Crédito: Pasivo por Impuestos Diferidos DTL (Balance) $500

Cuando la depreciación fiscal se agote en el futuro, ese DTL de $500 se revertirá pagando más impuestos en efectivo de los que marque el P&L ese año.

---

## Segundo ejercicio: la reversión del impuesto diferido

El asiento del Año 1 es solo el principio. Lo interesante es qué pasa después, porque un DTL
**no es deuda permanente: se revierte**.

MaqTec, depreciación fiscal acelerada sobre 5 años: $\$4,000$, $\$3,000$, $\$2,000$,
$\$1,000$, $\$0$. Contable, lineal: $\$2,000$ cada año. EBIT antes de depreciación:
$\$10,000$ constante. Impuesto: 25 %.

| Año | Dep. contable | Dep. fiscal | Base contable | Base fiscal | Impuesto P&L | Impuesto pagado | Δ DTL | **DTL acumulado** |
|---|---|---|---|---|---|---|---|---|
| 1 | 2,000 | 4,000 | 8,000 | 6,000 | 2,000 | 1,500 | +500 | **500** |
| 2 | 2,000 | 3,000 | 8,000 | 7,000 | 2,000 | 1,750 | +250 | **750** |
| 3 | 2,000 | 2,000 | 8,000 | 8,000 | 2,000 | 2,000 | 0 | **750** |
| 4 | 2,000 | 1,000 | 8,000 | 9,000 | 2,000 | 2,250 | **−250** | **500** |
| 5 | 2,000 | 0 | 8,000 | 10,000 | 2,000 | 2,500 | **−500** | **0** |
| | **10,000** | **10,000** | | | **10,000** | **10,000** | **0** | |

**Las dos columnas de impuesto suman exactamente lo mismo: $\$10,000$.**

El DTL crece hasta $\$750$ en el año 2, se estabiliza y **revierte a cero** en el año 5. La
depreciación acelerada no reduce el impuesto total: lo **desplaza en el tiempo**.

**¿Y entonces por qué vale la pena?** Por el valor del dinero en el tiempo. Al 8 %, el valor
presente de pagar $1{,}500, 1{,}750, 2{,}000, 2{,}250, 2{,}500$ es menor que el de pagar
$2{,}000$ cinco veces:

$$VP_{acelerada} = \$7{,}832 \qquad VP_{lineal} = \$7{,}985$$

**Un ahorro de $\$153$ en valor presente**, gratis, solo por el calendario. Es precisamente el
incentivo que el gobierno quiere dar a la inversión en capital.

!!! tip "Por qué un analista trata el DTL como deuda... a veces"
    Un DTL es una obligación futura con el fisco, así que la lógica dice restarlo del valor de
    la empresa como si fuera deuda. **Pero hay un matiz decisivo.**

    Si la empresa **sigue invirtiendo** en activos nuevos año tras año, los DTL de las
    inversiones nuevas compensan las reversiones de las viejas, y el **saldo de DTL nunca baja**.
    En la práctica se convierte en un **préstamo perpetuo sin intereses del gobierno**, y
    tratarlo como deuda exigible subvalúa la empresa.

    La regla práctica:

    * **Empresa en crecimiento con CapEx sostenido** → el DTL es cuasi-permanente. No lo restes
      del Enterprise Value, o hazlo solo por su valor presente.
    * **Empresa madura o en declive, con CapEx cayendo** → el DTL **sí revertirá** y consumirá
      caja real. Trátalo como deuda.

    Mira siempre la **tendencia del saldo de DTL** en las notas, no solo su nivel. Un DTL
    creciente durante años es señal de inversión; un DTL que empieza a caer anticipa mayores
    pagos de impuestos y menor flujo de caja libre en los años siguientes.

---

## Del impuesto contable al impuesto en caja

Para un modelo de valuación, la distinción es operativa:

$$\text{Impuesto en caja} = \text{Impuesto del P\&L} - \Delta DTL + \Delta DTA$$

Y la **tasa efectiva de caja**, que es la que importa para el FCFF:

$$t_{caja} = \frac{\text{Impuesto efectivamente pagado}}{EBT}$$

**Las tres tasas que hay que distinguir**, y que los estados financieros mezclan alegremente:

| Tasa | Definición | Para qué sirve |
|---|---|---|
| **Estatutaria** | La del código fiscal (ej. 25 %) | Punto de partida; casi nunca es la real |
| **Efectiva contable** | Gasto por impuestos / EBT | La que aparece en el P&L |
| **Efectiva de caja** | Impuesto pagado / EBT | **La que se usa en el DCF** |

**Al proyectar en un DCF:** usa la tasa **estatutaria** para el largo plazo y la **efectiva de
caja** para los primeros años si hay diferencias temporarias significativas o pérdidas fiscales
acumuladas (NOL) por compensar. Suponer una tasa efectiva del 12 % a perpetuidad porque la
empresa la tuvo el año pasado es el error que infla las valuaciones de las multinacionales — el
mismo que analizaste en el ejercicio de la sesión anterior.

---
