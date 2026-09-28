# Semana 33 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: El "Credit Crunch" de 2008 y el colapso del Multiplicador
*Eres un economista jefe en el año 2009. El Banco Central de EE. UU. (la FED) inyecta billones de dólares en el sistema bancario (Quantitative Easing) para evitar una recesión, pero la economía no reacciona. ¿Por qué?*

**El Multiplicador en Teoría vs. Realidad:**
La fórmula $m = \frac{1}{r}$ asume que los bancos siempre están dispuestos a prestar y los clientes siempre quieren pedir préstamos. 
En 2008, tras la caída de Lehman Brothers y la crisis de las hipotecas subprime, el pánico se apoderó de Wall Street. Los bancos comerciales dejaron de confiar en que otros bancos pudieran devolverles el dinero, por lo que dejaron de prestar en el mercado interbancario.

Las entidades bancarias se guardaron los billones inyectados por la FED como **"Reservas Excedentes"** (dinero congelado en sus bóvedas por encima del mínimo legal). 

**La Consecuencia:**
Matemáticamente, el multiplicador bancario real colapsó de 10x a casi 2x. La FED imprimió masa monetaria base masiva, pero el multiplicador se contrajo igual de masivo. El resultado neto fue que la oferta monetaria total de la economía no creció, provocando una deflación temporal y un *Credit Crunch* (estrangulamiento de crédito). Las empresas de Main Street no podían conseguir préstamos comerciales para pagar planillas, profundizando la recesión.

**Lección de Macro-Finanzas:** La política monetaria del Banco Central es el "acelerador", pero el sistema bancario comercial es el "motor". Si el motor está dañado (pánico bancario), no importa cuánto pises el acelerador, el coche no avanzará.

---

## 6. Tareas y Evaluación de la Semana 33

**A. Lectura Obligatoria:**
* Mishkin, Frederic. *The Economics of Money, Banking, and Financial Markets*. Capítulos sobre la industria bancaria y el proceso de creación de dinero.

**B. Preguntas de Reflexión:**
1. Describe el concepto de "Transformación de Madurez" en la banca comercial. ¿Por qué esta función, que es vital para el crecimiento económico, es a su vez la causa principal de las corridas bancarias (Bank Runs)?
2. Si el Banco Central de un país elimina el coeficiente de reserva obligatorio (lleva $r$ a 0%), ¿qué le ocurriría matemáticamente al multiplicador bancario teórico? ¿Qué riesgo extremo estaría asumiendo el sistema financiero?

**C. Ejercicio Matemático a entregar:**
La economía de "Atlantic Republic" tiene un coeficiente de reserva bancaria del **20%**. El Banco Central decide inyectar liquidez comprando bonos al mercado por un valor de **$500 Millones**.

Contesta y demuestra tus cálculos:
1. ¿Cuál es el multiplicador bancario ($m$) en esta economía?
2. Calcula la cantidad total máxima de dinero (Masa Monetaria / M) que puede crear el sistema bancario Atlantic a partir de esta inyección inicial de $500 Millones.
3. Si debido a una crisis de confianza, los bancos deciden guardar un 5% adicional como "Reservas Excedentes" por miedo a que no les pagen (el verdadero $r$ sube al 25%), ¿cuál es el nuevo multiplicador y cuánto dinero total se crea ahora? Explica cómo este simple cambio psicológico destruye liquidez en la economía.

??? success "Solución del Ejercicio C"

    **1. Multiplicador bancario**

    $$m = \frac{1}{r} = \frac{1}{0.20} = \mathbf{5}$$

    Cada peso de base monetaria puede sostener hasta 5 pesos de masa monetaria.

    **2. Creación total de dinero**

    $$M = \text{Inyección} \times m = \$500 \text{ M} \times 5 = \mathbf{\$2{,}500 \text{ millones}}$$

    De ese total, $\$500$ millones son el dinero original del Banco Central y
    **$\$2{,}000$ millones son dinero creado por el sistema bancario** al prestar
    repetidamente los depósitos.

    El mecanismo, ronda por ronda:

    | Ronda | Depósito | Reserva (20 %) | Préstamo |
    |---|---|---|---|
    | 1 | 500.00 | 100.00 | 400.00 |
    | 2 | 400.00 | 80.00 | 320.00 |
    | 3 | 320.00 | 64.00 | 256.00 |
    | 4 | 256.00 | 51.20 | 204.80 |
    | … | … | … | … |
    | **Total** | **2,500.00** | **500.00** | **2,000.00** |

    Es una serie geométrica de razón $0.8$:
    $500 \times (1 + 0.8 + 0.8^2 + \dots) = 500 \times \frac{1}{1-0.8} = 2{,}500$ ✓

    Nótese que el total de reservas retenidas ($\$500$ M) equivale exactamente a la
    inyección inicial. **El sistema no crea reservas: crea depósitos.**

    **3. El pánico eleva el coeficiente efectivo al 25 %**

    $$m_{nuevo} = \frac{1}{0.25} = \mathbf{4}$$

    $$M_{nuevo} = \$500 \text{ M} \times 4 = \mathbf{\$2{,}000 \text{ millones}}$$

    | | Normal | Con pánico | Diferencia |
    |---|---|---|---|
    | Coeficiente efectivo | 20 % | 25 % | +5 pp |
    | Multiplicador | 5.0 | 4.0 | **−20 %** |
    | Dinero creado | $2,500 M | $2,000 M | **−$500 M** |

    **Cómo un cambio psicológico destruye liquidez**

    Los bancos no hicieron nada ilegal ni imprudente. Simplemente **decidieron
    prestar menos y guardar más**, cada uno protegiéndose individualmente. Nadie
    ordenó nada; el Banco Central no retiró un solo peso.

    Y sin embargo **desaparecieron $\$500$ millones de la economía** — exactamente
    el monto que el Banco Central acababa de inyectar. **El estímulo se anuló por
    completo.**

    La mecánica es no lineal y por eso resulta traicionera. Como
    $m = 1/r$, cuanto más sube $r$, más se aplana la curva:

    | $r$ efectivo | Multiplicador | Dinero creado |
    |---|---|---|
    | 20 % | 5.00 | $2,500 M |
    | 25 % | 4.00 | $2,000 M |
    | 33 % | 3.03 | $1,515 M |
    | 50 % | 2.00 | $1,000 M |
    | 100 % | 1.00 | $500 M (ninguna creación) |

    !!! danger "La trampa de liquidez y el círculo vicioso"
        Aquí está el drama de la política monetaria en una crisis: **el Banco Central
        controla la base monetaria, pero no el multiplicador.** Puede inyectar toda la
        liquidez que quiera; si los bancos no prestan, el dinero se queda estacionado
        en reservas excedentes y nunca llega a la economía real.

        El círculo se retroalimenta: los bancos prestan menos → las empresas no se
        financian → quiebran → los bancos temen más impagos → prestan aún menos.

        Es exactamente lo que ocurrió tras 2008 y tras la crisis japonesa de los 90:
        expansiones monetarias enormes con inflación e inversión que no reaccionaban.
        Cuando el canal del crédito se atasca así, la respuesta convencional pierde
        potencia y los bancos centrales recurren a instrumentos no convencionales
        —QE, tasas negativas, préstamos condicionados a que el banco efectivamente
        preste— o el peso recae en la **política fiscal** (Semanas 5 y 6), que inyecta
        demanda sin depender del sistema bancario.
