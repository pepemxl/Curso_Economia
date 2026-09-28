# Semana 36 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El "Irish Double" de Apple y la SEO de Europa
*Eres analista de tech en 2014. La Comisión Europea multa a Apple con $14.5 Billones por evasión fiscal, algo que Apple niega rotundamente argumentando que cumplió todas las leyes.*

**La Estrategia Legal (El "Double Irish with a Dutch Sandwich"):**
Apple Inc. (EE. UU.) era dueña de la propiedad intelectual (patentes del iPhone). Vendió estos derechos a una filial irlandesa "Apple Operations Europe" (irlandés pero residente fiscal en Bermudas). 
Cuando alguien en Alemania compraba un iPhone, le pagaba a una filial holandesa (Apple Netherlands), la cual le pagaba a la filial irlandesa. 
1. El dinero fluía: Alemania -> Holanda -> Irlanda -> Bermudas (0% impuestos).
2. Holanda no cobraba impuestos por ser un tránsito intra-empresa (retención cero en royalties).
3. Irlanda decía: "La sede de tu gerencia está en Bermudas, así que no pagas en Irlanda". Y Bermudas no tiene impuesto a las sociedades.

**El Resultado:** Apple pagaba una tasa corporativa efectiva global de menos del **2%** sobre sus ganancias internacionales.
**El Impacto Financiero y Valuación:** Como el "Impuesto a las Sociedades" gasto era minimo, el NOPAT ($EBIT \times (1-T)$) era masivo. El Flujo de Caja Libre proyectado en los modelos de Excel descuentados a valor presente era billones de dólares más alto que el de sus competidores que pagaban el 25% de impuestos. Gran parte del crecimiento de las acciones tecnológicas en la última década fue impulsado por esta ingeniería fiscal. 

---

## 8. Tareas y Evaluación de la Semana 36

**A. Lectura Obligatoria:**
* *Fundamentos de Finanzas Corporativas* (Ross, Westerfield, Jordan). Capítulos sobre "Impuestos Diferidos" y "Estructura Corporativa Internacional".
* *Lectura macro:* Repasar el concepto de NOPAT visto en la Semana 22 y cómo impacta en el FCFF.

**B. Preguntas de Reflexión:**
1. Describe la diferencia fundamental entre un DTA (Activo por Impuesto Diferido) y un DTL (Pasivo por Impuesto Diferido). ¿Por qué un analista financiero considera un DTL una deuda que eventualmente destruirá flujo de caja?
2. ¿Qué es una NOL (Pérdida Neta Operativa) y por qué es un activo valioso en una transacción de M&A? ¿Por qué los gobiernos limitan su uso (como la Sección 382 en EEUU) cuando una empresa rentable compra a una empresa en quiebra?

**C. Ejercicio Práctico a entregar:**
La empresa "TechGood" opera filiales en dos países. 
* **Filial USA:** Genera una Utilidad Contable de $100 millones. La tasa de impuesto corporativo en EE. UU. es 21%. Impuesto a pagar = $21 millones.
* **Filial Bermudas:** Genera Utilidad Contable de $80 millones. La tasa es 0%. Impuesto a pagar = $0.

* **Estrategia de Precios de Transferencia (Legal y válida):** TechGood USA decide pagar $80 millones en "regalías de licencia de software" a TechGood Bermudas, reduciendo su Utilidad en EE. UU. de $100M a $20M.

Contesta:
1. ¿Cuál es el nuevo impuesto a pagar en EE. UU. después de pagar las regalías a Bermudas?
2. ¿Cuál es la utilidad retenida en Bermudas? ¿Cuánto impuesto pagan en Bermudas?
3. Calcula el ahorro fiscal total logrado por la multinacional gracias a esta planeación tributaria de precios de transferencia. Compara el gasto fiscal total consolidado antes y después de la estrategia.

??? success "Solución del Ejercicio C"

    **1. Nuevo impuesto a pagar en EE. UU.**

    $$\text{Utilidad USA} = \$100M - \$80M \;(\text{regalías}) = \$20M$$

    $$\text{Impuesto USA} = \$20M \times 21\% = \mathbf{\$4.2 \text{ millones}}$$

    **2. Utilidad e impuesto en Bermudas**

    $$\text{Utilidad Bermudas} = \$80M \;(\text{propia}) + \$80M \;(\text{regalías}) = \mathbf{\$160 \text{ millones}}$$

    $$\text{Impuesto Bermudas} = \$160M \times 0\% = \mathbf{\$0}$$

    **3. Ahorro fiscal total**

    | | Antes | Después |
    |---|---|---|
    | Utilidad USA | 100 | 20 |
    | Impuesto USA (21 %) | **21.0** | **4.2** |
    | Utilidad Bermudas | 80 | 160 |
    | Impuesto Bermudas (0 %) | **0.0** | **0.0** |
    | **Utilidad consolidada** | **180** | **180** |
    | **Gasto fiscal consolidado** | **21.0** | **4.2** |
    | **Tasa efectiva consolidada** | **11.67 %** | **2.33 %** |

    $$\text{Ahorro} = \$21M - \$4.2M = \mathbf{\$16.8 \text{ millones}}$$

    Una reducción del **80 % del gasto fiscal**, y la tasa efectiva pasa de 11.67 % a
    2.33 %.

    **El punto clave: la utilidad consolidada no cambió.** Siguen siendo $\$180$
    millones antes y después. La regalía es una transacción **intragrupo**: se elimina
    en la consolidación. No se generó ni un dólar de valor económico nuevo — solo se
    **reubicó la base gravable** desde una jurisdicción con impuestos hacia una sin
    ellos.

    **Impacto en la valuación (el motivo real de la estrategia)**

    Los $\$16.8$ millones ahorrados van directos al NOPAT y, por tanto, al FCFF:

    $$NOPAT = EBIT \times (1 - t_{efectiva})$$

    Con $t = 11.67\%$ frente a $t = 2.33\%$, el flujo de caja libre sube ~9 puntos
    porcentuales **cada año**. Descontado a perpetuidad en un DCF (Semana 37), ese
    diferencial recurrente puede representar **cientos de millones de valor
    empresarial**. Es exactamente el mecanismo que infló las valuaciones tecnológicas
    descrito en el caso de Apple.

    !!! warning "Legal ≠ sostenible: el riesgo que un analista debe modelar"
        Esta planeación es **elusión** (legal), no **evasión** (ilegal). Pero para
        quien valora la empresa, la distinción relevante es otra: **¿es sostenible?**

        Factores que han desmantelado estas estructuras desde 2015:

        * **BEPS (OCDE):** el proyecto contra la erosión de bases gravables obliga a
          que la utilidad se declare donde ocurre la **actividad económica real**, no
          donde está registrada la propiedad intelectual.
        * **Impuesto mínimo global del 15 %** (Pilar Dos, OCDE/G20): si la filial
          tributa por debajo del 15 %, **el país de la matriz cobra la diferencia**.
          Esto anula por completo el beneficio de una jurisdicción al 0 %.
        * **Irlanda cerró el "Double Irish"** en 2015, con período de gracia hasta 2020.
        * **Precios de transferencia:** una regalía de $\$80$ millones debe cumplir el
          principio de *arm's length* —el precio que cobrarían partes independientes—.
          Si el fisco la considera inflada, viene el ajuste más multas e intereses.

        **Implicación práctica para el modelo:** al valorar una multinacional con
        tasa efectiva anormalmente baja, **no proyectes esa tasa a perpetuidad.**
        Modela una convergencia gradual hacia la tasa estatutaria o al menos al 15 %
        global, y trata la diferencia como un **pasivo contingente**. Ese fue
        precisamente el error de quienes valoraron a las tecnológicas asumiendo un
        2 % eterno.
