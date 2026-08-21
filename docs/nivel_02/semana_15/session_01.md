# Semana 15 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Comprender las reglas básicas de la probabilidad y la diferencia entre variable discreta y continua.
* Entender y modelar la Distribución Binomial (éxito/fracaso) aplicada al riesgo de crédito.
* Entender y modelar la Distribución de Poisson (eventos en el tiempo) aplicada al riesgo operativo.
* Dominar la Distribución Normal (la campana de Gauss) y la estandarización (Z-score), base del modelo Black-Scholes y del Value at Risk (VaR).

---

## 2. Conceptos Básicos de Probabilidad
Una probabilidad mide la posibilidad de que ocurra un evento, y siempre está entre 0 (imposible) y 1 (100% seguro).
* **Variable Aleatoria Discreta:** Solo puede tomar valores enteros contables (Ej. Número de clientes que hacen default en un mes: 0, 1, 2, 3...).
* **Variable Aleatoria Continua:** Puede tomar cualquier valor dentro de un rango (Ej. El retorno de una acción hoy: puede ser 0.051%, 0.052%, -1.54%, etc.). Se mide por densidad de probabilidad (el área bajo la curva).

---

## 3. Distribución Binomial: El Modelo de Riesgo de Crédito
Se usa cuando un experimento tiene **solo dos resultados posibles**: Éxito o Fracaso (En finanzas: Pagar o Hacer Default). 
* **Parámetros:** $n$ (número de ensayos/préstamos), $p$ (probabilidad de éxito/pago), $q$ (probabilidad de fracaso/default, donde $q = 1 - p$).
* **Fórmula:** Probabilidad de exactamente $x$ éxitos en $n$ ensayos:
  $$ P(x) = \binom{n}{x} p^x q^{n-x} $$

> **💥 Aplicación Financiera (Riesgo de Crédito):** Eres un oficial de crédito en un banco y otorgas 10 microcrédamos ($n=10$). Sabes por tu historial que el 90% de los microcréditos se pagan ($p=0.9$) y el 10% fallan ($q=0.1$). ¿Cuál es la probabilidad de que **exactamente 8** créditos se paguen y 2 fallen?
> $$ P(8) = \frac{10!}{8!2!} \times (0.9)^8 \times (0.1)^2 = 45 \times 0.4304 \times 0.01 = \mathbf{0.1937} \text{ (19.37\%)} $$
> El banco knows que hay un 19% de probabilidad de perder dinero en 2 de esos 10 préstamos, y debe provisionar capital para soportar ese escenario exacto.

---

