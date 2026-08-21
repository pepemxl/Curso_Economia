# Semana 12 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Dominar el concepto de capitalización ($m$) y su impacto en el rendimiento real.
* Calcular tasas equivalentes para comparar correctamente instrumentos financieros con diferentes frecuencias de pago.
* Comprender y aplicar la Ecuación de Fisher (Tasa Real vs. Tasa Nominal).
* Aprender a "deflactar" flujos de efectivo para analizar el crecimiento real de una empresa o inversión.

---

## 2. Tasa Nominal vs. Tasa Efectiva (Profundización)
En la Semana 11 tocamos este tema brevemente; ahora lo dominaremos.
* **Tasa Nominal ($r_n$ o APR):** Es la tasa "de fachada". No incluye el efecto del interés compuesto dentro del año. Si un banco te dice "12% anual capitalizable mensualmente", la tasa nominal es 12%. 
* **Tasa Efectiva ($r_e$ o EAR):** Es la tasa que *realmente* ganas o pagas al final del año porque considera que los intereses de cada mes generan nuevos intereses en los meses siguientes.
* **Fórmula de la Tasa Efectiva (EAR):**
  $$ r_e = \left( 1 + \frac{r_n}{m} \right)^m - 1 $$
  Donde $m$ es el número de periodos de capitalización en el año (Anual=1, Semestral=2, Trimestral=4, Mensual=12, Diario=360 o 365).

> **💥 Regla Práctica del Analista:** *Nunca* compares dos instrumentos financieros usando la Tasa Nominal. Un préstamo al 12% nominal mensual es más caro que un préstamo al 12.5% nominal anual. ¿Por qué? El primero tiene una Tasa Efectiva del 12.68%, mientras que el segundo tiene una Tasa Efectiva del 12.5%.

---

## 3. Equivalencia de Tasas
A veces no queremos calcular la tasa efectiva anual, sino comparar dos tasas nominales con diferentes periodos de capitalización. Para ello, usamos la **Equivalencia de Tasas**, que busca que el rendimiento de dos alternativas sea exactamente el mismo.

* **Lógica matemática:** Para que dos tasas sean equivalentes, el Factor de Capitalización (lo que está dentro del paréntesis elevado a la potencia) debe ser idéntico.
  $$ \left( 1 + \frac{r_1}{m_1} \right)^{m_1 \times t} = \left( 1 + \frac{r_2}{m_2} \right)^{m_2 \times t} $$

* **Truco directo (Ecuación de Equivalencia):**
  $$ 1 + i_1 = (1 + i_2)^{\frac{m_1}{m_2}} $$
  Donde $i$ es la tasa del periodo (Tasa Nominal / $m$). *(Lo veremos en el ejercicio práctico para que quede súper claro).*

---

