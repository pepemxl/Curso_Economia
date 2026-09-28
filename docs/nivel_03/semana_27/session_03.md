# Semana 27 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: El Método de Capital de Riesgo

Eres socio de un fondo de Venture Capital. Dos estudiantes te presentan "CitrusAI", una app de agronomía. Piden **$2,000,000**.
Tú analizas el mercado:
* Estimas que en 5 años, la startup generará $10M de ventas. Los múltiplos de empresas tech agrícolas en ese momento son de 5x Ventas. **Valor Terminal = $50,000,000**.
* Tu fondo exige una tasa de retorno objetivo del **50% anual** por el altísimo riesgo.

**Calculando la Valoración:**
1. **Valor Post-Money (Hoy):** $\frac{50,000,000}{(1 + 0.50)^5} = \frac{50,000,000}{7.59} = \mathbf{\$6,585,774}$
2. **Valor Pre-Money:** Post-Money - Inversión = $\$6,585,774 - \$2,000,000 = \mathbf{\$4,585,774}$
3. **Participación de tu fondo (Ownership):** Inversión / Post-Money = $\$2M / \$6.58M = \mathbf{30.37\%}$

**El Veredicto Financiero:**
Le dices a los fundadores: *"Les daremos $2 millones. Su empresa vale $4.58 millones antes de nuestra inversión (Pre-money). Nos quedaremos con el 30.37% de las acciones de la compañía. Si en 5 años venden la empresa en $50 millones, nuestro 30% valdrá $15 millones, cumpliendo nuestro retorno del 50% anual. Tomen o dejen"*. (Los fundadores aceptan porque necesitan el dinero para sobrevivir, aceptando la dilución).

---

## Segundo ejercicio: la dilución que el método de VC ignora

El cálculo anterior asume que **no habrá más rondas**. Veamos qué pasa en la realidad.

Tu fondo entra con el **30,37 %** de CitrusAI. Dos años después, la empresa levanta una **Serie
B** de $\$5$ millones con una valoración pre-money de $\$20$ millones.

**Paso 1 — Nueva estructura tras la Serie B**

$$\text{Post-money} = 20 + 5 = \$25\text{M} \qquad \text{Nuevo inversor} = \frac{5}{25} = 20\%$$

**Paso 2 — Tu participación diluida**

$$30.37\% \times (1 - 0.20) = \mathbf{24.30\%}$$

**Paso 3 — Una Serie C de $\$15$ M sobre $\$60$ M pre-money**

$$\text{Nuevo inversor} = \frac{15}{75} = 20\% \quad \Rightarrow \quad 24.30\% \times 0.80 = \mathbf{19.44\%}$$

**Paso 4 — El *pool* de opciones para empleados**

Antes de la salida, el consejo amplía el *pool* de opciones en un 10 %:

$$19.44\% \times 0.90 = \mathbf{17.50\%}$$

**Resumen de la dilución:**

| Momento | Tu participación |
|---|---|
| Serie A (tu entrada) | **30,37 %** |
| Tras Serie B | 24,30 % |
| Tras Serie C | 19,44 % |
| Tras ampliar el *pool* | **17,50 %** |

**Perdiste el 42 % de tu participación sin vender una sola acción.**

**Paso 5 — ¿Se cumple el retorno objetivo?**

Si la salida es de $\$50$ M como se proyectó:

$$0.1750 \times 50{,}000{,}000 = \$8.75\text{M}$$

Sobre $\$2$ M invertidos son **4,37×** en 5 años, es decir un **34,3 % anual**. Muy lejos del
50 % objetivo.

Para alcanzar realmente el 50 % anual con esa dilución, la salida tendría que ser:

$$\frac{2{,}000{,}000 \times (1.50)^5}{0.1750} = \frac{15{,}187{,}500}{0.1750} = \mathbf{\$86.8 \text{ millones}}$$

**La salida tendría que ser un 73 % mayor de lo proyectado.**

!!! tip "Cómo se protege un fondo en la práctica"
    * **Derechos *pro-rata*:** el derecho (no la obligación) a participar en rondas futuras para
      mantener el porcentaje. Es la protección más común y la más valiosa.
    * **Cláusulas antidilución.** Si una ronda futura se hace a **menor** valoración (*down
      round*), ajustan el precio de conversión de tus acciones:
        * *Full ratchet:* tu precio se reajusta al de la nueva ronda. Brutal para los fundadores.
        * *Weighted average:* ajuste proporcional al tamaño de la ronda. Es el estándar de mercado.
    * **Preferencia de liquidación.** En una salida, cobras **antes** que los ordinarios. Una
      preferencia 1× no participativa significa que recuperas tu inversión primero, o conviertes
      a ordinarias y cobras tu porcentaje — lo que sea mayor.
    * **Calcular siempre sobre la base totalmente diluida** (*fully diluted*), incluyendo
      opciones, notas convertibles y SAFE pendientes. Un 30 % sobre acciones emitidas puede ser
      un 22 % sobre la base diluida.

---

## Los tres métodos de valuación en M&A y por qué dan resultados distintos

En una operación real nunca se presenta un solo número. Se presenta el **campo de fútbol**
(*football field*): un gráfico de barras con el rango que da cada método.

| Método | Qué mide | Sesgo típico |
|---|---|---|
| **DCF** | Valor intrínseco de los flujos | El más sensible a supuestos; rango amplio |
| **Trading comps** | Lo que el mercado paga hoy por empresas similares | **El más bajo**: no incluye prima de control |
| **Transaction comps** | Lo que compradores pagaron en operaciones pasadas | **El más alto**: incluye prima de control y sinergias |
| **LBO** | El máximo que un fondo de private equity podría pagar | Suelo de la valoración |

**Por qué los *transaction comps* son sistemáticamente más altos.** Tres razones acumulativas:

1. **Prima de control.** Quien compra el 100 % puede cambiar la dirección, la estrategia y la
   estructura de capital. Eso vale, y se paga: típicamente **20-40 %** sobre el precio de mercado.
2. **Sinergias.** El comprador espera ahorros de costos o ingresos adicionales que un accionista
   minoritario no puede capturar.
3. **Competencia en la subasta.** Si hay varios postores, el precio final incorpora parte del
   valor que el ganador esperaba capturar — la llamada **maldición del ganador**.

!!! danger "La aritmética de las sinergias"
    La regla que decide si una adquisición crea valor:

    $$\text{Valor creado} = \text{Sinergias} - \text{Prima pagada}$$

    Si compras una empresa que vale $\$100$ M pagando $\$130$ M porque esperas $\$50$ M de
    sinergias, creas $\$20$ M. Si las sinergias resultan ser $\$20$ M, **destruyes $\$10$ M**.

    Los estudios empíricos son consistentes y desalentadores: entre el **50 % y el 70 %** de las
    fusiones destruyen valor para el accionista del comprador. Las sinergias de **costos** (cerrar
    duplicidades) se materializan razonablemente; las de **ingresos** (venta cruzada) casi nunca.

    Por eso la reacción típica del mercado al anuncio de una gran adquisición es: **sube la
    acción del comprado, baja la del comprador**. El mercado está diciendo que la prima es
    demasiado alta.

---
