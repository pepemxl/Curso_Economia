# Semana 18 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: Las 5 Fórmulas Maestras
Estás construyendo el Año 1 de la empresa "RetailPro". Tienes los datos del Año 0 y los supuestos. Aquí está la anatomía de las 5 fórmulas que debes escribir en Excel para el Año 1:

1. **Ventas:** `= B2 * (1 + Supuestos!$B$3)` *(Donde B2 es la venta anterior y B3 es el 5% de crecimiento).*
2. **Cuentas por Cobrar:** `= (P&L!Ventas / 365) * Supuestos!DiasCobranza` *(Si vendes 1,000 y das 30 días de crédito, los clientes te deberán 82.2).*
3. **PP&E (Maquinaria):** `= B10 + P&L!CapEx - P&L!Depreciacion` *(Si tenías 500, invertiste 100 este año y depreciaste 50, tu PP&E neto final será 550).*
4. **Ganancias Retenidas:** `= B15 + P&L!UtilidadNeta - CashFlow!Dividendos` *(Tomas el saldo anterior, sumas la nueva riqueza generada y restas lo que le pagaste a los accionistas).*
5. **Efectivo (El plug):** `= B20 + FlujoDeEfectivo!VariacionNetaCash` *(Saldo Inicial de Caja + Dinero Generado este año).*

---

