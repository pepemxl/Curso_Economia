# Semana 30 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: El "Put Protector" (Opciones como Seguro)
Posees 100 acciones de "TechCorp" que cotizan a $150. Tienes miedo de que caigan antes de fin de año por la subida de tasas, pero no quieres venderlas hoy (para no pagar impuestos por ganancias).

**La jugada con Opciones:**
Compras un **Put** con un Strike (precio de venta garantizado) de $140, pagando una **Prima de $5 por acción**. Costo total del "seguro": $500 (100 x $5).

**Escenarios al Vencimiento:**
1. **La acción sube a $180:** El Put expira sin valor (pierdes la prima de $500). Pero tus acciones valen $18,000. Ganancia neta: $3,000 - $500 = $2,500. El seguro te costó $500, pero protegiste tu ganancia al alza.
2. **La acción se desploma a $100:** Activas tu Put. Tienes el derecho de vender tus acciones a $140, aunque en el mercado valgan $100.
   * Sin el Put: Perderías $5,000 (de $150 a $100).
   * Con el Put: Pierdes ($150 - $140) + $5 de prima = $15 por acción. Pérdida total $1,500. *El Put limitó tu pérdida matemáticamente, salvándote de la catástrofe.*

---

## Segundo ejercicio: el *covered call* y la venta de volatilidad

La estrategia opuesta al *put* protector. Sigues teniendo tus 100 acciones de TechCorp a
$\$150$, pero ahora crees que el precio **se quedará estable** y quieres generar ingresos.

**La jugada:** vendes un **Call** con strike de $\$160$, cobrando una prima de $\$4$ por
acción. Ingresas **$\$400$** hoy.

**Escenarios al vencimiento:**

| Precio final | Valor de las acciones | Resultado del Call vendido | **Total** |
|---|---|---|---|
| $130 | 13,000 (−2,000) | +400 (expira sin valor) | **−1,600** |
| $150 | 15,000 (0) | +400 | **+400** |
| $160 | 16,000 (+1,000) | +400 | **+1,400** |
| $180 | 16,000 (te ejercen a 160) | +400 − 2,000 | **+1,400** |
| $220 | 16,000 (te ejercen a 160) | +400 − 6,000 | **+1,400** |

**El perfil es asimétrico y en tu contra por arriba:** tu ganancia queda **topada en $\$1,400$**
por mucho que suba la acción, mientras que la pérdida por abajo sigue siendo casi ilimitada
(solo amortiguada por los $\$400$ de prima).

**Comparación de las tres posiciones:**

| Estrategia | Costo/ingreso | Protección a la baja | Participación al alza |
|---|---|---|---|
| **Solo acciones** | 0 | Ninguna | Ilimitada |
| **+ Put protector** | −$500 | **Fuerte** (desde $140) | Ilimitada − prima |
| **+ Call cubierto** | **+$400** | Mínima ($400) | **Topada en $160** |
| **Collar** (comprar put, vender call) | ≈ 0 | Fuerte | Topada |

El **collar** es la combinación favorita de los directivos con grandes paquetes accionarios:
financia el seguro vendiendo el potencial alcista, con costo neto cercano a cero.

!!! danger "Vender opciones descubiertas: la estrategia que ha quebrado más fondos"
    El *covered call* es prudente porque **posees las acciones** (por eso "cubierto"). Vender un
    call **sin tenerlas** (*naked call*) invierte completamente el perfil de riesgo:

    * Ganancia máxima: **la prima**, y nada más.
    * Pérdida máxima: **ilimitada**. Si la acción se dispara, tienes que comprarla al precio de
      mercado para entregarla al strike pactado.

    Es la aritmética que destruyó a los fondos de "recoger monedas delante de la apisonadora":
    ganan pequeñas primas mes tras mes durante años, y un solo movimiento extremo se lleva todas
    las ganancias acumuladas y el capital.

    En febrero de 2018, el índice de volatilidad VIX subió un 115 % en un día. Los productos que
    vendían volatilidad de forma sistemática perdieron el **96 % de su valor en una sesión**.
    Habían funcionado perfectamente durante años.

---

## Los cuatro derivados y para qué sirve cada uno

| Instrumento | Obligación o derecho | Se negocia en | Riesgo de contraparte | Uso típico |
|---|---|---|---|---|
| **Forward** | Obligación de ambas partes | OTC (a medida) | **Alto** | Cubrir tipo de cambio a medida |
| **Futuro** | Obligación de ambas partes | Bolsa (estandarizado) | Bajo (cámara + márgenes) | Cubrir materias primas, índices |
| **Opción** | **Derecho** del comprador, obligación del vendedor | Ambos | Según el mercado | Seguro asimétrico |
| **Swap** | Obligación de intercambiar flujos | OTC (con CCP tras 2008) | Medio | Transformar tasa variable en fija |

**La distinción que más se confunde: futuro frente a opción.**

* Con un **futuro** quedas obligado. Si cubres tu cosecha vendiendo futuros de trigo y el precio
  sube, **pierdes** en el futuro lo que ganas en la cosecha. Neutralizas: ni ganas ni pierdes.
* Con una **opción** compras un derecho. Si el precio sube, dejas expirar la opción y te quedas
  la subida, habiendo perdido solo la prima.

**Por eso la opción cuesta dinero por adelantado y el futuro no.** El futuro es simétrico y
gratuito; la opción es asimétrica y hay que pagar por esa asimetría. **No existe cobertura
gratuita que además te deje el potencial alcista.**

**Los cuatro determinantes del precio de una opción** (los inputs de Black-Scholes):

1. **Precio del subyacente** frente al strike — cuánto está *dentro del dinero*.
2. **Tiempo hasta el vencimiento** — más tiempo, más valor (más cosas pueden pasar).
3. **Volatilidad** — el factor dominante, y el único que no se observa directamente.
4. **Tasa de interés libre de riesgo** — efecto menor.

De ellos, la **volatilidad implícita** es la variable que realmente se negocia: cuando alguien
compra opciones no está apostando tanto a la dirección como a **cuánto se va a mover** el
subyacente. Esa es la mercancía que los VaR de la Semana 32 intentan medir.

---
