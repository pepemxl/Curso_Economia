# Semana 24 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Calculando el WACC de "OmegaCorp"

Eres el Director Financiero de OmegaCorp. Quieres evaluar la compra de una nueva fábrica que dará un retorno del 10%. ¿Creas o destruyes valor? Necesitas el WACC.

**Datos del Mercado y la Empresa:**
* Tasa Libre de Riesgo ($R_f$): 4%
* Prima por Riesgo de Mercado ($MRP$): 6%
* Beta ($\beta$) de OmegaCorp: 1.2
* Costo de la deuda antes de impuestos ($r_d$): 8%
* Tasa de Impuesto Corporativa ($T$): 25%
* Estructura de Capital: La empresa vale $1,000 millones. $600 millones son Patrimonio ($E$) y $400 millones son Deuda ($D$). (Por lo tanto, $E/V = 60\%$ y $D/V = 40\%$).

**Paso 1: Calcular el Costo del Patrimonio ($r_e$) con CAPM**
* $r_e = 4\% + 1.2 \times 6\% = 4\% + 7.2\% = \mathbf{11.2\%}$

**Paso 2: Calcular el Costo de la Deuda después de Impuestos**
* $r_d(1-T) = 8\% \times (1 - 0.25) = 8\% \times 0.75 = \mathbf{6.0\%}$

**Paso 3: Calcular el WACC**
* WACC = $(60\% \times 11.2\%) + (40\% \times 6.0\%)$
* WACC = $6.72\% + 2.40\% = \mathbf{9.12\%}$

**Veredicto de Inversión:**
El WACC es 9.12%. La nueva fábrica genera un 10%. Como el Retorno (10%) > Costo de Capital (9.12%), la fábrica **crea valor económico**. ¡Proyectos aprobados!


## Plantilla de Excel

!!! abstract "Descarga: WACC y valuación DCF"
    **[:material-file-excel: dcf_wacc.xlsx](../../assets/plantillas/dcf_wacc.xlsx)**

    La hoja **WACC** calcula el costo de capital paso a paso (CAPM, escudo fiscal de la deuda,
    pesos a valor de mercado). Con los datos de GoldRush de esta semana devuelve exactamente
    **8,00 %**.

    Cambia el peso de la deuda y observa el efecto sobre el WACC — y recuerda el matiz de la
    sesión anterior: en la realidad el *beta* del patrimonio también subiría, así que el WACC
    no baja indefinidamente por endeudarse más.

---

## Segundo ejercicio: el error de usar un único WACC para toda la empresa

OmegaCorp tiene un WACC del 9,12 %. Pero OmegaCorp opera **dos divisiones muy distintas**:

* **División Industrial:** negocio maduro, flujos estables. Beta del sector: **0,8**
* **División Tecnológica:** alto crecimiento, alta incertidumbre. Beta del sector: **1,8**

Si el CFO evalúa **todos** los proyectos con el WACC corporativo del 9,12 %, ocurre lo
siguiente:

| | Industrial | Tecnológica |
|---|---|---|
| Beta apropiada | 0.8 | 1.8 |
| $r_e = 4\% + \beta(6\%)$ | **8,8 %** | **14,8 %** |
| WACC divisional ($60/40$, $r_d(1-t)=6\%$) | **7,68 %** | **11,28 %** |
| WACC corporativo aplicado | 9,12 % | 9,12 % |

**Las consecuencias son sistemáticas y perversas:**

* Un proyecto **industrial** que rinde el 8,5 % se **rechaza** (parece por debajo del 9,12 %),
  cuando en realidad crea valor: supera su WACC divisional del 7,68 %.
* Un proyecto **tecnológico** que rinde el 10 % se **acepta** (parece superar el 9,12 %), cuando
  en realidad **destruye valor**: no llega al 11,28 % que exige su riesgo.

**Resultado a largo plazo:** la empresa rechaza sistemáticamente sus buenos proyectos de bajo
riesgo y acepta sistemáticamente sus malos proyectos de alto riesgo. **Se vuelve cada vez más
riesgosa y menos rentable**, sin que nadie tome una sola decisión deliberadamente mala.

**La solución: el método del beta comparable (*pure play*)**

1. Identifica empresas cotizadas dedicadas **solo** a esa actividad.
2. Toma su beta apalancada ($\beta_L$) y **desapalánquala** para aislar el riesgo del negocio:

$$\beta_U = \frac{\beta_L}{1 + (1-t)\frac{D}{E}}$$

3. **Reapalanca** con la estructura de capital de *tu* división:

$$\beta_L^{propia} = \beta_U \left[1 + (1-t)\frac{D}{E}\right]$$

4. Aplica CAPM con esa beta y calcula el WACC divisional.

**Ejemplo numérico.** Un comparable tecnológico tiene $\beta_L = 2.0$ con $D/E = 0.25$ y
$t = 25\%$:

$$\beta_U = \frac{2.0}{1 + 0.75(0.25)} = \frac{2.0}{1.1875} = 1.68$$

Si tu división tecnológica va a operar con $D/E = 0.67$ (los $40/60$ de OmegaCorp):

$$\beta_L = 1.68\left[1 + 0.75(0.67)\right] = 1.68 \times 1.5 = \mathbf{2.52}$$

$$r_e = 4\% + 2.52(6\%) = \mathbf{19.1\%}$$

Muy lejos del 11,2 % corporativo. **El riesgo del negocio y el riesgo financiero son cosas
distintas, y hay que separarlos antes de sumarlos.**

---

## De dónde salen realmente los tres inputs del CAPM

En la práctica, la mayor parte del debate sobre una valuación es un debate sobre estos tres
números:

**$R_f$ — Tasa libre de riesgo**

* Se usa el **bono soberano a 10 años** de la moneda en que estén los flujos, para casar la
  duración del bono con la del proyecto.
* En mercados emergentes se añade una **prima de riesgo país** (el diferencial del bono soberano
  frente al del Tesoro estadounidense).
* Error común: usar la letra a 3 meses. Es demasiado corta y demasiado volátil.

**$MRP$ — Prima por riesgo de mercado**

Es el input **más discutido** de todas las finanzas. Tres enfoques:

* **Histórico:** diferencia media entre el retorno de la bolsa y el bono, sobre 50-100 años.
  Da un 4-6 % según el período y si se usa media aritmética o geométrica.
* **Implícito:** la prima que iguala el precio actual del índice con el valor presente de sus
  dividendos esperados. Es prospectivo y suele dar 4-5 %.
* **Encuestas:** a académicos y profesionales. Rondan el 5-6 %.

**El rango razonable es 4,5 %–6 %.** Un punto porcentual de diferencia en el MRP puede cambiar
una valuación un 15-20 %, así que documenta siempre tu elección.

**$\beta$ — Beta**

* Se estima por regresión de los retornos de la acción contra los del índice, típicamente con
  5 años de datos mensuales o 2 años semanales.
* **Beta ajustada (Blume):** $\beta_{aj} = 0.67\beta + 0.33$. Corrige la tendencia empírica de
  las betas a revertir hacia 1 con el tiempo. Es lo que reportan Bloomberg y la mayoría de
  proveedores.
* Para empresas **no cotizadas**, el método *pure play* de arriba es la única vía.

!!! warning "Los límites del CAPM que un analista honesto declara"
    El CAPM asume que el único riesgo remunerado es el **sistemático**, que todos los
    inversionistas están diversificados y que los retornos son normales. Ninguna de las tres se
    cumple del todo.

    Empíricamente el CAPM explica **poco** de las diferencias de retorno entre acciones. Los
    modelos multifactoriales (Fama-French de 3 y 5 factores) añaden tamaño, valor,
    rentabilidad e inversión, y explican bastante más.

    Aun así el CAPM sigue siendo el estándar en valuación corporativa, por una razón práctica:
    es **transparente, replicable y defendible ante un comité**. Lo importante no es creer que
    da el número exacto, sino usarlo de forma consistente y presentar siempre un **rango**.

---
