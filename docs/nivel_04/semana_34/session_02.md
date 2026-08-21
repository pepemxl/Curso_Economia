# Semana 34 · Sesión 2: Profundización

## 4. Los Ratios de Liquidez de Basilea III
Para evitar corridas bancarias, Basilea III creó dos escudos de liquidez obligatorios.

**A. LCR (Liquidity Coverage Ratio - Cobertura de Liquidez a Corto Plazo):**
Asegura que el banco sobreviva a 30 días de pánico bancario.
* **Fórmula:** $LCR = \frac{\text{Activos Líquidos de Alta Calidad (HQLA)}}{\text{Salidas Netas de Efectivo a 30 días}}$
* **Regla:** Debe ser $\ge 100\%$. 
* *Activos HQLA:* Efectivo y Bonos Soberanos de países AAA (ej. Tesoro de EE. UU.). Se asume que los préstamos a clientes o los bonos corporativos NO se pueden vender en un día de pánico sin perder muchísimo valor.

**B. NSFR (Net Stable Funding Ratio - Fondos Estables a Largo Plazo):**
Asegura que el banco no use dinero de corto plazo (depósitos a la vista) para financiar activos de largo plazo (hipotecas a 30 años). Evita el descalce de madurez.
* **Fórmula:** $NSFR = \frac{\text{Fondos Estables Disponibles (ASF)}}{\text{Fondos Estables Requeridos (RSF)}}$
* **Regla:** Debe ser $\ge 100\%$.

---

## 5. Pruebas de Estrés (Stress Testing)
Cada año, los bancos centrales someten a los bancos a exámenes de estrés matemáticos. Se modelan en Excel/Python escenarios hipotéticos catastróficos.
* **Escenario Base:** La economía normal proyectada.
* **Escenario Adverso:** Recesión severa, desempleo al 10%, caída del PIB, colapso del sector inmobiliario.
* **Escenario Severamente Adverso ("Cisne Negro"):** Crisis de deuda soberana, caída del 30% de la bolsa, cero liquidez interbancaria.

El banco debe demostrar que, incluso en el Escenario Severamente Adverso, su ratio de capital (CET1) no cae por debajo del mínimo legal (ej. 4.5%). Si suspende el examen, el regulador le prohíbe pagar dividendos y le exige recapitalizarse inmediatamente.

---
