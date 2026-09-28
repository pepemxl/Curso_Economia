# Semana 9 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: Método Indirecto para calcular el Efectivo
La empresa "BlueSky Corp" reporta al final del año:
* Utilidad Neta: $\$200$
* Depreciación: $\$50$ (Gasto contable, no salida de efectivo)
* Aumento en Cuentas por Cobrar: $\$30$ (Clientes nos deben más, no nos pagaron)
* Aumento en Inventario: $\$20$ ( Compramos más productos y están en la bodega)
* Aumento en Cuentas por Pagar: $\$40$ (Le debemos más a los proveedores, retenimos efectivo)
* Compra de nueva maquinaria (CapEx): $\$80$
* Pago de préstamo del banco: $\$50$

**Cálculo del Flujo de Efectivo:**

**1. Flujo de Operación (CFO):**
* Utilidad Neta: $+200$
* Sumar Depreciación (no es gasto de efectivo): $+50$
* Restar Aumento en Cuentas por Cobrar (el efectivo no entró): $-30$
* Restar Aumento en Inventario (salió efectivo para comprar bienes): $-20$
* Sumar Aumento en Cuentas por Pagar (retenimos efectivo que debíamos): $+40$
* **Total CFO = $240$** *(Nota: Aunque la Utilidad fue 200, el flujo operativo fue 240 gracias a la depreciación y a retener pagos a proveedores).*

**2. Flujo de Inversión (CFI):**
* Compra de Maquinaria: $-80$
* **Total CFI = $-80$**

**3. Flujo de Financiamiento (CFF):**
* Pago de Préstamo: $-50$
* **Total CFF = $-50$**

**Variación Neta de Efectivo:** $CFO (240) + CFI (-80) + CFF (-50) = \mathbf{+\$110}$
*(La empresa generó $110 netos en efectivo en el banco este año).*

**Cálculo del Flujo de Caja Libre (FCF):** 
$FCF = CFO (240) - CapEx (80) = \mathbf{\$160}$. 
*La empresa tiene $160 de caja libre para pagar deudas extras, hacer adquisiciones o dar dividendos.*

---

## Segundo ejercicio: dos empresas con la misma utilidad y destinos opuestos

Aquí está el ejercicio que enseña de verdad para qué sirve este estado. Dos empresas del mismo
sector reportan **exactamente la misma utilidad neta de $\$200$**:

| Concepto | **SólidaCorp** | **FrágilCorp** |
|---|---|---|
| Utilidad neta | 200 | 200 |
| (+) Depreciación | 50 | 50 |
| (−) Aumento en cuentas por cobrar | (20) | **(180)** |
| (−) Aumento en inventario | (10) | **(120)** |
| (+) Aumento en cuentas por pagar | 30 | 20 |
| **CFO** | **250** | **(30)** |
| (−) CapEx | (80) | (80) |
| **FCF** | **170** | **(110)** |

**Misma utilidad. Una genera $\$170$ de caja libre; la otra quema $\$110$.**

Un inversionista que solo mirase el Estado de Resultados las consideraría idénticas.

**El diagnóstico de FrágilCorp:** sus cuentas por cobrar crecieron $\$180$ sobre una utilidad de
$\$200$. Está **vendiendo pero no cobrando**. Y su inventario subió $\$120$: produce más de lo
que vende. Las dos cosas a la vez apuntan a un mismo lugar: **está forzando ventas a crédito a
clientes de mala calidad para sostener el crecimiento reportado.**

**Cómo termina esta historia:** llega un momento en que la cartera vieja hay que provisionarla
como incobrable, y el inventario obsoleto hay que castigarlo. Ambas cosas golpean el P&L de
golpe, y ese trimestre la utilidad se desploma. El flujo de efectivo lo había anticipado con
varios trimestres de antelación.

---

## Tercer ejercicio: los ratios de calidad del beneficio

Sobre los mismos datos, calcula los tres indicadores que un analista revisa en este orden:

**1. Ratio de calidad del beneficio (*earnings quality*)**

$$\text{Calidad} = \frac{CFO}{\text{Utilidad neta}}$$

$$\text{Sólida} = \frac{250}{200} = \mathbf{1.25} \qquad \text{Frágil} = \frac{-30}{200} = \mathbf{-0.15}$$

**Interpretación:** por encima de 1 la empresa convierte cada peso de utilidad contable en más
de un peso de caja. Por debajo de 0,8 de forma sostenida, hay que investigar. Negativo es una
bandera roja inmediata.

**2. Conversión de efectivo (*cash conversion*)**

$$\frac{FCF}{\text{Utilidad neta}}: \quad \text{Sólida} = 0.85 \qquad \text{Frágil} = -0.55$$

**3. CapEx sobre depreciación**

$$\frac{80}{50} = 1.6\times \text{ en ambas}$$

Este ratio dice si la empresa está **manteniendo o expandiendo** su capacidad:

| Ratio | Lectura |
|---|---|
| $< 1$ | Invierte menos de lo que se desgasta: **se está descapitalizando** |
| $\approx 1$ | Solo mantenimiento; sin crecimiento orgánico |
| $> 1$ | Expansión de capacidad |

Cuidado con el caso $<1$ sostenido: mejora el FCF a corto plazo y por tanto el DCF, pero la
empresa se está comiendo su propia capacidad productiva. Es una forma sutil de maquillar la
generación de caja.

!!! danger "El orden en que un analista lee los estados financieros"
    Contra toda intuición, **no** se empieza por el Estado de Resultados:

    1. **Flujo de efectivo primero.** Es el más difícil de manipular: el efectivo o está en el
       banco o no está.
    2. **Balance segundo.** ¿Qué cuentas crecen más rápido que las ventas? Ahí se esconden los
       problemas.
    3. **Estado de Resultados al final.** Ya sabiendo qué buscar, se contrasta si la utilidad
       reportada es consistente con lo anterior.
    4. **Notas a los estados financieros.** Donde de verdad está la información: criterios
       contables, contingencias, vencimientos de deuda, partes relacionadas.

    La utilidad es una **opinión**; el efectivo es un **hecho**. Empieza siempre por los hechos.

---
