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

