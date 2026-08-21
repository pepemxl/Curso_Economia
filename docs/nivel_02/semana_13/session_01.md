# Semana 13 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Comprender el concepto de Anualidad (Ordinaria vs. Anticipada) y aplicar sus fórmulas de Valor Presente y Futuro.
* Entender las Perpetuidades y su aplicación en la valuación de acciones (Modelo de Gordon).
* Diferenciar matemáticamente los 3 sistemas de amortización de préstamos (Francés, Alemán, Americano).
* Construir mentalmente un "Cuadro de Amortización" (Amortization Schedule).

---

## 2. Las Anualidades
Una anualidad es una serie de pagos (o cobros) **iguales** que se realizan a intervalos **regulares** de tiempo. (Nota: Se llama "anualidad" aunque los pagos sean mensuales, trimestrales o diarios).

**A. Anualidad Ordinaria (o Vencida):**
Los pagos se realizan al **final** de cada periodo. Ejemplo: El pago de la cuota de tu auto, que pagas a fin de mes luego de usarlo.
* **Fórmula del Valor Presente (VP):** ¿Cuánto vale hoy una serie de pagos futuros?
  $$ VP = C \times \left[ \frac{1 - (1 + i)^{-n}}{i} \right] $$
  *(Donde $C$ es la cuota fija, $i$ es la tasa del periodo, $n$ es el número de periodos).*
* **Fórmula del Valor Futuro (VF):** ¿Cuánto ahorrarás si depositas una cuota fija cada mes?
  $$ VF = C \times \left[ \frac{(1 + i)^{n} - 1}{i} \right] $$

**B. Anualidad Anticipada (o Adelantada):**
Los pagos se realizan al **inicio** de cada periodo. Ejemplo: El alquiler de un apartamento, que pagas el día 1 del mes antes de ocuparlo.
* *Truco matemático:* Una anualidad anticipada equivale a una anualidad ordinaria multiplicada por $(1 + i)$.
  $$ VP_{anticipada} = VP_{ordinaria} \times (1 + i) $$

---

## 3. Las Perpetuidades
Una perpetuidad es una anualidad que **nunca termina**. Los pagos son iguales y se prolongan hasta el infinito ($n \to \infty$).
* **Fórmula del Valor Presente (VP):**
  $$ VP = \frac{C}{i} $$
*(Donde $C$ es el pago periódico constante e $i$ es la tasa de interés del periodo).*

> **💥 Impacto Financiero (El Modelo de Gordon):** Las acciones comunes no tienen fecha de vencimiento. Si suponemos que una empresa pagará un dividendo constante para siempre, su precio teórico es el VP de una perpetuidad. Más adelante, en la Semana 37, usaremos la **Perpetuidad Creciente** ($VP = \frac{C_1}{i - g}$), que es el modelo estándar de Wall Street para hallar el "Valor Terminal" de una empresa en un DCF.

---

