# Semana 1 · Sesión 3: Aplicación Práctica

## 7. Ejercicio Práctico: El mercado de los "Smartwatches"

Imaginemos el mercado de relojes inteligentes. Tenemos dos ecuaciones lineales:

* **Función de Demanda:** $Q_d = 1000 - 5P$ *(Donde $P$ es el precio y $Q$ es la cantidad)*
* **Función de Oferta:** $Q_s = -200 + 10P$

**Paso 1: Encontrar el precio y cantidad de equilibrio.**
Para hallar el equilibrio, igualamos ambas ecuaciones ( $Q_d = Q_s$ ):

$$1000 - 5P = -200 + 10P$$

$$1000 + 200 = 10P + 5P$$

$$1200 = 15P$$

**Precio de equilibrio ($P^*$) = 80**

**Paso 2: Encontrar la cantidad de equilibrio.**
Sustituimos $P = 80$ en cualquiera de las ecuaciones. Usamos la de demanda:

$$Q_d = 1000 - 5(80)$$

$$Q_d = 1000 - 400$$

**Cantidad de equilibrio ($Q^*$) = 600**

*Interpretación:* En este mercado, si el precio de un Smartwatch es de 80, se producirán y venderán exactamente 600 unidades. No habrá sobrantes. Si el precio fuera de 100, $Q_d$ sería 500 y $Q_s$ sería 800, creándose un excedente de 300 relojes que las tiendas no podrían vender, obligando a los fabricantes a bajar el precio hacia los 80.

---

## Segundo ejercicio: el efecto de un impuesto

Volvamos al mercado de Smartwatches, pero ahora el gobierno grava cada unidad vendida con un
**impuesto específico de $15** que debe pagar el productor.

* Demanda: $Q_d = 1000 - 5P$
* Oferta original: $Q_s = -200 + 10P$

**Paso 1 — ¿Qué le pasa a la oferta?**

El productor necesita recibir $15 más por unidad para estar igual de dispuesto a producir. Si
antes ofrecía según el precio $P$, ahora lo hace según el precio que efectivamente le queda,
$P - 15$:

$$Q_s^{imp} = -200 + 10(P - 15) = -200 + 10P - 150 = -350 + 10P$$

La curva de oferta **se desplaza a la izquierda**: a cualquier precio se ofrece menos.

**Paso 2 — Nuevo equilibrio**

$$1000 - 5P = -350 + 10P$$

$$1350 = 15P \Longrightarrow P^* = 90$$

$$Q^* = 1000 - 5(90) = 550$$

**Paso 3 — ¿Quién paga realmente el impuesto?**

Aquí está la parte que sorprende a todo el mundo. El impuesto lo *entrega al fisco* el
productor, pero el peso económico se reparte:

| | Antes | Después | Diferencia |
|---|---|---|---|
| Precio que paga el consumidor | 80 | **90** | +10 |
| Precio que recibe el productor | 80 | $90 - 15 = $ **75** | −5 |
| Cantidad de equilibrio | 600 | **550** | −50 |

**El consumidor absorbe $10 de los $15 (67 %) y el productor solo $5 (33 %)**, aunque la ley
diga que el impuesto es "del productor".

**Paso 4 — Recaudación y pérdida de eficiencia**

$$\text{Recaudación} = 15 \times 550 = \$8{,}250$$

Pero se dejaron de vender 50 unidades que antes sí se intercambiaban. Esas transacciones
generaban valor para ambas partes y ya no ocurren: es la **pérdida de eficiencia**
(*deadweight loss*), el área del triángulo entre ambas curvas:

$$DWL = \frac{1}{2} \times 15 \times 50 = \$375$$

!!! tip "La regla de la incidencia fiscal"
    **El lado del mercado más inelástico soporta la mayor parte del impuesto.**

    Aquí la demanda (pendiente $-5$) es menos sensible al precio que la oferta (pendiente
    $+10$), así que los consumidores cargan con la mayor parte. Es exactamente por eso que los
    gobiernos gravan tabaco, alcohol y combustibles: su demanda es muy inelástica, así que
    recaudan mucho y la cantidad apenas cae.

    Y funciona igual al revés: en un mercado laboral donde la oferta de trabajo es inelástica,
    las contribuciones "del empleador" acaban pagándolas los trabajadores vía salarios más bajos.

---

## Errores frecuentes en este tema

Antes de pasar a la sesión 4, revisa que no estés cometiendo ninguno de estos:

1. **Confundir el eje de la gráfica con el de las ecuaciones.** En economía, por convención
   histórica de Marshall, el **precio va en el eje vertical** aunque sea la variable
   independiente. Al despejar $P$ de $Q_d = 1000 - 5P$ obtienes $P = 200 - Q/5$: esa es la
   forma que grafica.
2. **Olvidar comprobar el resultado en la otra ecuación.** Si sustituyes $P^*$ en la demanda y
   en la oferta y no da lo mismo, hay un error aritmético. Es una comprobación gratis.
3. **Dar cantidades negativas por válidas.** La oferta $Q_s = -200 + 10P$ solo tiene sentido
   económico si $P \ge 20$; por debajo de ese precio ningún productor entra al mercado.
4. **Tratar un cambio de precio como desplazamiento.** Si lo único que cambió es el precio del
   propio bien, es un **movimiento** sobre la curva, no un desplazamiento. Repasa la sesión 2.
5. **Sumar mal las elasticidades del impuesto.** El impuesto desplaza la curva **verticalmente**
   en el monto del impuesto, no horizontalmente.

---
