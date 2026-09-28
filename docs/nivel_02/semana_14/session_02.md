# Semana 14 · Sesión 2: Profundización

## 4. Medidas de Dispersión (El Alma del Riesgo)
Saber que el retorno promedio de una acción es del 10% no sirve de nada si no sabes *cuánto se aleja* ese retorno del 10% en los peores y mejores años. La dispersión mide el riesgo.

1. **Rango (Range):** La diferencia entre el valor máximo y el mínimo. Muy básico y sensible a outliers.
2. **Varianza ($\sigma^2$ o $s^2$):** El promedio de las desviaciones al cuadrado respecto a la media.
   * *Fórmula (Muestra):* $s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1}$
   * *(Nota: Se elevan al cuadrado para que los valores negativos no anulen a los positivos).*
3. **Desviación Estándar ($\sigma$ o $s$):** Es la raíz cuadrada de la varianza.
   * *Fórmula:* $s = \sqrt{s^2}$
   > **💥 Impacto Financiero:** La Desviación Estándar es la definición matemática universal de **"Volatilidad"**. Un bono del gobierno tiene una desviación estándar del 3% (bajo riesgo). Una criptomoneda tiene una desviación estándar del 80% (alto riesgo). A mayor desviación, mayor es el riesgo de perder o ganar dinero.
4. **Coeficiente de Variación (CV):** Es la desviación estándar dividida por la media. $CV = \frac{s}{\bar{x}}$
   * Sirve para comparar el riesgo relativo entre dos inversiones. Te dice cuánto riesgo asumas por cada unidad de retorno.

---

## 5. Asimetría (Skewness) y Gráficos
No todos los datos se distribuyen de forma perfecta simétrica (como una campana perfecta).

* **Distribución Simétrica:** Media = Mediana = Moda. (Ej. Altura de hombres adultos).
* **Sesgo Positivo (Right-skewed):** La cola larga está hacia la derecha. La media es mayor que la mediana. *Ejemplo financiero:* Los retornos de las acciones de startups. La mayoría quiebra (retornos de -100%), pero unas pocas dan retornos de +10,000%. *(Media Alta, Mediana Baja).*
* **Sesgo Negativo (Left-skewed):** La cola larga está hacia la izquierda. *Ejemplo financiero:* Retornos de venta de opciones (Ventas de Put desnudos). La mayoría de los meses ganas un pequeño premio (primas), pero ocasionalmente sufres pérdidas masivas (-500%). ¡Cuidado con estas estrategias!

---

## Asimetría y curtosis: por qué los retornos no son una campana

La media y la desviación estándar describen bien una distribución **normal**. Los retornos
financieros no lo son, y los dos momentos siguientes explican por qué.

**Asimetría (*skewness*) — el tercer momento**

| Tipo | Forma | Relación | Ejemplo financiero |
|---|---|---|---|
| **Positiva** | Cola larga a la derecha | Media > Mediana | Capital riesgo: muchas pérdidas pequeñas, pocos aciertos enormes |
| **Simétrica** | Campana | Media = Mediana | El supuesto de los modelos |
| **Negativa** | Cola larga a la izquierda | **Media < Mediana** | **Acciones**: subidas graduales, caídas abruptas |

**Los retornos bursátiles tienen asimetría negativa**, y eso importa: significa que el
"escenario típico" es mejor que el promedio, pero cuando va mal, va **muy** mal. Un inversionista
que solo mire la media subestima la profundidad de las caídas.

**Curtosis — el cuarto momento**

Mide el grosor de las colas. La normal tiene curtosis 3 (*exceso* de curtosis = 0).

| Curtosis | Nombre | Implicación |
|---|---|---|
| < 3 | Platicúrtica | Colas finas; eventos extremos aún más raros |
| = 3 | Mesocúrtica | Normal |
| **> 3** | **Leptocúrtica** | **Colas gordas**: los extremos ocurren mucho más de lo previsto |

**Los retornos diarios de acciones tienen curtosis típica entre 5 y 10.** No es un detalle
técnico: es la razón matemática de que los modelos basados en normalidad **subestimen
sistemáticamente el riesgo de cola**, y de que Basilea III exija complementar el VaR con
Expected Shortfall (Semana 32).

Para dimensionarlo: bajo normalidad, una caída de 5 desviaciones estándar debería ocurrir una
vez cada **7.000 años**. En los mercados reales ocurre cada pocos años.

---

## La covarianza y la correlación: la base de todo lo que viene

Hasta ahora hemos medido el riesgo de **un** activo. La gestión de carteras necesita medir cómo
se mueven **dos** activos juntos.

**Covarianza:**

$$Cov(X,Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n-1}$$

El problema de la covarianza es que sus unidades son ininterpretables (%² ) y su magnitud
depende de la escala. Por eso se normaliza:

**Correlación:**

$$\rho_{XY} = \frac{Cov(X,Y)}{\sigma_X \sigma_Y} \qquad -1 \le \rho \le +1$$

| $\rho$ | Interpretación |
|---|---|
| $+1$ | Se mueven idénticamente |
| $+0.7$ | Fuerte relación positiva |
| $0$ | **Sin relación lineal** |
| $-0.7$ | Fuerte relación inversa |
| $-1$ | Espejos perfectos |

!!! warning "Tres advertencias sobre la correlación"
    1. **$\rho = 0$ no significa independencia.** Solo significa que no hay relación **lineal**.
       Si $Y = X^2$, la correlación puede ser cero y sin embargo $Y$ está perfectamente
       determinada por $X$.
    2. **La correlación no es estable.** Se calcula sobre una ventana histórica y cambia con el
       régimen de mercado. En las crisis, las correlaciones entre activos de riesgo convergen
       hacia 1 justo cuando la diversificación haría falta.
    3. **Correlación no es causalidad.** Es el error de la regresión espuria que verás en la
       Semana 16, y cuesta dinero real en construcción de carteras.

    La correlación es el ingrediente central de la frontera eficiente de Markowitz (Semana 39):
    combinar activos con $\rho < 1$ reduce el riesgo de la cartera **sin sacrificar retorno
    esperado**. Es lo más parecido a un almuerzo gratis que hay en finanzas.

---
