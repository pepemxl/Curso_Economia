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


??? success "Solución del Ejercicio C"

    **1. Distribución Binomial — el fondo de Venture Capital**

    Se cumplen los supuestos binomiales: 5 ensayos independientes e idénticos, dos
    resultados posibles (éxito/fracaso) y probabilidad constante.

    Parámetros: $n = 5$, $k = 2$, $p = 0.20$, $q = 1-p = 0.80$

    $$P(X=k) = \binom{n}{k} p^k q^{n-k}$$

    $$\binom{5}{2} = \frac{5!}{2!\,3!} = \frac{120}{2 \times 6} = 10$$

    $$P(X=2) = 10 \times (0.20)^2 \times (0.80)^3 = 10 \times 0.04 \times 0.512$$

    $$P(X=2) = 0.2048 = \mathbf{20.48\%}$$

    En Excel: `=DISTR.BINOM.N(2; 5; 0.2; FALSO)`.

    *Contexto:* el número **esperado** de éxitos es $E[X] = np = 5 \times 0.2 = 1$.
    Que salgan exactamente 2 es mejor que el promedio, y ocurre en 1 de cada 5
    fondos. Vale la pena notar que $P(X=0) = 0.8^5 = 32.8\%$: **un tercio de los
    fondos con esta estrategia no acierta ni una sola vez**. De ahí que el capital
    de riesgo exija retornos enormes en los aciertos — tienen que pagar por todos
    los fracasos.

    **2. Distribución Normal y VaR**

    *a) Puntuación Z:*

    $$Z = \frac{x - \mu}{\sigma} = \frac{-3.95\% - 0.05\%}{2\%} = \frac{-4.00\%}{2\%} = \mathbf{-2.00}$$

    La caída de 3.95 % está **exactamente 2 desviaciones estándar por debajo** del
    retorno esperado.

    *b) Probabilidad de perder más de 3.95 % en un día:*

    $$P(Z < -2.00) = 0.02275 = \mathbf{2.28\%}$$

    **Interpretación:** hay un 2.28 % de probabilidad de que Amazon caiga más de
    3.95 % en un día cualquiera. Con ~252 días hábiles al año, eso son
    $252 \times 0.0228 \approx$ **6 días al año**.

    Leído al revés, esto **es** un Value at Risk: con 97.72 % de confianza, la
    pérdida diaria no superará el 3.95 %. Es exactamente la herramienta que
    formalizarás en la Semana 32.

    !!! warning "El supuesto que mata: las colas gordas"
        Este cálculo asume que los retornos son **normales**, y los retornos
        bursátiles reales **no lo son**. Las crisis producen movimientos de 5, 8 o
        10 desviaciones estándar con una frecuencia muchísimo mayor que la que
        predice la campana de Gauss.

        Bajo normalidad, un evento de $-10\sigma$ debería ocurrir aproximadamente
        una vez cada $10^{21}$ años. En octubre de 1987 el Dow Jones cayó más de
        20 desviaciones estándar en un solo día.

        Por eso el VaR normal **subestima sistemáticamente el riesgo de cola**, y
        por eso Basilea III exige complementarlo con *Expected Shortfall* (CVaR) y
        pruebas de estrés (Semanas 32 y 34).

---
*¡Felicidades por completar la Semana 15! Hoy has dado tu primer paso serio en el modelado del riesgo cuantitativo. En la Semana 16 cerraremos el bloque de estadística con **Inferencia Estadística, Pruebas de Hipótesis y Regresión Lineal** para descubrir cómo se predicen las ventas de una empresa en base a variables externas.*