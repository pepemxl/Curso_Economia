# Semana 17 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Evaluando una Startup
Tienes los siguientes flujos de caja para una inversión en tecnología:
* Fecha de Inversión (15-Ene-2024): -$500,000
* Primer Retiro (20-Dic-2024): $100,000
* Segundo Retiro (10-Jul-2025): $200,000
* Venta Final / Exit (30-Dic-2026): $400,000

**Cómo lo modelas en Excel en 1 minuto:**
1. En la columna A pones las fechas (formato fecha). En la columna B pones los flujos (-500k, 100k, 200k, 400k).
2. En una celda calculas el retorno anualizado exacto考虑到 los días: `=TIR.NO.PER(B1:B4; A1:A4)`. 
   * *Resultado aproximado:* **15.6% anual real**.
3. Si tu exigencia de rentabilidad (Costo de Capital) es del 10%, calculas el VNA: `=B1 + VNA(10%; B2:B4)`. *(Recuerda dejar la inversión inicial B1 fuera del VNA y restarla, o usa la función VNA.NO.PER).*
   * *Resultado:* Valor Presente Neto de **+$48,500**. (El proyecto es viable, crea valor).

---

