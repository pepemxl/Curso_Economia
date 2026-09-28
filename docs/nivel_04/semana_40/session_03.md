# Semana 40 · Sesión 3: Entregables y Caso de Referencia

## 4. Entregables y Formato de Presentación

1. **Reporte en PDF:** Diseño profesional, limpio, usando gráficos (barras, líneas y tablas resumen). Evita parrafos enormes; usa bullet points. Wall Street no tiene tiempo de leer.
2. **Modelo en Excel:** Debes entregar el archivo `.xlsx` con:
   * Pestaña de Supuestos (validación de datos y escenarios).
   * Modelo de 3 Estados proyectados (formulas congeladas con F4, estructura azul para inputs, negro para fórmulas).
   * Pestaña de Valuación (Cálculo del WACC, TV y puente al Equity Value).
   * El Excel NO debe contener errores (`#REF!`, `#DIV/0!`). Usa `SI.ERROR` si es necesario.

---

## 5. Análisis de Caso Ejemplo: "Caso Tesla (TSLA) en su etapa de maduración"
*(Este es un ejemplo de cómo estructurar la tesis, NO copies esta empresa, elige la tuya).*

1. **Tesis:** *Comprar.* Tesla ya no es una startup, es un oligopolio global de vehículos eléctricos. El mercado la valúa como una automotriz (P/E 10x), pero su verdadero valor yace en su división de/software (márgenes del 80%) y su avanzada tecnología de baterías.
2. **Macro:** La inflación y las tasas altas enfrían el CapEx del sector, pero el gobierno de EE.UU. inyecta subsidios fiscales (Inflation Reduction Act) que sostienen la demanda.
3. **Contable:** ROE creciente de 10% a 20% impulsado puramente por Margen Neto (Dupont). El problema oculto: El Inventario de autos no vendidos crece un 40% vs Ventas que crecen 15% (Red Flag de demanda frenada). 
4. **Valuación DCF:** WACC de 11% (es una empresa Beta 1.8, altamente riesgosa). Proyectamos que el software pesará el 30% del EBITDA en 5 años. Valor Terminal con $g$ = 3%. Target Price = $280 (actual $170). Upside 65%.
5. **Comps:** Comparado con Ford (P/E 8x), Tesla transa a 40x. Pero si ajustamos Tesla como una empresa de Software/SaaS (EV/Sales 8x), Tesla justifica su múltiplo mixto. Precio Relativo: $250.
6. **Riesgos:** Si China invade Taiwán y se corta el suministro de chips, la producción cae un 50%. El Z-Score es de 3.5 (sin riesgo de quiebra financiera).
7. **Recomendación Final:** **COMPRAR**. Catalyst: Lanzamiento del modelo económico (Model 2) en 2025. El riesgo a la baja es la guerra comercial con China.


## Plantilla de Excel del proyecto final

!!! abstract "Descarga: andamiaje del modelo de valuación"
    **[:material-file-excel: plantilla_reporte_final.xlsx](../../assets/plantillas/plantilla_reporte_final.xlsx)**

    Cinco hojas que cubren el entregable de Excel exigido por la rúbrica:

    | Hoja | Contenido |
    |---|---|
    | **1 Supuestos** | Escenarios con `ELEGIR`, datos históricos y cálculo del WACC |
    | **2 Proyección** | Ventas → EBIT → NOPAT → **FCFF** a 5 años |
    | **3 Valuación DCF** | Descuento, valor terminal y puente EV → Equity → *target price* |
    | **4 Comparables** | Múltiplos del sector por **mediana**, valuación relativa y precio mezclado |
    | **5 Rúbrica** | Autoevaluación sobre 100 puntos y comprobaciones técnicas |

    Viene con datos de ejemplo coherentes para que funcione desde el primer momento: DCF
    **$47,12**, Comps **$47,32**, mezclado **$47,20** frente a un precio de mercado de $42
    (+12,4 % → **MANTENER**). Que dos métodos independientes converjan es precisamente la
    señal de una valuación sana.

    **Sustituye los datos de la hoja 1 por los de tu empresa.** La regla del modelo es que
    ningún número escrito a mano viva fuera de esa hoja.

---
