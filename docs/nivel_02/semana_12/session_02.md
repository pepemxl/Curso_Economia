# Semana 12 · Sesión 2: Profundización

## 4. La Inflación y la Ecuación de Fisher (Tasa Real vs. Tasa Nominal)
Hasta ahora, hemos trabajado con tasas "de mercado". Pero la inflación actúa como un impuesto invisible que erosiona el poder adquisitivo del dinero. 

El economista Irving Fisher formuló la relación exacta entre la inflación y las tasas de interés:
1. **Tasa Nominal ($i$):** Es la tasa que ves en el cartel del banco o en el contrato.
2. **Tasa Real ($r$):** Es el verdadero aumento en tu poder adquisitivo (lo que puedes comprar de más al final del año).
3. **Inflación ($h$ o $\pi$):** El porcentaje de aumento en el nivel general de precios.

* **Fórmula Aproximada de Fisher (solo para inflaciones bajas, < 5%):**
  $$ r \approx i - h $$
  *(Si el banco te paga 6% y la inflación es 4%, tu tasa real es 2%).*

* **Fórmula Exacta de Fisher (debe usarse siempre para análisis riguroso):**
  $$ 1 + r = \frac{1 + i}{1 + h} \quad \rightarrow \quad r = \left( \frac{1 + i}{1 + h} \right) - 1 $$

> **💥 Impacto Financiero:** La Tasa Real es lo que *realmente* enriquece a un inversor. Si compras un bono del gobierno que paga 15% anual, pero la inflación del país es del 18%, tu **tasa real es -2.55%**. Estás perdiendo poder adquisitivo a pesar de tener más billetes en la mano.

---

## 5. Tratamiento de la Inflación en los Flujos de Caja (Nominal vs. Real)
Al modelar un proyecto de inversión en Excel (lo que haremos en la Semana 18), los flujos de caja pueden proyectarse de dos maneras estrictas:

1. **Flujos Nominales ($Q_t$):** Proyectas los ingresos incluyendo el aumento de precios cada año según la inflación. Para descontarlos a Valor Presente, **debes usar la Tasa Nominal ($i$)**.
2. **Flujos Reales ($q_t$):** Proyectas los ingresos a precios de hoy (sin inflación). Para descontarlos a Valor Presente, **debes usar la Tasa Real ($r$)**.
* **La regla de consistencia:** *Nunca* mezcles flujos nominales con tasa real, ni flujos reales con tasa nominal. El resultado del Valor Presente (VP) será exactamente el mismo en ambos métodos si se aplica la matemática correcta.

---

