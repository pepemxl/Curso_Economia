# Semana 16 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El Modelo CAPM (Capital Asset Pricing Model)
*Eres un analista de equity (acciones). Necesitas calcular el costo de capital de una acción (la tasa de retorno que los inversores exigen).*

La teoría financiera dice que la rentabilidad de una acción depende de cuánto se mueve con el mercado (el Riesgo Sistemático, llamado **Beta, $\beta$**).
La fórmula del CAPM es: $E(R_i) = R_f + \beta_i (E(R_m) - R_f)$

**Cómo lo resuelves con regresión:**
1. Descargas el histórico de 5 años de rendimientos mensuales de la acción de Coca-Cola ($Y$).
2. Descargas el histórico del índice S&P 500 ($X$).
3. El rendimiento libre de riesgo ($R_f$), como el bono del tesoro a 10 años, a menudo se resta primero de ambas series para obtener "exces returns" (retornos en exceso).
4. Corres una regresión lineal simple en Excel: Retorno de Coca-Cola = $\alpha$ + $\beta \times$ Retorno del S&P 500.
5. El **Coeficiente $\beta_1$ de la regresión** es el Beta de la acción. Si sale 0.85, significa que Coca-Cola es "defensiva" (se mueve menos que el mercado). Si sale 1.40, es agresiva (se mueve más que el mercado).
6. El **$\alpha$ (intercepto)** de la regresión te dice si el fondo ha generado valor agregado (habilidad del gestor) o si simplemente sigue el mercado.

---

## 8. Tareas y Evaluación de la Semana 16

**A. Lectura Obligatoria:**
* *Estadística para Administración y Economía* (Anderson, Sweeney, Williams). Capítulos 9 (Pruebas de Hipótesis), 14 (Regresión Lineal Simple) y 15 (Regresión Lineal Múltiple).

**B. Preguntas de Reflexión:**
1. Define con tus propias palabras la diferencia entre "Correlación" y "Causalidad". Da un ejemplo absurdo donde exista correlación matemática pero no causalidad económica.
2. ¿Por qué un modelo de regresión con un R-cuadrado del 95% (muy alto) no garantiza que vayamos a predecir correctamente el futuro de los mercados financieros? ¿Qué factor externo rompe el modelo?

**C. Ejercicio Práctico a entregar:**
Tienes un modelo de regresión para predecir las ventas de autos de una concesionaria ($Y$, en unidades vendidas). Usas dos variables: Presupuesto en Publicidad ($X_1$, en miles de dólares) y Tasa de Interés del Banco Central ($X_2$, en porcentaje).

El software estadístico arroja estos resultados:
* Intercepto ($\beta_0$): 500
* Coeficiente Publicidad ($\beta_1$): 4.2 (p-value: 0.03)
* Coeficiente Tasa de Interés ($\beta_2$): -15.5 (p-value: 0.20)
* R-cuadrado: 0.65

Contesta:
1. ¿Es la Publicidad un predictor estadísticamente significativo? Explica por qué usando el p-value.
2. Interpreta el coeficiente de la Tasa de Interés. ¿Qué significa matemáticamente ese número negativo? ¿Es estadísticamente confiable para tomar decisiones?
3. Si el año que viene la empresa planea gastar $100,000 en publicidad (valor $X_1 = 100$) y se espera que la tasa de interés sea del 5% (valor $X_2 = 5$), ¿cuántas unidades matemáticas predice el modelo que se venderán? (Usa la fórmula $Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2$).

---
*¡Felicidades por completar la Semana 16! Has terminado el bloque de estadística pura. Ya sabes medir el riesgo, probar teorías y modelar variables. En la Semana 17 empezamos el Nivel 2 del Nivel 2: Excel financiero intermedio-avanzado y Modelación de Estados Financieros.*