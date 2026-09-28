# Semana 37 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: El DCF de "CloudCorp" en Excel

* **Datos de CloudCorp (Proyectados a 5 años):**
  * WACC: 10%
  * Suma del Valor Presente de los FCFF de los años 1 al 5: **$150 Millones**
  * FCFF del Año 5: **$30 Millones**
  * Tasa de crecimiento perpetuo ($g$): **2%**
  * Deuda Total: **$50 Millones**
  * Efectivo: **$10 Millones**
  * Número de Acciones: **10 Millones**

**Modelaje en Excel paso a paso:**

**Paso 1: Cálculo del Valor Terminal (TV) al final del Año 5**
* $FCFF_{Año6} = 30 \times (1 + 0.02) = 30.6$
* $TV = \frac{30.6}{0.10 - 0.02} = \frac{30.6}{0.08} = \mathbf{\$382.5 \text{ Millones}}$

**Paso 2: Traer el Valor Terminal a Valor Presente (Año 0)**
* El TV ocurre en el Año 5, así que debe descontarse 5 años al WACC.
* $VP_{TV} = \frac{382.5}{(1.10)^5} = \frac{382.5}{1.6105} = \mathbf{\$237.5 \text{ Millones}}$

**Paso 3: Calcular el Enterprise Value (EV)**
* $EV = VP_{FCFFs} (150) + VP_{TV} (237.5) = \mathbf{\$387.5 \text{ Millones}}$

**Paso 4: El Puente al Equity Value**
* Deuda Neta = Deuda (50) - Efectivo (10) = $40 Millones.
* Equity Value = EV (387.5) - Deuda Neta (40) = **$347.5 \text{ Millones}}**

**Paso 5: Precio por Acción**
* Target Price = Equity Value / Acciones = $347.5M / 10 Millones = **$34.75 por acción**.

*(Si la acción hoy cotiza en la bolsa a $25, tu recomendación de inversión es **COMPRAR**, porque el valor intrínseco es 39% superior al precio de mercado).*


## Plantilla de Excel

!!! abstract "Descarga: modelo DCF con sensibilidad"
    **[:material-file-excel: dcf_wacc.xlsx](../../assets/plantillas/dcf_wacc.xlsx)**

    La hoja **DCF** monta el modelo completo: flujos explícitos, valor terminal por Gordon,
    puente de Enterprise Value a precio por acción, y el **peso del valor terminal sobre el EV**
    como señal de alarma.

    La hoja **Sensibilidad** es una matriz WACC × g de 36 celdas, cada una recalculando el DCF
    entero. Es la forma profesional de presentar una valuación: **un rango, no un número**.

    Con los datos de LogiTrans reproduce la solución de esta semana: EV **623,94**,
    Equity **583,94** y **$116,79 por acción** (con el valor terminal pesando el 77 %).

---
