# Semana 39 · Sesión 3: Aplicación Práctica

## 7. Ejercicio Práctico: Diversificación y Ratio de Sharpe

Tienes dos activos en tu portafolio:
* **Activo A (Acciones Tech):** Retorno = 15%, Volatilidad ($\sigma$) = 20%.
* **Activo B (Bonos Gubernamentales):** Retorno = 5%, Volatilidad ($\sigma$) = 5%.
* **Correlación entre A y B:** 0.0 (Cero. Suben y bajan de forma totalmente independiente).

Montas un portafolio 50% Acciones y 50% Bonos. Calculemos su rendimiento y su riesgo:

**1. Retorno del Portafolio (Promedio Ponderado):**
* $R_p = (0.5 \times 15\%) + (0.5 \times 5\%) = 7.5\% + 2.5\% = \mathbf{10\%}$.

**2. Volatilidad del Portafolio (La Magia de Markowitz):**
La fórmula de la varianza de un portafolio es: $\sigma_p = \sqrt{w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B(\rho_{AB}\sigma_A\sigma_B)}$
* Como la correlación ($\rho$) es 0, el último término se vuelve cero.
* $\sigma_p = \sqrt{(0.5^2 \times 20^2) + (0.5^2 \times 5^2)} = \sqrt{(0.25 \times 400) + (0.25 \times 25)} = \sqrt{100 + 6.25} = \sqrt{106.25} = \mathbf{10.3\%}$

**El Veredicto:**
El promedio simple de la volatilidad sería $(20\% + 5\%) / 2 = 12.5\%$. Pero gracias a la falta de correlación, la volatilidad real del portafolio bajó a **10.3%**. 
Obtuviste un 10% de retorno asumiendo 2 puntos porcentuales *menos* de riesgo que si hubieras hecho un promedio simple. Acabas de crear valor matemático de la nada. (Un fondo indexado a 1 sola acción no logra esto).

---
