# Semana 33 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: La Magia Matemática del Multiplicador

El Banco Central de "MacroState" inyecta $1,000 millones en efectivo comprando bonos al sistema bancario (Política Monetaria Expansiva, Semana 6). El Coeficiente de Caja (Reserva) que exige el regulador es del **10%** ($r = 0.10$).

**El Efecto Dominó:**
* **Banco A:** Recibe los $1,000M. Guarda $100M (10%). Presta $900M a una fábrica.
* **Banco B:** La fábrica paga a sus proveedores. Esos $900M se depositan en el Banco B. El Banco B guarda $90M (10%). Presta $810M.
* **Banco C:** Esos $810M se depositan. Guarda $81M. Presta $729M.
* *(Y así hasta el infinito).*

**Cálculo Matemático Total:**
1. Multiplicador ($m$): $1 / 0.10 = \mathbf{10}$.
2. Dinero Total Creado ($M$): $\$1,000M \times 10 = \mathbf{\$10,000 \text{ Millones}}$.

*Interpretación Financiera:* Con solo imprimir billetes por $1,000M, el Banco Central logró expandir el crédito y la economía en $10,000M gracias a la red de bancos comerciales. Si el Banco Central quiere frenar la inflación, sube el $r$ al 20%, reduciendo el multiplicador a 5x, destruyendo $5,000M de liquidez sistémica instantáneamente.

---

## Segundo ejercicio: las fugas que reducen el multiplicador real

El multiplicador de 10 es el **máximo teórico**. En la realidad nunca se alcanza, porque hay dos
fugas que el modelo simple ignora.

**Fuga 1 — El efectivo que la gente no deposita.** Si el público mantiene una parte de su
dinero en billetes bajo el colchón, ese dinero **sale del sistema bancario** y no se puede
prestar.

**Fuga 2 — Las reservas excedentes.** Los bancos pueden guardar más del mínimo legal por
prudencia, como vimos en el ejercicio de la sesión 4.

El multiplicador completo:

$$m = \frac{1 + c}{r + e + c}$$

donde $c$ es la proporción efectivo/depósitos que prefiere el público, $r$ el encaje legal y
$e$ las reservas excedentes.

**Aplicación a MacroState.** Con $r = 0.10$, y supuestos realistas de $c = 0.15$ y $e = 0.05$:

$$m = \frac{1 + 0.15}{0.10 + 0.05 + 0.15} = \frac{1.15}{0.30} = \mathbf{3.83}$$

$$M = 1{,}000 \times 3.83 = \mathbf{\$3{,}830 \text{ millones}}$$

**Frente a los $\$10,000$ millones del modelo simple: menos del 40 %.**

| Escenario | $r$ | $e$ | $c$ | Multiplicador | Dinero creado |
|---|---|---|---|---|---|
| Teórico | 0.10 | 0 | 0 | **10.00** | $10,000 M |
| Normal | 0.10 | 0.05 | 0.15 | **3.83** | $3,830 M |
| Crisis de confianza | 0.10 | 0.30 | 0.30 | **1.86** | $1,860 M |
| Pánico bancario | 0.10 | 0.50 | 0.50 | **1.36** | $1,360 M |

**Fíjate en el escenario de crisis:** el banco central no cambió nada, el encaje legal sigue en
el 10 %. Pero como los bancos acumulan reservas ($e$ sube) y el público retira efectivo ($c$
sube), **el multiplicador se derrumba de 3,83 a 1,86**. La misma inyección crea la mitad de
dinero.

---

## Por qué el modelo del multiplicador está en revisión

El relato clásico —"el banco recibe depósitos y presta una fracción"— es didácticamente útil
pero **describe mal cómo funciona la banca moderna**. El propio Banco de Inglaterra publicó en
2014 un artículo señalando que la causalidad va al revés:

> **Los bancos no prestan los depósitos que reciben: crean depósitos al prestar.**

Cuando un banco concede un préstamo de $\$100,000$, **no busca ese dinero en su bóveda**.
Simplemente anota simultáneamente:

* Un **activo**: el préstamo por cobrar de $\$100,000$.
* Un **pasivo**: un depósito de $\$100,000$ en la cuenta del cliente.

**El dinero se creó con un asiento contable.** Es exactamente la partida doble de la Semana 7,
aplicada a escala macroeconómica.

**¿Qué limita entonces la creación de dinero?** No las reservas, sino:

1. **La demanda de crédito solvente.** Si nadie quiere endeudarse —o nadie es lo bastante
   solvente— no hay préstamos que crear.
2. **El capital regulatorio.** Cada préstamo consume capital (Basilea III, Semana 34). Ese es el
   límite que de verdad muerde hoy.
3. **La rentabilidad.** El banco presta si el margen compensa el riesgo y el capital consumido.
4. **La política monetaria, indirectamente:** el banco central influye en el precio del crédito
   (la tasa), no en su cantidad.

!!! tip "Por qué esto explica la ausencia de inflación tras 2008"
    Entre 2008 y 2021 los bancos centrales expandieron la base monetaria de forma sin
    precedentes con los programas de compra de activos. El modelo clásico del multiplicador
    predecía una explosión inflacionaria que **no ocurrió durante más de una década**.

    La explicación es la de este ejercicio: las reservas excedentes se dispararon. Los bancos
    recibieron liquidez y **la dejaron aparcada en el banco central** en lugar de prestarla,
    porque la demanda de crédito solvente era baja y su capital estaba dañado. El multiplicador
    se desplomó, compensando casi exactamente el aumento de la base.

    La inflación de 2021-2023 tuvo un origen distinto: shocks de oferta, cuellos de botella
    logísticos y —esta vez sí— transferencias fiscales directas a los hogares, que **no
    dependen del canal bancario**. Es la distinción entre política monetaria y fiscal de la
    Semana 6, en un caso real.

---
