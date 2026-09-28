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

## Ejercicio: el poder de la diversificación, con números

La afirmación *"diversificar reduce el riesgo"* se demuestra con una sola fórmula. La varianza
de un portafolio de dos activos:

$$\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho_{12}\sigma_1\sigma_2$$

**Lo decisivo es el tercer término**, y en concreto la correlación $\rho$.

Dos activos, cada uno con retorno esperado del **10 %** y volatilidad del **20 %**, en una
cartera 50/50:

| Correlación | Cálculo de $\sigma_p$ | $\sigma_p$ | Reducción del riesgo |
|---|---|---|---|
| $\rho = +1.0$ | $\sqrt{0.01+0.01+0.02}$ | **20,0 %** | **Ninguna** |
| $\rho = +0.5$ | $\sqrt{0.01+0.01+0.01}$ | **17,3 %** | 13 % |
| $\rho = 0$ | $\sqrt{0.01+0.01+0}$ | **14,1 %** | 29 % |
| $\rho = -0.5$ | $\sqrt{0.01+0.01-0.01}$ | **10,0 %** | 50 % |
| $\rho = -1.0$ | $\sqrt{0.01+0.01-0.02}$ | **0,0 %** | **Riesgo eliminado** |

**El retorno esperado es del 10 % en las cinco filas.** Solo cambia el riesgo.

Esto es lo más parecido a un almuerzo gratis que existe en finanzas: **combinar activos
imperfectamente correlacionados reduce el riesgo sin sacrificar retorno esperado.** Y funciona
con cualquier $\rho < 1$: no hacen falta activos que se muevan en contra, basta con que **no se
muevan exactamente igual**.

---

## Cuántos activos hacen falta

Al añadir activos a una cartera, el riesgo total cae — pero no indefinidamente:

$$\sigma_p^2 = \underbrace{\frac{1}{n}\overline{\sigma^2}}_{\text{idiosincrásico} \to 0} + \underbrace{\frac{n-1}{n}\overline{cov}}_{\to \overline{cov}}$$

Cuando $n \to \infty$, el primer término desaparece y **solo queda la covarianza media**. Ese
residuo es el **riesgo sistemático**, y no hay diversificación que lo elimine.

| Nº de acciones | Riesgo total típico | Riesgo eliminado |
|---|---|---|
| 1 | 49 % | 0 % |
| 5 | 28 % | 43 % |
| 10 | 24 % | 51 % |
| 20 | 22 % | 55 % |
| 50 | 20,5 % | 58 % |
| 1,000 | 19,2 % | 61 % |

**Con 20-30 acciones bien elegidas se captura casi toda la diversificación posible.** Pasar de
30 a 1,000 apenas mejora nada.

!!! tip "Por qué el mercado solo paga por el riesgo sistemático"
    Esta tabla **es** la justificación del CAPM que usaste en la Semana 24.

    El riesgo **idiosincrásico** (que a una empresa se le queme la fábrica) se puede eliminar
    gratis: basta con diversificar. Como cualquiera puede hacerlo sin costo, **el mercado no
    paga prima por asumirlo**. Quien concentra su cartera en una sola acción asume riesgo
    adicional sin compensación esperada.

    El riesgo **sistemático** ($\beta$) es inevitable: no hay cartera de acciones que escape a
    una recesión global. Como nadie puede eliminarlo, **es el único por el que el mercado paga
    una prima**.

    De ahí la fórmula del CAPM: $r_e = R_f + \beta \times MRP$. La beta y solo la beta.

---

## Los límites prácticos de Markowitz

El caso de LTCM muestra el fallo espectacular. Los fallos cotidianos son más aburridos y más
frecuentes:

1. **Los inputs son estimaciones ruidosas.** Con $n$ activos hay que estimar $n$ retornos, $n$
   varianzas y $n(n-1)/2$ covarianzas. Con 100 activos son **5,150 parámetros** a partir de
   datos históricos limitados.
2. **El optimizador amplifica los errores.** Markowitz es notoriamente inestable: un cambio
   pequeño en un retorno esperado produce carteras radicalmente distintas, a menudo
   concentradas en dos o tres activos. Se le llama *maximizador de errores de estimación*.
3. **Las correlaciones no son estables**, y se disparan justo en las crisis — cuando la
   diversificación más falta hace.
4. **La volatilidad no es riesgo.** $\sigma$ penaliza igual las sorpresas al alza que a la baja.
   El **ratio de Sortino**, que solo penaliza la desviación negativa, corrige esto.

**Cómo se responde en la práctica moderna:**

* **Restricciones de peso** (mínimos y máximos por activo) para evitar concentraciones absurdas.
* **Estimadores robustos** (contracción de Ledoit-Wolf) para la matriz de covarianzas.
* **Paridad de riesgo:** ponderar por contribución al riesgo, no por retorno esperado — evita
  tener que estimar retornos, que es lo más difícil.
* **Black-Litterman:** parte del equilibrio de mercado y solo incorpora las opiniones del
  gestor donde las tenga, con su nivel de confianza.
* **Activos con correlación negativa estructural** (oro, bonos largos, estrategias de
  volatilidad larga) como cobertura de cola, aceptando su costo de acarreo.

---
