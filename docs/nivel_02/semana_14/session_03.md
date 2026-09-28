# Semana 14 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Comparando dos Fondos de Inversión

Eres un asesor financiero y tienes que recomendar un fondo a un cliente conservador. Analizas los retornos anuales de los últimos 5 años de dos fondos:

* **Fondo "Crecimiento Agresivo" (Retornos %):** 5, 15, -20, 30, 20
* **Fondo "Value Conservador" (Retornos %):** 6, 8, 5, 7, 9

**Cálculo para el Fondo "Crecimiento Agresivo":**
1. **Media:** $(5 + 15 - 20 + 30 + 20) / 5 = 50 / 5 = \mathbf{10\%}$
2. **Desviaciones respecto a la media:** $(5-10) = -5$; $(15-10) = 5$; $(-20-10) = -30$; $(30-10) = 20$; $(20-10) = 10$.
3. **Varianza:** $[(-5)^2 + (5)^2 + (-30)^2 + (20)^2 + (10)^2] / (5-1) = [25 + 25 + 900 + 400 + 100] / 4 = 1450 / 4 = \mathbf{362.5}$
4. **Desviación Estándar:** $\sqrt{362.5} = \mathbf{19.03\%}$

**Cálculo para el Fondo "Value Conservador":**
1. **Media:** $(6 + 8 + 5 + 7 + 9) / 5 = 35 / 5 = \mathbf{7\%}$
2. **Varianza:** $[(-1)^2 + (1)^2 + (-2)^2 + (0)^2 + (2)^2] / 4 = 10 / 4 = \mathbf{2.5}$
3. **Desviación Estándar:** $\sqrt{2.5} = \mathbf{1.58\%}$

**Conclusión Financiera con Coeficiente de Variación:**
* Fondo Agresivo: $CV = 19.03 / 10 = 1.90$ (1.9 unidades de riesgo por cada 1 de retorno).
* Fondo Conservador: $CV = 1.58 / 7 = 0.22$ (0.22 unidades de riesgo por cada 1 de retorno).
*El Fondo Conservador es matemáticamente superior en relación riesgo/return. Se lo recomiendas al cliente.*

---

## Segundo ejercicio: comparar dos activos con el coeficiente de variación

Un cliente te pide elegir entre dos fondos con estos retornos anuales de los últimos 5 años:

| Año | Fondo Conservador | Fondo Agresivo |
|---|---|---|
| 1 | 6 % | 22 % |
| 2 | 5 % | −12 % |
| 3 | 7 % | 30 % |
| 4 | 4 % | −8 % |
| 5 | 8 % | 28 % |

**Paso 1 — Media aritmética**

$$\bar{x}_C = \frac{6+5+7+4+8}{5} = 6.0\% \qquad \bar{x}_A = \frac{22-12+30-8+28}{5} = 12.0\%$$

**Paso 2 — Desviación estándar muestral**

*Conservador:* desviaciones $0, -1, 1, -2, 2$ → suma de cuadrados $= 10$

$$s_C = \sqrt{\frac{10}{4}} = \sqrt{2.5} = \mathbf{1.58\%}$$

*Agresivo:* desviaciones $10, -24, 18, -20, 16$ → suma de cuadrados $= 100+576+324+400+256 = 1656$

$$s_A = \sqrt{\frac{1656}{4}} = \sqrt{414} = \mathbf{20.35\%}$$

**Paso 3 — Coeficiente de variación**

$$CV_C = \frac{1.58}{6.0} = \mathbf{0.26} \qquad CV_A = \frac{20.35}{12.0} = \mathbf{1.70}$$

**El Agresivo rinde el doble pero asume 6,5 veces más riesgo por unidad de retorno.**

**Paso 4 — La media geométrica, que es la que el cliente cobra**

$$CAGR_C = (1.06 \times 1.05 \times 1.07 \times 1.04 \times 1.08)^{1/5} - 1 = \mathbf{5.99\%}$$

$$CAGR_A = (1.22 \times 0.88 \times 1.30 \times 0.92 \times 1.28)^{1/5} - 1 = \mathbf{10.45\%}$$

Fíjate en la brecha: el Conservador pierde 0,01 puntos entre media aritmética y geométrica; el
Agresivo pierde **1,55 puntos**. Es el *arrastre de volatilidad* que anticipaba la fórmula
$\approx \sigma^2/2$: con $\sigma = 20{,}35\%$, la pérdida esperada es
$0.2035^2/2 = 2.07$ puntos, del mismo orden de magnitud.

**La volatilidad no solo es riesgo: se come rentabilidad real.**

---

## Tercer ejercicio: por qué la media puede mentir

Una consultora informa que el **salario promedio** de una empresa de 10 empleados es de
$\$85,000$ anuales. Los salarios reales:

`[30, 32, 33, 34, 35, 36, 38, 40, 42, 530]` (en miles)

**Media:** $850/10 = \mathbf{\$85{,}000}$

**Mediana:** promedio del 5.º y 6.º valor ordenados $= (35+36)/2 = \mathbf{\$35{,}500}$

**El "empleado promedio" gana $85,000, pero 9 de cada 10 ganan menos de $42,000.** El fundador,
con $\$530,000$, arrastra la media él solo.

| Medida | Valor | Cuándo usarla |
|---|---|---|
| **Media** | $85,000 | Datos simétricos, sin valores extremos |
| **Mediana** | $35,500 | Datos asimétricos: salarios, precios de vivienda, patrimonios |
| **Moda** | — | Datos categóricos |

!!! tip "Dónde importa esto en finanzas"
    * **Múltiplos de comparables (Semana 38).** Se usa la **mediana** del sector, no la media:
      un solo comparable con un P/E de 90 distorsionaría la valuación entera.
    * **Retornos de un portafolio de capital riesgo.** La distribución es extremadamente
      asimétrica (unos pocos aciertos enormes); la mediana de los retornos de las participadas
      suele ser negativa aunque el fondo gane dinero.
    * **Ingresos de un país.** El PIB per cápita es una media. La mediana del ingreso cuenta una
      historia muy distinta, y es la que explica por qué "la economía va bien" y la gente no lo
      siente.

    **La regla:** si la media y la mediana difieren mucho, la distribución es asimétrica y la
    media por sí sola es engañosa. Repórtalas siempre juntas, junto con la desviación estándar.

---
