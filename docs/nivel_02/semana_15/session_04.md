# Semana 15 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El colapso de Long-Term Capital Management (LTCM)
*Eres un regulador financiero en 1998. LTCM es un Hedge Fund gestionado por dos Premiados economistas ganadores del Nobel (Robert Merton y Myron Scholes). Utilizan modelos matemáticos supremamente complejos basados en la **Distribución Normal**.*

Su modelo decía: "Los retornos de los bonos rusos y americanos siguen una campana de Gauss. Para que perdamos todo nuestro capital, tendría que ocurrir un evento de 10 desviaciones estándar (sigma), algo que estadísticamente ocurre una vez cada $10^{24}$ años. Es matemáticamente imposible quebrar nuestro fondo".

**La Realidad y el Error de la Normalidad:**
En agosto de 1998, Rusia suspende el pago de su deuda soberana de forma inesperada ( un Cisne Negro). Los mercados se congelaron por pánico. El evento de pánico fue de "10 sigmas", una probabilidad "imposible" en teoría, pero que en los mercados financieros ocurre cada 10 o 15 años debido a la interconexión emocional de los humanos (pánico).

**Lección para tu modelado en Excel (Semana futura):** La Distribución Normal es fantástica para modelar el 95% de los días bursátiles comunes. Pero los analistas de riesgo modernos usan la **Distribución T-Student** o Simulaciones Monte Carlo para capturar los eventos extremos (las "Colas Gordas"), porque asumir que el mundo comercial es perfecto y simétrico causó la mayor quiebra de un hedge fund de la historia (LTCM fue rescatado por la Reserva Federal).

---

## 8. Tareas y Evaluación de la Semana 15

**A. Lectura Obligatoria:**
* *Estadística para Administración y Economía* (Anderson, Sweeney, Williams). Capítulos 5 y 6 (Probabilidad y Distribuciones de Probabilidad).

**B. Preguntas de Reflexión:**
1. Explica con tus propias palabras por qué el modelo de Distribución Normal es engañoso en la valoración del "Riesgo de Cola" (Tail Risk) en los mercados financieros gubernamentales y bancarios.
2. Da un ejemplo práctico en el área de seguros donde se debería utilizar una distribución Binomial y donde se debería utilizar una de Poisson.

**C. Ejercicio Matemático a entregar:**
1. **Binomial:** Un fondo de capital de riesgo (Venture Capital) invierte en 5 startups idénticas. La probabilidad histórica de éxito de una startup (salida a bolsa) es del 20%. ¿Cuál es la probabilidad de que el fondo tenga **exactamente 2** startups exitosas y 3 fracasos? (Muestra la fórmula y despeje).
2. **Normal y VaR:** Las acciones de Amazon tienen un retorno diario esperado ($\mu$) del 0.05% y una desviación estándar diaria ($\sigma$) del 2%. 
   a) Calcula la puntuación Z (Z-score) para un retorno diario de -3.95%.
   b) Usando cualquier tabla Z de internet o Excel (función `=DISTR.NORM.N(-3.95%; 0.05%; 2%; VERDADERO)`), ¿Cuál es la probabilidad de que un día cualquiera Amazon pierda más del 3.95% de su valor?

---
*¡Felicidades por completar la Semana 15! Hoy has dado tu primer paso serio en el modelado del riesgo cuantitativo. En la Semana 16 cerraremos el bloque de estadística con **Inferencia Estadística, Pruebas de Hipótesis y Regresión Lineal** para descubrir cómo se predicen las ventas de una empresa en base a variables externas.*