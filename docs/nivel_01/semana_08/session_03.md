# Semana 8 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: Construyendo los Estados Financieros

La empresa "AlphaTech" tiene las siguientes cuentas al cierre del año (en miles de dólares):
* Efectivo: $50
* Cuentas por Pagar: $30
* Ingresos por Ventas: $1,000
* Deuda a Largo Plazo: $200
* Costo de Ventas: $600
* Gastos Administrativos: $150
* Gasto por Intereses: $20
* Impuestos (30% sobre la Utilidad antes de impuestos)
* Edificios y Equipos: $400
* Cuentas por Cobrar: $100
* Inventario: $80
* Capital Social: $100
* Ganancias Retenidas (Año anterior): $139

**A. Construcción del Estado de Resultados:**
1. Ventas: $1,000
2. (-) Costo de Ventas: $600
3. **Utilidad Bruta:** $400 *(Margen Bruto = 40%)*
4. (-) Gastos Operativos: $150
5. **Utilidad Operativa (EBIT):** $250 *(Margen EBIT = 25%)*
6. (-) Gasto Financiero: $20
7. **Utilidad antes de Impuestos (EBT):** $230
8. (-) Impuestos (30% de $230): $69
9. **Utilidad Neta:** $161 *(Margen Neto = 16.1%)*

*(Supongamos que AlphaTech decide no pagar dividendos este año).*

**B. Construcción del Balance General:**
Primero actualizamos las Ganancias Retenidas: $139 (Año anterior) + $161 (Utilidad Neta de este año) - $0 (Dividendos) = **$300**.

| | Cuenta | Monto |
|---|---|---|
| **ACTIVO** | Efectivo | 50 |
| | Cuentas por Cobrar | 100 |
| | Inventario | 80 |
| | Edificios y Equipos | 400 |
| | **Total Activo** | **630** |
| **PASIVO** | Cuentas por Pagar | 30 |
| | Deuda a Largo Plazo | 200 |
| | **Total Pasivo** | **230** |
| **PATRIMONIO** | Capital Social | 100 |
| | Ganancias Retenidas ($139 + $161) | 300 |
| | **Total Patrimonio** | **400** |

**Comprobación de la ecuación contable:**

$$A = P + E \Longrightarrow 630 = 230 + 400 \quad ✓$$

!!! tip "Qué hacer cuando el balance NO cuadra"
    Esta es la situación más común al construir estados financieros a mano, y hay un
    procedimiento para diagnosticarla en lugar de forzar el número:

    1. **Calcula la diferencia y divídela entre 2.** Si el resultado coincide con alguna cuenta,
       probablemente la registraste en el lado equivocado (un débito donde iba un crédito).
    2. **¿La diferencia es divisible entre 9?** Casi siempre es una **transposición de dígitos**
       (escribir 91 en lugar de 19).
    3. **¿La diferencia coincide exactamente con una cuenta?** La omitiste por completo.
    4. **Revisa el puente P&L → Balance.** El error más frecuente es olvidar llevar la utilidad
       neta a las Ganancias Retenidas, o restar dividendos que no correspondían.
    5. **Comprueba la balanza antes de los estados.** Si la suma de débitos no iguala a la de
       créditos en la balanza de comprobación, el error está en el registro, no en la
       presentación.

    **Lo que nunca debes hacer es "cuadrarlo" metiendo una cifra de ajuste.** Un balance que no
    cierra es la contabilidad avisándote de un error real; taparlo lo convierte en un error
    invisible. Es exactamente la misma disciplina que exige la fila de comprobación del modelo
    de Excel de la Semana 18.

---

## Segundo ejercicio: el mismo negocio con y sin deuda

AlphaTech tiene una hermana gemela, **BetaTech**: idéntica en todo lo operativo, pero
financiada de forma distinta. Compara ambas para aislar el efecto de la estructura de capital.

| | AlphaTech | BetaTech |
|---|---|---|
| Ventas | 1,000 | 1,000 |
| Costo de ventas | 600 | 600 |
| Gastos administrativos | 150 | 150 |
| **EBIT** | **250** | **250** |
| Deuda | 200 | 500 |
| Gasto financiero (10 %) | 20 | 50 |
| Patrimonio | 400 | 100 |

**Estado de Resultados comparado:**

| Concepto | AlphaTech | BetaTech |
|---|---|---|
| EBIT | 250 | 250 |
| (−) Intereses | (20) | (50) |
| EBT | 230 | 200 |
| (−) Impuestos (30 %) | (69) | (60) |
| **Utilidad neta** | **161** | **140** |

**Ratios de rentabilidad:**

$$ROA_{Alpha} = \frac{161}{630} = 25.6\% \qquad ROA_{Beta} = \frac{161}{630} \text{ (operativo idéntico)}$$

$$ROE_{Alpha} = \frac{161}{400} = \mathbf{40.3\%} \qquad ROE_{Beta} = \frac{140}{100} = \mathbf{140\%}$$

**BetaTech gana menos dinero y sin embargo su ROE es tres veces y media mayor.**

No es magia: el apalancamiento reparte el mismo beneficio operativo entre una base de capital
mucho más pequeña. Es exactamente el tercer componente del **Dupont** que descompondrás en la
Semana 22.

**El otro lado de la moneda — cobertura de intereses:**

$$\text{Alpha} = \frac{250}{20} = 12.5\times \qquad \text{Beta} = \frac{250}{50} = 5.0\times$$

Y si el EBIT cayera un 60 % en una recesión (a 100):

| | AlphaTech | BetaTech |
|---|---|---|
| EBIT | 100 | 100 |
| (−) Intereses | (20) | (50) |
| EBT | **80** | **50** |
| Utilidad neta | 56 | 35 |
| Cobertura | 5.0× | **2.0×** |

Alpha sigue holgada; Beta queda al límite del *covenant* típico. Una caída algo mayor la pondría
en incumplimiento técnico.

**La lección:** el apalancamiento **amplifica en ambas direcciones**. Un ROE alto no es
necesariamente señal de un buen negocio; puede ser señal de un balance frágil. Por eso jamás se
mira el ROE sin mirar a la vez la cobertura de intereses y el ratio de endeudamiento.

**El escudo fiscal, de paso:** BetaTech pagó $\$9$ menos de impuestos ($60$ frente a $69$).
Ese ahorro es real y es exactamente el $D \times T$ de Modigliani-Miller que verás en la
Semana 26: $\$30$ de intereses adicionales $\times 30\% = \$9$.

---

## Errores frecuentes al construir estados financieros

1. **Meter los dividendos en el Estado de Resultados.** No son un gasto: son una distribución
   de utilidad ya ganada. Van directos contra las Ganancias Retenidas.
2. **Confundir depreciación acumulada con gasto de depreciación.** El **gasto** es del período y
   va al P&L; la **acumulada** es el saldo histórico y vive en el balance como contra-activo.
3. **Restar los intereses antes de calcular el EBIT.** El orden es sagrado: EBIT primero,
   intereses después, impuestos al final. Invertirlo destruye la comparabilidad entre empresas.
4. **Olvidar la parte corriente de la deuda de largo plazo.** La porción que vence en los
   próximos 12 meses se reclasifica a pasivo corriente. Ignorarlo infla artificialmente la razón
   corriente (Semana 21).
5. **Aplicar la tasa impositiva sobre el EBIT en lugar del EBT.** Los intereses son deducibles;
   la base gravable es después de intereses.
6. **Sumar el inventario como si fuera efectivo.** Es activo corriente, sí, pero es justo el que
   la prueba ácida excluye por buenas razones.

---
