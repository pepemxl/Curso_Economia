# Semana 31 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: El escándalo de "Fat Finger" en Knight Capital (La fusión de los 3 riesgos)
*Eres un regulador el 1 de agosto de 2012. Knight Capital Group, uno de los mayores creadores de mercado de Wall Street, pierde $440 millones en 45 minutos.*

**La Autopsia del Riesgo:**
1. **Riesgo Operativo (El origen):** Knight Capital actualizó su software de trading. En un servidor viejo, olvidaron borrar un código de prueba. Al abrir el mercado, ese código muerto se activó y empezó a comprar acciones al precio más alto del día y venderlas al precio más bajo, automáticamente y miles de veces por segundo.
2. **Riesgo de Mercado (El efecto):** Este error operativo se tradujo en una posición masiva y desastrosa en el mercado de acciones. El algoritmo compró millones de acciones que no valían nada en nanosegundos. El mercado reaccionó bajando los precios.
3. **Riesgo de Crédito (El desenlace):** Knight Capital quedó en bancarrota técnica. No podía pagar a sus contrapartes (Clearinghouses). Tuvo que ser rescatada por un consorcio de bancos a un precio de liquidación.

**Lección de Gestión de Riesgos:** Los riesgos no viven en frascos separados. Un fallo tecnológico (Op Risk) se convierte instantáneamente en una pérdida masiva de trading (Market Risk), lo que desencadena un impago a los clearinghouses (Credit Risk). El Risk Management moderno exige pruebas de estrés cruzadas: *"¿Qué pasa si nuestro sistema falla (Op) justo el día que la Reserva Federal sube tasas sorpresivamente (Market) y nuestro mayor cliente se declara en bancarrota (Credit)?"*

---

## 6. Tareas y Evaluación de la Semana 31

**A. Lectura Obligatoria:**
* *Risk Management and Financial Institutions* (John C. Hull). Capítulos 2 y 3 (Tipos de Riesgo y Riesgo de Crédito).
* *Lectura recomendada:* Normativa de Basilea III (Resumen ejecutivo del Banco de Pagos Internacionales - BIS).

**B. Preguntas de Reflexión:**
1. Menciona por qué el riesgo operativo es más difícil de cuantificar matemáticamente y de cubrir con derivados financieros que el riesgo de mercado o el riesgo de crédito.
2. Si una empresa vende sus productos a crédito a 90 días a clientes en el extranjero (ej. el cliente está en Europa y la empresa en USA), ¿Qué dos tipos de riesgos de los tres vistos en clase está enfrentando simultáneamente la empresa? Explica cómo interactúan.

**C. Ejercicio Práctico a entregar:**
Evalúas a una empresa petrolera que pidió un préstamo corporativo de **$50 Millones** al banco donde trabajas. Debido a la caída del precio del petróleo, tu equipo de análisis ajusta sus métricas de riesgo:

* **Exposición al Default (EAD):** $50 Millones ( la empresa aún debe todo el principal).
* **Probabilidad de Default (PD):** Aumenta del 2% al 8% anual (recesión inminente).
* **Pérdida Dado el Default (LGD):** Si quiebra, sus plataformas petroleras (inservibles para otros fines) sólo se venden a precio de chatarra. Tu recuperación será del 30% (LGD = 70%).

Contesta:
1. Calcula la Pérdida Esperada (Expected Loss - EL) para el banco en el escenario actual (PD 8% y LGD 70%). Muestra la fórmula detallada.
2. El banco exige provisiones de capital iguales a la Pérdida Esperada más un colchón de seguridad (Capital Económico). Si esta pérdida esperada es mayor al 1% de la cartera total del banco, el regulador intervendrá la institución. ¿Cuánto dinero en efectivo debe apartar el banco hoy en su cuenta de provisiones para cubrir este único cliente?
3. Como Director de Riesgos, ¿qué instrumento de los vistos en la Semana 30 (Derivados) sugerirías usar para mitigar el Riesgo de Crédito si la empresa efectivamente entra en default en 12 meses? (Pista: Piensa en un contrato que pague si la empresa se va a cero).

??? success "Solución del Ejercicio C"

    **1. Pérdida Esperada (Expected Loss)**

    $$EL = PD \times LGD \times EAD$$

    $$EL = 0.08 \times 0.70 \times \$50{,}000{,}000$$

    $$\mathbf{EL = \$2{,}800{,}000}$$

    Cada factor responde una pregunta distinta:

    | Componente | Pregunta | Valor |
    |---|---|---|
    | $PD$ | ¿Qué probabilidad hay de que quiebre? | 8 % |
    | $LGD$ | Si quiebra, ¿qué fracción pierdo? | 70 % |
    | $EAD$ | ¿Cuánto tengo expuesto en ese momento? | $50 M |

    **El efecto del deterioro macro es brutal.** Con la PD original del 2 %:

    $$EL_{anterior} = 0.02 \times 0.70 \times 50{,}000{,}000 = \$700{,}000$$

    La pérdida esperada **se cuadruplicó** ($+\$2.1$ millones) sin que la empresa
    dejara de pagar un solo peso todavía. Solo cambió la *probabilidad*. Así es como
    una recesión golpea el balance de un banco antes de que aparezca el primer
    impago real.

    Nota además de dónde viene el $LGD$ tan alto: las plataformas petroleras son
    **activos específicos**, sin uso alternativo ni mercado secundario. Un colateral
    genérico —bienes raíces urbanos, flota de camiones— tendría un LGD mucho menor.
    La calidad de la garantía importa tanto como la salud del deudor.

    **2. Provisiones que debe apartar el banco**

    El banco debe provisionar como mínimo la pérdida esperada:

    $$\text{Provisión} = EL = \mathbf{\$2{,}800{,}000}$$

    Sobre el umbral regulatorio del enunciado: para que esta pérdida esperada
    represente **como máximo el 1 %** de la cartera total, el banco necesitaría una
    cartera de al menos

    $$\frac{2{,}800{,}000}{0.01} = \mathbf{\$280 \text{ millones}}$$

    Si la cartera total del banco es menor a $\$280$ millones, este **único cliente**
    dispara la intervención del regulador. Es un caso de libro de **riesgo de
    concentración**: un préstamo de $\$50$ millones a un solo deudor de un solo sector
    cíclico.

    !!! note "EL vs. Capital Económico: dos colchones distintos"
        La distinción es central en gestión de riesgos:

        * La **Pérdida Esperada** es un **costo previsible del negocio**. Se cubre con
          provisiones contables y, en el fondo, se financia cobrando un *spread* de
          crédito a todos los clientes. No es una sorpresa: es el precio de prestar.
        * La **Pérdida Inesperada** —la desviación por encima de la media— se cubre
          con **Capital Económico**, es decir, patrimonio de los accionistas. Ese es
          el colchón para los años malos, y es lo que Basilea III regula (Semana 34).

        Regla mental: **las provisiones absorben lo que esperas; el capital absorbe lo
        que te sorprende.**

    **3. Instrumento de mitigación: el Credit Default Swap (CDS)**

    El derivado indicado es un **CDS (Credit Default Swap)** sobre la deuda de la
    petrolera.

    **Cómo funciona:** el banco paga una prima periódica (el *spread* del CDS,
    típicamente en puntos básicos anuales sobre el nocional) a un vendedor de
    protección. A cambio, si ocurre un **evento de crédito** —impago, quiebra,
    reestructuración forzosa—, el vendedor compensa al banco por la pérdida.

    Es **exactamente un seguro contra el impago de un tercero**, con la misma
    estructura de la *protective put* de la Semana 30: prima cierta y pequeña hoy a
    cambio de protección contra una pérdida grande e incierta.

    El efecto sobre las métricas: el CDS **no reduce la PD de la petrolera** —esa
    sigue siendo 8 %—, sino que **reduce el LGD efectivo del banco**, y con él la
    pérdida esperada y el capital regulatorio requerido.

    Alternativas complementarias, por si el CDS resulta caro o ilíquido:

    * **Sindicar el préstamo:** repartir la exposición con otros bancos y bajar el EAD.
    * **Vender la posición** en el mercado secundario de préstamos.
    * **Exigir colateral adicional** o garantías de la matriz.
    * **Cubrir el factor de riesgo subyacente** con futuros sobre el crudo: si el
      problema real es el precio del petróleo, cubrirlo ataca la causa de la PD.

    !!! warning "Riesgo de contraparte: quién asegura al asegurador"
        Un CDS traslada el riesgo, **no lo elimina**. Si el vendedor de protección
        quiebra justo cuando lo necesitas, te quedas sin cobertura y sin las primas
        pagadas.

        Es literalmente lo que ocurrió en 2008: AIG había vendido cientos de miles de
        millones en CDS sobre hipotecas subprime sin capital que los respaldara.
        Cuando los eventos de crédito llegaron todos a la vez, AIG no pudo pagar y
        requirió un rescate de $\$182$ mil millones.

        Por eso hoy la mayoría de los CDS se liquidan a través de **cámaras de
        compensación centrales (CCP)** con márgenes diarios — una de las reformas
        estructurales post-crisis.
