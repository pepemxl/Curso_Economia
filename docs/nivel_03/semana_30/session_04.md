# Semana 30 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: El "Margin Call" que quebró a Metallgesellschaft
*A principios de los 90, la gigante alemana Metallgesellschaft (MG) tenía contratos para suministrar gasolina a sus clientes a un precio fijo a 10 años. Para cubrirse de que el petróleo subiera, compró Futuros de petróleo en la bolsa.*

**El Problema del "Mark-to-Market":**
El precio del petróleo cayó. Como MG tenía Futuros de compra, las pérdidas en sus contratos de futuros se liquidaban **diariamente**. La bolsa le exigía millones de dólares en efectivo (Margin Calls) todos los días para mantener el contrato abierto.

Aunque matemáticamente, a largo plazo (10 años) la empresa iba a estar perfectamente cubierta y equilibrada (ganaba en la venta de gasolina lo que perdía en el futuro), **se quedaron sin efectivo (liquidez)** para pagar los márgenes diarios. El pánico en la junta directiva obligó a cerrar los contratos de futuros con pérdidas masivas de $1.5 billones de dólares. 

**Lección de Finanzas:** La diferencia entre un Forward y un Futuro puede destruir una empresa. Los Forwards no exigen efectivo diario (solo se liquida al final), pero tienen riesgo de contraparte. Los Futuros eliminan el riesgo de contraparte pero exigen liquidez constante. Un CFO debe modelar el flujo de caja del Margen antes de comprar Futuros.

---

## 7. Tareas y Evaluación de la Semana 30

**A. Lectura Obligatoria:**
* *Options, Futures, and Other Derivatives* (John C. Hull) - El "Libro de la Biblia" de los derivados. Lee los capítulos introductorios de Capítulo 1 y 2.

**B. Preguntas de Reflexión:**
1. ¿Por qué una empresa pediría un Swap de Tasa de Interés en lugar de simplemente cancelar su préstamo a tasa variable y sacar un nuevo préstamo a tasa fija? (Pista: Costos de transacción, penalizaciones por pago anticipado y relaciones bancarias).
2. Explica por qué un comprador de una Opción Call nunca puede perder más dinero que la "Prima" pagada, mientras que el vendedor (emisor) de esa misma Call puede tener pérdidas teóricamente ilimitadas.

**C. Ejercicio Matemático a entregar:**
Un fondo de inversión compra **10 contratos de Opciones Put** sobre el índice S&P 500.
* Precio actual del S&P 500: 4,500 puntos.
* Strike (Precio de ejercicio) del Put: 4,400 puntos.
* Prima pagada por cada Put: 50 puntos (En el mercado de índices, 1 punto = $100).
* Multiplicador del contrato: 100.

Contesta:
1. ¿Cuánto efectivo pagó el fondo en total por comprar estas opciones Put? (Calcula la Prima Total).
2. Si al vencimiento el S&P 500 está en 4,200 puntos (caída del mercado), ¿el fondo ejercerá la opción? ¿Cuál será la ganancia bruta (pago total) y la ganancia neta (restando la prima) de esta jugada de cobertura?
3. ¿Cuál sería la pérdida máxima que puede sufrir el comprador de este Put si el mercado, en lugar de caer, sube a 5,000 puntos?

??? success "Solución del Ejercicio C"

    **1. Prima total pagada**

    $$\text{Prima por contrato} = 50 \text{ puntos} \times 100 \;(\text{multiplicador}) = \$5{,}000$$

    $$\text{Prima total} = \$5{,}000 \times 10 \text{ contratos} = \mathbf{\$50{,}000}$$

    Esos $\$50{,}000$ salen de la caja **hoy**, pase lo que pase después. Es el costo
    del "seguro".

    **2. El S&P 500 cae a 4,200 al vencimiento**

    *¿Se ejercerá?* **Sí.** El Put da el derecho a **vender** a 4,400 cuando el
    mercado está en 4,200. Está *in the money* por:

    $$4{,}400 - 4{,}200 = 200 \text{ puntos}$$

    *Ganancia bruta (payoff):*

    $$200 \text{ puntos} \times 100 \times 10 \text{ contratos} = \mathbf{\$200{,}000}$$

    *Ganancia neta:*

    $$\$200{,}000 - \$50{,}000 \;(\text{prima}) = \mathbf{\$150{,}000}$$

    Un retorno del **300 %** sobre la prima invertida. El **punto de equilibrio** de
    la posición está en $4{,}400 - 50 = \mathbf{4{,}350}$ puntos: por debajo de ahí
    la cobertura empieza a dar ganancia neta.

    **3. Pérdida máxima si el mercado sube a 5,000**

    $$\text{Pérdida máxima} = \text{Prima pagada} = \mathbf{\$50{,}000}$$

    Con el índice en 5,000, nadie ejerce el derecho de vender a 4,400 —sería regalar
    600 puntos—. La opción **expira sin valor** y se pierde íntegra la prima.

    Esta es la asimetría que define la compra de opciones:

    | | Comprador del Put |
    |---|---|
    | Pérdida máxima | **Limitada** a la prima ($\$50{,}000$) |
    | Ganancia máxima | Enorme (crece punto a punto según cae el índice) |

    !!! tip "Esto no es una apuesta: es un seguro"
        El enunciado dice que el fondo hace una "jugada de cobertura", y el matiz lo
        cambia todo. Supongamos que el fondo tiene una cartera de $\$4.5$ millones
        replicando el S&P 500 (equivalente a $4{,}500 \times 100 \times 10$).

        | Escenario | Cartera | Puts | **Neto** |
        |---|---|---|---|
        | Índice cae a 4,200 | −$300,000 | +$150,000 | **−$150,000** |
        | Índice sube a 5,000 | +$500,000 | −$50,000 | **+$450,000** |

        Cuando el mercado cae, los puts **amortiguan la mitad de la pérdida**. Cuando
        sube, el costo del seguro apenas recorta el 10 % de la ganancia.

        Es exactamente la lógica del seguro de automóvil: pagas la prima todos los
        años esperando **no** usarla. Perder los $\$50{,}000$ no es un fracaso de la
        estrategia — significa que el escenario que temías no ocurrió.

        Una *protective put* como esta es la forma más directa de gestionar riesgo de
        mercado con derivados, y reaparece en la Semana 32 junto al VaR. Y ojo con el
        otro lado de la operación: **vender** puts descubiertos invierte la asimetría
        —ganancia limitada a la prima, pérdida potencialmente enorme—. Es la
        estrategia que ha quebrado más fondos en la historia.
