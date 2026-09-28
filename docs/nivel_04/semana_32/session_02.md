# Semana 32 · Sesión 2: Profundización

## 4. Expected Shortfall (CVaR): El Sucesor del VaR
Basilea III (la regulación bancaria moderna) obliga a los bancos a usar el **Expected Shortfall** (también llamado CVaR o Conditional VaR) porque resuelve el defecto del VaR.
* **Definición:** Es el promedio matemático de todas las pérdidas que exceden el VaR. Te dice: *"Si las cosas salen mal (caes en el peor 1%), ¿cuánto perderás en promedio?"*
* **Cálculo en Excel (VaR Histórico):** Si tuviste 100 días malos peores que el VaR, el CVaR es el `=PROMEDIO()` de esos 100 días.

---

## 5. Uso de Derivados para Cobertura (Hedging)
La cobertura (Hedging) es tomar una posición en un derivado que genere una ganancia si tu cartera principal pierde valor, neutralizando el riesgo. 

**A. Hedging de Renta Variable (Acciones) con Futuros:**
Si gestionas un portafolio de $10 Millones en acciones del S&P 500 y temes que la bolsa caiga un 10% el próximo mes por una decisión del Banco Central, puedes vender Futuros del S&P 500.
* *Cálculo:* Necesitas vender $10 Millones en futuros. Si la bolsa cae 10%, tu portafolio pierde $1 Millón, pero tu futuro corto te genera +$1 Millón. 
* *Matemática con Beta:* Si tu portafolio tiene una Beta de 1.5 (Semana 24), debes sobre-cubrirte. Venderás $15 Millones en futuros ($10M \times 1.5$) para compensar que tus acciones caerán más fuerte que el mercado.

**B. Hedging de Renta Fija (Bonos) con Swaps:**
Si tienes una cartera de bonos a largo plazo y temes que las tasas de interés suban (lo que destruiría el precio de tus bonos, como vimos en la Semana 28), entras en un **Swap de Tasa de Interés** donde pagas una tasa fija y recibes una tasa variable. Al subir las tasas, la tasa variable que recibes sube, compensando la caída del precio de tus bonos.

---

## Los tres métodos para calcular el VaR

El VaR paramétrico de la sesión anterior es solo uno de tres enfoques, y no siempre el mejor.

| Método | Cómo funciona | Ventaja | Limitación |
|---|---|---|---|
| **Paramétrico** (varianza-covarianza) | Asume normalidad; $VaR = V \times Z \times \sigma$ | Rápido, analítico | Falla con colas gordas y con opciones |
| **Histórico** | Ordena los retornos reales de los últimos N días y toma el percentil | No asume distribución alguna | Solo conoce el pasado; sensible a la ventana |
| **Monte Carlo** | Simula miles de escenarios según distribuciones y correlaciones | Maneja carteras complejas y no lineales | Costoso; depende de los supuestos |

**Ejemplo comparativo** sobre la misma cartera de $\$5$ M con $\sigma$ diaria del 2 %:

* **Paramétrico 99 %:** $5{,}000{,}000 \times 2.326 \times 0.02 = \$232{,}600$
* **Histórico 99 %:** se ordenan los 500 retornos diarios de los últimos 2 años y se toma el
  5.º peor. Si ese día la cartera cayó un 5,4 %, el VaR es $\$270{,}000$ — **un 16 % mayor**,
  porque los datos reales tienen más cola de la que predice la normal.
* **Monte Carlo:** permite modelar que las opciones de la cartera tienen pagos no lineales, algo
  que el paramétrico no puede capturar.

**Cuándo usar cada uno:**

* Cartera simple de acciones y bonos → **paramétrico** basta.
* Cartera con **opciones o instrumentos no lineales** → paramétrico **falla**; usa Monte Carlo.
* Se quiere evitar cualquier supuesto distribucional → **histórico**, con ventana larga.

---

## El *backtesting*: la prueba que valida (o rompe) el modelo

Un VaR al 99 % afirma que las pérdidas superarán ese umbral **1 día de cada 100**. Con ~250 días
hábiles, se esperan **2 o 3 excepciones al año**. El *backtesting* comprueba si eso se cumple.

Basilea define un **semáforo** según el número de excepciones en 250 días:

| Zona | Excepciones | Consecuencia |
|---|---|---|
| **Verde** | 0-4 | Modelo aceptado |
| **Amarilla** | 5-9 | Multiplicador de capital aumenta progresivamente (de 3,0 a 3,65) |
| **Roja** | 10 o más | Modelo rechazado; se impone el método estándar |

**Lo que revela un backtest fallido:**

* **Demasiadas excepciones** → el modelo subestima el riesgo. Casi siempre por asumir
  normalidad, o por usar una ventana histórica que no incluye ninguna crisis.
* **Muy pocas excepciones** → el modelo es excesivamente conservador. Suena bien, pero inmoviliza
  capital que podría estar generando rentabilidad.
* **Excepciones agrupadas** → la señal más grave. Si las 5 excepciones del año ocurrieron en la
  misma semana, el modelo no captura el ***clustering* de volatilidad**: la tendencia de los días
  turbulentos a venir juntos.

Ese agrupamiento es un hecho estilizado de los mercados y la razón de que existan los modelos
**GARCH**, que hacen que la volatilidad estimada dependa de la volatilidad reciente en lugar de
ser constante.

---

## Del VaR al Expected Shortfall: por qué Basilea cambió de métrica

El VaR tiene un defecto conceptual serio: **no es una medida coherente de riesgo**. En concreto,
no cumple la propiedad de **subaditividad**:

$$VaR(A + B) \le VaR(A) + VaR(B) \quad \text{— puede NO cumplirse}$$

Traducido: **el VaR puede decir que diversificar aumenta el riesgo**, lo cual es absurdo. Ocurre
con carteras que tienen pagos discontinuos, como las opciones o los bonos con riesgo de impago.

El **Expected Shortfall** (o CVaR) sí es coherente, y además responde la pregunta correcta:

$$ES_{\alpha} = E[\text{Pérdida} \mid \text{Pérdida} > VaR_{\alpha}]$$

| | **VaR** | **Expected Shortfall** |
|---|---|---|
| Pregunta | ¿Cuál es el umbral del peor 1 %? | Si estoy en el peor 1 %, ¿cuánto pierdo en promedio? |
| Información sobre la cola | **Ninguna** | Completa |
| Subaditivo | No | **Sí** |
| Basilea | Marco anterior | **Marco actual (FRTB)**, al 97,5 % |

Bajo normalidad, la relación es directa:

$$ES = \sigma \times \frac{\phi(z_\alpha)}{1 - \alpha}$$

Con la cartera de $\$5$ M: $VaR_{99\%} = \$232{,}635$ y $ES_{99\%} = \$266{,}521$ — un
**15 % más**. En distribuciones con colas gordas reales, la brecha es mucho mayor.

!!! danger "La crítica que ninguna métrica resuelve"
    Nassim Taleb lleva décadas señalando el problema de fondo: **todas estas métricas se calibran
    con datos históricos, y los eventos que de verdad importan no están en el histórico.**

    Un VaR calculado con datos de 2003-2007 no contenía nada parecido a 2008. Uno calculado con
    2010-2019 no contenía una pandemia.

    Por eso el marco regulatorio no se apoya solo en modelos estadísticos, sino que añade:

    * **Pruebas de estrés** con escenarios **hipotéticos** diseñados a mano, no extraídos de la
      historia.
    * **Análisis de escenarios inversos** (*reverse stress testing*): en lugar de preguntar
      "¿cuánto pierdo si pasa X?", preguntar **"¿qué tendría que pasar para que quebremos?"**.
      Es una pregunta mucho más incómoda y mucho más útil.
    * **Límites de concentración** duros, que no dependen de ningún modelo.

---
