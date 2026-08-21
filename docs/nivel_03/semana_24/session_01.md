# Semana 24 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Entender el concepto del WACC (Costo Promedio Ponderado de Capital) y el Apalancamiento Financiero.
* Calcular el Costo de la Deuda ($r_d$) después de impuestos (Tax Shield).
* Calcular el Costo del Patrimonio ($r_e$) utilizando el Modelo de Valuación de Activos de Capital (CAPM) y la Beta ($\beta$).
* Integrar todo en la fórmula maestra del WACC y entender su impacto en la valuación de empresas.

---

## 2. El WACC: El Punto de Equilibrio Financiero
Una empresa se financia de dos maneras:
1. **Deuda ($D$):** Préstamos bancarios, bonos. (Barato, pero riesgo de bancarrota).
2. **Patrimonio/Equity ($E$):** Dinero de los accionistas. (Caro, porque los accionistas exigen más retorno por asumir el riesgo de perderlo todo).

El **WACC** (Weighted Average Cost of Capital) es el promedio de estos dos costos, ponderado por el porcentaje que cada uno representa en la estructura total de capital ($V = D + E$). 
* Es la **Tasa de Descuento** que usarás en todos tus modelos de Excel para traer los flujos de caja futuros al Valor Presente.

---

## 3. El Costo de la Deuda ($r_d$)
El dinero prestado por el banco no cuesta lo mismo que el dinero de los accionistas. 
* **Tasa Antes de Impuestos ($r_d$):** Es la tasa de interés que el banco le cobra a la empresa. Se halla mirando el rendimiento al vencimiento (YTM) de los bonos de la empresa en el mercado.
* **El Escudo Fiscal (Tax Shield):** Los gobiernos fomentan la inversión dándole a las empresas un beneficio: los intereses de la deuda son **deducibles de impuestos**. 
* **Fórmula Costo de Deuda Después de Impuestos:** 
  $$ r_d \times (1 - T) $$
  *(Donde $T$ es la tasa de impuesto a las ganancias corporativas. Si la deuda cuesta 10% y el impuesto es 25%, el costo real de la deuda para la empresa es $10\% \times (1 - 0.25) = 7.5\%$. El gobierno "paga" el 2.5% restante).*
