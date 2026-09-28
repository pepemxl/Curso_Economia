# Semana 35 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: El Escudo Fiscal y el IVA en acción

**Parte A: El Escudo Fiscal de la Depreciación**
La empresa "Mueblería Moderna" tiene:
* Ventas: $10,000
* Costos Operativos: $4,000
* Depreciación de camiones: $2,000
* Tasa de Impuesto: 25%

*Cálculo del Escudo:*
1. EBIT = 10,000 - 4,000 - 2,000 = **$4,000**
2. Impuestos pagados (25%) = **$1,000**. (Utilidad Neta = $3,000).

*Si la empresa NO tuviera depreciación:*
1. EBIT = $6,000.
2. Impuestos pagados (25%) = $1,500. (Utilidad Neta = $4,500).
*Conclusión:* Gracias a la depreciación de $2,000, la empresa pagó $500 menos en impuestos. Ese $500 es el "Escudo Fiscal", que es efectivo real retenido en la caja.

**Parte B: La Trampa del IVA en el Flujo de Caja**
Mueblería Moderna compra inventario en marzo por $10,000 + 16% IVA = Paga **$11,600** en efectivo hoy. En abril vende todo por $15,000 + 16% IVA = Cobra **$17,400**.
* *Declaración Fiscal de Abril:* IVA Cobrado ($2,400) - IVA Pagado en marzo ($1,600) = Pagar al gobierno **$800**.
* *Movimiento de Caja Total:* Salida en marzo -$11,600. Entrada en abril +$17,400. Salida en abril al fisco -$800. 
* *Flujo de Caja Neto:* +$5,000 (que coincide con la utilidad bruta contable). El IVA fluyó a través del balance, pero recordatorio: **se necesita caja para pagarlo antes de cobrarlo**.

---

## Segundo ejercicio: el IVA y por qué no afecta al FCFF (pero sí a la caja)

El IVA es el impuesto que más confunde en un modelo financiero, porque **la empresa no lo paga:
lo recauda**. Es un intermediario del fisco.

GreenSolar vende $\$1{,}000{,}000$ con IVA del 21 % y compra insumos por $\$600{,}000$ más IVA.

| Concepto | Base | IVA (21 %) | Total facturado |
|---|---|---|---|
| Ventas | 1,000,000 | **+210,000** (repercutido) | 1,210,000 |
| Compras | 600,000 | **−126,000** (soportado) | 726,000 |
| **A ingresar al fisco** | | **84,000** | |

**En el Estado de Resultados el IVA no aparece por ningún lado.** Los ingresos son
$\$1{,}000{,}000$ y las compras $\$600{,}000$, ambos **sin IVA**. Por tanto **el IVA no afecta
al EBIT, ni al NOPAT, ni al FCFF**.

**Pero sí afecta a la caja, y a veces mucho.** El desfase temporal es real: cobras el IVA de
tus clientes en el momento de la venta, pero lo liquidas al fisco trimestralmente. Entre ambos
momentos, ese dinero está en tu cuenta.

* **Si cobras al contado y liquidas a 90 días:** el IVA es una **fuente de financiación gratuita**.
* **Si vendes a crédito a 120 días** pero debes liquidar el IVA a los 90: **pagas al fisco un
  IVA que aún no has cobrado**. Es una salida de caja pura, y una causa habitual de asfixia en
  empresas que crecen vendiendo a plazo.

!!! warning "Dónde sí entra el IVA en un modelo"
    1. **En el capital de trabajo.** Las cuentas por cobrar y por pagar van **con IVA incluido**,
       mientras que ventas y compras van sin él. Si proyectas el capital de trabajo con
       porcentajes sobre ventas sin IVA, lo subestimas en un 21 %.
    2. **En la inversión inicial.** El IVA del CapEx se recupera, pero **hay que
       desembolsarlo primero**. En un proyecto grande puede ser un problema de liquidez de
       varios meses.
    3. **Cuando la empresa no puede deducirlo.** Bancos, seguros y sanidad realizan operaciones
       exentas: **no pueden recuperar el IVA soportado**, así que para ellos sí es un costo real
       que entra en el P&L.

---

## Tercer ejercicio: el escudo fiscal de la deuda frente al de la depreciación

GreenSolar tiene dos fuentes de ahorro fiscal. Compáralas, porque se tratan de forma muy
distinta en una valuación.

| | **Escudo de la depreciación** | **Escudo de la deuda** |
|---|---|---|
| Origen | $\text{Dep} \times t = 500{,}000 \times 0.20$ | $\text{Int} \times t = 200{,}000 \times 0.20$ |
| Monto anual | **$100,000** | **$40,000** |
| ¿Está en el FCFF? | **Sí**, implícito en el NOPAT | **No**, está en el WACC |
| ¿Requiere endeudarse? | No | Sí |
| ¿Es sostenible? | Solo mientras haya activos que depreciar | Mientras haya deuda y utilidades |

**Por qué el trato es distinto** —y es la pregunta de examen más frecuente del nivel—:

El escudo de la **depreciación** es un fenómeno **operativo**: existe tenga o no tenga deuda la
empresa. Por eso entra en el cálculo del NOPAT y viaja dentro del FCFF.

El escudo de la **deuda** es un fenómeno **financiero**. Si lo metieras también en el FCFF *y*
además usaras el WACC (que ya lo incorpora vía $r_d(1-t)$), lo estarías contando **dos veces**.

$$\text{Ahorro fiscal total anual} = 100{,}000 + 40{,}000 = \$140{,}000$$

De los cuales $\$100{,}000$ están ya dentro del FCFF de $\$1{,}000{,}000$ que calculaste, y
$\$40{,}000$ están en el denominador, dentro del WACC.

!!! tip "La comprobación que evita el doble conteo"
    Antes de dar por bueno cualquier DCF, verifica estas tres cosas:

    1. ¿El flujo parte del **EBIT** (no del EBT)? → correcto para FCFF.
    2. ¿La tasa de descuento es el **WACC** (que ya incluye $r_d(1-t)$)? → correcto.
    3. ¿Los intereses aparecen restados en algún lugar del flujo? → **error**: quítalos.

    Si respondes sí, sí, no, el modelo está bien construido.

---
