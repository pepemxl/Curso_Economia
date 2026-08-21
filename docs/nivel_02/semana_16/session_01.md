# Semana 16 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Comprender la inferencia estadística y el concepto del Valor P (p-value).
* Formular y probar Hipótesis Nulas y Alternativas.
* Entender la Regresión Lineal Simple y blues bluesinterpretar sus coeficientes.
* Diferenciar entre correlación y causalidad.
* Introducir la Regresión Múltiple y el problema de la Multicolinealidad.

---

## 2. Inferencia Estadística y el "P-Value"
La inferencia estadística consiste en sacar conclusiones sobre una población entera basándonos únicamente en una muestra. 

* **El Valor P (p-value):** Es la probabilidad de obtener un resultado Equal o más extremo al observado, asumiendo que la hipótesis nula es cierta. En finanzas, es el "detector de mentiras" estadístico.
* **Nivel de Significancia ($\alpha$):** El umbral de riesgo de error que estamos dispuestos a aceptar. En finanzas Usually es 5% (0.05) o 1% (0.01).
* **Regla práctica:** Si el $p\text{-value} < \alpha$, rechazamos la hipótesis nula. El resultado es **estadísticamente significativo**. Si $p\text{-value} > \alpha$, no tenemos suficiente evidencia (aceptamos la hipótesis nula).

---

## 3. Pruebas de Hipótesis (Hypothesis Testing)
Todo test estadístico empieza con dos hipótesis mutuamente excluyentes:
1. **Hipótesis Nula ($H_0$):** Es la "status quo" o el efecto nulo. (Ej. "Esta estrategia de trading NO genera beneficios", "El coeficiente es cero"). Asumimos que es cierta hasta probar lo contrario.
2. **Hipótesis Alternativa ($H_a$):** Es lo que el analista quiere demostrar. (Ej. "La estrategia SÍ genera beneficios", "El coeficiente es mayor que cero").

> **💥 Impacto Financiero:** Imagina que un gestor de fondos te dice: *"Mi algoritmo de trading batió al mercado por un 3% este año"*. Corres una prueba de hipótesis en Excel: $H_0$: El alpha del gestor es 0. $H_a$: El alpha es > 0. El Excel te arroja un p-value de 0.35 (35%).
> *Conclusión:* Hay un 35% de probabilidad de que ese 3% de rentabilidad Extra sea pura suerte (ruido estadístico). Como 0.35 > 0.05, **no rechazas $H_0$**. El gestor no ha demostrado habilidad; fue simple suerte. No le confías tu dinero.

---

