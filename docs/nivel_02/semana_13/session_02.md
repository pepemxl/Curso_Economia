# Semana 13 · Sesión 2: Profundización

## 4. Sistemas de Amortización de Préstamos
Amortizar significa "pagar una deuda de forma gradual". Todo pago de una cuota tiene dos componentes:
1. **Intereses:** Lo que le cobras al deudor por usar el dinero en ese periodo.
2. **Amortización al Capital:** La parte de la cuota que reduce el saldo de la deuda original.

Existen 3 sistemas clásicos en la banca mundial:

**A. Sistema Francés (El más común en hipotecas y autos)**
* **Característica:** La **cuota total (C) es FIJA** durante toda la vida del préstamo.
* **Dinámica interna:** Al principio, como la deuda es muy grande, la mayor parte de tu cuota va a pagar intereses y muy poco a bajar el capital. Al final del préstamo, casi toda la cuota es capital y muy poco es interés.
* *Fórmula de la cuota:* Se usa la misma fórmula de VP de Anualidad Ordinaria, despejando $C$.

**B. Sistema Alemán (El favorito de las empresas con flujos decrecientes)**
* **Característica:** Lo que es **fija es la amortización al capital**. Se paga la misma cantidad de principal en cada cuota. La cuota total va disminuyendo mes a mes.
* **Dinámica interna:** Como el principal baja linealmente, los intereses van bajando rápido. Las primeras cuotas son las más caras, y las últimas son muy baratas.

**C. Sistema Americano (El "Bullet Loan" de la banca corporativa)**
* **Característica:** El deudor paga **únicamente los intereses** en cada periodo, y devuelve **todo el capital (préstamo original) en un solo pago al final** del plazo.
* **Dinámica interna:** Las cuotas periódicas son bajas y constantes, pero requiere una enorme capacidad de ahorro o refinanciamiento al final. Usado en bonos corporativos y préstamos puente (Bridge loans) para fusiones empresariales.

---

## Anualidades: las cuatro variantes que hay que distinguir

Una **anualidad** es una serie de pagos iguales a intervalos regulares. Las cuatro formas y sus
fórmulas de valor presente:

| Tipo | Cuándo ocurre el pago | Valor presente |
|---|---|---|
| **Ordinaria** (vencida) | Al **final** de cada período | $VP = C \cdot \dfrac{1-(1+i)^{-n}}{i}$ |
| **Anticipada** (*due*) | Al **inicio** de cada período | $VP_{ant} = VP_{ord} \times (1+i)$ |
| **Perpetuidad** | Para siempre, al final | $VP = \dfrac{C}{i}$ |
| **Perpetuidad creciente** | Para siempre, creciendo a $g$ | $VP = \dfrac{C}{i-g}$ |

**La diferencia entre ordinaria y anticipada** es exactamente un período de descuento. Un
alquiler se paga por adelantado (anticipada); una cuota de préstamo, al final del mes
(ordinaria). Sobre 20 años al 6 %, confundirlas cambia el resultado un 6 %.

**La perpetuidad creciente** es la fórmula de Gordon que usarás en la Semana 37 para el valor
terminal, y en la Semana 13 para valorar acciones preferentes con dividendo creciente. Su única
condición es $i > g$: si el crecimiento igualara o superara la tasa de descuento, el valor
sería infinito.

*Ejemplo:* una acción preferente que paga $\$5$ este año, creciendo al 2 % anual, con
rendimiento exigido del 8 %:

$$VP = \frac{5}{0.08 - 0.02} = \$83.33$$

Frente a los $\$62.50$ que valdría sin crecimiento ($5/0.08$). **Un 2 % de crecimiento perpetuo
añade un 33 % de valor** — la sensibilidad que hace tan peligroso el valor terminal de un DCF.

---
