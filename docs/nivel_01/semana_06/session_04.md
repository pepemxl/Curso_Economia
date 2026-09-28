# Semana 6 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: La Curva de Rendimientos (Yield Curve) y la valuación de acciones
*Eres un analista de fondos de inversión evaluando el mercado de acciones y bonos de EE. UU.*

El gobierno (Fiscal) está gastando masivamente, generando inflación. Para combatirla, el Banco Central (Reserva Federal) sube agresivamente la tasa de interés de referencia a corto plazo (Política Monetaria Restringida).

**El impacto en la Curva de Rendimientos:**
En condiciones normales, cuanto más largo es el plazo de un bono, mayor es su interés (por el riesgo). Pero en este escenario, la subida abrupta de tasas a corto plazo por parte del Banco Central hace que los intereses a corto plazo sean más altos que los intereses a largo plazo (10 años). La Curva de Rendimientos se **invierte** (pendiente negativa hacia afuera).

**Impacto en Finanzas Corporativas (Ganancia/Advertencia):**
1. **Renta Variable (Acciones):** Una curva invertida indica que el mercado espera una recesión en 12-18 meses. Las acciones de empresas cíclicas (automotrices, banca, consumo discrecional) ven sus proyecciones de ingresos a futuro recortadas en tus modelos de Excel. Es hora de mover capital a acciones *defensivas* (salud, energía, consumo básico).
2. **Valuación de Empresas (WACC):** El incremento en la "tasa libre de riesgo" (generalmente el bono a 10 años del gobierno) elevará el Costo de Capital (WACC) de las empresas en tus modelos DCF (Descuento de Flujos de Caja). Al descontar los flujos futuros por una tasa más alta, el Valor Presente de la empresa cae. Las acciones bajan de precio intrínsecamente, aunque la empresa no haya hecho nada malo. Es pura matemática impulsada por la política monetaria.

---


## 7. Tareas y Evaluación de la Semana 6

**A. Lectura Obligatoria:**
* Mankiw, N. Gregory. *Principios de Economía*. Capítulos 16 (La influencia de la política monetaria y fiscal) y el Capítulo 20 (Las fluctuaciones económicas). 

**B. Preguntas de Reflexión:**
1. Si un gobierno entra en recesión y decide recortar el gasto público y subir impuestos para "equilibrar su presupuesto" (Política Fiscal Restrictiva), ¿cómo reaccionará el PIB a corto plazo según el multiplicador keynesiano? ¿Por qué muchos economistas critican esta medida en medio de una recesión?
2. Explica el concepto de "Efecto Expulsión" (Crowding out), en el cual una política fiscal expansiva puede ir en detrimento de la inversión privada.

**C. Ejercicio Matemático a entregar:**
La economía de "MacroState" está sobrecalentada (Brecha Inflacionaria). 
El gobierno quiere aplicar una **Política Fiscal Restrictiva** aumentando los impuestos para reducir el consumo. 
*El PIB actual es de $\$2,400$ millones, y el PIB Potencial es de $\$2,000$ millones. (Hay una brecha inflacionaria de $\$400$ millones).*
* La propensión marginal a consumir ($PMgC$) es $0.8$.

Contesta:
1. ¿Cuál es el multiplicador de los impuestos en este país? (Pista: El multiplicador de los impuestos es igual al multiplicador del gasto, pero negativo y ligeramente menor: $k_{imp} = - \frac{PMgC}{1 - PMgC}$). Calcula su valor.
2. ¿Cuánto debe subir los impuestos ($\Delta T$) el gobierno exactamente para cerrar esa brecha inflacionaria y enfriar el PIB de $\$2,400$ hasta el nivel potencial de $\$2,000$? (Recuerda: la reducción del PIB será $k_{imp} \times \Delta T$. Despeja $\Delta T$).

??? success "Solución del Ejercicio C"

    **1. Multiplicador de los impuestos**

    $$k_{imp} = -\frac{PMgC}{1 - PMgC} = -\frac{0.8}{1 - 0.8} = -\frac{0.8}{0.2} = \mathbf{-4}$$

    Cada peso de impuesto adicional **reduce** el PIB en 4 pesos.

    **2. Subida de impuestos necesaria**

    La brecha inflacionaria a cerrar es de $-400$ millones (hay que enfriar el PIB
    de $2{,}400$ a $2{,}000$):

    $$\Delta PIB = k_{imp} \times \Delta T$$
    
    $$-400 = -4 \times \Delta T \Longrightarrow \Delta T = \mathbf{100 \text{ millones}}$$

    **Comprobación:** $-4 \times 100 = -400$ ✓

    **¿Por qué el multiplicador fiscal es menor en valor absoluto que el del gasto?**

    Con la misma $PMgC = 0.8$, el multiplicador del **gasto** sería
    $k_G = 1/(1-0.8) = 5$, frente a $|k_{imp}| = 4$.

    La razón es que el gasto público entra **completo** al flujo circular: el
    gobierno gasta los 100 millones y los 100 se convierten en ingreso de alguien.
    En cambio, un impuesto de 100 no reduce el consumo en 100, sino solo en
    $0.8 \times 100 = 80$: el contribuyente absorbe los otros 20 reduciendo su
    **ahorro**, no su consumo. El impuesto actúa con un paso de retraso.

    **Implicación de política:** para enfriar la economía, **subir impuestos es
    menos potente que recortar gasto**. Para cerrar los mismos 400 millones bastaría
    con recortar $400/5 = 80$ millones de gasto, frente a los 100 de impuestos.

---
