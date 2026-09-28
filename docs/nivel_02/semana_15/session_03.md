# Semana 15 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: El primer cálculo de Riesgo (VaR)
Tu portafolio de inversiones tiene un Retorno Promedio Esperado ($\mu$) del **10%** y una Desviación Estándar ($\sigma$) de la rentabilidad del **15%**. Asumimos que sigue una distribución Normal.

Tu jefe te pregunta: *¿Cuál es la probabilidad de que el portafolio pierda dinero (tenga un retorno menor al 0%) el próximo año?*

**Cálculo paso a paso:**
1. Tenemos $x = 0\%$. Queremos saber $P(X < 0)$.
2. Estandarizamos a Variable $Z$:
   $$ Z = \frac{0 - 10}{15} = \frac{-10}{15} = -0.667 $$
3. Buscamos en la Tabla de Distribución Normal Estándar (Tabla Z) el valor de $-0.667$.
4. La tabla nos arroja un valor de **0.2524**.

**Conclusión:** Hay una **25.24% de probabilidad** matemática de que el portafolio tenga un rendimiento negativo (pérdida) este año. Con esa probabilidad, el área de "Gestión de Riesgos" exige que el fondo reserve capital en efectivo como colchón para soportar esa posible caída.

---

## Segundo ejercicio: probabilidad condicional y el error del fiscal

Un banco usa un modelo de *scoring* para detectar créditos que acabarán en impago. El modelo
tiene una precisión del **95 %**: si un cliente va a impagar, lo detecta el 95 % de las veces;
y si no va a impagar, lo declara sano el 95 % de las veces.

La tasa histórica de impago de la cartera es del **2 %**.

**Pregunta:** el modelo marca a un cliente como "alto riesgo". ¿Cuál es la probabilidad de que
realmente impague?

**La respuesta intuitiva es 95 %. La respuesta correcta es 27,9 %.**

**Teorema de Bayes:**

$$P(D \mid +) = \frac{P(+ \mid D) \cdot P(D)}{P(+ \mid D)P(D) + P(+ \mid \neg D)P(\neg D)}$$

$$P(D \mid +) = \frac{0.95 \times 0.02}{0.95 \times 0.02 + 0.05 \times 0.98} = \frac{0.019}{0.019 + 0.049} = \frac{0.019}{0.068}$$

$$P(D \mid +) = \mathbf{27.9\%}$$

**Verifícalo con frecuencias, que es mucho más intuitivo.** Sobre 10,000 clientes:

| | Impagan (200) | No impagan (9,800) | Total |
|---|---|---|---|
| **Modelo dice "alto riesgo"** | 190 | **490** | 680 |
| **Modelo dice "sano"** | 10 | 9,310 | 9,320 |

De los 680 marcados como alto riesgo, solo 190 impagan de verdad: $190/680 = 27.9\%$.

**Por qué:** los que **no** impagan son 49 veces más numerosos. Aunque el modelo falle solo el
5 % de las veces con ellos, ese 5 % de 9,800 son 490 falsos positivos, que aplastan a los 190
verdaderos.

!!! danger "La falacia de la tasa base"
    Es el error estadístico más costoso de las finanzas y la medicina. Confundir
    $P(\text{señal} \mid \text{evento})$ con $P(\text{evento} \mid \text{señal})$.

    **Dónde muerde en finanzas:**

    * **Detección de fraude.** Un modelo con 99 % de precisión sobre una tasa de fraude del
      0,1 % genera 10 falsos positivos por cada fraude real.
    * **Señales de trading.** Un indicador que "acierta el 80 % de los cracks" es inútil si
      también dispara en el 20 % de los mercados normales: como los cracks son raros, casi
      todas sus señales serán falsas alarmas.
    * **Calificaciones crediticias.** Es la razón por la que un rating BBB no significa 0 % de
      riesgo, sino una probabilidad de impago históricamente baja **sobre una base amplia**.

    **La regla práctica:** cuando el evento que buscas es raro, **la tasa base domina la
    precisión del test**. Siempre pregunta por la prevalencia antes de creer en un porcentaje de
    acierto.

---

## Tercer ejercicio: valor esperado y la decisión de un proyecto

Un fondo evalúa un proyecto minero. Tres escenarios posibles a un año:

| Escenario | Probabilidad | Resultado |
|---|---|---|
| Yacimiento rico | 20 % | +$50 M |
| Yacimiento medio | 50 % | +$10 M |
| Yacimiento seco | 30 % | −$25 M |

**Paso 1 — Valor esperado**

$$E[X] = 0.20(50) + 0.50(10) + 0.30(-25) = 10 + 5 - 7.5 = \mathbf{+\$7.5 \text{ M}}$$

**Paso 2 — Desviación estándar**

$$\sigma^2 = \sum p_i (x_i - E[X])^2$$

| Escenario | $p_i$ | $x_i - E[X]$ | $(x_i-E[X])^2$ | $p_i \times$ |
|---|---|---|---|---|
| Rico | 0.20 | 42.5 | 1,806.25 | 361.25 |
| Medio | 0.50 | 2.5 | 6.25 | 3.13 |
| Seco | 0.30 | −32.5 | 1,056.25 | 316.88 |
| | | | **Varianza** | **681.26** |

$$\sigma = \sqrt{681.26} = \mathbf{\$26.1 \text{ M}}$$

**Paso 3 — La decisión**

$$CV = \frac{26.1}{7.5} = \mathbf{3.48}$$

El valor esperado es positivo, pero **la desviación estándar es 3,5 veces mayor que el retorno
esperado**. Y hay un **30 % de probabilidad de perder $\$25 millones**.

Un valor esperado positivo **no basta** para aceptar un proyecto. Hay que preguntarse además:

* ¿Puede el fondo **sobrevivir** al escenario malo? Si $\$25 M es el 5 % del fondo, sí. Si es
  el 60 %, la apuesta es de vida o muerte aunque el VE sea positivo.
* ¿Es una decisión **repetible**? El valor esperado es una promesa estadística que se cumple
  sobre muchas repeticiones. Con una sola tirada, lo relevante es la distribución completa.
* ¿Está **correlacionado** con el resto de la cartera? Si el fondo ya está lleno de mineras, el
  escenario seco llegará justo cuando todo lo demás también caiga.

!!! tip "El puente hacia el Nivel 4"
    Este ejercicio es, en miniatura, todo lo que harás en la Semana 20 (Monte Carlo, que
    sustituye tres escenarios por mil) y en la Semana 32 (VaR y Expected Shortfall, que miden
    precisamente la cola izquierda de esta distribución).

    La idea central es la misma en los tres: **una decisión financiera no se toma con un número,
    se toma con una distribución.**

---
