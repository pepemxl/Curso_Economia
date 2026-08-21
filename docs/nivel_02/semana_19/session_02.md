# Semana 19 · Sesión 2: Profundización

## 4. Tablas Dinámicas (Pivot Tables): El Analista de Datos
A veces, el CFO te entrega un Excel con 50,000 filas de transacciones de ventas (fecha, vendedor, producto, monto). Es imposible leer eso. Las Tablas Dinámicas resumen millones de datos en 5 segundos.

* **Cómo funciona:** Arrastras y sueltas. Pones "Vendedor" en Filas, "Mes" en Columnas y "Monto" en Valores. Mágicamente verás una matriz resumida que te dice exactamente cuánto vendió cada persona por mes.
* **Uso en Modelación:** Extraes los resultados anuales de la Tabla Dinámica (Ej. Total Ventas 2019, 2020, 2021) y debes usar un CORTAR (Slicer) para conectarlas a tu dashboard.

---

## 5. El Rey del Modelo: Configuración de Escenarios
Hasta ahora, tus modelos tenían un solo "Supuesto Base". En finanzas, esto es inaceptable. El Banco Central, el equipo de ventas y la economía son inciertos. Debemos crear 3 escenarios:

1. **Escenario Base (Expected):** Lo que racionalmente creemos que va a pasar.
2. **Escenario Optimista (Upside / Bull):** Todo sale bien. Ventas altas, costos bajos, tasas de interés bajas.
3. **Escenario Pesimista (Downside / Bear):** Lo peor. Pérdida de clientes, inflación alta, costos de petróleo disparados.

**La Herramienta "ELEGIR" (CHOOSE):**
En Excel, la forma más limpia de cambiar de escenarios sin que el modelo colapse (sin usar macros complejas) es creando un "Switch" con la función ELEGIR. 
* *Fórmula:* `=ELEGIR(index_num; valor1; valor2; valor3)`
* *Lógica:* Creas una celda llamada "Selector de Escenario" (donde validas que solo se pueda escribir 1, 2 o 3). 
  * Si escribe 1 -> La celda jala el supuesto Base.
  * Si escribe 2 -> La celda jala el supuesto Optimista.
  * Si escribe 3 -> La celda jala el supuesto Pesimista.
* Todo tu P&L referenciará a esa celda. Cambias el 1 a un 3, y tu Utilidad Neta cambiará de ying a yang instantáneamente.

---

