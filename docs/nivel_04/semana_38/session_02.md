# Semana 38 · Sesión 2: Profundización

## 4. El Múltiplo Rey de Wall Street: EV/EBITDA
Los múltiplos de Equity (Market Cap) tienen un problema: se distorsionan por la estructura de capital (deuda). Para comparar correctamente, usamos el **Enterprise Value (EV)**, que es el valor de *toda* la firma (Deuda + Patrimonio - Efectivo).

* **EV/EBITDA (Enterprise Value to EBITDA):**
  * **Fórmula:** EV / EBITDA. (Vimos el EBITDA en la Semana 22).
  * **Interpretación:** Mide el valor total de la firma contra su flujo operativo bruto, *antes* de intereses, impuestos, depreciación y amortización.
  * **Por qué es el Rey:** Es neutral al capital (ignora si la empresa se financia con deuda o acciones), neutral a impuestos (cada país tiene tasas distintas) y neutral a la depreciación (activos viejos vs nuevos). 
  * *Regla:* Empresas de tecnología (poco CapEx) transan a EV/EBITDA de 15x a 25x. Empresas industriales pesadas (mucho CapEx) transan a 5x a 8x.

---

## 5. Trading Comps vs. Transaction Comps
En un proceso de M&A (Semana 27), los banqueros usan dos tipos de comparables:
1. **Trading Comps (Empresas cotizadas):** Miras las empresas similares que cotizan en la bolsa hoy. Multiplicas el EV/EBITDA promedio del sector por el EBITDA de tu empresa. Da el valor "en mercado normal".
2. **Transaction Comps (Precedentes):** Miras el precio exacto que se pagó en fusiones o adquisiciones recientes del sector. Se le añade una **Prima de Adquisición** (Control Premium, generalmente 20-30% arriba del Trading Comp) porque el comprador paga extra por el control total de la empresa.

---

## Cómo se construye un conjunto de comparables

La calidad de una valuación relativa depende casi por completo de esta selección. Los criterios,
en orden de importancia:

1. **Mismo sector y modelo de negocio.** No basta con el código sectorial: una aerolínea de bajo
   costo y una de red compiten en el mismo sector con economías distintas.
2. **Tamaño similar.** Un rango de 0,3× a 3× las ventas de la empresa objetivo es una regla
   práctica razonable.
3. **Perfil de crecimiento parecido.** Es el factor que más explica las diferencias de múltiplo.
4. **Mismo mercado geográfico**, o al menos exposición macro similar.
5. **Estructura de capital comparable** — o, mejor, usar múltiplos de EV que la neutralizan.

**El mínimo son 4-5 comparables.** Con menos, un solo dato atípico domina; con muchos más, se
diluye la comparabilidad al incluir empresas que ya no se parecen.

---

## Los ajustes de normalización

Antes de calcular ningún múltiplo hay que **limpiar** las cifras, o estarás comparando cosas
distintas:

| Ajuste | Por qué |
|---|---|
| **Partidas no recurrentes** | Un deterioro puntual distorsiona el EBITDA del año |
| **Arrendamientos (NIIF 16 vs. otras normas)** | Unas empresas los llevan al balance y otras no |
| **Pensiones sin financiar** | Son deuda económica; súmalas a la deuda neta |
| **Participaciones minoritarias** | El EV incluye el 100 % del negocio; ajusta el equity |
| **Caja excedente** | La caja operativa mínima no es "caja neta" disponible |
| **Opciones sobre acciones** | Usa el número de acciones **totalmente diluido** |
| **Diferencias en capitalización de I+D** | Una capitaliza y otra gasta: los EBIT no son comparables |

**El ajuste de arrendamientos**, en concreto, puede cambiar el EV/EBITDA de un retailer en más
de un punto entero. Ignorarlo hace que las empresas que alquilan sus locales parezcan mucho más
baratas que las que los poseen, cuando la diferencia es puramente contable.

!!! danger "El sesgo de supervivencia en los comparables"
    Los conjuntos de comparables se construyen con las empresas que **siguen cotizando hoy**.
    Las que quebraron o fueron excluidas de bolsa **no aparecen**.

    En sectores en dificultades, eso sesga sistemáticamente los múltiplos **al alza**: solo
    quedan las supervivientes, que por definición son las mejores. Aplicar esa mediana a una
    empresa en problemas la sobrevalúa.

    Es el mismo sesgo que infla las rentabilidades históricas de los fondos de inversión: los
    fondos malos se cierran y desaparecen de las estadísticas.

---
