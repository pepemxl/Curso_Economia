# Semana 28 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: La matemática de un Bono en el Mercado Secundario
Compraste un bono del gobierno hace 2 años. El Bono tiene un **Valor Nominal de $1,000** y paga un **cupón (interés) fijo del 5% anual** ($50 al año) hasta su vencimiento en 3 años más.

Hoy, el Banco Central ha subido las tasas de interés, y los bonos nuevos de la misma duración pagan un **7%**. Quieres vender tu bono en el mercado secundario. ¿A qué precio lo puedes vender?

**Cálculo Matemático (Aplicando Valor Presente de la Semana 11):**
Nadie te pagará $1,000 por un bono que rinde $50 si pueden comprar uno nuevo que rinde $70. El precio de tu bono debe bajar hasta que su rendimiento real sea del 7%. Descontamos los flujos al 7%:
* Año 1: $50 / (1.07)^1 = $46.73
* Año 2: $50 / (1.07)^2 = $43.67
* Año 3: ($50 + $1,000 Valor Nominal) / (1.07)^3 = $1,050 / 1.225 = $857.14
* **Precio de Mercado = $46.73 + $43.67 + $857.14 = $947.54**

*Conclusión:* Tu bono cayó de $1,000 a **$947.54** por culpa de la subida de tasas (política monetaria macroeconómica afectando el mercado de renta fija).

---

## Segundo ejercicio: duración, o cuánto duele una subida de tasas

El bono anterior cayó de $\$1,000$ a $\$947.54$ (−5,2 %) ante una subida de 2 puntos. ¿Habría
caído lo mismo un bono a 20 años? No, ni de lejos. La medida que lo cuantifica es la
**duración**.

**Duración de Macaulay:** el plazo medio ponderado de los flujos, usando su valor presente como
ponderador.

| Año | Flujo | VP al 7 % | Peso | Año × Peso |
|---|---|---|---|---|
| 1 | 50 | 46.73 | 0.0493 | 0.0493 |
| 2 | 50 | 43.67 | 0.0461 | 0.0922 |
| 3 | 1,050 | 857.14 | 0.9046 | 2.7138 |
| | | **947.54** | **1.0000** | **2.855** |

$$D_{Macaulay} = \mathbf{2.855 \text{ años}}$$

**Duración modificada** — la que mide sensibilidad:

$$D_{mod} = \frac{D_{Macaulay}}{1 + YTM} = \frac{2.855}{1.07} = \mathbf{2.668}$$

**Regla de aproximación:**

$$\%\Delta P \approx -D_{mod} \times \Delta YTM$$

Si las tasas suben 1 punto más (del 7 % al 8 %):

$$\%\Delta P \approx -2.668 \times 0.01 = -2.67\%$$

Precio estimado: $947.54 \times (1 - 0.0267) = \$922.2$. El valor exacto descontando al 8 % es
$\$922.69$ — la aproximación es excelente para movimientos pequeños.

**Comparación por plazo** (cupón 5 %, YTM 7 %, subida de 100 pb):

| Vencimiento | Duración modificada | Caída de precio |
|---|---|---|
| 3 años | 2.67 | −2,7 % |
| 10 años | 7.02 | −7,0 % |
| 30 años | 12.47 | −12,5 % |

**El bono a 30 años cae casi cinco veces más que el de 3 años ante el mismo movimiento.** Esta
es la razón cuantitativa de que los fondos de bonos de largo plazo perdieran dos dígitos en
2022, y del colapso de Silicon Valley Bank en 2023: tenía su cartera en bonos largos comprados
con tasas cerca de cero.

!!! tip "Convexidad: la corrección de segundo orden"
    La duración es una aproximación **lineal**; la relación precio-tasa es en realidad una curva.
    La **convexidad** mide esa curvatura:

    $$\%\Delta P \approx -D_{mod}\Delta y + \frac{1}{2}C(\Delta y)^2$$

    La convexidad es **positiva** en bonos normales, y es una buena noticia para el tenedor: los
    precios suben **más** de lo que predice la duración cuando las tasas bajan, y caen **menos**
    cuando suben. Por eso, entre dos bonos con la misma duración, se prefiere el de mayor
    convexidad.

    (Las hipotecas titulizadas tienen convexidad **negativa**: cuando las tasas bajan, los
    deudores refinancian y el bono se cancela justo cuando más valdría. Ese fue uno de los
    mecanismos que amplificaron la crisis de 2008.)

---

## Tercer ejercicio: rendimiento corriente, YTM y rendimiento total

Tres formas de medir "lo que rinde un bono", y la mayoría de la gente confunde las dos primeras.

Sobre el mismo bono comprado hoy a $\$947.54$:

**1. Rendimiento corriente**

$$\frac{\text{Cupón anual}}{\text{Precio}} = \frac{50}{947.54} = \mathbf{5.28\%}$$

Solo mira el cupón. **Ignora la ganancia de capital** de los $\$52.46$ que recuperarás al
vencimiento (de 947.54 a 1,000).

**2. Rendimiento al vencimiento (YTM)**

Es la TIR del bono: la tasa que iguala el precio con el valor presente de todos los flujos.
Aquí, por construcción, es el **7 %**. Incluye cupones **y** ganancia de capital.

**3. Rendimiento total realizado**

Es lo que **de verdad** obtienes, y depende de algo que el YTM asume sin decirlo: **que puedes
reinvertir cada cupón al propio YTM**.

Si los cupones se reinvierten al 7 %:

$$50(1.07)^2 + 50(1.07) + 1{,}050 = 57.25 + 53.50 + 1{,}050 = \$1{,}160.75$$

$$\text{Rendimiento realizado} = \left(\frac{1{,}160.75}{947.54}\right)^{1/3} - 1 = \mathbf{7.00\%} \;✓$$

Pero si las tasas caen y solo puedes reinvertir al 3 %:

$$50(1.03)^2 + 50(1.03) + 1{,}050 = 53.05 + 51.50 + 1{,}050 = \$1{,}154.55$$

$$\text{Rendimiento realizado} = \left(\frac{1{,}154.55}{947.54}\right)^{1/3} - 1 = \mathbf{6.81\%}$$

**El YTM prometía 7 % y obtuviste 6,81 %.** Es el **riesgo de reinversión**, la contrapartida
del riesgo de precio: cuando las tasas bajan, tu bono se revaloriza pero tus cupones rinden
menos. Un bono cupón cero no tiene riesgo de reinversión, porque no paga cupones — por eso es el
instrumento preferido para calzar un pasivo con fecha cierta.

---
