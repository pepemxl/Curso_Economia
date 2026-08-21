# Semana 15 · Sesión 2: Profundización

## 4. Distribución de Poisson: El Modelo de Riesgo Operativo
Se usa para modelar el número de veces que ocurre un evento en un **intervalo específico de tiempo o espacio**. Es ideal para eventos raros (tasas de ocurrencia muy bajas).
* **Parámetro:** $\lambda$ (lambda), la tasa media de ocurrencia esperada en el periodo.
* **Fórmula:** Probabilidad de exactamente $x$ eventos:
  $$ P(x) = \frac{\lambda^x \cdot e^{-\lambda}}{x!} $$ *(Donde $e$ es la base del logaritmo natural, 2.71828)*

> **💥 Aplicación Financiera (Riesgo Operativo):** Eres el Director de Riesgos de una plataforma de Trading (Brokerage). Estadísticamente, el sistema se cae por caer un servidor en promedio 2 veces al año ($\lambda = 2$). ¿Cuál es la probabilidad de que este año ocurran **exactamente 0 caídas**? Y ¿Cuál de que ocurran **exactamente 3 caídas**?
> * Para 0 caídas: $P(0) = \frac{2^0 \cdot e^{-2}}{0!} = \frac{1 \cdot 0.1353}{1} = \mathbf{13.53\%}$ (Tienes un 13% de chance de tener un año perfecto).
> * Para 3 caídas: $P(3) = \frac{2^3 \cdot e^{-2}}{3!} = \frac{8 \cdot 0.1353}{6} = \frac{1.0824}{6} = \mathbf{18.02\%}$
> Con esta data, el equipo de IT (Tecnología) decide si vale la pena pagar $50,000 extra por servidores redundantes para reducir $\lambda$ de 2 a 1, sabiendo que una caída de 4 horas les cuesta a la firma $100,000 en clientes enojados.

---

## 5. Distribución Normal: El Rey de Wall Street
Es la distribución más importante en estadística financiera. Es simétrica (forma de campana), donde la Media, la Mediana y la Moda son iguales. Sus colas se acercan infinitamente al eje horizontal pero nunca lo tocan (teóricamente, cualquier valor es posible, aunque muy poco probable).

* **Propiedades clave (Regla Empírica):**
  * El 68% de los datos están a $\pm 1$ Desviación Estándar ($\sigma$) de la media ($\mu$).
  * El 95% de los datos están a $\pm 2\sigma$ de la media.
  * El 99.7% de los datos están a $\pm 3\sigma$ de la media.

**La Estandarización (Puntuación Z):**
Todas las acciones tienen diferentes medias y desviaciones. Para comparar el riesgo de Apple con el de Tesla, debemos llevar ambas a una "misma escala". Se hace restando la media y dividiendo entre la desviación estándar, creando una variable $Z$ que sigue una Normal Estándar (media 0, desviación 1).
$$ Z = \frac{x - \mu}{\sigma} $$
*(El resultado $Z$ nos dice "cuántas desviaciones estándar está el valor $x$ por encima o por debajo de la media").*

> **💥 Aplicación Financiera (Value at Risk - VaR):** La distribución Normal es la base matemática del modelo de Black-Scholes para valuar opciones y del VaR (Valor en Rieslo) bancaario. Asume que los retornos de las acciones se distribuyen normalmente. (Nota para el analista moderno: La realidad tiene "Colas Gordas" o Fat Tails, donde crisis extremas ocurren más a menudo de lo que la Normal predice. En el Nivel 4 abordaremos esto en Gestión de Riesgos).

---

