# Semana 18 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: Las 5 Fórmulas Maestras
Estás construyendo el Año 1 de la empresa "RetailPro". Tienes los datos del Año 0 y los supuestos. Aquí está la anatomía de las 5 fórmulas que debes escribir en Excel para el Año 1:

1. **Ventas:** `= B2 * (1 + Supuestos!$B$3)` *(Donde B2 es la venta anterior y B3 es el 5% de crecimiento).*
2. **Cuentas por Cobrar:** `= (P&L!Ventas / 365) * Supuestos!DiasCobranza` *(Si vendes 1,000 y das 30 días de crédito, los clientes te deberán 82.2).*
3. **PP&E (Maquinaria):** `= B10 + P&L!CapEx - P&L!Depreciacion` *(Si tenías 500, invertiste 100 este año y depreciaste 50, tu PP&E neto final será 550).*
4. **Ganancias Retenidas:** `= B15 + P&L!UtilidadNeta - CashFlow!Dividendos` *(Tomas el saldo anterior, sumas la nueva riqueza generada y restas lo que le pagaste a los accionistas).*
5. **Efectivo (El plug):** `= B20 + FlujoDeEfectivo!VariacionNetaCash` *(Saldo Inicial de Caja + Dinero Generado este año).*


## Plantilla de Excel

!!! abstract "Descarga: modelo de tres estados"
    **[:material-file-excel: modelo_3_estados.xlsx](../../assets/plantillas/modelo_3_estados.xlsx)**

    Modelo completo de P&L, Balance y Flujo de Efectivo a 5 años, con **selector de
    escenario** (Base / Optimista / Pesimista) mediante `ELEGIR`, el *plug* de efectivo ya
    montado y una fila de comprobación que se pone **verde si el balance cuadra y roja si no**.

    Las celdas **amarillas** son las únicas editables: todo lo demás son fórmulas. Con los
    supuestos por defecto reproduce exactamente el ejercicio de esta semana
    (Ventas 1.100, EBIT 200, Utilidad Neta 127,5, Total Activo 1.227,5).

    Pruébalo: cambia el escenario a 3 (Pesimista) y observa cómo el margen EBITDA cae al 15 %
    y todo el modelo se recalcula sin que el balance deje de cuadrar.

---

## El orden en que se construye un modelo de tres estados

Hay un orden correcto, y saltárselo es la causa habitual de que un modelo no cuadre:

1. **Históricos primero.** Introduce 3 años reales antes de proyectar nada. Sirven para calibrar
   los supuestos (márgenes, rotaciones, CapEx/ventas) y para detectar errores de captura.
2. **Hoja de supuestos.** Todos los *drivers* en un solo sitio: crecimiento, márgenes, días de
   cobro/pago/inventario, CapEx, tasa impositiva, tasa de interés.
3. **P&L hasta el EBIT.** Es la parte que no depende de nada más.
4. **Programas de apoyo (*schedules*).** El de PP&E (saldo inicial + CapEx − depreciación) y el
   de deuda (saldo inicial + emisiones − amortizaciones). Estos alimentan la depreciación y el
   gasto financiero que faltaban en el P&L.
5. **Completa el P&L** con depreciación e intereses → utilidad neta.
6. **Flujo de efectivo**, partiendo de la utilidad neta.
7. **Balance**, con el efectivo del flujo como saldo de caja.
8. **Fila de comprobación** y solo entonces, análisis.

**El problema circular.** Fíjate en el bucle: los intereses dependen de la deuda, la deuda
depende de cuánto efectivo falte, el efectivo depende de la utilidad, y la utilidad depende de
los intereses. Excel lo señalará como **referencia circular**.

Tres formas de resolverlo:

* **Activar el cálculo iterativo** (Archivo → Opciones → Fórmulas → Habilitar cálculo
  iterativo, 100 iteraciones). Funciona, pero es frágil: un error en cualquier celda propaga
  `#¡REF!` por todo el modelo.
* **Interruptor de circularidad:** una celda 1/0 que corta el bucle y permite reiniciar el
  modelo cuando explota. Es la práctica estándar en banca.
* **Calcular los intereses sobre el saldo inicial** de deuda en lugar del promedio. Elimina la
  circularidad por completo a costa de una pequeña imprecisión. **Es lo que hace la plantilla
  de esta semana**, y para la mayoría de los propósitos es más que suficiente.

---

## Segundo ejercicio: proyectar el capital de trabajo con ratios

El ejercicio principal mantenía inventario y cuentas por pagar constantes. En un modelo real se
proyectan con **días de rotación**, porque crecen con el negocio.

**Datos del Año 0:** Ventas 1,000 · Costo de ventas 700 · Cuentas por cobrar 120 · Inventario
200 · Cuentas por pagar 100.

**Paso 1 — Calcular los días históricos**

$$DSO = \frac{CxC}{\text{Ventas}} \times 365 = \frac{120}{1{,}000} \times 365 = \mathbf{43.8 \text{ días}}$$

$$DIO = \frac{\text{Inventario}}{\text{Costo de ventas}} \times 365 = \frac{200}{700} \times 365 = \mathbf{104.3 \text{ días}}$$

$$DPO = \frac{CxP}{\text{Costo de ventas}} \times 365 = \frac{100}{700} \times 365 = \mathbf{52.1 \text{ días}}$$

**Paso 2 — El ciclo de conversión de efectivo**

$$CCE = DSO + DIO - DPO = 43.8 + 104.3 - 52.1 = \mathbf{96 \text{ días}}$$

**La empresa financia 96 días de operación con su propio dinero.** Desde que paga la mercancía
hasta que cobra al cliente pasan más de tres meses. Cuanto más crezca, **más caja necesitará**
solo para sostener el crecimiento.

**Paso 3 — Proyectar el Año 1** (ventas +10 % → 1,100; costo de ventas +10 % → 770), asumiendo
los mismos días:

$$CxC = \frac{43.8}{365} \times 1{,}100 = 132 \qquad \text{Inventario} = \frac{104.3}{365} \times 770 = 220$$

$$CxP = \frac{52.1}{365} \times 770 = 110$$

**Paso 4 — El efecto en la caja**

| Partida | Año 0 | Año 1 | Variación | Efecto en caja |
|---|---|---|---|---|
| Cuentas por cobrar | 120 | 132 | +12 | **−12** |
| Inventario | 200 | 220 | +20 | **−20** |
| Cuentas por pagar | 100 | 110 | +10 | **+10** |
| **Capital de trabajo neto** | **220** | **242** | **+22** | **−22** |

**Crecer un 10 % consumió $\$22$ de caja** que no aparece en ninguna línea del Estado de
Resultados.

!!! tip "Por qué las empresas rentables quiebran creciendo"
    Este es el mecanismo exacto. Si la empresa crece al 50 % en lugar del 10 %, el capital de
    trabajo absorbe $\$110$ en lugar de $\$22$. Si su utilidad neta es de $\$80$, **está
    quemando caja aunque sea rentable**.

    Las tres palancas para romper el círculo:

    1. **Reducir DSO:** cobrar antes (descuentos por pronto pago, *factoring*).
    2. **Reducir DIO:** rotar más rápido (*just in time*, mejor previsión de demanda).
    3. **Aumentar DPO:** pagar más tarde — la palanca favorita de las grandes superficies, que
       cobran al contado y pagan a 90 días. Su CCE es **negativo**: los proveedores financian su
       crecimiento.

    Un CCE negativo es una máquina de generar caja. Es la razón de fondo de la ventaja
    financiera de Amazon o Mercadona sobre sus competidores, y lo estudiarás formalmente en la
    Semana 23.

---
