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
