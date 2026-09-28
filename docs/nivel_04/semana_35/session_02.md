# Semana 35 · Sesión 2: Profundización

## 4. El Impacto en el Flujo de Caja Libre (FCFF)
A diferencia del Estado de Resultados, el Flujo de Caja Libre (FCFF) que usas para valorar proyectos descuenta los impuestos reales pagados en efectivo. 
* Vimos en la Semana 22 la fórmula del FCFF:
  $$ FCFF = EBIT \times (1 - \text{Tasa de Impuestos}) + \text{Depreciación} - \text{CapEx} - \Delta \text{Capital de Trabajo} $$
* El término $EBIT \times (1 - T)$ es el **NOPAT** (Utilidad Operativa Después de Impuestos). Es el efectivo que le queda a la empresa para pagar a bancos y accionistas, *después* de que el gobierno se lleva su parte, pero *antes* de pagar intereses (para no mezclar el escudo fiscal de la deuda con el operativo).

---

## Los impuestos en el flujo de caja de un proyecto

En un modelo de proyecto, los impuestos entran por tres vías, y olvidar cualquiera de ellas
distorsiona el VAN:

**1. Impuesto sobre la utilidad operativa.** Es el $EBIT \times t$ del NOPAT.

**2. El escudo fiscal de la depreciación.** Aunque la depreciación no sea flujo, **reduce la
base gravable**, y ese ahorro sí es caja:

$$\text{Escudo} = \text{Depreciación} \times t$$

**3. El tratamiento fiscal del valor residual.** Si al final del proyecto vendes el activo por
encima de su valor en libros, esa ganancia **tributa**:

$$\text{Flujo neto por venta} = \text{Precio} - t \times (\text{Precio} - \text{Valor en libros})$$

*Ejemplo:* vendes por $\$50,000$ un activo cuyo valor en libros es $\$20,000$, con $t = 25\%$:

$$50{,}000 - 0.25(30{,}000) = \mathbf{\$42{,}500}$$

Si lo vendieras **por debajo** del valor en libros, la pérdida genera un **ahorro** fiscal, y el
flujo neto sería mayor que el precio de venta.

---

## Cómo la fiscalidad cambia la decisión de invertir

Dos proyectos idénticos en un país con 25 % de impuesto y en otro con 35 %:

| | País A ($t = 25\%$) | País B ($t = 35\%$) |
|---|---|---|
| EBIT | 1,000 | 1,000 |
| NOPAT | 750 | 650 |
| (+) Depreciación | 200 | 200 |
| (−) CapEx | (250) | (250) |
| **FCFF** | **700** | **600** |
| A perpetuidad al 10 % | **7,000** | **6,000** |

**Una diferencia de 10 puntos en la tasa cambia el valor del proyecto un 14 %.** Es la razón
económica —no la moral— de que las multinacionales dediquen tanto esfuerzo a la localización
fiscal, y el tema que desarrollarás en la Semana 36.

**Los tres instrumentos fiscales que más mueven la aguja en un proyecto:**

* **Depreciación acelerada.** No cambia el impuesto total, pero lo **difiere**, y por valor del
  dinero en el tiempo eso vale dinero.
* **Créditos fiscales a la inversión.** Descuentan directamente de la cuota, no de la base: un
  crédito de $\$100$ vale mucho más que una deducción de $\$100$.
* **Compensación de pérdidas (NOL).** Si el proyecto pierde dinero los primeros años, esas
  pérdidas pueden compensar utilidades futuras. Un proyecto dentro de una empresa ya rentable
  aprovecha el escudo **de inmediato**; el mismo proyecto en una empresa nueva tiene que esperar.

!!! warning "La tasa impositiva que debes usar en un DCF"
    Usa la **tasa marginal**, no la media.

    La decisión de invertir es incremental: lo relevante es el impuesto que se pagará **sobre
    la utilidad adicional** que genere el proyecto, no la tasa media histórica de la empresa
    (que puede estar distorsionada por créditos puntuales o pérdidas antiguas).

    Y para el **valor terminal**, converge hacia la tasa **estatutaria**: ninguna ventaja fiscal
    dura para siempre, y asumir a perpetuidad una tasa efectiva anormalmente baja es uno de los
    errores que más infla las valuaciones.

---
