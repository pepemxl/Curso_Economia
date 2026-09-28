# Semana 25 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: La Expansión de la Planta
La empresa "AgriCorp" quiere comprar una nueva cosechadora. La máquina cuesta **$10,000** (Inversión Año 0). Generará flujos de caja de **$4,000** al año durante 3 años. El WACC de AgriCorp es del **10%**.

**Cálculo Matemático:**
1. **VAN:**
   * Año 1: $4,000 / (1.10)^1 = $3,636
   * Año 2: $4,000 / (1.10)^2 = $3,305
   * Año 3: $4,000 / (1.10)^3 = $3,005
   * Total VP de Flujos = $9,946
   * VAN = -$10,000 + $9,946 = **-$54**.
   * *Veredicto VAN:* Rechazar. El proyecto está destruyendo $54 de valor presente porque no logra cubrir el WACC.

2. **TIR:**
   * Probamos con multiple tasas. (En Excel: `=TIR(-10000, 4000, 4000, 4000)`).
   * La tasa que hace el VAN cero es **9.70%**.
   * *Veredicto TIR:* Rechazar. La TIR (9.70%) es menor que el WACC (10%). Coincide con el VAN.

3. **Payback Descontado:**
   * Fin del Año 1 recuperamos $3,636 (Falta $6,364).
   * Fin del Año 2 recuperamos $3,305 (Acumulado $6,941. Falta $3,059).
   * En el Año 3 necesitamos $3,059. Ese año generamos $3,005 descontados.
   * No alcanzamos a recuperar la inversión en los 3 años. El proyecto se paga en approx 3.02 años.
   * *Veredicto Payback:* Rechazado. *(Nota: Si el VAN fuera positivo y se recuperara en el año 2.5, el proyecto se aceptaría si la política de la empresa acepta proyectos de hasta 3 años de recuperación).*

---

## Segundo ejercicio: cuando la TIR y el VAN se contradicen

Los dos criterios coinciden en proyectos convencionales. Cuando hay que **elegir entre
proyectos mutuamente excluyentes**, pueden dar respuestas opuestas — y solo uno de los dos tiene
razón.

AgriCorp debe elegir **uno** de estos dos proyectos (WACC = 10 %):

| | **Proyecto A** (cosechadora pequeña) | **Proyecto B** (planta completa) |
|---|---|---|
| Inversión (Año 0) | −10,000 | −50,000 |
| Flujo Año 1 | 6,000 | 25,000 |
| Flujo Año 2 | 6,000 | 25,000 |
| Flujo Año 3 | 6,000 | 25,000 |

**Cálculos:**

| | Proyecto A | Proyecto B |
|---|---|---|
| VP de flujos | 14,921 | 62,171 |
| **VAN** | **+4,921** | **+12,171** |
| **TIR** | **36,3 %** | **23,4 %** |

**Contradicción:** la TIR prefiere A (36,3 % frente a 23,4 %), el VAN prefiere B (+12,171 frente
a +4,921).

**¿Cuál manda? El VAN, siempre.**

La razón es de fondo: **la TIR es una tasa; el VAN es dinero.** Un 36 % sobre $\$10,000$ genera
menos riqueza que un 23 % sobre $\$50,000$. El objetivo de una empresa no es maximizar
porcentajes, sino **maximizar valor absoluto para el accionista**.

**Comprobación por el proyecto incremental.** Analiza la diferencia B − A:

| | B − A |
|---|---|
| Inversión adicional | −40,000 |
| Flujo adicional (×3 años) | +19,000 |
| **VAN incremental** | **+7,250** |
| **TIR incremental** | **20,1 %** |

Los $\$40,000$ adicionales que exige B rinden un **20,1 %**, muy por encima del WACC del 10 %.
**Merece la pena invertirlos.** El análisis incremental y el VAN coinciden, como debe ser.

---

## Los cuatro fallos de la TIR

1. **Escala.** El caso anterior: ignora el tamaño del proyecto.
2. **TIR múltiples.** Con flujos no convencionales (más de un cambio de signo), hay tantas TIR
   como cambios de signo. Un proyecto minero $(-100, +300, -250)$ tiene **dos** TIR; ninguna
   significa nada. Usa `TIRM` o quédate con el VAN.
3. **Supuesto de reinversión.** La TIR asume implícitamente que los flujos intermedios se
   reinvierten **a la propia TIR**. Si un proyecto tiene una TIR del 40 %, eso supone que
   podrás reinvertir cada flujo al 40 % — casi nunca cierto. El VAN asume reinversión al WACC,
   mucho más realista.
4. **Perfiles temporales distintos.** Dos proyectos con flujos concentrados al principio o al
   final pueden intercambiar su orden de preferencia según la tasa de descuento. El punto donde
   se cruzan sus perfiles de VAN se llama **tasa de Fisher**.

!!! tip "Cuándo cada criterio es el adecuado"
    | Criterio | Úsalo para | No lo uses para |
    |---|---|---|
    | **VAN** | **Decidir**. Siempre. | — |
    | **TIR** | Comunicar rentabilidad; comparar con el WACC | Elegir entre excluyentes; flujos no convencionales |
    | **Payback descontado** | Medir exposición temporal y riesgo de liquidez | Decidir |
    | **Índice de rentabilidad** ($VP/I_0$) | Priorizar con **presupuesto limitado** | Proyectos independientes con capital disponible |

    El **índice de rentabilidad** merece atención: cuando el capital está racionado y no puedes
    hacer todos los proyectos con VAN positivo, ordénalos por $VP/I_0$ (A: 1,49; B: 1,24) y ve
    tomando hasta agotar el presupuesto. Es el criterio que maximiza el VAN total por peso
    disponible.

---

## Tercer ejercicio: los flujos que sí cuentan

La mitad de los errores de presupuesto de capital no están en la matemática, sino en **qué
flujos se meten en la tabla**. AgriCorp evalúa una nueva línea de producto. ¿Cuáles de estos
conceptos entran en el análisis?

| Concepto | ¿Entra? | Por qué |
|---|---|---|
| Costo de la maquinaria | ✅ Sí | Desembolso incremental |
| Estudio de mercado ya pagado ($15,000) | ❌ **No** | **Costo hundido**: se pagó pase lo que pase |
| Aumento del capital de trabajo | ✅ Sí | Inmoviliza caja real |
| Recuperación del capital de trabajo al final | ✅ Sí | Se libera al cerrar el proyecto |
| Depreciación | ⚠️ **Indirectamente** | No es flujo, pero **genera escudo fiscal** |
| Escudo fiscal de la depreciación | ✅ Sí | $\text{Dep} \times t$ es caja real ahorrada |
| Gastos generales ya existentes | ❌ No | No cambian con el proyecto |
| Caída de ventas de otro producto propio | ✅ **Sí, restando** | **Canibalización**: es un costo de oportunidad |
| Alquiler de una nave que ya posees | ✅ Sí, como costo | Podrías alquilarla a un tercero: costo de oportunidad |
| Intereses del préstamo que lo financia | ❌ **No** | Ya están en el WACC. Incluirlos es contarlos dos veces |
| Valor de rescate del equipo al final | ✅ Sí, neto de impuestos | Entrada de caja |

!!! danger "Los tres errores que más destruyen valor"
    1. **Incluir los intereses en el flujo Y descontar al WACC.** Doble contabilidad del costo
       financiero. El flujo del proyecto se calcula **como si no hubiera deuda**; el
       financiamiento vive en la tasa.
    2. **Olvidar la canibalización.** Un producto nuevo que roba ventas al existente no aporta
       lo que factura, sino la **diferencia**. Es el sesgo favorito de los equipos de producto.
    3. **Arrastrar costos hundidos.** *"Ya gastamos $15,000 en el estudio"* no es un argumento
       para nada. Ese dinero no vuelve ni continuando ni abandonando.

---
