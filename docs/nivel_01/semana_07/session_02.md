# Semana 7 · Sesión 2: Profundización

## 4. El Ciclo Contable
Es el proceso continuo paso a paso que la contabilidad de una empresa realiza cada año. 

1. **Identificar y medir la transacción:** Ocurre un evento económico (Ej. se compra una máquina). Se recoge el comprobante o factura.
2. **Asiento en el Libro Diario (Journal Entry):** Se registra la transacción cronológicamente usando la partida doble (Débitos y Créditos).
3. **Traspaso al Libro Mayor (Ledger):** Las cantidades de los asientos del diario se copian a las cuentas individuales (cuenta de "Efectivo", cuenta de "Bancos", etc.). Se usa la "Cuenta T" para visualizar esto.
4. **Balanza de Comprobación (Trial Balance):** Se hace una lista de todas las cuentas con sus saldos finales y se comprueba que la suma de los Débitos sea igual a la suma de los Créditos. Si no cuadra, hay un error matemático de registro.
5. **Asientos de Ajuste:** Al final del periodo, se ajustan cuentas que no se han registrado día a día (Ej. depreciación de la máquina, pago de salarios acumulados no pagados).
6. **Estados Financieros:** Se elaboran los reportes finales (Estado de Resultados, Balance General - vista en Semana 8).
7. **Cierre (Closing entries):** Se "cierran" las cuentas temporales (ingresos y gastos) contra la cuenta de patrimonio, dejándolas en cero para empezar el nuevo año.

---

## La regla mecánica de los débitos y créditos

Los principiantes intentan razonar cada asiento desde cero y se pierden. Los contadores usan una
regla mecánica que nunca falla. Las cinco cuentas se dividen en dos familias según **de qué lado
de la ecuación viven**:

$$\underbrace{\text{ACTIVO}}_{\text{izquierda}} \;=\; \underbrace{\text{PASIVO} + \text{PATRIMONIO}}_{\text{derecha}}$$

| Cuenta | Naturaleza | Aumenta con | Disminuye con |
|---|---|---|---|
| **Activo** | Deudora | **Débito** | Crédito |
| **Gasto** | Deudora | **Débito** | Crédito |
| **Pasivo** | Acreedora | Débito | **Crédito** |
| **Patrimonio** | Acreedora | Débito | **Crédito** |
| **Ingreso** | Acreedora | Débito | **Crédito** |

**Por qué gastos e ingresos siguen esa lógica.** Ambos son en realidad cuentas de patrimonio
disfrazadas: un ingreso *aumenta* el patrimonio (por eso se acredita, como el patrimonio), y un
gasto lo *reduce* (por eso se debita, en sentido contrario). Al cerrar el ejercicio, ambas se
vuelcan sobre las Ganancias Retenidas y quedan en cero. Son temporales; las otras tres son
permanentes.

!!! warning "Débito no significa 'bueno' ni crédito 'malo'"
    En el lenguaje cotidiano asociamos "crédito" con recibir y "débito" con pagar, y esa
    intuición **es engañosa aquí**. En contabilidad son simplemente **izquierda** y **derecha**:
    débito es la columna izquierda de la cuenta T, crédito la derecha. Nada más.

    Por eso cuando el banco te dice que "abonó" (acreditó) tu cuenta, desde *su* contabilidad
    está aumentando un **pasivo**: te debe ese dinero. Tu depósito es un activo tuyo y un pasivo
    del banco. Ese mismo hecho es la base de la creación de dinero que estudiarás en la
    Semana 33.

---

## Devengo frente a caja: la distinción que lo explica casi todo

La contabilidad puede llevarse con dos criterios, y entender la diferencia es la base de todo el
análisis financiero posterior:

| | **Base de devengo** (*accrual*) | **Base de caja** (*cash*) |
|---|---|---|
| Ingreso se reconoce | cuando se **gana** (se entrega el bien) | cuando se **cobra** |
| Gasto se reconoce | cuando se **incurre** | cuando se **paga** |
| Obligatoria para | empresas auditadas (NIIF, US GAAP) | muy pequeños negocios, fiscalidad simplificada |

Las normas contables exigen **devengo** por el *principio de correspondencia*: los gastos deben
reconocerse en el mismo período que los ingresos que ayudaron a generar. Si vendes en diciembre
y cobras en febrero, la venta es de diciembre.

**Y aquí nace el problema central del análisis financiero.** Como la utilidad se calcula por
devengo pero las facturas se pagan con efectivo, **una empresa puede ser rentable y quedarse sin
caja**. Es la causa de quiebra más común en empresas que crecen rápido, y la razón por la que
existe un estado financiero entero —el de Flujos de Efectivo (Semana 9)— dedicado a reconciliar
ambos mundos.

---

## Los asientos de ajuste: dónde vive el criterio (y la manipulación)

El paso 5 del ciclo es el más delicado, porque es el único que depende de **juicios**, no de
comprobantes. Los cuatro tipos:

1. **Gastos devengados no pagados.** Salarios de la última quincena de diciembre que se pagan en
   enero: *Débito Gasto de sueldos / Crédito Sueldos por pagar*.
2. **Ingresos devengados no cobrados.** Servicio prestado en diciembre, facturado en enero:
   *Débito Cuentas por cobrar / Crédito Ingresos*.
3. **Gastos pagados por anticipado que se consumen.** Una póliza anual pagada en enero se
   consume mes a mes: *Débito Gasto de seguro / Crédito Seguros pagados por anticipado*.
4. **Ingresos cobrados por anticipado que se ganan.** Una suscripción anual cobrada por
   adelantado: *Débito Ingresos diferidos (pasivo) / Crédito Ingresos*.

A ellos se suma la **depreciación**, que reparte el costo de un activo a lo largo de su vida
útil sin que salga efectivo alguno.

!!! danger "Por qué un analista vigila los ajustes"
    Los asientos de ajuste no tienen factura que los respalde: dependen de estimaciones sobre
    vidas útiles, incobrables o grado de avance de un contrato. Son, por tanto, **la puerta de
    entrada de la contabilidad creativa**.

    Señales que hay que mirar:

    * **Cuentas por cobrar creciendo más rápido que las ventas** → reconocimiento agresivo de
      ingresos.
    * **Vidas útiles inusualmente largas** frente a las de los competidores → menor depreciación,
      mayor utilidad.
    * **Provisión de incobrables que baja** mientras la cartera envejece.
    * **Ingresos diferidos que caen** de golpe → se está adelantando el reconocimiento.

    Todas ellas comparten un síntoma común: **la utilidad crece pero el flujo de caja operativo
    no la acompaña.** Ese será el diagnóstico que practiques en la Semana 10.

---
