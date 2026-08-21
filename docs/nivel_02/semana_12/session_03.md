# Semana 12 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Equivalencia y Fisher

**Parte A: Equivalencia de Tasas**
Eres el CFO de una empresa y debes elegir entre dos préstamos:
* **Banco A:** Ofrece una tasa nominal del **12% capitalizable mensualmente** ($m=12$).
* **Banco B:** Ofrece una tasa nominal del **12.36% capitalizable trimestralmente** ($m=4$).

*¿Son equivalentes estos préstamos? Vamos a calcularlo.*
1. Paso 1: Encontrar la tasa efectiva del periodo para ambos.
   * Banco A: $i_A = 12\% / 12 = 1\%$ mensual.
   * Banco B: $i_B = 12.36\% / 4 = 3.09\%$ trimestral.
2. Paso 2: Llevar ambos a una medida común (ej. Tasa Efectiva Anual o EAR).
   * $EAR_A = (1 + 0.01)^{12} - 1 = 1.1268 - 1 = 12.68\%$
   * $EAR_B = (1 + 0.0309)^4 - 1 = 1.1268 - 1 = 12.68\%$
* **Conclusión:** ¡Son matemáticamente equivalentes! El Banco B pone un número nominal ligeramente más alto para que parezca peor, pero al capitalizar trimestralmente, la Tasa Efectiva es idéntica. Ambos préstamos costarán lo mismo.

**Parte B: Ecuación Exacta de Fisher**
Un fondo de inversión yielded el año pasado una rentabilidad nominal del **24%**. La inflación reportada fue del **12%**.
El gerente del fondo dice: "¡Generamos un 12% de rentabilidad real para nuestros clientes!"
* **Cálculo Exacto:**
  $r = \frac{1 + 0.24}{1 + 0.12} - 1 = \frac{1.24}{1.12} - 1 = 1.1071 - 1 = 0.1071$
* **Conclusión:** El gerente está mintiendo o es un mal matemático. Con la fórmula aproximada da 12%, pero con la fórmula exacta de Fisher, el rendimiento real para el inversor fue del **10.71%**. El 1.29% restante se perdió por el efecto compuesto de la inflación.

---

