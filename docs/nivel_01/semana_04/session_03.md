# Semana 4 · Sesión 3: Aplicación Práctica

## 7. Ejercicio Práctico: Deflactando el PIB
El país de "MacroLandia" produce solo dos bienes: Manzanas y Computadoras.

* **Año Base (2010):** 
  * Manzanas: 100 producidas a $1 c/u. (Valor = $100)
  * Computadoras: 10 producidas a $100 c/u. (Valor = $1,000)
  * PIB Nominal 2010 = $1,100
* **Año 2020:** 
  * Manzanas: 120 producidas a $2 c/u. (Valor = $240)
  * Computadoras: 12 producidas a $150 c/u. (Valor = $1,800)
  * PIB Nominal 2020 = $2,040

A simple vista, MacroLandia dice: "¡Nuestro PIB casi se duplicó! Pasamos de $1,100 a $2,040. ¡Somos gigantes de la economía!". 
* **Pero... ¿de verdad produjeron mucho más?** Solo produjeron un 20% más de manzanas y un 20% más de computadoras.

**Cálculo del PIB Real 2020 (usando precios del año base 2010):**
* Manzanas: 120 (cantidad actual) x $1 (precio base) = $120
* Computadoras: 12 (cantidad actual) x $100 (precio base) = $1,200
* **PIB Real 2020 = $1,320**

*Interpretación Financiera:* El PIB Nominal creció un ~85%, pero el PIB Real (el verdadero crecimiento de bienes y servicios que la gente puede disfrutar) solo creció un 20%. El resto de la ilusión (el 65% restante) fue puramente inflación de precios.

---

## Segundo ejercicio: construir el IPC y medir la inflación

MacroLandia define su canasta familiar con las cantidades que consume un hogar **típico del año
base**, y esas cantidades **no cambian** aunque cambien los precios.

**Canasta fija (cantidades del año base 2010):** 200 manzanas y 5 computadoras.

| Bien | Cantidad fija | Precio 2010 | Precio 2020 |
|---|---|---|---|
| Manzanas | 200 | $1 | $2 |
| Computadoras | 5 | $100 | $150 |

**Paso 1 — Costo de la canasta en cada año**

$$\text{Costo}_{2010} = 200(1) + 5(100) = 200 + 500 = \$700$$

$$\text{Costo}_{2020} = 200(2) + 5(150) = 400 + 750 = \$1{,}150$$

**Paso 2 — Índice de Precios al Consumidor**

$$IPC_t = \frac{\text{Costo de la canasta en } t}{\text{Costo de la canasta en el año base}} \times 100$$

$$IPC_{2010} = \frac{700}{700} \times 100 = 100 \qquad IPC_{2020} = \frac{1{,}150}{700} \times 100 = 164.3$$

**Paso 3 — Inflación acumulada de la década**

$$\pi = \frac{164.3 - 100}{100} = \mathbf{64.3\%}$$

**Paso 4 — Comparación con el deflactor**

Del ejercicio anterior teníamos $PIB_{nominal}^{2020} = 2{,}040$ y $PIB_{real}^{2020} = 1{,}320$:

$$\text{Deflactor}_{2020} = \frac{2{,}040}{1{,}320} \times 100 = 154.5$$

$$\pi_{deflactor} = \mathbf{54.5\%}$$

**Dos medidas de la misma inflación, con 10 puntos de diferencia.** ¿Por qué?

Porque **ponderan distinto**. El IPC usa las cantidades **fijas de 2010** (200 manzanas, 5
computadoras); el deflactor usa las cantidades **efectivamente producidas en 2020** (120
manzanas, 12 computadoras). Como la producción se desplazó hacia las computadoras —cuyo precio
subió un 50 %, menos que el 100 % de las manzanas—, el deflactor recoge una inflación menor.

Esta es exactamente la diferencia entre un índice de **Laspeyres** (canasta fija del año base,
el IPC) y uno de **Paasche** (canasta del año corriente, el deflactor). El primero tiende a
sobreestimar la inflación; el segundo, a subestimarla.

---

## Tercer ejercicio: tasa de desempleo y participación

MacroLandia publica los siguientes datos de su población:

* Población total: **1,000,000**
* Menores de 16 años e institucionalizados: **250,000**
* Ocupados: **480,000**
* Desempleados que buscan trabajo activamente: **60,000**
* Estudiantes, jubilados y amas de casa que no buscan trabajo: **210,000**

**Paso 1 — Población en edad de trabajar**

$$1{,}000{,}000 - 250{,}000 = 750{,}000$$

**Paso 2 — Fuerza laboral (población económicamente activa)**

$$FL = \text{Ocupados} + \text{Desempleados} = 480{,}000 + 60{,}000 = 540{,}000$$

Comprobación: $540{,}000 + 210{,}000 = 750{,}000$ ✓

**Paso 3 — Tasa de desempleo**

$$u = \frac{\text{Desempleados}}{\text{Fuerza laboral}} = \frac{60{,}000}{540{,}000} = \mathbf{11.1\%}$$

Nótese el denominador: es la **fuerza laboral**, no la población total ni la población en edad
de trabajar. Dividir entre 750,000 daría un 8 % engañosamente bajo.

**Paso 4 — Tasa de participación**

$$\text{Participación} = \frac{540{,}000}{750{,}000} = \mathbf{72\%}$$

!!! danger "La trampa del trabajador desalentado"
    Supongamos que al año siguiente 40,000 desempleados **se rinden** y dejan de buscar trabajo.
    No encontraron nada y se retiran del mercado. Nada más cambia.

    * Nueva fuerza laboral: $480{,}000 + 20{,}000 = 500{,}000$
    * Nueva tasa de desempleo: $20{,}000/500{,}000 = \mathbf{4\%}$

    **El desempleo se desplomó del 11,1 % al 4 % sin que se creara ni un solo empleo.** Al
    contrario: la situación empeoró.

    Por eso nunca se lee la tasa de desempleo aislada. Se contrasta siempre con la **tasa de
    participación** (aquí caería del 72 % al 66,7 %, delatando el problema) y con el número
    absoluto de ocupados. Un analista que solo mira el titular del desempleo se equivocará
    sistemáticamente en los puntos de giro del ciclo.

---
