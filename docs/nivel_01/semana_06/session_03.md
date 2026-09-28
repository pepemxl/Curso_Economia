# Semana 6 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: Impuestos y Balanza Fiscal
El país de "Fiscalandia" tiene los siguientes datos anuales:
* Recaudación por Impuestos ($T$) = $\$80,000$ millones
* Gasto Público ($G$) = $\$120,000$ millones
* PIB de Fiscalandia = $\$500,000$ millones

**Análisis:**
1. **Déficit Fiscal:** $\$120,000$ (Gasto) - $\$80,000$ (Ingresos) = **$\$40,000$ millones de déficit**.
2. **Deuda:** Para pagar ese déficit, el Ministerio de Finanzas tendrá que emitir $\$40,000$ millones en Bonos Soberanos.
3. **Porcentaje del PIB:** Si el PIB es $\$500,000$, el déficit representa el **8% del PIB**. Un nivel muy alto para un solo año que probablemente obligará al Banco Central a subir tasas para atraer compradores para esos bonos, frenando la economía privada (Efecto Expulsión).

---

## Segundo ejercicio: la sostenibilidad de la deuda

Fiscalandia sigue preocupada. Su deuda pública acumulada es de **$\$300{,}000$ millones** sobre
un PIB de $\$500{,}000$ millones.

**Paso 1 — Ratio Deuda / PIB**

$$\frac{300{,}000}{500{,}000} = \mathbf{60\%}$$

**Paso 2 — La ecuación de la dinámica de la deuda**

Lo que determina si una deuda es sostenible no es su nivel, sino si el ratio **crece o
decrece**. La condición depende de tres variables:

$$\Delta\left(\frac{D}{Y}\right) \approx (r - g)\frac{D}{Y} - sp$$

donde $r$ es la tasa de interés real de la deuda, $g$ el crecimiento real del PIB y $sp$ el
**superávit primario** (balance fiscal *antes* de intereses) como porcentaje del PIB.

**Paso 3 — Aplicación con dos escenarios**

Fiscalandia paga un $r = 5\%$ real y tiene un déficit primario. Recordemos su déficit total de
$\$40{,}000$ millones (8 % del PIB). Si los intereses son $5\% \times 300{,}000 = \$15{,}000$
millones (3 % del PIB), su **déficit primario** es del 5 % ($sp = -0.05$).

*Escenario A — La economía crece al 2 %:*

$$\Delta(D/Y) = (0.05 - 0.02)(0.60) + 0.05 = 0.018 + 0.05 = \mathbf{+6.8 \text{ pp por año}}$$

La deuda pasaría del 60 % al 66,8 % del PIB **en un solo año**. Insostenible.

*Escenario B — La economía crece al 6 %:*

$$\Delta(D/Y) = (0.05 - 0.06)(0.60) + 0.05 = -0.006 + 0.05 = \mathbf{+4.4 \text{ pp}}$$

Mejor, pero sigue creciendo: el déficit primario del 5 % es demasiado grande para compensarlo
solo con crecimiento.

**Paso 4 — ¿Cuánto tendría que ajustar?**

Para estabilizar el ratio ($\Delta = 0$) con $g = 2\%$:

$$sp = (r - g)\frac{D}{Y} = (0.05 - 0.02)(0.60) = 0.018$$

Fiscalandia necesita un **superávit primario del 1,8 % del PIB**, cuando hoy tiene un déficit
primario del 5 %. **El ajuste requerido es de 6,8 puntos del PIB** — políticamente brutal:
equivale a subir impuestos o recortar gasto por $\$34{,}000$ millones.

!!! danger "La condición $r > g$ y por qué es el corazón del problema"
    * Si $r < g$ (la economía crece más rápido que el costo de su deuda), el ratio se **licúa
      solo**, incluso con déficit primario moderado. Es lo que ocurrió en las economías
      desarrolladas entre 2010 y 2021, con tasas cerca de cero.
    * Si $r > g$, la deuda crece por sí sola por el interés compuesto, y **hace falta superávit
      primario solo para no empeorar**.

    Cuando los bancos centrales subieron tasas en 2022, muchos países pasaron de $r < g$ a
    $r > g$ de golpe. Ese cambio de régimen es la razón de fondo de las tensiones actuales sobre
    deuda soberana, y explica por qué la prima de riesgo de algunos países se disparó sin que su
    nivel de deuda hubiera cambiado.

---

## Tercer ejercicio: el impacto en una empresa concreta

Eres el CFO de una constructora de Fiscalandia. El Banco Central sube la tasa de referencia del
**4 % al 9 %** para financiar el déficit y contener la inflación. Tus datos:

* Deuda a tasa variable: **$\$50$ millones**
* EBIT anual: **$\$12$ millones**
* El 60 % de tus ingresos proviene de obra pública

**a) Impacto en el gasto financiero**

$$\text{Antes: } 50 \times 4\% = \$2.0\text{M} \qquad \text{Después: } 50 \times 9\% = \$4.5\text{M}$$

**b) Cobertura de intereses**

$$\text{Antes: } \frac{12}{2.0} = 6.0\times \qquad \text{Después: } \frac{12}{4.5} = 2.7\times$$

Todavía por encima del umbral habitual de 2,0×, pero el margen se ha reducido a menos de la
mitad.

**c) El segundo golpe, que casi nadie modela**

El gobierno subió tasas porque tiene déficit. Para cerrarlo, lo más probable es que **recorte
inversión pública** — que es el 60 % de tu cartera. Si la obra pública cae un 30 %:

$$\text{Ingresos} \downarrow 18\% \Longrightarrow EBIT \approx \$8\text{M (asumiendo margen constante)}$$

$$\text{Cobertura} = \frac{8}{4.5} = \mathbf{1.8\times} \;\Rightarrow\; \textbf{incumplimiento de covenant}$$

**d) Qué haría el CFO**

1. **Cubrir el riesgo de tasa** con un swap de variable a fijo (Semana 30), fijando el costo
   antes de que suba más.
2. **Alargar vencimientos** ahora, aunque cueste más, para no tener que refinanciar en el peor
   momento.
3. **Renegociar covenants** con el banco *antes* de incumplirlos: la posición negociadora es
   incomparablemente mejor.
4. **Diversificar la cartera** hacia obra privada, reduciendo la correlación con el ciclo fiscal.

**La lección de método:** el análisis macroeconómico no es contexto decorativo para el modelo.
Aquí, una única decisión del Banco Central golpea **simultáneamente** el numerador (EBIT, vía
menor obra pública) y el denominador (intereses) del mismo ratio. Modelar solo uno de los dos
efectos subestima gravemente el riesgo.

---
