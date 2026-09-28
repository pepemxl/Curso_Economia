# Semana 30 · Sesión 2: Profundización

## 4. Swaps: Intercambio de Flujos de Caja
Un Swap (canje) es un acuerdo entre dos partes para intercambiar flujos de caja en el futuro. El más común es el **Vanilla Interest Rate Swap**.

* **Mecánica:** Una empresa tiene una deuda a tasa variable (ej. SOFR + 3%) pero teme que las tasas suban. Su banco le ofrece un Swap: la empresa le paga al banco una tasa fija (ej. 5%), y el banco le paga a la empresa una tasa variable.
* *Efecto neto:* La empresa transformó matemáticamente su deuda variable en una deuda fija. Se elimina el riesgo de tipo de interés.

---

## Los tipos de swap y para qué se usa cada uno

| Swap | Qué se intercambia | Uso típico |
|---|---|---|
| **De tasa de interés** (*IRS*) | Flujos fijos por variables sobre un nocional | Convertir deuda variable en fija (o al revés) |
| **De divisas** (*Cross-currency*) | Principal e intereses en dos monedas | Empresa que factura en euros y se endeudó en dólares |
| **De materias primas** | Precio fijo por precio de mercado | Aerolínea que fija el precio del combustible |
| **De incumplimiento crediticio** (*CDS*) | Prima periódica por protección ante impago | Cubrir riesgo de crédito (Semana 31) |
| **De rendimiento total** (*TRS*) | Rendimiento de un activo por una tasa | Exposición sintética sin poseer el activo |

**El nocional nunca se intercambia** en un swap de tasas: solo se liquida la **diferencia neta**
entre ambos flujos. Sobre un nocional de $\$100$ M, si la empresa paga 5 % fijo y recibe SOFR
al 4 %, transfiere solo $\$1$ M al año, no $\$100$ M. Por eso el riesgo de contraparte de un
swap es mucho menor que su tamaño aparente.

---

## Cómo se valora un swap

Un swap de tasas es, en el fondo, **dos bonos**: se está largo en uno y corto en el otro.

$$V_{swap} = B_{recibe} - B_{paga}$$

**En el momento de contratarlo, la tasa fija se elige precisamente para que $V = 0$**: ninguna de
las dos partes paga nada por entrar. Esa tasa fija de equilibrio se llama **tasa swap**, y la
curva de tasas swap es una de las referencias centrales del mercado de renta fija.

**Después, el swap adquiere valor.** Si las tasas suben, quien paga fijo gana (está pagando
menos de lo que costaría hoy contratar el mismo swap) y quien paga variable pierde. Ese valor
de mercado (*mark to market*) es el que aparece en el balance como activo o pasivo derivado, y
el que genera llamadas de garantía.

**Ejemplo.** Una empresa contrata un swap pagando 5 % fijo sobre $\$100$ M a 5 años. Al año
siguiente las tasas suben y el swap equivalente a 4 años se cotiza al 6,5 %. La empresa está
pagando 150 pb menos que el mercado:

$$V_{swap} \approx 100\text{M} \times 1.5\% \times \text{duración}(≈3.7) = \mathbf{+\$5.5\text{M}}$$

El swap vale $\$5,5$ M a favor de la empresa. Ese es exactamente el importe que su deuda a tasa
variable se ha encarecido: **la cobertura funcionó.**

!!! tip "Por qué una empresa usa un swap en lugar de emitir deuda fija"
    Si lo que quiere es tasa fija, ¿por qué no emitir directamente un bono a tasa fija?

    * **Ventaja comparativa.** A veces una empresa consigue mejores condiciones en variable (por
      su relación con el banco) y luego convierte con un swap. La suma sale más barata que la
      emisión fija directa.
    * **Flexibilidad.** Un swap se puede cancelar o revertir sin tocar la deuda subyacente ni
      renegociar con los bonistas.
    * **Rapidez y costo.** Emitir un bono exige folleto, calificación y colocación. Un swap se
      contrata en una llamada.
    * **Gestión dinámica.** Se puede cubrir el 60 % de la deuda hoy y ajustar el porcentaje
      según cambie la visión sobre las tasas.

    El precio de esa flexibilidad es el **riesgo de contraparte** y las **garantías** que hay
    que aportar cuando el swap se mueve en contra — precisamente lo que asfixió a varias
    empresas energéticas en 2022, cuando sus coberturas de precio exigieron márgenes
    multimillonarios de la noche a la mañana.

---
