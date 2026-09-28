# Semana 8 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: La trampa del "Crecimiento de Ventas"
*Eres un analista de crédito en un banco evaluando si otorgar un préstamo de $5 millones a una empresa de retail llamada "FastGrow".*

El CEO de FastGrow entra a tu oficina muy emocionado: "¡Nuestras ventas (Ingresos) crecieron un 50% este año! Y nuestra Utilidad Neta creció un 30%. Somos saludables y muy rentables. Necesitamos el crédito para abrir nuevas tiendas."

El CEO te enseña el Estado de Resultados, y todo luce increíble. Pero tú, como buen analista financiero, le pides el **Balance General**. Al revisarlo, descubres dos cosas alarmantes:
1. **Cuentas por Cobrar** (dinero que clientes le deben a FastGrow) se triplicó. 
2. **Inventario** se cuadruplicó.

**Tu análisis y Veredicto:**
El P&L muestra *reconocimiento contable* de ventas, pero el Balance General te muestra la *realidad del efectivo*. FastGrow está vendiendo a crédito y los clientes no le están pagando a tiempo. Además, está acumulando inventario que no logra vender.
Aunque el P&L muestra "Utilidad Neta" positiva (dinero contable), el Balance General revela que el **Flujo de Caja Libre** está seco. Todo su capital de trabajo está atrapado. Darles un préstamo sería muy riesgoso, porque no tienen efectivo líquido (Activos Corrientes) para pagar los intereses. Les negarías el crédito. *(Este descubrimiento nos llevará directamente a la Semana 9: Flujos de Efectivo).*

---


## 7. Tareas y Evaluación de la Semana 8

**A. Lectura Obligatoria:**
* Warren, Reeve, Duchac. *Contabilidad Financiera* (Capítulo sobre Estados Financieros). O revisión de las normativas locales (NIIF 1 / US GAAP) sobre presentación de Estados Financieros.

**B. Preguntas de Reflexión:**
1. ¿Por qué un Estado de Resultados se considera un reporte de "flujo", mientras que un Balance General se considera un reporte de "saldo" o "fotografía"?
2. Explica la relación matemática y contable entre la "Utilidad Neta" del Estado de Resultados y la cuenta de "Ganancias Retenidas" del Balance General. ¿Qué ocurre si una empresa tiene Utilidad Neta negativa (pérdida)?

**C. Ejercicio Práctico a entregar:**
La empresa "BlueOcean S.A." te reporta lo siguiente al final del año fiscal:
* Ventas: $2,000
* Costo de ventas: $1,200
* Gastos de marketing: $150
* Sueldos administrativos: $250
* Depreciación: $50
* Intereses: $40
* Tasa de Impuestos: 25%
* Dividendos pagados este año: $30
* Ganancias Retenidas (inicio de año): $200

Contesta:
1. Prepara el Estado de Resultados completo hasta la Utilidad Neta. Muestra tus cálculos paso a paso.
2. ¿Cuál será el saldo final de la cuenta de "Ganancias Retenidas" que aparecerá en el Balance General de fin de año de BlueOcean S.A.? (Pista: Recuerda sumar la utilidad neta y restar los dividendos).

??? success "Solución del Ejercicio C"

    **1. Estado de Resultados de "BlueOcean S.A."**

    | Concepto | Monto | Cálculo |
    |---|---|---|
    | Ventas | 2,000 | |
    | (−) Costo de Ventas | (1,200) | |
    | **= Utilidad Bruta** | **800** | $2{,}000 - 1{,}200$ |
    | (−) Gastos de Marketing | (150) | |
    | (−) Sueldos Administrativos | (250) | |
    | (−) Depreciación | (50) | |
    | **= Utilidad Operativa (EBIT)** | **350** | $800 - 150 - 250 - 50$ |
    | (−) Intereses | (40) | |
    | **= Utilidad Antes de Impuestos (EBT)** | **310** | $350 - 40$ |
    | (−) Impuestos (25 %) | (77.5) | $310 \times 0.25$ |
    | **= Utilidad Neta** | **232.5** | $310 - 77.5$ |

    Márgenes que un analista calcularía de inmediato:
    margen bruto $800/2{,}000 = 40\%$, margen operativo $350/2{,}000 = 17.5\%$,
    margen neto $232.5/2{,}000 = 11.6\%$.

    **2. Saldo final de Ganancias Retenidas**

    $$GR_{final} = GR_{inicial} + \text{Utilidad Neta} - \text{Dividendos}$$
    
    $$GR_{final} = 200 + 232.5 - 30 = \mathbf{402.5}$$

    !!! tip "El puente entre los dos estados"
        Esta fórmula es **la bisagra que conecta el Estado de Resultados con el
        Balance General**, y es exactamente el "plug" que tendrás que programar
        cuando modeles tres estados en Excel (Semanas 18-19).

        Nota además que los **dividendos no son un gasto**: no aparecen en el Estado
        de Resultados ni reducen la utilidad neta. Son una *distribución* de
        utilidad ya ganada, y por eso se restan aquí, en el patrimonio.

        Cuidado con el orden: los intereses se restan **antes** de impuestos. Esa es
        la razón de que la deuda genere un escudo fiscal — un tema que reaparece
        en el WACC (Semana 24) y en Modigliani-Miller (Semana 26).

---
