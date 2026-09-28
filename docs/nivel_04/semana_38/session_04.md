# Semana 38 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: La trampa de los Múltiplos Cíclicos (El caso Petrolero)
*Eres analista de equity cubriendo el sector energético (petróleo). Estamos en el pico de la crisis del petróleo (ej. petróleo a $120 el barril).*

Miras a "DrillOil Inc.", una empresa sólida. Su acción está a $100. Sus utilidades netas últimos 12 meses (LTM) son de $20 por acción. 
* **Cálculo del P/E (LTM):** $100 / $20 = **5.0x**. 

El equipo de ventas de tu banco dice: *"¡Compremos DrillOil! El sector transa a 15x, y DrillOil está a 5x. Es una ganga nunca vista"*.

**Tu Análisis Profesional (Cyclical Trap):**
Detienes la orden de compra. Las empresas de commodities son altamente cíclicas. Su utilidad masiva hoy ($20/acción) se debe al pico anómalo del precio del petróleo. Pero los mercados son miradores hacia el futuro (forward-looking). El mercado sabe que el petróleo caerá a $60 el barril el próximo año, y las utilidades de DrillOil colapsarán a $2 por acción.
* **Cálculo del P/E Forward (Año que viene):** $100 / $2 = **50.0x**. 
* ¡DrillOil no estaba barata a 5x! Era extremadamente cara a 50x basada en el futuro. Usar múltiplos LTM (Trailing) en industrias cíclicas es una trampa mortal. Debes usar siempre múltiplos **Forward ( NTM - Next Twelve Months)**.

---

## 8. Tareas y Evaluación de la Semana 38

**A. Lectura y Práctica Obligatoria:**
* *Investment Banking: Valuation, Leveraged Buyouts, and Mergers and Acquisitions* (Rosenbaum & Pearl) - Capítulo sobre Comparable Company Analysis (Comps).
* *Práctica en Excel:* Descarga los balances de 3 bancos locales. Calcula su P/B y EV/EBITDA para ver cuál es el mejor valorado de la manada.

**B. Preguntas de Reflexión:**
1. ¿Por qué el múltiplo P/E (Precio / Utilidad) es prácticamente inútil para valuar una startup de tecnología en etapa Serie A que tiene altísimos ingresos pero Utilidad Neta negativa (porque gasta todo en I+D y marketing)?
2. Explica por qué los "Transaction Comps" (Precedentes de M&A) suelen tener múltiplos matemáticamente más altos que los "Trading Comps" (empresas cotizadas en bolsa).
3. Si una empresa química es muy intensiva en capital (capex masivo) y otra empresa de software (no tiene capex), ¿por qué el múltiplo EV/EBITDA puede dar una comparación engañosa entre ambas?

**C. Ejercicio Práctico a entregar:**
Tienes las siguientes cuatro empresas. Tu tarea es recomendar cuál de ellas es la **más barata** basada en los múltiplos adjuntos y la historia financiera. (Pista: Busca la empresa cuyos múltiplos bajos son justificados por bajo crecimiento o alto riesgo, y descarta la ganga aparente).

* **Empresa A:** P/E = 5x. EV/EBITDA = 3x. P/S = 0.5x. *(Una aerolínea en peligro de quiebra; alta deuda, márgenes decrecientes).*
* **Empresa B:** P/E = 25x. EV/EBITDA = 15x. P/S = 8x. *(Una empresa SaaS de software B2B; crecimiento del 40% anual, márgenes netos del 30%).*
* **Empresa C:** P/E = 10x. EV/EBITDA = 6x. P/S = 1.2x. *(Un banco comercial maduro; crecimiento del 5% anual, ROE del 12%).*
* **Empresa D:** P/E = 8x. EV/EBITDA = 5x. P/S = 0.8x. *(Un supermercado maduro; crecimiento del 3% anual, pero ROTACIÓN de activos altísima).*

Redacta un breve informe (1 párrafo) identificando cuál de las cuatro empresas constituye la mejor oportunidad de inversión (Value Opportunity) justificando por qué su múltiplo, a pesar de no ser el más bajo de todos, refleja una buena relación riesgo/retorno.

??? success "Solución orientativa del Ejercicio C"

    **Recomendación: Empresa B (SaaS B2B).**

    > La Empresa A es la clásica **trampa de valor**: sus múltiplos (P/E 5x,
    > EV/EBITDA 3x) no son una ganga sino el descuento que exige el mercado por una
    > aerolínea sobreendeudada con márgenes en deterioro y riesgo real de quiebra —
    > un P/E bajo sobre utilidades que están por desaparecer no significa nada, y su
    > EV/EBITDA de 3x resulta especialmente engañoso porque el EV ya incorpora una
    > deuda que podría llevarse todo el patrimonio. Las Empresas C y D son negocios
    > sanos pero maduros, correctamente valorados: con crecimientos del 5 % y 3 %,
    > sus PEG de 2.0x y 2.7x indican que se paga un precio justo, sin margen de
    > seguridad ni catalizador que reevalúe el múltiplo. **La Empresa B, pese a tener
    > los múltiplos más altos del grupo, ofrece la mejor relación riesgo/retorno:**
    > su PEG de $25/40 = \mathbf{0.63}$ —muy por debajo del umbral de 1.0 que
    > Peter Lynch consideraba atractivo— significa que se paga menos de un punto de
    > múltiplo por cada punto de crecimiento. Con un margen neto del 30 % y el modelo
    > SaaS de ingresos recurrentes, alta retención y márgenes brutos elevados, ese
    > crecimiento del 40 % es además de calidad y razonablemente predecible. A 25x,
    > el múltiplo no es caro: es **barato en relación con lo que la empresa crece**.

    **El razonamiento cuantitativo detrás**

    | Empresa | P/E | Crecimiento | **PEG** | Veredicto |
    |---|---|---|---|---|
    | A — Aerolínea | 5x | negativo | n/a | **Trampa de valor** |
    | **B — SaaS** | 25x | 40 % | **0.63** | **Mejor riesgo/retorno** |
    | C — Banco | 10x | 5 % | 2.00 | Precio justo |
    | D — Supermercado | 8x | 3 % | 2.67 | Precio justo |

    $$PEG = \frac{P/E}{\text{Tasa de crecimiento (\%)}}$$

    **Por qué A es una trampa y no una oportunidad**

    Un múltiplo bajo es **información**, no una oferta. El mercado descuenta:

    * **Márgenes decrecientes** → la "E" del P/E se contraerá, y con ella el
      múltiplo aparentemente barato subirá solo.
    * **Alta deuda** → en una aerolínea en dificultades, el valor residual del
      patrimonio puede ser **cero** tras pagar a los acreedores, por mucho EBITDA
      que genere.
    * **Ciclicidad extrema** → es exactamente la trampa del caso petrolero de esta
      misma semana: múltiplos LTM engañosos en el pico del ciclo.

    !!! tip "Cómo distinguir una ganga de una trampa"
        La pregunta correcta nunca es *"¿cuál tiene el múltiplo más bajo?"* sino
        **"¿está el múltiplo bajo justificado por los fundamentales?"**.

        Cuatro comprobaciones antes de comprar algo "barato":

        1. **¿Por qué está barato?** Si la respuesta es "deuda, márgenes en caída,
           disrupción del modelo de negocio", el mercado tiene razón.
        2. **¿Qué "E" estoy usando?** Múltiplos **forward (NTM)**, nunca *trailing*
           (LTM), sobre todo en sectores cíclicos.
        3. **¿Hay un catalizador?** Sin un evento que corrija la percepción —cambio
           de gestión, venta de una división, fin del ciclo— una acción barata puede
           seguir barata durante años. *Dead money*.
        4. **¿Es comparable el comparable?** El EV/EBITDA castiga sistemáticamente a
           las empresas intensivas en capital: el EBITDA ignora el CapEx, así que
           una química con inversión masiva y una SaaS sin ella **no son comparables
           con ese múltiplo**. Para la química conviene EV/EBIT o EV/FCF.

        La valuación relativa nunca decide sola: **contrástala siempre con un DCF**
        (Semana 37). Si ambos métodos apuntan al mismo lado, la tesis es sólida.
