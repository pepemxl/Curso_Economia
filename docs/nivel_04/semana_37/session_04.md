# Semana 37 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: El Peligro de editar "g" (La ilusión de WeWork)
*Eres analista de Venture Capital en 2019. El banco JP Morgan te entrega un modelo DCF de WeWork justificando una valoración de $60 Billones antes de su IPO.*

Revisas el modelo y te das cuenta de que el analista que lo armó asumió:
1. Un WACC bajísimo del 8% (Para una empresa que quema efectivo y no tiene activos colaterales, el riesgo es altísimo. Debería ser 15%+).
2. Una tasa de crecimiento perpetuo ($g$) del **5%**.

**La Destrucción Matemática del Valor:**
En la fórmula $TV = \frac{FCFF}{WACC - g}$, el denominador es $0.08 - 0.05 = 0.03$. El Valor Terminal se inflaba masivamente por un denominador minúsculo.
Ajustas la realidad: Una empresa de coworking no va a crecer al 5% para siempre; es una empresa inmobiliaria cíclica atada a las tasas de interés. Si la economía global a largo plazo crece al 2%, $g$ debería ser 2%. Y el WACC real de WeWork por su riesgo es 15%.

**El Nuevo Resultado:**
* El nuevo denominador es $0.15 - 0.02 = 0.13$. El Valor Terminal se desploma a una décima parte. 
* El Valor de la Empresa de WeWork cae de $60 Billones a menos de $10 Billones. 

**El Veredicto:** Solicitas el modelo en Excel, cambias celda de $g$ de 5% a 2% y la celda del WACC de 8% a 15%. El modelo implosiona a $8 Billones. Rechazas la inversión. Meses más tarde, WeWorks suspende su IPO y colapsa a una valoración de $3 Billones. El DCF te salvó de perder $50 Billones en una burbuja corporativa. *(Y Gordon, el matemático que inventó la fórmula de perpetuidad, salvó tu carrera).*

---

## 7. Tareas y Evaluación de la Semana 37

**A. Lectura y Práctica Obligatoria:**
* *Investment Banking: Valuation, Leveraged Buyouts, and Mergers and Acquisitions* (Rosenbaum & Pearl) - Capítulo sobre Discounted Cash Flow (DCF) Analysis.
* *Práctica Excel:* Construye una tabla con 5 años de flujos de caja ficticios (ej. $10M, $12M, $15M, $18M, $20M), calcula el TV y el EV en Excel usando las funciones `=VNA()` y la fórmula matemática.

**B. Preguntas de Reflexión:**
1. ¿Por qué el WACC es la tasa de descuento correcta para traer a Valor Presente el Flujo de Caja Libre de la Firma (FCFF), pero NO lo es para descontar el Flujo de Caja Libre del Accionista (FCFE)? 
2. En la fórmula del Valor Terminal $TV = \frac{FCFF_{n+1}}{WACC - g}$, ¿qué sucede matemáticamente si la tasa de crecimiento perpetuo ($g$) es mayor o igual al WACC? ¿Por qué se considera un error de modelado fatal?

**C. Ejercicio Práctico a entregar:**
Haz un mini-DCF en Excel o en papel para la empresa "LogiTrans".
* **WACC:** 12%
* **Período explícito:** 3 años.
* **FCFF Año 1:** $50 Millones
* **FCFF Año 2:** $60 Millones
* **FCFF Año 3:** $70 Millones
* **Crecimiento perpetuo después del Año 3 ($g$):** 1.5%
* **Deuda Neta actual:** $40 Millones
* **Acciones en circulación:** 5 Millones

Contesta:
1. Calcula el Valor Presente de los FCFF de los 3 años explícitos (trae a valor presente cada año al 12%).
2. Calcula el Valor Terminal al final del Año 3 y tráelo a Valor Presente (Año 0). Recuerda que $FCFF_{Año4} = FCFF_{Año3} \times (1+g)$.
3. Calcula el Enterprise Value (EV) total.
4. Calcula el Equity Value (Valor del Patrimonio) y el Valor Intrínseco por Acción (Target Price).
