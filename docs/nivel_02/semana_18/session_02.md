# Semana 18 · Sesión 2: Profundización

## 3. Paso a Paso: Cómo Proyectar

### A. El Estado de Resultados (P&L)
Se proyecta de arriba hacia abajo usando combinaciones de matemáticas y estadística:
* **Ventas (Revenue):** Se proyecta usando el crecimiento porcentual histórico o una regresión lineal. (Año 1 = Ventas Año 0 * (1 + Tasa de Crecimiento)).
* **Costo de Ventas (COGS):** Se proyecta como un porcentaje de las Ventas (Ej. Si el margen bruto histórico es 40%, COGS será 60% de las ventas).
* **Depreciación:** No se proyecta en el P&L. Se jala de la pestaña de *PP&E Schedule* (donde calculas cuánto se deprecia la maquinaria existente + la nueva).
* **Intereses:** Se jalan de la pestaña de *Debt Schedule* (donde calculas la deuda promedio del año por la tasa de interés).
* **Impuestos:** Se calcula como (EBT * Tasa de Impuesto). 
* **Utilidad Neta:** Fluye mágicamente al Balance General (a Ganancias Retenidas) y al Flujo de Efectivo (como base del CFO).

### B. El Balance General (Balance Sheet)
Proyectar el Balance es más difícil porque requiere calendarios de apoyo (*Schedules*).
* **Capital de Trabajo (Activo Corriente):** 
  * Cuentas por Cobrar = Días de Cobranza / 365 * Ventas. 
  * Inventario = Días de Inventario / 365 * COGS.
* **Propiedad, Planta y Equipo (PP&E):** Se necesita un *Schedule* de PP&E. 
  * Fórmula: PP&E Año 1 = PP&E Año 0 + CapEx (Inversión nueva) - Depreciación del año.
* **Deuda (Pasivos Largo Plazo):** Se necesita un *Debt Schedule*. Deuda Año 1 = Deuda Año 0 - Amortización del principal + Nueva deuda emitida.

### C. La Conexión Final: El "Plug" de Efectivo (Circulo Virtuoso)
Una vez que tienes todo proyectado, el Flujo de Efectivo resume los cambios. 
1. Utilidad Neta + Depreciación + Cambios en Capital de Trabajo - CapEx = Flujo de Caja Libre Operativo (CFO).
2. CFO + Emisión/Reembolso de Deuda + Dividendos = Variación Neta de Efectivo.
3. **El Circulo:** La "Variación Neta de Efectivo" de este año es la cuenta de "Efectivo" que debe aparecer al final del Balance General del próximo año. 
4. Si el Efectivo entra como activo, hace que el Balance cuadre. **El Efectivo es el "Plug" (tapón)** que hace que $Activos = Pasivos + Patrimonio$ en tu modelo.

---

