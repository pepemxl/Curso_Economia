# Semana 26 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: El Escudo Fiscal de "DebtCorp"
Tienes dos empresas idénticas: "NoDebt Inc." (sin deuda) y "DebtCorp" (con deuda). Ambas generan un EBIT de $1,000 al año. La tasa de impuestos es del 30%.

**NoDebt Inc. (100% Patrimonio):**
* EBIT = $1,000
* Impuestos (30%) = $300
* **Utilidad Neta = $700**. (Flujo total a inversores = $700).

**DebtCorp (Con Deuda):**
* EBIT = $1,000
* Gasto por Intereses = $200 (Asumamos que pagamos $200 de intereses)
* Ganancia antes de Impuestos (EBT) = $800
* Impuestos (30%) = $240
* **Utilidad Neta = $560**
* Flujo total a inversores = Utilidad Neta ($560) + Intereses que fuimos al banco ($200) = **$760**.

**Conclusión Matemática:**
La empresa con deuda repartió **$760** entre bancos y accionistas, mientras que la empresa sin deuda solo repartió **$700**. 
¿De dónde salieron los $60 extra? Del gobierno. Al pagar $200 de intereses, los impuestos bajaron de $300 a $240. El "Escudo Fiscal" nos ahorró $60 (que es el 30% de los $200 de intereses). Ese dinero extra incrementa el valor total de la firma.

---

## Segundo ejercicio: el valor de la firma con y sin deuda

El ejercicio anterior mostró el escudo **anual**. Traduzcámoslo a **valor de empresa**.

Supón que ambas empresas generan ese EBIT de $\$1,000$ **a perpetuidad**, que el costo del
patrimonio sin deuda es del **10 %**, y que DebtCorp tiene $\$2,000$ de deuda al **10 %** (de
ahí los $\$200$ de intereses).

**Valor de NoDebt Inc. (empresa no apalancada):**

$$V_U = \frac{EBIT(1-t)}{r_U} = \frac{1{,}000 \times 0.70}{0.10} = \frac{700}{0.10} = \mathbf{\$7{,}000}$$

**Valor de DebtCorp (empresa apalancada), por M&M con impuestos:**

$$V_L = V_U + D \times t = 7{,}000 + 2{,}000 \times 0.30 = \mathbf{\$7{,}600}$$

**Comprobación por el escudo perpetuo:**

$$VP_{escudo} = \frac{\text{Intereses} \times t}{r_d} = \frac{200 \times 0.30}{0.10} = \frac{60}{0.10} = \$600 \quad ✓$$

Los $\$600$ de valor adicional son exactamente el valor presente de los $\$60$ anuales de
ahorro fiscal.

**El reparto del pastel:**

| | NoDebt | DebtCorp |
|---|---|---|
| Valor de la firma | 7,000 | **7,600** |
| (−) Deuda | 0 | 2,000 |
| **Patrimonio** | **7,000** | **5,600** |
| Flujo anual a inversores | 700 | **760** |

**El costo del patrimonio sube con el apalancamiento.** No es gratis:

$$r_E = r_U + (r_U - r_d)\frac{D}{E}(1-t) = 0.10 + (0.10 - 0.10)\frac{2{,}000}{5{,}600}(0.70) = 10\%$$

En este caso particular $r_U = r_d$, así que no cambia. Pero si $r_U = 12\%$ y $r_d = 8\%$:

$$r_E = 0.12 + (0.12 - 0.08)\frac{2{,}000}{5{,}600}(0.70) = 0.12 + 0.01 = \mathbf{13\%}$$

**Los accionistas exigen más porque asumen más riesgo.** El apalancamiento no crea valor por
hacer el capital "más barato": lo crea **únicamente** por el escudo fiscal.

---

## Tercer ejercicio: hasta dónde endeudarse (Trade-off)

Si $V_L = V_U + Dt$, la fórmula sugiere endeudarse infinitamente. La teoría del **trade-off**
introduce el otro plato de la balanza: los **costos esperados de dificultades financieras**.

$$V_L = V_U + \underbrace{D \times t}_{\text{escudo fiscal}} - \underbrace{PV(\text{costos de quiebra})}_{\text{crece exponencialmente}}$$

Simulemos DebtCorp con distintos niveles de deuda. Supón que la probabilidad de dificultades
financieras crece con el apalancamiento y que su costo, si ocurren, es del 25 % del valor de la
firma ($\$1,750$):

| Deuda | Escudo $D \times t$ | Prob. dificultades | Costo esperado | **$V_L$** |
|---|---|---|---|---|
| 0 | 0 | 0 % | 0 | 7,000 |
| 1,000 | 300 | 1 % | 18 | 7,282 |
| 2,000 | 600 | 4 % | 70 | **7,530** |
| 3,000 | 900 | 12 % | 210 | **7,690** |
| 4,000 | 1,200 | 28 % | 490 | **7,710** |
| 5,000 | 1,500 | 50 % | 875 | 7,625 |
| 6,000 | 1,800 | 75 % | 1,313 | 7,487 |

**El óptimo está en torno a $\$4,000$ de deuda**, donde el valor alcanza $\$7,710$. A partir de
ahí, cada peso adicional de deuda **destruye** más valor por riesgo de quiebra del que crea por
escudo fiscal.

La curva es **plana cerca del óptimo** (entre 3,000 y 5,000 el valor apenas varía) y **cae
bruscamente después**. Eso tiene una implicación práctica importante: **es mucho más costoso
pasarse que quedarse corto**. Por eso las empresas prudentes mantienen capacidad de
endeudamiento sin usar (*financial slack*).

!!! tip "Qué predice cada teoría, y qué se observa"
    | Teoría | Predicción | ¿Se observa? |
    |---|---|---|
    | **M&M sin impuestos** | La estructura es irrelevante | No, pero aclara *por qué* importa |
    | **M&M con impuestos** | 100 % deuda | No |
    | **Trade-off** | Existe un óptimo interior; ratio objetivo por sector | Parcialmente |
    | **Jerarquía (*pecking order*)** | Primero utilidades retenidas, luego deuda, y emitir acciones al final | **Sí, es lo que más se observa** |

    La **jerarquía** explica dos hechos que el trade-off no: que las empresas **más rentables**
    suelen ser las **menos endeudadas** (generan caja suficiente y no necesitan deuda), y que
    anunciar una emisión de acciones **hace caer la cotización** — el mercado lo lee como señal
    de que la dirección cree que la acción está cara.

    Ese efecto señalización es información asimétrica pura, y es la razón de que las empresas
    prefieran casi cualquier cosa antes que emitir capital.

---
