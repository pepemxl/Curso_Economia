# Semana 27 · Sesión 2: Profundización

## 3. Valoración de Startups: El "Método VC"
¿Cómo valora una empresa de quant en Wall Street a un equipo de 3 universitarios en un garaje con una app de Inteligencia Artificial que no ha generado ni un dólar de ingresos?

La respuesta es: No puedes usar un Descuento de Flujos de Caja tradicional (DCF) porque el WACC es inestimable (la beta de una startup no existe) y los flujos de caja a 5 años son pura ciencia ficción (IncrementalCash = 0).

Se utiliza el **Método de Capital de Riesgo (Venture Capital Method)**, cuyos pasos son:
1. **Proyectar el Valor Terminal en el "Exit" (Salida):** Generalmente, los fondos VC esperan que la startup sea comprada o salga a bolsa en 5 años. Estiman el Valor de la empresa en el Año 5 usando múltiplos de empresas comparables (ej. Valor = 10x Ventas del Año 5).
2. **Aplicar una Tasa de Descuento Gigantesca:** Como el riesgo de que la startup quiebre es altísimo (30-40% de ellas mueren), el VC no usa WACC. Usa una tasa objetivo de retorno (Target Rate) del 40% al 80% anual.
3. **Calcular el Valor Post-Money (Postinversión):** $VP = \text{Valor Terminal} / (1 + Target Rate)^5$
4. **Calcular Valor Pre-Money (Preinversión):** $Pre-money = Post-money - Inversión Recibida$.
5. **Calcular la Participación (Ownership):** $Participación = Inversión / Post-money Value$.

---

## Cómo se estructura una operación de M&A

Las decisiones de estructura determinan quién asume qué riesgo, y a menudo importan más que el
precio.

**Compra de acciones frente a compra de activos**

| | **Acciones** (*share deal*) | **Activos** (*asset deal*) |
|---|---|---|
| Qué se adquiere | La sociedad entera | Activos y pasivos seleccionados |
| Pasivos ocultos | **Se heredan todos** | Se dejan atrás los no asumidos |
| Contratos y licencias | Continúan | Hay que renovarlos uno a uno |
| Fiscalidad | Suele favorecer al **vendedor** | Suele favorecer al **comprador** (revaloriza la base) |
| Complejidad | Menor | Mayor |

**Forma de pago**

* **Efectivo:** el vendedor no asume riesgo del negocio combinado. Suele exigir menos prima.
* **Acciones del comprador:** el vendedor comparte el riesgo (y el potencial) de las sinergias.
  Señala que el comprador cree que **sus propias acciones están caras**.
* **Earn-out:** parte del precio se paga solo si se cumplen objetivos futuros. Resuelve la
  discrepancia de valoración cuando comprador y vendedor no se ponen de acuerdo sobre el futuro.

**Las etapas de un proceso**

1. **Teaser y NDA** — información anónima; acuerdo de confidencialidad.
2. **Cuaderno de venta (*Information Memorandum*)** — la información completa.
3. **Ofertas no vinculantes** — rango de precio indicativo.
4. **Due diligence** — financiera, legal, fiscal, laboral, ambiental, tecnológica.
5. **Oferta vinculante y SPA** — contrato de compraventa con garantías (*reps & warranties*).
6. **Cierre e integración** — donde se gana o se pierde el valor de verdad.

!!! danger "Dónde se destruye el valor: la integración"
    Los estudios coinciden en que entre el 50 % y el 70 % de las fusiones destruyen valor para
    el accionista del comprador. Las causas casi nunca son de valuación:

    * **Choque cultural.** Es la causa citada con más frecuencia en las post-mortem.
    * **Fuga de talento.** Los mejores profesionales de la adquirida son los que tienen más
      alternativas, y se van primero.
    * **Sinergias de ingresos que no llegan.** Las de **costos** (cerrar duplicidades) se
      cumplen razonablemente; las de venta cruzada casi nunca.
    * **Distracción de la dirección.** Una integración consume 18-24 meses de atención directiva
      que el negocio base deja de recibir.

    Por eso, al modelar una adquisición, la disciplina es: **sé conservador con las sinergias de
    ingresos, realista con las de costos, y presupuesta explícitamente los costos de
    integración**, que suelen equivaler a un año entero de las sinergias esperadas.

---
