# Semana 13 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: El Cuadro de Amortización Francés
Pides un préstamo al banco de **$1,000** a una tasa del **10% anual** para pagar en **2 años (2 cuotas anuales)**. 

**Paso 1: Calcular la Cuota Fija (Sistema Francés)**
Usamos la fórmula de VP de anualidad ordinaria: $VP = C \times \frac{1 - (1+i)^{-n}}{i}$
$1,000 = C \times \frac{1 - (1.10)^{-2}}{0.10}$
$1,000 = C \times 1.7355$
**$C = \$576.19$** (Esta será tu cuota fija durante los 2 años).

**Paso 2: Construcción del Cuadro de Amortización**

| Año | Saldo Inicial | Cuota Total | Interés (10% s/ Saldo) | Amort. Capital | Saldo Final |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | $1,000.00 | $576.19 | $100.00 | $476.19 | **$523.81** |
| 2 | $523.81 | $576.19 | $52.38 | $523.81 | **$0.00** |

*Análisis de la tabla:*
* Año 1: Debes $1,000. El interés es 100. Tu cuota de 576.19 paga los 100 de interés y sobran 476.19 para bajar el capital. El saldo final es 523.81.
* Año 2: Ahora debes 523.81. El interés es 52.38. La misma cuota de 576.19 paga los intereses y sobra justo 523.81 para saldar la deuda por completo.

---

## Segundo ejercicio: el mismo préstamo en los tres sistemas

Compara los tres sistemas sobre el mismo préstamo de **$\$1,000$ al 10 % a 2 años**, para ver
la diferencia con números en la mano.

**A. Sistema Alemán** (amortización a capital fija $= 1{,}000/2 = \$500$)

| Año | Saldo inicial | Interés | Amortización | **Cuota** | Saldo final |
|---|---|---|---|---|---|
| 1 | 1,000.00 | 100.00 | 500.00 | **600.00** | 500.00 |
| 2 | 500.00 | 50.00 | 500.00 | **550.00** | 0.00 |
| | | **150.00** | **1,000.00** | **1,150.00** | |

**B. Sistema Americano** (solo intereses, capital al final)

| Año | Saldo inicial | Interés | Amortización | **Cuota** | Saldo final |
|---|---|---|---|---|---|
| 1 | 1,000.00 | 100.00 | 0.00 | **100.00** | 1,000.00 |
| 2 | 1,000.00 | 100.00 | 1,000.00 | **1,100.00** | 0.00 |
| | | **200.00** | **1,000.00** | **1,200.00** | |

**C. Comparación con el Francés del ejercicio anterior**

| Sistema | Cuota año 1 | Cuota año 2 | **Intereses totales** | Total pagado |
|---|---|---|---|---|
| **Alemán** | 600.00 | 550.00 | **150.00** | 1,150.00 |
| **Francés** | 576.19 | 576.19 | **152.38** | 1,152.38 |
| **Americano** | 100.00 | 1,100.00 | **200.00** | 1,200.00 |

**La conclusión es siempre la misma, y se deduce sin calcular nada:** cuanto **antes** devuelvas
el capital, menos intereses pagas, porque el interés se calcula sobre el saldo pendiente. El
Alemán amortiza más rápido → paga menos. El Americano no amortiza nada hasta el final → paga
más.

!!! tip "Todos son equivalentes en valor presente"
    Aquí está el detalle que sorprende: **descontados al 10 %, los tres flujos de cuotas valen
    exactamente $\$1,000$**.

    $$\text{Alemán: } \frac{600}{1.10} + \frac{550}{1.10^2} = 545.45 + 454.55 = \$1{,}000$$

    $$\text{Americano: } \frac{100}{1.10} + \frac{1{,}100}{1.10^2} = 90.91 + 909.09 = \$1{,}000$$

    Tiene que ser así: los tres son **el mismo préstamo** a la misma tasa. El banco es
    indiferente entre ellos.

    Entonces, ¿por qué difieren los intereses totales? Porque "intereses totales" es una **suma
    de pesos de distintos años**, y sumar dinero de distintos momentos sin descontar no
    significa nada financieramente. Es una cifra útil para la caja, no para la valuación.

    **La elección real no es de costo, sino de perfil de caja:** el Americano libera flujo hoy
    a cambio de un riesgo de refinanciación enorme al vencimiento; el Alemán exige esfuerzo
    inicial; el Francés reparte de forma predecible. Un bono corporativo es, por construcción,
    un préstamo americano.

---

## Tercer ejercicio: pago anticipado y el coste de cancelar

Vuelves al **préstamo francés** original, pero a mayor escala: **$\$200,000$ a 20 años al 6 %
anual**, con cuotas mensuales.

**Paso 1 — Cuota mensual**

$$i = \frac{0.06}{12} = 0.005 \qquad n = 240$$

$$C = 200{,}000 \times \frac{0.005}{1 - (1.005)^{-240}} = \mathbf{\$1{,}432.86}$$

Total pagado: $1{,}432.86 \times 240 = \$343{,}886$. **De los cuales $\$143,886 son
intereses: el 72 % del capital prestado.**

**Paso 2 — La composición de la primera cuota**

$$\text{Interés} = 200{,}000 \times 0.005 = \$1{,}000$$

$$\text{Amortización} = 1{,}432.86 - 1{,}000 = \$432.86$$

**Solo el 30 % de tu primera cuota reduce la deuda.** El otro 70 % es interés puro. Esta es la
característica que define al sistema francés y la que más sorprende a quien firma su primera
hipoteca.

**Paso 3 — El efecto de un abono a capital**

Supón que en el mes 1 haces un abono extraordinario de **$\$20,000$** directamente a capital.
El saldo baja a $\$180,000$ y, manteniendo la misma cuota:

$$n = \frac{-\ln\left(1 - \frac{180{,}000 \times 0.005}{1{,}432.86}\right)}{\ln(1.005)} \approx 198 \text{ meses}$$

**El préstamo se acorta de 240 a ~198 meses: 42 meses menos.**

Intereses ahorrados: $42 \times 1{,}432.86 \approx \mathbf{\$60{,}180}$.

**Un abono de $\$20,000 ahorra unos $\$60,000 de intereses.** Un retorno del 201 % sobre el abono —
libre de impuestos y sin riesgo, porque no es una inversión sino una deuda evitada.

!!! warning "Antes de correr a amortizar tu hipoteca"
    El razonamiento anterior es correcto **pero incompleto**. Amortizar deuda equivale a una
    inversión que rinde exactamente la tasa del préstamo, con riesgo cero. La comparación
    honesta es contra la alternativa:

    * Si tu hipoteca está al 6 % y puedes invertir con seguridad al 4 %, **amortiza**.
    * Si tu hipoteca está al 3 % (heredada de la época de tasas cero) y los bonos rinden 5 %,
      **no amortices**: tu deuda barata es un activo.
    * Considera la **deducibilidad fiscal** de los intereses donde exista: reduce el costo
      efectivo del préstamo.
    * Y sobre todo, **mira la liquidez**: el dinero que metes en la hipoteca deja de estar
      disponible. Un fondo de emergencia vale más que unos puntos de interés ahorrados.

    Es el mismo razonamiento de costo de oportunidad de la Semana 1, aplicado a tu propio
    balance.

---
