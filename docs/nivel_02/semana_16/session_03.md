# Semana 16 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Prediciendo los Ingresos de una aerolínea
Quieres predecir los Ingresos por Pasajeros ($Y$, en millones) de una aerolínea basándote en el PIB Nacional ($X$, en miles de millones). Corres un modelo de regresión en Excel ( usando la herramienta Análisis de Datos) y obtienes estos resultados:

* **Intercepto ($\beta_0$):** 50
* **Coeficiente del PIB ($\beta_1$):** 2.5
* **p-value del coeficiente:** 0.01
* **R-cuadrado ($R^2$):** 0.78

**Interpretación financiera:**
1. **El p-value (0.01)** es menor a 0.05. El PIB es un predictor estadísticamente significativo.
2. **El Coeficiente (2.5):** Por cada mil millones de dólares que crezca el PIB, los ingresos de la aerolínea subirán 2.5 millones.
3. **El Intercepto (50):** Si el PIB fuera cero (sólo teoría), la aerolínea tendría ingresos base de 50 millones.
4. **R-cuadrado (0.78):** El 78% de los ingresos de la aerolínea se explican por el PIB. El restante 22% se debe a factores no contemplados (precio del petróleo, huelgas, tipo de cambio, etc.).

---

## Segundo ejercicio: interpretar una salida de regresión completa

Un analista estima el siguiente modelo para las ventas trimestrales de una cadena de retail:

$$\text{Ventas} = \beta_0 + \beta_1 (\text{PIB}) + \beta_2 (\text{Publicidad}) + \beta_3 (\text{Tiendas})$$

| Variable | Coeficiente | Error estándar | Estadístico $t$ | $p$-value |
|---|---|---|---|---|
| Intercepto | 120.0 | 45.0 | 2.67 | 0.012 |
| PIB (% crec.) | 8.5 | 2.1 | **4.05** | 0.000 |
| Publicidad ($M) | 3.2 | 1.4 | **2.29** | 0.029 |
| Nº de tiendas | 0.9 | 1.8 | **0.50** | 0.621 |

$R^2 = 0.78$ · $R^2$ ajustado $= 0.75$ · $F = 26.4$ ($p < 0.001$) · $n = 40$

**a) ¿Qué variables son significativas?**

La regla rápida: **$|t| > 2$** equivale aproximadamente a $p < 0.05$ con muestras razonables.

* **PIB** ($t = 4.05$): altamente significativa.
* **Publicidad** ($t = 2.29$): significativa al 5 %.
* **Número de tiendas** ($t = 0.50$, $p = 0.62$): **no significativa**.

**b) ¿Por qué el número de tiendas no sale significativo, si obviamente importa?**

Casi con seguridad, por **multicolinealidad**: el número de tiendas está muy correlacionado con
el gasto en publicidad (más tiendas → más publicidad). Cuando dos regresores se mueven juntos,
el modelo no puede separar sus efectos y **infla los errores estándar de ambos**.

Síntomas de multicolinealidad: $R^2$ alto con coeficientes individualmente no significativos, y
un estadístico $F$ muy significativo mientras los $t$ no lo son. Aquí el $F = 26.4$ dice que el
modelo **en conjunto** explica muchísimo, aunque una variable aislada no destaque.

**c) $R^2$ frente a $R^2$ ajustado**

El $R^2$ **siempre sube** al añadir variables, aunque sean ruido puro. El **ajustado** penaliza
por el número de regresores:

$$R^2_{aj} = 1 - (1 - R^2)\frac{n-1}{n-k-1}$$

Si al añadir una variable el $R^2$ sube pero el **ajustado baja**, esa variable **no aporta**.

**d) La predicción**

Con PIB creciendo 3 %, publicidad de $\$20$ M y 150 tiendas:

$$\hat{Y} = 120 + 8.5(3) + 3.2(20) + 0.9(150) = 120 + 25.5 + 64 + 135 = \mathbf{344.5}$$

Pero un $R^2$ de 0,78 significa que el **22 % de la variación queda sin explicar**. La
predicción es el centro de un intervalo, no una certeza. Reportar "344,5" sin su intervalo de
confianza es transmitir una precisión falsa.

---

## Los supuestos que hacen válida una regresión

Un modelo puede tener un $R^2$ espectacular y ser completamente inválido. Los supuestos que
hay que comprobar:

| Supuesto | Qué pasa si falla | Cómo detectarlo |
|---|---|---|
| **Linealidad** | El modelo está mal especificado | Gráfico de residuos vs. valores ajustados |
| **Independencia de los errores** | Errores estándar subestimados → falsa significancia | Durbin-Watson (crítico en series temporales) |
| **Homocedasticidad** | Inferencia inválida | Residuos en forma de embudo |
| **Normalidad de los residuos** | Intervalos de confianza incorrectos | Gráfico Q-Q |
| **Sin multicolinealidad** | Coeficientes inestables | VIF > 10 |

!!! danger "Correlación no es causalidad — y en finanzas cuesta dinero"
    Tres trampas concretas:

    * **Regresión espuria.** Dos series con tendencia creciente correlacionan aunque no tengan
      ninguna relación. El caso clásico: el consumo de queso *mozzarella* correlaciona al 95 %
      con los doctorados en ingeniería civil. En series temporales financieras, **siempre**
      trabaja con retornos o diferencias, no con niveles.
    * **Variable omitida.** Si falta un factor que afecta a ambas variables, el coeficiente
      estimado recoge su efecto y está sesgado.
    * **Sobreajuste (*overfitting*).** Con suficientes variables se explica el pasado a la
      perfección y no se predice nada. La prueba real de un modelo es su desempeño **fuera de
      la muestra**, no su $R^2$.

    En finanzas cuantitativas esto tiene nombre propio: *data mining*. Si pruebas 100
    estrategias sobre datos históricos, unas 5 parecerán significativas al 5 % **por puro
    azar**. Es exactamente el mismo problema de tasa base del ejercicio de la Semana 15.

---
