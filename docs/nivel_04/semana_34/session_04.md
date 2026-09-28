# Semana 34 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: Silicon Valley Bank (SVB) y la violación del NSFR
*A principios de 2023, el Silicon Valley Bank colapsó. Eres el analista forense del regulador tratando de entender qué ratio de Basilea no cumplieron.*

SVB tenía depósitos a la vista (clientes de tecnología que podían retirar su dinero en 1 clic) de Startups. Con ese dinero de *corto plazo*, SVB compró Bonos del Tesoro a 10 años (giros a *largo plazo*). 

**La Falla del NSFR (Descalce de Madurez):**
A nivel contable, SVB cumplía el LCR porque los Bonos del Tesoro eran considerados "HQLA" (activos líquidos). Pero Basilea III los penalizaba en el NSFR: los bonos a 10 años requieren fondos estables (fondos que no se vayan a retirar en 30 días). SVB los estaba financiando con depósitos inestables de corto plazo. 

*El Cisne Negro:* Acelerado por Twitter, los clientes retiran $42 billones en un día. SVB no tiene el efectivo/Pago inhibido, debe vender los Bonos del Tesoro a 10 años *hoy* para pagar. Pero como las tasas subieron (Semana 24), esos bonos valían menos. Al venderlos, realizaron pérdidas masivas que borraron su capital contable (CET1). Quiebra técnica.

**Lección regulatoria:** El LCR le dio una falsa sensación de seguridad a SVB porque asumía que los bonos del gobierno eran tan líquidos como el efectivo. La nueva regulación propuesta post-SVB obliga a trucar los bonos a su valor de mercado real (Hi-Fi) en las hojas de cálculo de liquidez, aplicando cortes ("haircuts") a los HQLA en proporción a su riesgo de tasa de interés.

---

## 8. Tareas y Evaluación de la Semana 34

**A. Lectura Obligatoria:**
* *Risk Management and Financial Institutions* (John C. Hull). Capítulos sobre Regulación (Basilea I, II y III) y Riesgo de Liquidez.
* *Lectura recomendada:* Resumen ejecutivo del documento "Basel III: Finalising post-crisis reforms" del Banco de Pagos Internacionales (BIS).

**B. Preguntas de Reflexión:**
1. Explica la diferencia entre "Solvencia" y "Liquidez" en un banco. ¿Cómo puede un banco ser contablemente millonario (solvencia) y fallar en pagar a sus clientes que hacen fila en la puerta (liquidez)?
2. ¿Por qué Basilea III exige que el capital CET1 (Patrimonio de Nivel 1) esté compuesto casi exclusivamente por acciones comunes y utilidades retenidas, en lugar de permitir activos intangibles como el "Goodwill" (Crédito Mercantil)?

**C. Ejercicio Práctico a entregar:**
El "GlobalBank" reporta la siguiente información para su cálculo de Liquidez (LCR):
* Efectivo en bóveda y reservas en el Banco Central: $2,000 Millones.
* Bonos del gobierno soberano (AAA), vencimiento a 6 meses: $3,000 Millones.
* Bonos corporativos de empresas de alta calidad (AA), vencimiento a 1 año: $1,500 Millones.
* Préstamos hipotecarios a 30 años otorgados a clientes: $10,000 Millones.

El regulador le informa a GlobalBank que, para el cálculo del LCR, solo el Efectivo y los Bonos Soberanos a corto plazo cuentan al 100% de su valor como Activos Líquidos de Alta Calidad (HQLA). Los corporativos AA solo cuentan al 50% (haircut del 50%) y los préstamos hipotecarios no cuentan como HQLA (0%).
Además, en un escenario de Stress Testing, el banco proyecta salidas netas de efectivo a 30 días de **$6,000 Millones**.

Contesta:
1. Calcula el valor ajustado (HQLA) de GlobalBank aplicando los "haircuts" regulatorios de Basilea III.
2. Calcula el LCR de GlobalBank. ¿Supera el banco el mínimo legal del 100%?
3. Si los depositantes entran en pánico y las salidas netas proyectadas suben de $6,000 Millones a $7,000 Millones (Escenario Severamente Adverso), ¿cuál sería el nuevo LCR? ¿Sobreviviría GlobalBank a esta prueba de estrés?

??? success "Solución del Ejercicio C"

    **1. HQLA ajustado por haircuts de Basilea III**

    | Activo | Valor | Ponderación | HQLA computable |
    |---|---|---|---|
    | Efectivo y reservas en Banco Central | 2,000 | 100 % | **2,000** |
    | Bonos soberanos AAA a 6 meses | 3,000 | 100 % | **3,000** |
    | Bonos corporativos AA a 1 año | 1,500 | 50 % | **750** |
    | Hipotecas a 30 años | 10,000 | 0 % | **0** |
    | | **16,500** | | **5,750** |

    $$\mathbf{HQLA = \$5{,}750 \text{ millones}}$$

    El dato revelador: **el banco tiene $\$16{,}500$ millones en activos, pero solo
    $\$5{,}750$ millones cuentan como liquidez de alta calidad.** Los $\$10{,}000$
    millones en hipotecas —el 61 % del balance— valen **cero** a efectos de LCR.

    No es que sean malos activos; muchas hipotecas son excelentes préstamos. Es que
    **no se pueden convertir en efectivo el martes por la mañana** para atender a
    depositantes que hacen fila. La regla de Basilea mide *liquidez inmediata*, no
    solvencia.

    **2. Ratio de Cobertura de Liquidez**

    $$LCR = \frac{HQLA}{\text{Salidas netas de efectivo a 30 días}}$$

    $$LCR = \frac{5{,}750}{6{,}000} = 0.9583 = \mathbf{95.83\%}$$

    **No supera el mínimo legal del 100 %.**

    GlobalBank tiene un **déficit de $\$250$ millones** ($6{,}000 - 5{,}750$). En
    términos prácticos: podría atender retiros durante unos **29 días** del escenario
    de estrés de 30 días exigido, y se quedaría sin liquidez justo antes de llegar
    a la meta.

    Consecuencias regulatorias inmediatas: notificación al supervisor con un plan de
    restauración, probable restricción de dividendos y bonos, y exigencia de corregir
    el ratio en un plazo determinado.

    **3. Escenario severamente adverso — salidas de $7,000 millones**

    $$LCR_{estrés} = \frac{5{,}750}{7{,}000} = 0.8214 = \mathbf{82.14\%}$$

    **No sobrevive.** El déficit se amplía a **$\$1{,}250$ millones**, y la cobertura
    cae a unos **24-25 días** de los 30 requeridos.

    | Escenario | Salidas | LCR | Déficit | ¿Cumple? |
    |---|---|---|---|---|
    | Base | 6,000 | 95.83 % | 250 | ❌ |
    | Severamente adverso | 7,000 | 82.14 % | 1,250 | ❌❌ |

    **Qué haría un tesorero para cerrar la brecha**

    * **Subir el numerador:** vender bonos corporativos AA y sustituirlos por deuda
      soberana (cada peso movido añade $\$0.50$ de HQLA); captar depósitos estables.
    * **Bajar el denominador:** alargar el vencimiento del *funding* mayorista a más
      de 30 días —lo que sale de la ventana de cálculo deja de computar como salida—
      y migrar depósitos mayoristas volátiles hacia depósitos minoristas, que Basilea
      pondera con tasas de fuga mucho menores.
    * **Reducir compromisos** no dispuestos de líneas de crédito, que también generan
      salidas proyectadas.

    !!! tip "LCR y NSFR: dos plazos, dos preguntas"
        Basilea III introdujo **dos** ratios de liquidez complementarios, y conviene
        no confundirlos:

        | | **LCR** | **NSFR** |
        |---|---|---|
        | Horizonte | 30 días | 1 año |
        | Pregunta | ¿Sobrevivo a una corrida bancaria? | ¿Mi financiamiento es estructuralmente estable? |
        | Fórmula | HQLA / Salidas netas 30d | Financiamiento estable disponible / requerido |
        | Mínimo | 100 % | 100 % |

        El **LCR** es el extintor de incendios; el **NSFR** es la calidad de la
        construcción.

        Ambos nacieron de una lección concreta de 2008: **Lehman Brothers y Northern
        Rock eran solventes en el papel** —sus activos superaban sus pasivos— pero
        murieron por iliquidez. No pudieron convertir activos en efectivo lo bastante
        rápido cuando el financiamiento mayorista de corto plazo se evaporó en
        cuestión de días.

        La lección que resume Basilea III: **la solvencia te mata lentamente; la
        liquidez te mata en una semana.**
