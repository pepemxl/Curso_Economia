# Semana 11 · Sesión 2: Profundización

## 4. Valor Futuro (VF) y Valor Presente (VP)
**A. Valor Futuro (Calcular hacia adelante):** 
Saber cuánto valdrá una inversión hoy en el futuro. (Usa la fórmula de interés compuesto de arriba).

**B. Valor Presente (Calcular hacia atrás / "Descontar"):**
Saber cuánto vale hoy una suma de dinero que recibiremos en el futuro. Hay que "traerla al presente" quitándole el interés que generaría (tasa de descuento).
* **Fórmula del Valor Presente (VP):**
  $$ VP = \frac{VF}{(1 + r)^t} $$
  Donde $r$ es la **tasa de descuento** (la rentabilidad exigida por el inversor).

> **💥 Regla de Oro del Analista:** Las acciones, los bonos, las casas y las empresas NO se valen por lo que "valdrán" en el futuro; se valen por el **Valor Presente** de todo el efectivo que generarán en el futuro. *Descontar* flujos es el corazón de las finanzas corporativas (lo veremos en la Semana 24).

---

## 5. Tasa Nominal vs. Tasa Efectiva (Cuidado con el fraude bancario)
Rara vez una inversión dura exactamente "1 año" sin ningún pago intermedio. Muchas veces losinterests se capitalizan varias veces al año (mensual, trimestral, diario). 

1. **Tasa Nominal ($r_n$):** Es la tasa que el banco te "anuncia" en la cartelera. No refleja la capitalización real si el interés se paga más de una vez al año.
2. **Tasa Efectiva ($r_e$):** Es la tasa que *realmente* ganas o pagas al final del año, considerando el efecto del interés compuesto intra-anual.
* **Fórmula de la Tasa Efectiva (EAR):**
  $$ r_e = \left( 1 + \frac{r_n}{m} \right)^m - 1 $$
  Donde $m$ es el número de periodos de capitalización al año (ej. mensual es 12, trimestral es 4).

> *Ejemplo clásico:* Si una tarjeta de crédito te cobra "1.5% mensual". 
> El banco podría decir: "¡Es solo un 18% anual! (1.5% x 12 meses = Tasa Nominal)".
> Pero la matemática dice: Tasa Efectiva = $(1 + 0.015)^{12} - 1 = 0.1956$ o **19.56% anual real**. ¡Como analista, siempre calculas la efectiva!

---

