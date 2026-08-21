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
