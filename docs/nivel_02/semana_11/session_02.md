# Semana 11 · Sesión 2: Profundización

## 4. Valor Futuro (VF) y Valor Presente (VP)
**A. Valor Futuro (Calcular hacia adelante):** 
Saber cuánto valdrá una inversión hoy en el futuro. (Usa la fórmula de interés compuesto de arriba).

**B. Valor Presente (Calcular hacia atrás / "Descontar"):**
Saber cuánto vale hoy una suma de dinero que recibiremos en el futuro. Hay que "traerla al presente" quitándole el interés que generaría (tasa de descuento).
* **Fórmula del Valor Presente (VP):**
  $$ VP = \frac{VF}{(1 + r)^t} $$
  Donde $r$ es la **tasa de descuento** (la rentabilidad exigida por el inversor).

> **💥 Regla de Oro del Analista:** Las acciones, los bonos, las casas y las empresas NO se valen por lo que "valdrán" en el futuro; se valen por el **Valor Presente** de todo el efectivo que generarán en el futuro. *Descontar* flujos es el corazón de las finanzas corporativas (lo veremos en la Semana 24).

---

## 5. Tasa Nominal vs. Tasa Efectiva (Cuidado con el fraude bancario)
Rara vez una inversión dura exactamente "1 año" sin ningún pago intermedio. Muchas veces los intereses se capitalizan varias veces al año (mensual, trimestral, diario). 

1. **Tasa Nominal ($r_n$):** Es la tasa que el banco te "anuncia" en la cartelera. No refleja la capitalización real si el interés se paga más de una vez al año.
2. **Tasa Efectiva ($r_e$):** Es la tasa que *realmente* ganas o pagas al final del año, considerando el efecto del interés compuesto intra-anual.
* **Fórmula de la Tasa Efectiva (EAR):**
  $$ r_e = \left( 1 + \frac{r_n}{m} \right)^m - 1 $$
  Donde $m$ es el número de periodos de capitalización al año (ej. mensual es 12, trimestral es 4).

> *Ejemplo clásico:* Si una tarjeta de crédito te cobra "1.5% mensual". 
> El banco podría decir: "¡Es solo un 18% anual! (1.5% x 12 meses = Tasa Nominal)".
> Pero la matemática dice: Tasa Efectiva = $(1 + 0.015)^{12} - 1 = 0.1956$ o **19.56% anual real**. ¡Como analista, siempre calculas la efectiva!

---

## Interés simple frente a compuesto: la diferencia que crece sola

| | **Interés simple** | **Interés compuesto** |
|---|---|---|
| Base de cálculo | Siempre el capital inicial | Capital **más** intereses acumulados |
| Fórmula | $VF = VP(1 + r \cdot t)$ | $VF = VP(1+r)^t$ |
| Crecimiento | **Lineal** | **Exponencial** |
| Uso real | Préstamos muy cortos, algunos descuentos comerciales | Prácticamente todo lo demás |

Sobre $\$10,000$ al 10 % anual:

| Años | Simple | Compuesto | Diferencia |
|---|---|---|---|
| 1 | 11,000 | 11,000 | 0 |
| 5 | 15,000 | 16,105 | +1,105 |
| 10 | 20,000 | 25,937 | +5,937 |
| 20 | 30,000 | 67,275 | **+37,275** |
| 40 | 50,000 | 452,593 | **+402,593** |

A un año son idénticos. A cuarenta años, el compuesto da **nueve veces más**. Toda la
diferencia son "intereses sobre intereses".

---

## Capitalización continua: el límite del proceso

¿Qué pasa si la capitalización no es mensual ni diaria, sino **instantánea**? El límite existe y
es elegante:

$$\lim_{m \to \infty}\left(1 + \frac{r}{m}\right)^{m} = e^{r}$$

$$VF = VP \cdot e^{rt}$$

Sobre $\$1,000$ al 10 % durante un año:

| Frecuencia | $m$ | Valor futuro | EAR |
|---|---|---|---|
| Anual | 1 | 1,100.00 | 10.00 % |
| Semestral | 2 | 1,102.50 | 10.25 % |
| Trimestral | 4 | 1,103.81 | 10.38 % |
| Mensual | 12 | 1,104.71 | 10.47 % |
| Diaria | 365 | 1,105.16 | 10.52 % |
| **Continua** | $\infty$ | **1,105.17** | **10.52 %** |

Fíjate en el patrón: **el aumento se va agotando**. Pasar de anual a mensual añade 47 puntos
básicos; pasar de diaria a continua añade menos de uno. La capitalización continua no es una
ganga oculta, es el **techo matemático** del proceso.

**Por qué importa en finanzas:** la capitalización continua es la convención estándar en la
teoría de derivados. Black-Scholes descuenta con $e^{-rT}$, y los retornos logarítmicos
($\ln(P_t/P_{t-1})$) se usan precisamente porque son aditivos en el tiempo, lo que simplifica
enormemente la estadística de series financieras (Semana 32).

---

## Las cinco variables y cómo despejar cada una

Todo problema de valor del dinero en el tiempo tiene cinco variables. Conocidas cuatro, se
despeja la quinta:

| Variable | Qué es | Función de Excel |
|---|---|---|
| $VP$ | Valor presente | `VA` (PV) |
| $VF$ | Valor futuro | `VF` (FV) |
| $r$ | Tasa por período | `TASA` (RATE) |
| $n$ | Número de períodos | `NPER` |
| $PMT$ | Pago periódico | `PAGO` (PMT) |

**Despejar la tasa:**

$$r = \left(\frac{VF}{VP}\right)^{1/n} - 1$$

**Despejar el plazo:**

$$n = \frac{\ln(VF/VP)}{\ln(1+r)}$$

*Ejemplo:* ¿cuánto tarda $\$10,000$ en llegar a $\$25,000$ al 7 %?

$$n = \frac{\ln(2.5)}{\ln(1.07)} = \frac{0.9163}{0.0677} = \mathbf{13.5 \text{ años}}$$

!!! warning "La convención de signos que confunde a todo el mundo"
    Excel exige que las entradas y salidas de caja tengan **signos opuestos**. Si inviertes
    $\$10,000$ hoy, ese flujo es **negativo** (sale de tu bolsillo); lo que recibes después es
    positivo.

    Si escribes `=TASA(10; 0; 10000; -25000)` obtienes el resultado correcto. Si pones ambos
    positivos, Excel devuelve `#¡NUM!` porque el problema no tiene solución: no existe una tasa
    que convierta dinero que entra en más dinero que entra sin que salga nada.

    La misma lógica explica por qué `PAGO` devuelve un número negativo: recibiste el préstamo
    (positivo), así que las cuotas salen (negativo).

---
