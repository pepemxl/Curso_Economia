# Semana 38 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: El múltiplo de "AutoCorp"
Tienes dos empresas de fabricación de autos:
* **AutoCorp USA:** Mucho apalancamiento financiero. Muy poco efectivo en caja.
* **AutoCorp Mexico:** No tiene deuda, opera con todo efectivo.

Ambas empresas cotizan en bolsa a $500 Millones (Market Cap). ¿Cuál es más cara?

**Análisis con Market Cap (P/E):** 
Si miras solo las acciones, ambas valen $500M. Alias, parecen iguales. Pero AutoCorp USA tiene $1,000 Millones en deuda, y AutoCorp Mexico tiene $0 deuda y $200M de efectivo.

**Cálculo del Enterprise Value (EV):**
* $EV_{USA} = \$500 \text{ (Market Cap)} + \$1,000 \text{ (Deuda)} - \$0 \text{ (Cash)} = \mathbf{\$1,500 \text{ Millones}}$
* $EV_{Mexico} = \$500 \text{ (Market Cap)} + \$0 \text{ (Deuda)} - \$200 \text{ (Cash)} = \mathbf{\$300 \text{ Millones}}$

**Veredicto Financiero:** 
Si comparas solo acciones (P/E), parecen iguales. Pero si calculas el **EV/EBITDA**, AutoCorp USA es matemáticamente **5 veces más cara** que AutoCorp Mexico. Un analista junior se dejaría engañar por el Market Cap idéntico, pero el analista senior usa EV/EBITDA y ve que AutoCorp Mexico es una gangosa inmobiliaria perfecta.

---

## Ejercicio: construir una tabla de comparables desde cero

La valuación relativa parece fácil y es donde más se hace trampa. Vamos paso a paso con una
tabla real.

**Empresa objetivo — "RetailPlus":** Ventas 2,000 · EBITDA 300 · Utilidad neta 120 · Deuda 500 ·
Caja 100 · 50 M de acciones · Precio $18.

**Paso 1 — Calcular sus propias métricas**

$$\text{Market Cap} = 50 \times 18 = \$900\text{M}$$

$$\text{Deuda neta} = 500 - 100 = \$400\text{M}$$

$$EV = 900 + 400 = \$1{,}300\text{M}$$

$$EV/EBITDA = \frac{1{,}300}{300} = 4.33\times \qquad P/E = \frac{900}{120} = 7.5\times$$

**Paso 2 — La tabla de comparables**

| Empresa | EV/EBITDA | P/E | Margen EBITDA | Crecimiento | Deuda/EBITDA |
|---|---|---|---|---|---|
| Comp A | 6.2× | 12.1× | 14 % | 5 % | 2.1× |
| Comp B | 7.8× | 15.4× | 18 % | 9 % | 1.4× |
| Comp C | 5.1× | 9.8× | 11 % | 2 % | 3.2× |
| Comp D | 6.9× | 13.5× | 16 % | 7 % | 1.8× |
| **Mediana** | **6.55×** | **12.8×** | **15 %** | **6 %** | **1.95×** |
| **RetailPlus** | **4.33×** | **7.5×** | **15 %** | **4 %** | **1.33×** |

**Paso 3 — La valuación implícita**

$$EV_{implícito} = 6.55 \times 300 = \$1{,}965\text{M}$$

$$\text{Equity} = 1{,}965 - 400 = \$1{,}565\text{M} \quad \Rightarrow \quad \frac{1{,}565}{50} = \mathbf{\$31.30/acción}$$

Frente a los $\$18$ del mercado: **+74 % de potencial**.

**Paso 4 — La pregunta que hay que hacerse antes de comprar**

Un descuento del 34 % frente a la mediana del sector es enorme. **¿Por qué existe?** Tres
posibilidades, y solo una es una oportunidad:

1. **El mercado se equivoca** → oportunidad real de valor.
2. **RetailPlus es peor de lo que muestran estas métricas** → descuento justificado.
3. **La tabla está mal construida** → el análisis no vale nada.

Los datos apuntan en direcciones mixtas: su margen EBITDA (15 %) está **en la mediana**, y su
apalancamiento (1,33×) es **el mejor del grupo**. Pero su crecimiento (4 %) está **por debajo**
de la mediana del 6 %.

Un menor crecimiento justifica un menor múltiplo, pero **no un 34 % de descuento**. Aquí es
donde el analista tiene que ir a las notas y buscar qué falta: ¿litigios pendientes?
¿concentración en un cliente? ¿un accionista de control con mala reputación? ¿arrendamientos
fuera de balance que inflarían la deuda real?

!!! danger "Los cinco errores que invalidan una tabla de comparables"
    1. **Mezclar EV con métricas de equity.** El EV incluye la deuda, así que se compara con
       métricas **antes de intereses**: EBITDA, EBIT, ventas. El P/E, en cambio, es de equity y
       va contra la utilidad neta. **`EV/Utilidad neta` no significa nada.**
    2. **Mezclar períodos.** Todos los múltiplos deben ser del mismo año fiscal y de la misma
       naturaleza: todos *forward* (NTM) o todos *trailing* (LTM). Comparar un forward contra un
       trailing en un sector cíclico produce el error del caso petrolero de esta semana.
    3. **Elegir "comparables" que no lo son.** Deben coincidir en sector, tamaño, geografía,
       crecimiento y modelo de negocio. Comparar una cadena de descuento con una de lujo, o una
       empresa de un mercado emergente con una estadounidense, no es análisis.
    4. **Usar la media en vez de la mediana.** Un solo comparable con P/E de 80 destruye el
       promedio.
    5. **No ajustar la deuda por arrendamientos.** Bajo NIIF 16 los arrendamientos van al
       balance, pero si comparas empresas bajo normas distintas, unas tendrán deuda que otras
       ocultan. Ajusta antes de comparar.

---

## Qué múltiplo usar en cada situación

| Múltiplo | Úsalo cuando | Evítalo cuando |
|---|---|---|
| **EV/EBITDA** | Comparar empresas con distinto apalancamiento; el estándar en M&A | La intensidad de capital difiere mucho (ignora el CapEx) |
| **EV/EBIT** | La intensidad de capital difiere: sí recoge la depreciación | Las políticas de amortización son muy dispares |
| **EV/Ventas** | La empresa **no gana dinero** todavía (SaaS, biotech) | Los márgenes del sector son heterogéneos |
| **P/E** | Empresas maduras y rentables del mismo sector | Utilidad negativa, o estructuras de capital muy distintas |
| **P/B (Precio/Valor libro)** | **Bancos y aseguradoras**, donde el balance *es* el negocio | Empresas cuyo valor está en intangibles |
| **EV/FCF** | El más riguroso conceptualmente | El FCF de un año concreto es muy volátil |
| **PEG** ($P/E \div g$) | Comparar empresas con crecimientos muy distintos | El crecimiento es negativo o errático |

**El PEG aplicado a RetailPlus:**

$$PEG_{RetailPlus} = \frac{7.5}{4} = 1.88 \qquad PEG_{mediana} = \frac{12.8}{6} = 2.13$$

Ajustado por crecimiento, el descuento se reduce mucho: RetailPlus está **un 12 % más barata**,
no un 34 %. **Buena parte del descuento aparente era simplemente su menor crecimiento.**

Esa es la lección de método: un múltiplo bajo casi nunca es una anomalía; suele ser el mercado
descontando algo que el múltiplo solo, aislado, no muestra.

---
