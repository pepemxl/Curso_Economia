# Semana 31 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: Calculando la Pérdida Esperada (Riesgo de Crédito)
Eres el Director de Riesgos de un Banco Comercial. Tienes una cartera de 1,000 préstamos hipotecarios, cada uno por **$200,000**. El banco ha calculado estos parámetros basándose en su historial pasado y en el modelo de scoring de crédito:

* **EAD (Exposure at Default):** $200,000 ( saldo promedio del préstamo)
* **PD (Probability of Default):** 3% anual ( Hay un 97% de probabilidad de que el cliente pague la hipoteca sin problemas).
* **LGD (Loss Given Default):** 40% (Que la casa, en caso de ejecución de la hipoteca, solo cubra el 60% de la deuda debido a la caída de los precios inmobiliarios y comisiones legales).

**Cálculo Matemático (Pérdida Esperada de un Solo Préstamo):**
$$ EL = 0.03 \text{ (PD)} \times 0.40 \text{ (LGD)} \times \$200,000 \text{ (EAD)} $$
$$ EL = 0.012 \times \$200,000 = \mathbf{\$2,400} $$

**Cálculo para Toda la Cartera (1,000 clientes):**
$$ EL_{total} = 1,000 \times \$2,400 = \mathbf{\$2,400,000} $$

**Veredicto Financiero:**
El banco *sabe* matemáticamente que perderá $2.4 millones este año en su cartera hipotecaria. No es una sorpresa, es la estadística promedio. Por lo tanto, el banco cobra a todos los clientes un "spread" (ej. 1% extra de interés) para cubrir esos $2.4M. Si la recaudación de ese spread supera los $2.4M, el riesgo ha sido rentable y el banco gana dinero de forma segura.

---
