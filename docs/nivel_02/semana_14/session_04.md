# Semana 14 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El pelotón de caza de los Hedge Funds
*Gestionas un fondo de cobertura (Hedge Fund). Comparas tus dos mejores traders estrella.*

* **Trader A:** Tiene un retorno promedio anual del 25%, pero con una desviación estándar altísima del 40%. Es brillante, pero volátil. Sus "drawdowns" (caídas de capital máximas) llegan al -35%.
* **Trader B:** Tiene un retorno promedio del 15%, con una desviación estándar minúscula del 4%. Nunca tiene malos meses, sube lento pero constante (como un bono).

**La trampa de la "Media":**
El gerente del fondo quiere despedir al Trader B porque "sus retornos son la mitad de buenos que los del Trader A". 
Tu análisis estadístico lo detiene: El Trader A toma riesgos asimétricos negativos. En un año malo puede borrar toda la ganancia de 3 años buenos (Riesgo de Cola Negra o *Black Swan*). El Trader B genera un "Sharpe Ratio" altísimo (Retorno ajustado por volatilidad que veremos en el Nivel 4). 

*Acción:* No despides al Trader B, sino que hiper-apalancas su capital, porque su baja desviación estándar permite usar deuda bancaria barata para multiplicar su retorno seguro. Al Trader A se le reduce el capital asignado por riesgo de wipe-out.

---

## 8. Tareas y Evaluación de la Semana 14

**A. Lectura Obligatoria:**
* *Estadística para Administración y Economía* de Anderson, Sweeney y Williams. Capítulos 2 y 3 (Descriptiva, Tendencia central y Dispersión).

**B. Preguntas de Reflexión:**
1. ¿Por qué en finanzas se suele elevar al cuadrado las desviaciones para calcular la varianza, y por qué se usa $(n - 1)$ en el denominador al calcular una muestra en lugar de $n$?
2. Explica con un ejemplo financiero por qué confiar únicamente en la "Media" de los retornos históricos de un índice bursátil puede ser una decisión catastrófica para un fondos de pensiones.

**C. Ejercicio Estadístico a entregar:**
Los siguientes datos representan la tasa de retorno anual (en %) de un portafolio inmobiliario durante los últimos 8 años:
`[8, 12, -4, 15, 9, 11, -2, 13]`

1. Calcula la Media (Promedio).
2. Calcula la Mediana (Recuerda ordenar de menor a mayor primero).
3. Calcula la Varianza (Muestral, divisor $n - 1$).
4. Calcula la Desviación Estándar y el Coeficiente de Variación. Interpreta qué significa el resultado del CV en términos de riesgo.

---
*¡Felicidades por completar la Semana 14! Ya sabes medir el riesgo básico. En la Semana 15 dejaremos los datos pasados y entraremos en el futuro con la Teoría de Probabilidades y las Distribuciones de Probabilidad (Normal, Binomial y Poisson).*