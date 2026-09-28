# Semana 5 · Sesión 2: Profundización

## 4. El Equilibrio Macroeconómico
El equilibrio es la intersección entre la curva de Demanda Agregada (DA) y la Oferta Agregada a Corto Plazo (OACP).
* **Brecha Recesiva:** Si el PIB de equilibrio es menor al PIB Potencial (OALP). Hay desempleo cíclico; la economía está funcionando por debajo de su capacidad.
* **Brecha Inflacionaria:** Si el PIB de equilibrio es mayor al PIB Potencial. La economía está sobrecalentada. Las empresas están trabajando horas extra, y el resultado normal es que los precios suban (Inflación).

---

## 5. El Multiplicador Keynesiano (y el Efecto Acelerador)
John Maynard Keynes descubrió que cuando hay una brecha recesaria, el gobierno puede inyectar dinero para reactivarla. Pero el gasto del gobierno no genera solo un dólar de crecimiento; **se multiplica**.

**El Efecto Dominó:**
1. El gobierno construye un puente y paga $1,000 a los obreros.
2. Los obreros gastan parte de ese $1,000 en el supermercado (consumo).
3. El cajero del supermercado recibe ese salario, y a su vez va al cine (consumo).
4. El dueño del cine compra insumos, y gasta su ganancia en una cena.

En cada paso, **una fracción del ingreso se gasta y el resto se ahorra o se paga en impuestos**. La fracción del ingreso adicional que se gasta en consumo se llama **Propensión Marginal a Consumir (PMgC)**.

**Fórmula del Multiplicador ($k$):**
$$ k = \frac{1}{1 - PMgC} $$

> **💥 Impacto Financiero:** Si la PMgC es 0.8 (por cada dólar extra que gana la gente, gasta 80 centavos y ahorra 20), el multiplicador es: $1 / (1 - 0.8) = 5$.
> Esto significa que si el gobierno aumenta su gasto en $1,000 millones, ¡el crecimiento real del PIB será de $5,000 millones a corto plazo!
> En el mundane financiero: Los analistas usan el multiplicador para calibrar el impacto del gasto fiscal en las ventas de las empresas. Inversionistas en sectores cíclicos (construcción, retail) compran acciones de empresas proveedoras esperando que el multiplicador llegue a sus cuentas de resultados.

**Efecto expulsión (Crowding out) - La limitación del Multiplicador:**
En la realidad mundial, no existe un multiplicador infinito. Si el gobierno gasta mucho, necesita endeudarse. Para endeudarse emite bonos. Si emite muchos bonos, las tasas de interés suben (alta demanda de préstamos). Tasas más altas desincentivan la inversión privada (I). Por tanto, el aumento en "G" se compensa con una caída en "I", reduciendo el tamaño del multiplicador keynesiano.

---

## Por qué la Oferta Agregada cambia de forma con el horizonte

La distinción entre corto y largo plazo es lo que separa el análisis keynesiano del clásico, y
explica casi todos los debates de política económica que leerás en la prensa.

**Oferta Agregada de Corto Plazo (OACP): pendiente positiva.** Si suben los precios de venta
pero los salarios y los contratos de insumos están **pactados de antemano**, el margen de la
empresa se ensancha y le conviene producir más. Las tres explicaciones habituales:

1. **Salarios rígidos:** los convenios colectivos fijan el salario nominal por 1 o 2 años.
2. **Precios rígidos (*menu costs*):** cambiar catálogos, etiquetas y contratos tiene un costo,
   así que las empresas ajustan con retraso.
3. **Percepciones erróneas:** el productor confunde una subida general de precios con una
   subida del precio *de su* producto, y expande la producción por error.

**Oferta Agregada de Largo Plazo (OALP): vertical.** Con el tiempo, los salarios se renegocian,
los contratos se actualizan y las percepciones se corrigen. La producción vuelve a depender
únicamente de los factores reales —capital, trabajo, tecnología, instituciones— y no del nivel
de precios. La OALP se sitúa en el **PIB potencial**.

**La consecuencia es la que importa:** una política de demanda (fiscal o monetaria) puede
aumentar el PIB **a corto plazo**, pero a largo plazo solo mueve el nivel de precios. Para
elevar el PIB potencial hay que desplazar la OALP a la derecha, y eso exige políticas de
oferta: inversión en capital, educación, tecnología, instituciones que funcionen.

---

## Las expectativas: por qué la Curva de Phillips se rompe

En los años 60 parecía existir un menú estable: más inflación a cambio de menos desempleo. Los
gobiernos creyeron que podían elegir un punto de ese menú.

Friedman y Phelps advirtieron el fallo lógico, y los años 70 les dieron la razón. Si el gobierno
genera inflación sistemáticamente para bajar el desempleo, **los trabajadores aprenden** y
exigen subidas salariales que la anticipan. El truco deja de funcionar:

$$u = u_n - \alpha(\pi - \pi^e)$$

El desempleo solo baja de su tasa natural $u_n$ cuando la inflación **sorprende**
($\pi > \pi^e$). Y no se puede sorprender a la gente indefinidamente.

El resultado fue la **estanflación**: alta inflación *y* alto desempleo a la vez, algo que la
Curva de Phillips original declaraba imposible. La Curva de Phillips de largo plazo es
**vertical** en $u_n$.

!!! tip "Por qué esto explica el comportamiento de los bancos centrales hoy"
    De aquí salen dos pilares de la política monetaria moderna:

    * **La credibilidad es un activo.** Si el banco central es creíble, $\pi^e$ permanece
      anclada y desinflar cuesta poco desempleo. Si no lo es, cada punto de inflación que
      quiera bajar le costará mucho más producto — es el llamado *ratio de sacrificio*.
    * **La independencia del banco central.** Un gobierno tiene incentivo a generar inflación
      sorpresa antes de una elección. Si los agentes lo saben, la inflación esperada sube sin
      que nadie gane nada. Sacar la decisión del ciclo político resuelve el problema.

    Cuando en 2022 los bancos centrales insistían en que las expectativas seguían "ancladas",
    estaban hablando precisamente de $\pi^e$ en esta ecuación.

---

## El multiplicador realista

La fórmula $k = 1/(1 - PMgC)$ es el caso más simple posible: economía cerrada, sin impuestos.
Cada supuesto que se relaja **reduce** el multiplicador, porque introduce una nueva fuga del
flujo circular:

$$k = \frac{1}{1 - PMgC(1 - t) + m}$$

donde $t$ es la tasa impositiva marginal y $m$ la propensión marginal a importar.

Con $PMgC = 0.8$, $t = 0.25$ y $m = 0.15$:

$$k = \frac{1}{1 - 0.8(0.75) + 0.15} = \frac{1}{1 - 0.6 + 0.15} = \frac{1}{0.55} = 1.82$$

**El multiplicador cae de 5 a 1,82.** El estímulo sigue funcionando, pero mucho menos de lo que
promete el modelo de manual. Las tres fugas son claras: lo que se ahorra, lo que se va en
impuestos y lo que se gasta en productos importados no vuelve al circuito doméstico.

A esto se añaden dos límites más:

* **Efecto expulsión (*crowding out*)**, que ya vimos: el endeudamiento público sube las tasas
  y desplaza inversión privada. Es más severo cuanto más cerca esté la economía del pleno
  empleo, y casi inexistente en una recesión profunda con tasas en cero.
* **Equivalencia ricardiana:** si los hogares anticipan que el gasto de hoy son impuestos de
  mañana, ahorran el estímulo en lugar de gastarlo. En su forma pura es poco realista, pero el
  efecto parcial existe.

**Estimaciones empíricas:** los multiplicadores fiscales reales suelen estimarse entre **0,5 y
1,5**, con valores más altos en recesión, en economías cerradas y cuando el estímulo es
inversión pública en lugar de transferencias.

---
