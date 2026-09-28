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

??? success "Solución del Ejercicio C"

    **1. Valor Presente de los FCFF explícitos (WACC = 12 %)**

    | Año | FCFF | Factor $1/(1.12)^t$ | Valor Presente |
    |---|---|---|---|
    | 1 | 50.00 | 0.8929 | **44.6429** |
    | 2 | 60.00 | 0.7972 | **47.8316** |
    | 3 | 70.00 | 0.7118 | **49.8246** |
    | | | **Suma** | **142.2991** |

    $$\mathbf{VP_{explícito} = \$142.30 \text{ millones}}$$

    **2. Valor Terminal (Gordon) y su valor presente**

    Primero el flujo del primer año de la perpetuidad:

    $$FCFF_4 = FCFF_3 \times (1+g) = 70 \times 1.015 = \$71.05$$

    $$TV_3 = \frac{FCFF_4}{WACC - g} = \frac{71.05}{0.12 - 0.015} = \frac{71.05}{0.105}$$

    $$TV_3 = \$676.67 \text{ millones}$$

    Este valor está expresado **al final del Año 3**, así que hay que traerlo 3
    períodos:

    $$VP(TV) = \frac{676.67}{(1.12)^3} = \frac{676.67}{1.404928} = \mathbf{\$481.64 \text{ millones}}$$

    !!! danger "El error de descuento más común del DCF"
        El Valor Terminal calculado con Gordon queda situado en el **año $n$**, no en
        el año $n+1$, aunque use el flujo del año 4 en el numerador. Se descuenta
        por $(1+WACC)^3$, **nunca** por $(1+WACC)^4$.

        Descontar un período de más subvaluaría la empresa en un 12 % del componente
        más grande del modelo. Es un error que aparece constantemente en modelos
        reales.

    **3. Enterprise Value**

    $$EV = VP_{explícito} + VP(TV) = 142.30 + 481.64$$

    $$\mathbf{EV = \$623.94 \text{ millones}}$$

    **4. Equity Value y Target Price**

    $$\text{Equity Value} = EV - \text{Deuda Neta} = 623.94 - 40 = \mathbf{\$583.94 \text{ millones}}$$

    $$\text{Valor por acción} = \frac{583.94}{5 \text{ M acciones}} = \mathbf{\$116.79}$$

    **Resumen del puente de valuación:**

    | Concepto | Millones |
    |---|---|
    | VP de flujos explícitos (Años 1-3) | 142.30 |
    | (+) VP del Valor Terminal | 481.64 |
    | **= Enterprise Value** | **623.94** |
    | (−) Deuda Neta | (40.00) |
    | **= Equity Value** | **583.94** |
    | ÷ Acciones en circulación | 5.00 M |
    | **= Valor intrínseco por acción** | **$116.79** |

    !!! warning "El Valor Terminal es el 77 % de la valuación"
        $$\frac{481.64}{623.94} = \mathbf{77.2\%}$$

        Más de tres cuartas partes del valor de LogiTrans **no provienen de los flujos
        que proyectaste con detalle**, sino de una fórmula que asume crecimiento
        constante para siempre. Es completamente normal —en DCF reales el TV suele
        pesar entre 60 % y 80 %— pero obliga a dos disciplinas:

        **Primera: sé conservador con $g$.** Ninguna empresa puede crecer
        indefinidamente por encima de la economía global (~2-3 % real), porque
        acabaría siendo el PIB mundial. Aquí $g = 1.5\%$ es prudente.

        Observa la sensibilidad, que es la lección del caso WeWork de esta misma
        semana:

        | $g$ | TV | Valor por acción |
        |---|---|---|
        | 1.0 % | $642.7 | $111.0 |
        | **1.5 %** | **$676.7** | **$116.79** |
        | 2.5 % | $755.4 | $128.0 |
        | 5.0 % | $1,050.0 | $170.0 |

        Y si alguien pusiera $g \ge WACC$, el denominador se vuelve cero o negativo:
        el modelo devuelve infinito o un valor negativo sin sentido. Matemáticamente
        significaría una empresa que crece más rápido que su costo de capital para
        siempre — algo imposible.

        **Segunda: presenta siempre un rango, no un punto.** Un target price de
        $\$116.79$ transmite una falsa precisión. Lo profesional es una **matriz de
        sensibilidad bidimensional WACC × g** y una recomendación del tipo
        *"valor razonable entre $\$105$ y $\$130$"*.
