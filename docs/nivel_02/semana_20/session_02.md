# Semana 20 · Sesión 2: Profundización

## 4. Las Funciones Clave en Excel para Monte Carlo
Para hacer Monte Carlo sin necesidad de programar en Python o VBA, usamos dos funciones de Excel combinadas:

1. **=ALEATORIO() o =ALEATORIO.ENTRE():** Genera un número al azar entre 0 y 1. Es el "motor aleatorio" de la simulación (representa la probabilidad acumulada).
2. **=INV.NORM(probabilidad; media; desv_estándar):** Toma un número de probabilidad (entre 0 y 1) y lo traduce a un valor real basado en la Campana de Gauss (Distribución Normal de la Semana 15).

* **La Magia:** `=INV.NORM(ALEATORIO(); 10; 1)`
  Excel generará un número aleatorio (ej. 0.45), lo meterá en la inversa de la distribución normal con media 10 y desviación 1, y te arrojará un precio de venta aleatorio de $9.87. Cada vez que presiones F9 (recalcular), Excel lanzará los "dados" y te dará un nuevo escenario completo.

---

## Análisis de sensibilidad, escenarios y simulación: tres herramientas distintas

Se confunden constantemente, pero responden preguntas diferentes:

| Herramienta | Qué varía | Qué responde | Limitación |
|---|---|---|---|
| **Sensibilidad** | Una variable a la vez | ¿A qué soy más sensible? | Ignora que las variables se mueven juntas |
| **Escenarios** | Varias a la vez, en combinaciones coherentes | ¿Qué pasa si se cumple esta historia? | Solo 3 o 4 futuros posibles |
| **Monte Carlo** | Todas, miles de veces, según su distribución | ¿Cuál es la **distribución** de resultados? | Exige estimar distribuciones y correlaciones |

**Sensibilidad: el gráfico tornado.** Se varía cada supuesto ±20 % manteniendo el resto fijo y
se ordenan las variables por el ancho de su efecto sobre el resultado. La forma resultante —
barras largas arriba, cortas abajo— da nombre al gráfico. Su utilidad es de priorización: **te
dice dónde invertir el esfuerzo de investigación.** No tiene sentido afinar una variable que
mueve el VAN un 2 % mientras otra lo mueve un 60 %.

**Escenarios: coherencia interna.** El error de la sensibilidad es que trata las variables como
independientes. En una recesión no cae solo el volumen de ventas: también bajan los precios,
suben los días de cobro y se encarece el crédito. Un escenario pesimista **debe mover todas
esas variables a la vez y en la dirección correcta**. Por eso se construyen como narrativas, no
como porcentajes sueltos.

**Monte Carlo: la distribución completa.** Es el único de los tres que devuelve
**probabilidades**. No dice "el VAN pesimista es −$500,000", dice "hay un 12 % de probabilidad
de perder más de $500,000". Esa diferencia es la que permite decidir con criterio de riesgo.

---

## Cómo elegir la distribución de cada variable

Es la decisión que más determina la calidad de una simulación, y la que más se improvisa:

| Distribución | Cuándo usarla | Parámetros |
|---|---|---|
| **Normal** | Variables simétricas alrededor de un valor central (precios, retornos) | media, $\sigma$ |
| **Lognormal** | Variables que **no pueden ser negativas** y tienen cola derecha (precios de activos, ingresos) | media y $\sigma$ del logaritmo |
| **Triangular** | Cuando solo tienes las estimaciones de un experto: mínimo, más probable, máximo | 3 puntos |
| **Uniforme** | Ignorancia total dentro de un rango | mínimo, máximo |
| **PERT / Beta** | Como la triangular, pero con más peso en el valor más probable | 3 puntos |
| **Discreta** | Eventos con resultados contables (¿aprueban la licencia?) | valores y probabilidades |

!!! warning "Los dos errores que invalidan una simulación"
    **1. Usar la normal para variables acotadas.** Un costo de construcción no puede ser
    negativo, pero la normal siempre asigna probabilidad a la cola izquierda. Con media 300,000
    y $\sigma$ 50,000, la probabilidad de un costo negativo es despreciable; con media 100,000
    y $\sigma$ 80,000, ya no lo es. Para esos casos, **lognormal o triangular**.

    **2. Ignorar las correlaciones.** Es el error grave. Si simulas precio de venta y costo de
    construcción como **independientes**, estás asumiendo que pueden moverse en direcciones
    opuestas libremente. En la realidad ambos dependen del ciclo inmobiliario y están
    **positivamente correlacionados**.

    El efecto es sistemático: **ignorar correlaciones positivas subestima el riesgo**, porque
    la diversificación aparente no existe. Es exactamente el fallo que hundió a LTCM en 1998
    (Semana 39) y a los modelos de hipotecas subprime en 2008: se asumió que los impagos de
    distintas regiones eran independientes.

---

## Cuántas iteraciones hacen falta

El error estándar de la media simulada decrece con la raíz del número de iteraciones:

$$SE = \frac{\sigma}{\sqrt{N}}$$

**Para reducir el error a la mitad hay que cuadruplicar las iteraciones.** Órdenes de magnitud
prácticos:

| Iteraciones | Para qué alcanza |
|---|---|
| 1,000 | Estimar la media y la probabilidad de éxito |
| 10,000 | Percentiles centrales (P10, P90) |
| 100,000+ | Colas extremas (P99, VaR al 99 %) |

**Convergencia:** grafica la media acumulada frente al número de iteraciones. Cuando la línea se
aplana, has convergido. Si sigue oscilando, necesitas más.

**Semilla aleatoria.** Para que un resultado sea **reproducible** —y por tanto auditable— hay
que fijar la semilla del generador. Excel no lo permite de forma nativa con `ALEATORIO()`, que
es una de las razones por las que las simulaciones serias se hacen en Python o R. El script que
genera la figura de esta semana usa `default_rng(42)` precisamente para eso.

---
