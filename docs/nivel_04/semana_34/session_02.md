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

## Los tres pilares de Basilea

El marco no es solo un conjunto de ratios: se estructura en tres pilares complementarios.

**Pilar 1 — Requerimientos mínimos de capital.** Las fórmulas: capital sobre activos ponderados
por riesgo, para riesgo de crédito, mercado y operativo. Es la parte cuantitativa.

**Pilar 2 — Revisión supervisora.** El supervisor evalúa si el capital del Pilar 1 es suficiente
para el perfil **concreto** de esa entidad, y puede exigir más. Aquí entran riesgos que las
fórmulas no capturan: concentración, riesgo de tasa en la cartera bancaria, riesgo de modelo.

**Pilar 3 — Disciplina de mercado.** Obligación de publicar información detallada sobre riesgos
y capital, para que analistas, acreedores y depositantes puedan juzgar por sí mismos. La lógica:
la transparencia disciplina mejor que la norma.

**La evolución del marco:**

| Acuerdo | Año | Aportación principal | Fallo revelado |
|---|---|---|---|
| **Basilea I** | 1988 | Capital mínimo del 8 % sobre activos ponderados | Ponderaciones demasiado toscas; arbitraje regulatorio |
| **Basilea II** | 2004 | Modelos internos; los tres pilares | **Prociclicidad**; los bancos calibraban a la baja |
| **Basilea III** | 2010-19 | Más y mejor capital, colchones, **LCR y NSFR**, ratio de apalancamiento | — |
| **Basilea III final** ("IV") | 2017-25 | *Output floor*: el modelo interno no puede dar menos del 72,5 % del estándar | — |

!!! warning "La prociclicidad: el defecto de diseño más difícil de resolver"
    En la expansión, los impagos son bajos, los modelos estiman poco riesgo, se exige poco
    capital y los bancos **prestan más** — alimentando la burbuja.

    En la recesión ocurre lo contrario: los modelos ven más riesgo, se exige más capital, y los
    bancos **restringen el crédito** justo cuando la economía más lo necesita. La regulación
    amplifica el ciclo en lugar de amortiguarlo.

    La respuesta de Basilea III es el **colchón anticíclico**: capital adicional (0-2,5 %) que
    el supervisor exige acumular en los buenos tiempos y **libera** en los malos. Es
    conceptualmente correcto y políticamente difícil: exige que alguien declare que la economía
    va "demasiado bien".

---
