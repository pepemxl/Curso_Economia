# Semana 5 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Choques de Mercado y el Multiplicador

**Escenario A: Choque Adverso de Oferta (Estanflación)**
La economía de "Solaria" está en equilibrio. De repente, una guerra internacional triplica el precio del petróleo (insumo clave).
* **Análisis DA-OA:** El costo de producción para casi todas las empresas sube drásticamente. La curva de Oferta Agregada a Corto Plazo (OACP) se desplaza hacia la izquierda.
* **Resultado final:** Disminución del PIB (contracción económica) y aumento del nivel general de precios (inflación). A este fenómeno se le llama **Estanflación** (Estancamiento + Inflación).

**Escenario B: Aplicación del Multiplicador**
La economía de Solaria entra en recesión. El gobierno decide aplicar un estímulo de $500 millones construyendo hospitales. En Solaria, la propensión marginal a consumir ($PMgC$) es del $0.75$ (75%).
1. **Cálculo del multiplicador ($k$):**
   $$ k = \frac{1}{1 - 0.75} = \frac{1}{0.25} = 4 $$
2. **Impacto en el PIB:**
   $$ \Delta PIB = k \times \Delta Gasto = 4 \times \$500 millones = \$2,000 \text{ millones} $$
*Conclusión:* El estímulo inicial de $500 millones del gobierno se traducirá, a corto plazo, en un aumento esperado de $2,000 millones en el PIB. 

---

## Tercer ejercicio: el multiplicador con impuestos y comercio exterior

El gobierno de Solaria descubre que su estímulo de $500 millones no generó los $2,000 millones
prometidos. El ministerio revisa los parámetros reales del país:

* $PMgC = 0.75$
* Tasa impositiva marginal $t = 0.20$
* Propensión marginal a importar $m = 0.12$

**Paso 1 — Multiplicador realista**

$$k = \frac{1}{1 - PMgC(1-t) + m} = \frac{1}{1 - 0.75(0.80) + 0.12}$$

$$k = \frac{1}{1 - 0.60 + 0.12} = \frac{1}{0.52} = \mathbf{1.92}$$

**Paso 2 — Impacto real sobre el PIB**

$$\Delta PIB = 1.92 \times \$500 = \mathbf{\$962 \text{ millones}}$$

Frente a los $2,000 millones que predecía el modelo simple: **menos de la mitad**.

**Paso 3 — ¿A dónde se fue la diferencia?**

De cada peso adicional de ingreso que reciben los hogares de Solaria:

| Destino | Cálculo | Fuga |
|---|---|---|
| Impuestos | $1 \times 0.20$ | $0.20 |
| Ahorro | $0.80 \times 0.25$ | $0.20 |
| Importaciones | | $0.12 |
| **Total de fugas** | | **$0.52** |
| Se re-gasta en la economía local | | $0.48 |

**Solo 48 centavos de cada peso vuelven al circuito doméstico.** Ahí está todo el misterio.

---

## Cuarto ejercicio: elegir el instrumento fiscal

El gobierno tiene $\$400$ millones y debe decidir cómo usarlos. Con $PMgC = 0.75$ y el
multiplicador simple ($k_G = 4$), compara tres opciones:

**Opción A — Gasto público directo (construir hospitales)**

$$\Delta PIB = 4 \times 400 = \$1{,}600 \text{ millones}$$

Los $400 entran **completos** al flujo: el gobierno los gasta y se convierten en ingreso de
constructoras, proveedores y trabajadores.

**Opción B — Recorte de impuestos de $400 millones**

$$k_T = \frac{PMgC}{1 - PMgC} = \frac{0.75}{0.25} = 3$$

$$\Delta PIB = 3 \times 400 = \$1{,}200 \text{ millones}$$

Menos potente, y la razón es la misma de siempre: el contribuyente **ahorra** el 25 % de lo que
recibe. Solo $300 de los $400 entran realmente a la economía en la primera ronda.

**Opción C — Transferencias a hogares de renta baja**

Mismo multiplicador que el recorte de impuestos en el modelo estándar, **pero** los hogares de
renta baja tienen una $PMgC$ mucho más alta —cercana a 0.95, porque gastan casi todo lo que
reciben—. Con $PMgC = 0.95$:

$$k = \frac{0.95}{0.05} = 19 \;\Rightarrow\; \text{efecto muy superior}$$

En la práctica el efecto se modera por las mismas fugas del ejercicio anterior, pero la
conclusión se sostiene: **quién recibe el dinero importa tanto como cuánto se reparte**.

| Opción | Multiplicador | Impacto | Velocidad |
|---|---|---|---|
| **A** Gasto en infraestructura | 4.0 | $1,600 M | Lenta (proyectos tardan) |
| **B** Recorte de impuestos | 3.0 | $1,200 M | Media |
| **C** Transferencias focalizadas | Alto | Alto | **Inmediata** |

!!! tip "El dilema real de la política fiscal"
    La infraestructura tiene el multiplicador más alto **y** eleva el PIB potencial a largo
    plazo (desplaza la OALP). Su problema son los **rezagos**: entre que se aprueba un proyecto
    y se mueve la primera pala pueden pasar dos años, y para entonces la recesión puede haber
    terminado — con lo que el estímulo llega justo cuando la economía ya está sobrecalentada.

    Las transferencias actúan en semanas, pero no dejan nada instalado.

    De ahí la importancia de los **estabilizadores automáticos** (seguro de desempleo,
    impuestos progresivos): actúan **sin necesidad de aprobación política**, en el momento
    exacto en que se necesitan y con la intensidad justa.

---
