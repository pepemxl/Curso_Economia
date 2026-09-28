# Semana 10 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: "La trampa de la depreciación en una economia inflacionaria"

Eres analista de inversiones y evalúas comprar acciones de una empresa de transporte de carga que tiene camiones muy antiguos. 

* Su Estado de Resultados muestra una Utilidad Operativa positivamente enorme. 
* ¿Por qué? Porque el gasto por **Depreciación** de sus camiones es minúsculo. Contablemente, esos camiones se compraron hace 15 años a un precio muy bajo, y la depreciación anual que se resta en el P&L es de $1,000 mensuales por camión.

* **El entorno Macro:** La inflación en el país ha subido. Un camión nuevo hoy cuesta $200,000. 

**El Veredicto Financiero:**
La empresa está mostrando "Utilidades Contables" infladas porque no está reflejando el costo de reemplazo de sus activos. En el **Flujo de Efectivo**, cuando esos camiones se rompan definitivamente, la empresa tendrá que gastar $200,000 en efectivo (CapEx masivo) para comprar uno nuevo. Su Flujo de Caja Libre (FCF) se va a desploma. 
* Si solo hubieras mirado el Estado de Resultados sin entender el entorno de inflación y el Flujo de CapEx, habrías comprado una acción que parece rentable pero que va a ir a la quiebra por falta de efectivo de reposición.

---


## 6. Tareas y Evaluación Final del Nivel 1

**A. Lectura Obligatoria:**
* Repaso de los apuntes de las semanas 1 a 9. 
* *Lectura recomendada:* "El inversor inteligente" de Benjamin Graham (Capítulo sobre interpretación de estados financieros y el impacto del entorno).

**B. Preguntas de Reflexión:**
1. ¿Por qué una empresa con un ROE altísimo puede ser una pésima inversión si se encuentra en un país con alta inflación y tasas de interés en aumento?
2. Si la tasa de desempleo cae al 2% (muy por debajo de la tasa natural del 5%), ¿qué le dirías a un gestor de fondos que quiere invertir agresivamente en bonos a largo plazo de empresas cíclicas?

**C. Ejercicio Final Integrador a entregar:**
Tienes a tu disposición las siguientes situaciones de inversión. Como analista financiero, redacta un análisis de media página explicando cómo combinas macro y contabilidad para resolverlas:

1. **La empresa TSLA (ficticia) reporta que sus ventas crecieron 25% y sus Utilidades Netas crecieron 60%. Sin embargo, sus flujos de efectivo de operación (CFO) fueron negativos.** Explica qué líneas del Balance General (inventarios, cuentas por cobrar, etc.) pudieron haber provocado que la utilidad crezca pero el efectivo sea negativo. ¿Es esto sostenible a largo plazo?
2. El Banco Central anuncia una **subida de tasas de interés del 2% al 8%** para frenar una inflación inesperada del 10%. Describe cómo impactará esta medida en: (a) Los gastos financieros del P&L de una empresa con Deuda de Largo Plazo a tasa flotante, y (b) El Flujo de Caja Libre de esa misma empresa.

---
??? success "Solución orientativa del Ejercicio Integrador"

    *(Este ejercicio es de redacción; lo que sigue es una respuesta modelo con los
    puntos que un evaluador esperaría encontrar.)*

    **Caso 1 — Ventas +25 %, Utilidad Neta +60 %, pero CFO negativo**

    El síntoma es una **divergencia entre devengo y caja**. Bajo contabilidad de
    devengo, una venta se reconoce cuando se *factura*, no cuando se *cobra*. Las
    cuentas del Balance que pueden explicarlo:

    * **Cuentas por Cobrar disparadas.** Si TSLA creció vendiendo a crédito con
      plazos cada vez más laxos, la venta entra al P&L pero el efectivo no llega.
      Señal de alarma: que las CxC crezcan **más rápido que las ventas** (aquí,
      más de 25 %). Los *días de cobro* (DSO) se estarían alargando.
    * **Inventario acumulado.** Producción que no se vendió. Peor aún: el inventario
      no vendido **no** pasa a Costo de Ventas, así que *infla* artificialmente el
      margen bruto del período mientras consume caja.
    * **Cuentas por Pagar reducidas.** Si además pagó a proveedores más rápido,
      drenó caja adicional.
    * **Utilidad de baja calidad.** Que la utilidad crezca 60 % con ventas al 25 %
      puede venir de partidas no monetarias: capitalización de gastos de desarrollo,
      revaluación de activos o ganancias contables por única vez. Ninguna trae caja.

    **¿Es sostenible?** **No.** Una empresa puede reportar utilidades y quebrar por
    falta de liquidez — es la causa más común de quiebra en empresas en crecimiento
    rápido. Sin CFO positivo, el crecimiento se financia con deuda o con emisión de
    acciones, y ambas fuentes se agotan. El diagnóstico se completa con las
    herramientas de las Semanas 21-23: ciclo de conversión de efectivo y Altman Z-Score.

    **Caso 2 — El Banco Central sube tasas del 2 % al 8 %**

    **(a) Impacto en los gastos financieros del P&L**

    Con deuda a **tasa flotante**, el costo se reprecia casi de inmediato: los
    intereses se **cuadruplican** (de 2 % a 8 % sobre el mismo saldo). Sobre una
    deuda de, digamos, $\$1{,}000$, el gasto financiero pasa de $\$20$ a $\$80$ al año.

    Recorrido por el estado de resultados: el **EBIT no cambia** (la tasa no afecta
    la operación), pero la Utilidad Antes de Impuestos cae por los mayores
    intereses, y con ella la **Utilidad Neta**. La *cobertura de intereses*
    (EBIT/Intereses) se deteriora, lo que puede activar *covenants* bancarios.
    Compensación parcial: al ser los intereses deducibles, el mayor gasto genera un
    **escudo fiscal** mayor, así que la utilidad neta cae algo menos que los intereses.

    **(b) Impacto en el Flujo de Caja Libre**

    El golpe es doble o triple:

    1. **Menos caja por intereses.** Salida directa de efectivo.
    2. **Más capital de trabajo.** Con inflación del 10 %, reponer el mismo
       inventario físico cuesta 10 % más, y la nómina y los insumos suben. El
       capital de trabajo absorbe caja aunque el negocio no crezca en volumen.
    3. **Menos demanda agregada.** El alza de tasas es contractiva (Semana 6):
       enfría el consumo y la inversión, así que las ventas mismas pueden caer.

    **Y la vuelta de tuerca de valuación:** una tasa libre de riesgo más alta sube
    el **WACC** (Semana 24). O sea que la empresa genera *menos* flujo y ese flujo
    se descuenta a una tasa *mayor*. El valor presente cae por ambos lados a la vez
    — es la razón por la que las bolsas caen cuando los bancos centrales endurecen
    la política monetaria.

---

### 🎉 ¡FELICIDADES! HAS COMPLETADO EL NIVEL 1 🎉

Has construido una base sólida en los cimientos de la ciencia económica y financiera. Ya comprendes cómo interactúan individuos, empresas y gobiernos, cómo se registran los números de una empresa y cómo el entorno global afecta esos resultados. 

**Próximo paso: NIVEL 2 (Matemáticas Financieras, Estadística y Modelación).**
