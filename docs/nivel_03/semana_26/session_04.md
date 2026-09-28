# Semana 26 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: El trillón de dólares de Apple
*Eres analista de equity cubriendo Apple Inc. en 2024.*

Apple tiene cientos de miles de millones de dólares en efectivo acumulado en el balance general. Durante años no pagó dividendos. En 2012, bajo la presión de inversionistas (ej. Carl Icahn), Apple comenzó a pagar dividendos. Pero la mayor parte de su Programa de Retorno de Capital (Capital Return Program) se basa en **Recompra Masiva de Acciones (Buybacks)**. Apple gasta decenas de miles de millones cada año comprando sus propias acciones y reduciendo el número de acciones en circulación.

**Tu Análisis como Estratega de Inversiones:**
1. **Estructura de Capital:** Apple tiene deuda a pesar de tener liquidez extrema. ¿Por qué? Porque la deuda en EE.UU. es barata y da Escudo Fiscal (visto en M&M con impuestos). Prefieren endeudarse a pagar impuestos repatriando dinero desde el extranjero.
2. **El Impacto del Buyback:** Al reducir el número de acciones año tras año, el "denominador" baja. Aunque las Utilidades Netas totales de Apple no crezcan a tasas de startup, la **Utilidad por Acción (EPS)** sube mágicamente porque se divide entre menos acciones. Esto mantiene el precio de la acción en alta.
3. **La trampa del "Financial Engineering":** Si Apple gasta demasiado efectivo en buybacks en lugar de inventar el "próximo iPhone" (CapEx e I+D), a largo plazo la empresa perderá ventaja competitiva. Debes monitorear en tus modelos de Excel que el gasto en I+D no sea destruido por el gasto en recompra de acciones.

---

## 7. Tareas y Evaluación de la Semana 26

**A. Lectura Obligatoria:**
* *Fundamentos de Finanzas Corporativas* (Ross, Westerfield, Jordan). Capítulos 16 (Estructura de Capital: Límites al uso de la deuda) y 17 (Política de Dividendos y Pago de Utilidades).

**B. Preguntas de Reflexión:**
1. Según el Teorema de Modigliani-Miller con impuestos, el valor de la empresa aumenta linealmente con la deuda. ¿Por qué en la vida real las empresas no se endeudan al 99.9% para maximizar su valor?
2. Un inversor compra acciones de una empresa de biotecnología en crecimiento. En la junta de accionistas, exige que la empresa empiece a pagar dividendos en efectivo. Como CFO de la empresa, ¿qué argumento basado en la Teoría de la Jerarquía y la Señalización le das para rechazar esta demanda?

**C. Ejercicio Práctico a entregar:**
La empresa "BlueSky" no tiene deuda y vale $10,000 millones (100% patrimonio). El gobierno aplica una tasa de impuesto corporativa del 25%. BlueSky decide hacer un apalancamiento: emitirá **$3,000 millones en bonos** y usará ese efectivo para recomprar acciones (reduciendo el patrimonio).

Contesta:
1. Usando la fórmula de M&M con impuestos, calcula el Valor Total de la firma apalancada ($V_L$). (Recuerda: $V_L = V_U + D \times T$).
2. ¿Cuánto dinero en efectivo le ahorra la deuda a la empresa anualmente en concepto de impuestos, si la tasa de interés de los bonos es del 8%? (Escudo Fiscal = Intereses \times Tasa de Impuesto).
3. Si el valor de la firma aumenta gracias al escudo fiscal, ¿este aumento beneficia a los accionistas restantes o a los tenedores de bonos? Explica cómo se distribuye el "pastel" ahora.

??? success "Solución del Ejercicio C"

    **1. Valor de la firma apalancada ($V_L$)**

    $$V_L = V_U + D \times T$$

    $$V_L = 10{,}000 + 3{,}000 \times 0.25 = 10{,}000 + 750$$

    $$\mathbf{V_L = \$10{,}750 \text{ millones}}$$

    Endeudarse creó **$\$750$ millones de valor de la nada** — sin vender un producto
    más ni reducir un costo. El valor proviene íntegramente de que el fisco deja de
    cobrar impuestos sobre los intereses.

    **2. Escudo fiscal anual en efectivo**

    $$\text{Intereses} = 3{,}000 \times 8\% = \$240 \text{ millones}$$

    $$\text{Escudo Fiscal} = 240 \times 0.25 = \mathbf{\$60 \text{ millones por año}}$$

    **Comprobación elegante:** si ese ahorro de $\$60$ millones se percibe a
    perpetuidad y se descuenta al costo de la deuda (8 %):

    $$VP_{escudo} = \frac{60}{0.08} = \$750 \text{ millones} \quad ✓$$

    Coincide exactamente con el $D \times T$ del punto 1. **La fórmula de M&M no es
    magia: es el valor presente de una perpetuidad de ahorros fiscales.**

    **3. ¿Quién se queda con los $750 millones?**

    **Los accionistas. Íntegramente.**

    Los **bonistas no ganan nada extra**: prestaron $\$3{,}000$ y reciben su 8 % de
    mercado, que es exactamente la compensación justa por el riesgo que asumen. Un
    bono comprado a valor par no genera valor para quien lo compra; entrega
    precisamente el rendimiento exigido.

    El reparto del "pastel", paso a paso:

    | | Antes (sin deuda) | Después (apalancada) |
    |---|---|---|
    | Valor total de la firma | 10,000 | **10,750** |
    | (−) Deuda (bonistas) | 0 | 3,000 |
    | **= Patrimonio (accionistas)** | **10,000** | **7,750** |

    A primera vista el patrimonio *cayó* de $10{,}000$ a $7{,}750$. Pero los
    accionistas originales **también recibieron $\$3{,}000$ millones en efectivo** por
    las acciones recompradas:

    $$\$7{,}750 \;(\text{acciones}) + \$3{,}000 \;(\text{efectivo}) = \$10{,}750$$

    Empezaron con $\$10{,}000$ y terminaron con $\$10{,}750$: **ganaron los $\$750$
    millones completos.**

    ¿De dónde salió ese valor? **Del gobierno.** El tercer socio silencioso de toda
    empresa es el fisco, y la deuda simplemente reduce su porción del pastel. El
    valor no se creó: se transfirió.

    !!! danger "Por qué entonces no endeudarse al 100 %"
        Llevada al extremo, la fórmula $V_L = V_U + DT$ diría que conviene financiarse
        con 100 % deuda. En el mundo real eso no ocurre, y la razón son los **costos
        de dificultades financieras** que M&M omite deliberadamente:

        * **Costos de quiebra directos:** abogados, liquidación forzada de activos.
        * **Costos indirectos:** clientes y proveedores que huyen de una empresa
          percibida como frágil, talento que se va, crédito comercial que se corta.
        * **Riesgo de sobreendeudamiento (*debt overhang*):** proyectos con VAN
          positivo que no se financian porque la ganancia iría a los acreedores.
        * **Pérdida del escudo:** si no hay utilidades, no hay impuestos que ahorrar,
          y el escudo fiscal simplemente desaparece.

        La **Teoría del Trade-off** dice que la estructura óptima está donde el valor
        marginal del escudo fiscal iguala el costo marginal esperado de la quiebra.
        Y la **Teoría de la Jerarquía** (*pecking order*) añade que las empresas, en
        la práctica, prefieren primero utilidades retenidas, luego deuda, y solo en
        último lugar emitir acciones — porque emitir señala al mercado que la
        dirección cree que la acción está cara.
