# Semana 7 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: La Startup "TechRise S.A."
Acabas de fundar una empresa de software. Estas fueron tus primeras transacciones en Enero:

**Transacción 1:** Inviertes $\$10,000$ de tu propio bolsillo para crear la empresa (capital).
* Análisis: Entra efectivo a la empresa (Activo Aumenta -> Debitas). Al mismo tiempo, registras el aporte de los dueños (Patrimonio Aumenta -> Acreditas).
* **Asiento en el Libro Diario:**
  * Débito: Cuenta "Efectivo" $\$10,000$
  * Crédito: Cuenta "Capital Social" $\$10,000$
* *Comprobación Ecuación:* $A (10,000) = P (0) + E (10,000)$. ¡Balancea!

**Transacción 2:** Compras computadoras por $\$3,000$ en efectivo.
* Análisis: Entra un nuevo activo, las computadoras (Equipo aumenta -> Debitas). Sale efectivo de las arcas (Activo Efectivo disminuye -> Acreditas).
* **Asiento en el Libro Diario:**
  * Débito: Cuenta "Equipo de Cómputo" $\$3,000$
  * Crédito: Cuenta "Efectivo" $\$3,000$
* *Comprobación Ecuación:* El total de Activos seguía siendo 10,000, pero cambió su composición: Efectivo 7,000 + Equipos 3,000. Pasivos 0, Patrimonio 10,000. ¡Balancea!

**Transacción 3:** Compras licencias de software para revender por $\$2,000$, pero el proveedor te da 30 días de crédito para pagar.
* Análisis: Entra inventario de software (Activo Aumenta -> Debitas). Nace una deuda con el proveedor (Pasivo Aumenta -> Acreditas).
* **Asiento en el Libro Diario:**
  * Débito: Cuenta "Inventario" $\$2,000$
  * Crédito: Cuenta "Cuentas por Pagar" (Pasivo) $\$2,000$
* *Comprobación Ecuación final:* 
  * Activos = 7,000 (Efectivo) + 3,000 (Equipos) + 2,000 (Inventario) = $\$12,000$
  * Pasivos = 2,000 (Cuentas por Pagar)
  * Patrimonio = 10,000 (Capital)
  * **$12,000 (A) = 2,000 (P) + 10,000 (E)$**. ¡Perfecto!

---

## Continuación: las transacciones que sí tocan el Estado de Resultados

Las tres primeras transacciones de TechRise solo movieron el Balance. Sigamos con febrero, donde
por fin aparece el negocio.

**Transacción 4:** Vendes licencias por **$\$5,000$**, cobrando $\$3,000$ al contado y dejando
$\$2,000$ a crédito. El costo de esas licencias (que tenías en inventario) fue de $\$1,200$.

Ojo: **son dos asientos**, no uno. Uno reconoce el ingreso, otro da de baja el inventario.

*Asiento 4a — Reconocimiento del ingreso:*

| Cuenta | Débito | Crédito |
|---|---|---|
| Efectivo (Activo) | 3,000 | |
| Cuentas por Cobrar (Activo) | 2,000 | |
| Ingresos por ventas | | 5,000 |

*Asiento 4b — Costo de la mercancía vendida:*

| Cuenta | Débito | Crédito |
|---|---|---|
| Costo de ventas (Gasto) | 1,200 | |
| Inventario (Activo) | | 1,200 |

**Transacción 5:** Pagas $\$800$ de sueldos del mes en efectivo.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto de sueldos | 800 | |
| Efectivo (Activo) | | 800 |

**Transacción 6 (ajuste):** Las computadoras de $\$3,000$ tienen una vida útil de 3 años. La
depreciación mensual es $3{,}000 / 36 = \$83.33$.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto de depreciación | 83.33 | |
| Depreciación acumulada (contra-activo) | | 83.33 |

Nótese que **no se acredita directamente la cuenta "Equipo"**: se usa una cuenta correctora
(*Depreciación acumulada*) para conservar visible el costo histórico del activo. En el balance
aparecerán ambos, y su diferencia es el **valor neto en libros**.

---

## Cierre del período: del libro diario a los estados

**Estado de Resultados de febrero:**

| Concepto | Monto |
|---|---|
| Ingresos por ventas | 5,000.00 |
| (−) Costo de ventas | (1,200.00) |
| **Utilidad bruta** | **3,800.00** |
| (−) Sueldos | (800.00) |
| (−) Depreciación | (83.33) |
| **Utilidad neta** | **2,916.67** |

**Balance al cierre:**

| | Cuenta | Monto |
|---|---|---|
| **ACTIVO** | Efectivo ($7{,}000 + 3{,}000 - 800$) | 9,200.00 |
| | Cuentas por cobrar | 2,000.00 |
| | Inventario ($2{,}000 - 1{,}200$) | 800.00 |
| | Equipo de cómputo | 3,000.00 |
| | (−) Depreciación acumulada | (83.33) |
| | **Total Activo** | **14,916.67** |
| **PASIVO** | Cuentas por pagar | 2,000.00 |
| **PATRIMONIO** | Capital social | 10,000.00 |
| | Ganancias retenidas (utilidad del período) | 2,916.67 |
| | **Total Pasivo + Patrimonio** | **14,916.67** |

$$14{,}916.67 = 14{,}916.67 \quad ✓$$

!!! tip "El detalle que revela por qué existe el estado de flujos"
    La utilidad neta del mes fue de **$\$2,916.67**, pero el efectivo solo aumentó en
    $\$2,200$ (de 7,000 a 9,200). ¿Dónde está la diferencia?

    | Concepto | Efecto |
    |---|---|
    | Utilidad neta | +2,916.67 |
    | (+) Depreciación (no salió caja) | +83.33 |
    | (−) Aumento de cuentas por cobrar (no se cobró) | (2,000.00) |
    | (+) Disminución de inventario (de 2,000 a 800; ya estaba pagado a crédito) | +1,200.00 |
    | **Variación del efectivo** | **+2,200.00** |

    Ganaste $\$2,916$ en el papel, pero $\$2,000$ siguen en el bolsillo de tus clientes. Si
    esos clientes no pagan, la utilidad era ficticia. **Esa es exactamente la conciliación que
    formaliza el método indirecto de la Semana 9.**

---
