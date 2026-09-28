# Semana 35 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: El "Leasing" vs. "Compraventa" y la aceleración del Escudo Fiscal
*Eres el CFO de una aerolínea. NecesitasAgregar un avión de $100 Millones a tu flota. Lo mantendrás por 5 años. La tasa de impuesto corporativa es del 30%.*

**Opción A: Compraventa Tradicional**
Compras el avión. Contablemente, la ley te obliga a depreciarlo en línea recta a 20 años, es decir, $5 Millones de depreciación anual.
* *Escudo Fiscal Anual:* $5M × 30% = **$1.5 Millones de ahorro de impuestos al año**. (Empiezas a ver el efecto en el año 1).

**Opción B: Arrendamiento Financiero (Leasing)**
No compras el avión, lo alquilas (Leasing). Bajo las normas contables (NIIF 16), el alquiler se trata como deuda y el avión se activa en el balance. PERO, en el contrato de leasing pagas una cuota anual de $15 Millones (que cubre capital e intereses). Los $15 Millones son **gastos deducibles en su totalidad el año 1** (no estás limitado a la depreciación de 20 años).
* *Escudo Fiscal Año 1:* $15M × 30% = **$4.5 Millones de ahorro de impuestos este año**.

**Veredicto Financiero:**
El costo matemático del leasing es exactamente el mismo que el préstamo bancario (por el Teorema de Modigliani-Miller visto en la Semana 26). Pero eliges el Leasing por una razón estratégica: el **Valor del Dinero en el Tiempo**. Prefieres ahorrar $4.5 Millones en impuestos el Año 1 (leasing) a que ahorrar $1.5 Millones anuales (compraventa). El escudo fiscal acelerado, descontado a tu WACC, genera un VAN positivo que el banco recompensa apoyando la transacción. *Los impuestos distorsionan la decisión de inversión puramente financiera.*

---

## 7. Tareas y Evaluación de la Semana 35

**A. Lectura Obligatoria:**
* *Fundamentos de Finanzas Corporativas* (Ross, Westerfield, Jordan). Capítulo sobre "Impuestos y Flujos de Caja".
* *Lectura macro:* Repasa el capítulo de Contabilidad sobre el tratamiento de los impuestos diferidos (DTA / DTL).

**B. Preguntas de Reflexión:**
1. Explica la diferencia fundamental de cómo el IGV/IVA impacta el Estado de Resultados y el Flujo de Efectivo de una empresa comercializadora. ¿Por qué una empresa con altísima utilidad contable puede suspender pagos por culpa de la "trampa del IVA"?
2. ¿Por qué en la fórmula del Flujo de Caja Libre de la Firma (FCFF) sumamos la De representación los impuestos se calculan sobre el EBIT (utilidad operativa) y NO sobre el EBT (utilidad antes de impuestos que ya tiene intereses restados)?

**C. Ejercicio Práctico a entregar:**
La empresa industrial GreenSolar está evaluando su Flujo de Caja Libre para este año. Tienes los siguientes datos:
* EBIT: $2,000,000
* Depreciación: $500,000
* Intereses: $200,000 (No incluidos en el EBIT)
* CapEx (Nueva inversión en paneles): $800,000
* Aumento en Capital de Trabajo: $300,000
* Tasa de Impuesto a las Sociedades: 20%

Contesta:
1. Calcula el NOPAT: $EBIT \times (1 - \text{Tasa de Impuestos})$.
2. Calcula el Valor del Escudo Fiscal de la depreciación (en efectivo).
3. Construye el Flujo de Caja Libre de la Firma (FCFF): NOPAT + Depreciación - CapEx - Aumento en Capital de Trabajo. Muestra el resultado final en dólares.

??? success "Solución del Ejercicio C"

    **1. NOPAT (Utilidad Operativa Neta Después de Impuestos)**

    $$NOPAT = EBIT \times (1 - t) = \$2{,}000{,}000 \times (1 - 0.20)$$

    $$\mathbf{NOPAT = \$1{,}600{,}000}$$

    **2. Escudo fiscal de la depreciación**

    $$\text{Escudo}_{dep} = \text{Depreciación} \times t = \$500{,}000 \times 0.20$$

    $$\mathbf{= \$100{,}000}$$

    Este es uno de los conceptos más elegantes de la fiscalidad corporativa: **la
    depreciación no cuesta efectivo, pero ahorra efectivo.**

    El razonamiento en dos columnas:

    | | Sin depreciación | Con depreciación |
    |---|---|---|
    | Base gravable | 2,500,000 | 2,000,000 |
    | Impuestos (20 %) | 500,000 | 400,000 |
    | | | **−$100,000 de impuestos** |

    La empresa **no desembolsa** los $\$500{,}000$ de depreciación —ese dinero ya
    salió cuando compró el activo— pero sí **deja de pagar $\$100{,}000$ al fisco**.
    Es efectivo real que se queda en la caja.

    Por eso los gobiernos usan la **depreciación acelerada** como incentivo a la
    inversión: no cambia el impuesto total pagado a lo largo de la vida del activo,
    pero lo **adelanta en el tiempo**, y por valor del dinero en el tiempo eso vale
    dinero para la empresa.

    **3. Flujo de Caja Libre de la Firma (FCFF)**

    $$FCFF = NOPAT + \text{Depreciación} - CapEx - \Delta CT$$

    | Concepto | Monto |
    |---|---|
    | NOPAT | 1,600,000 |
    | (+) Depreciación | 500,000 |
    | (−) CapEx | (800,000) |
    | (−) Aumento en Capital de Trabajo | (300,000) |
    | **= FCFF** | **1,000,000** |

    $$\mathbf{FCFF = \$1{,}000{,}000}$$

    !!! warning "Por qué los intereses de $200,000 no aparecen por ningún lado"
        Es el error más frecuente en este cálculo, y el enunciado tiende la trampa al
        dar el dato.

        El **FCFF** es el flujo disponible para **todos** los proveedores de capital
        —accionistas *y* acreedores— **antes** de repartirlo. Restar los intereses
        sería descontar el pago a los acreedores de un flujo que precisamente les
        pertenece en parte: los estarías contando dos veces.

        El efecto del financiamiento **ya está incorporado en el WACC**, que es la
        tasa a la que se descuenta este FCFF (Semana 24). Meter los intereses aquí
        *y* usar el WACC sería doble contabilidad, y subvaluaría la empresa.

        Por eso se parte del **EBIT** (antes de intereses) y no del EBT.

        Si en cambio quisieras el **FCFE** (flujo para el accionista), entonces sí:

        $$FCFE = FCFF - \text{Intereses}(1-t) + \text{Nueva deuda neta}$$

        Con estos datos y sin deuda nueva:
        $1{,}000{,}000 - 200{,}000(1-0.20) = \$840{,}000$.

        **Regla para no equivocarse:** FCFF se descuenta al **WACC** y da el
        *Enterprise Value*; FCFE se descuenta al **costo del patrimonio ($r_e$)** y da
        directamente el *Equity Value*. Nunca mezcles los pares.
