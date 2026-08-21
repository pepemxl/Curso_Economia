# Semana 16 · Sesión 2: Profundización

## 4. Regresión Lineal Simple
Modela la relación entre una variable dependiente ($Y$, lo que quieres predecir) y una variable independiente ($X$, el predictor).
* **La Ecuación de la Recta:**
  $$ Y = \beta_0 + \beta_1 X + \epsilon $$
  * $\beta_0$: Intercepto (donde empieza Y si X fuera cero).
  * $\beta_1$: Coeficiente (cuánto cambia Y por cada unidad adicional de X).
  * $\epsilon$: Error (lo que el modelo no puede explicar).

**Métricas clave de un modelo de regresión:**
1. **R-Cuadrado ($R^2$):** El Coeficiente de Determinación. Va de 0 a 1 (o 0% a 100%). Te dice qué porcentaje de la variación de Y es explicado por X. (Un $R^2$ de 0.85 significa que el 85% de los movimientos de tu variable se explican por tu modelo; el otro 15% es ruido o variables omitidas).
2. **p-value de los coeficientes:** Verifica si la variable X tiene impacto estadístico real. Si el $p\text{-value}$ del coeficiente $\beta_1$ es menor a 0.05, X es un predictor significativo para Y.

> **⚠️ Aviso Legal Estadístico: CORRELACIÓN NO IMPLICA CAUSALIDAD.** Puedes hacer una regresión y encontrar un $R^2$ altísimo entre el precio del Bitcoin y la lluvia en Londres. Matemática cuadran, pero no hay lógica de negocios. Un buen analista financiero siempre exige sentido económico antes que matemático.

---

## 5. Regresión Lineal Múltiple
En la economía, rara vez un solo factor explica todo. La regresión múltiple usa varias variables independientes ($X_1, X_2, X_3$) para predecir $Y$.
$$ Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k + \epsilon $$

**El gran problema: Multicolinealidad**
Ocurre cuando dos o más variables independientes en tu modelo están altamente correlacionadas entre sí. (Ejemplo: Usar "Precio del Petróleo" y "Precio de la Gasolina" para predecir inflación de transporte). Esto infla artificialmente la varianza y vuelve inestables los coeficientes, haciendo que el p-value suba y variables importantes parezcan irrelevantes.
* *Solución:* Eliminar una de las variables duplicadas o usar técnicas avanzadas (como Análisis de Componentes Principales - PCA).

---

