# Semana 23 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico: ¿Sobrevive "ClassicGrid" a la recesión?

Eres un analista de crédito en un banco. La empresa de energía "ClassicGrid" pide un préstamo de $500 millones. En lugar de mirar su hermoso lobby, calculas su Z-Score desde su último reporte anual:

* **Datos Financieros:**
  * Capital de Trabajo = $200 millones
  * Utilidades Retenidas = $400 millones
  * EBIT = $250 millones
  * Valor de Mercado de las Acciones (Market Cap) = $600 millones
  * Pasivo Total = $1,200 millones
  * Ventas = $3,000 millones
  * Activos Totales = $2,000 millones

**Cálculo paso a paso:**
* $X_1 = 200 / 2000 = 0.100$
* $X_2 = 400 / 2000 = 0.200$
* $X_3 = 250 / 2000 = 0.125$
* $X_4 = 600 / 1200 = 0.500$
* $X_5 = 3000 / 2000 = 1.500$

**Aplicación de la Fórmula:**
$Z = 1.2(0.100) + 1.4(0.200) + 3.3(0.125) + 0.6(0.500) + 1.0(1.500)$
$Z = 0.12 + 0.28 + 0.4125 + 0.30 + 1.50 = \mathbf{2.6125}$

**Tu Veredicto Financiero:**
El Z-Score es **2.61**. La empresa está en la **Zona Gris** ($1.81 < Z < 2.99$).
No es un desastre inminente, pero no es seguro. Descubres que su $X_5$ (Rotación de Activos) es alto, pero su $X_4$ (Valor de mercado/Pasivo) es débil (0.5). Están muy endeudados.
*Acción bancaria:* Le otorgas el préstamo, pero le cobras una tasa de interés 2 puntos porcentuales más alta que al mercado (Prima de riesgo) y exiges garantías colaterales (activos físicos).

---

## Segundo ejercicio: el Z-Score en el tiempo, no en un punto

Un Z-Score aislado dice poco. Lo que un analista de crédito mira es su **trayectoria**. Los
últimos cuatro años de ClassicGrid:

| Componente | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| $X_1$ Capital de trabajo / Activos | 0.180 | 0.150 | 0.120 | **0.100** |
| $X_2$ Utilidades retenidas / Activos | 0.280 | 0.250 | 0.220 | **0.200** |
| $X_3$ EBIT / Activos | 0.160 | 0.150 | 0.135 | **0.125** |
| $X_4$ Valor mercado / Pasivos | 0.900 | 0.750 | 0.620 | **0.500** |
| $X_5$ Ventas / Activos | 1.450 | 1.470 | 1.480 | **1.500** |
| **Z-Score** | **3.13** | **2.94** | **2.75** | **2.61** |

**El Z-Score cae 0,51 puntos en tres años, a un ritmo estable de ~0,17 anuales.** Y el dato que
más pesa: en 2022 ClassicGrid estaba en **zona segura** ($Z = 3.13 > 2.99$); hoy ya no. Si la
tendencia continúa, entra en **zona de peligro** ($Z < 1.81$) en unos **4,7 años**.

Y hay algo más grave en el detalle: **cuatro de los cinco componentes se deterioran**. El único
que mejora es $X_5$, la rotación de ventas — y mejora poco. Cuando el deterioro es
generalizado, no es un problema de un área concreta: es el negocio entero perdiendo fuerza.

**El componente que más cae es $X_4$**, que se desploma de 0,90 a 0,50: **el mercado ha reducido
casi a la mitad su valoración del patrimonio frente a las deudas**. El mercado ya lo vio.

---

## Tercer ejercicio: las tres variantes de la fórmula

Aplicar la fórmula original a una empresa que no es manufacturera ni cotiza es un error común.
Altman publicó variantes precisamente por eso:

**A. Z original — manufactureras cotizadas**

$$Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 1.0X_5$$

Zonas: seguro $> 2.99$ · gris $1.81$–$2.99$ · peligro $< 1.81$

**B. Z' — empresas privadas** (no hay valor de mercado, se usa el **contable**)

$$Z' = 0.717X_1 + 0.847X_2 + 3.107X_3 + 0.420X_4 + 0.998X_5$$

Zonas: seguro $> 2.90$ · gris $1.23$–$2.90$ · peligro $< 1.23$

**C. Z'' — no manufactureras y mercados emergentes** (se **elimina $X_5$**)

$$Z'' = 6.56X_1 + 3.26X_2 + 6.72X_3 + 1.05X_4$$

Zonas: seguro $> 2.60$ · gris $1.10$–$2.60$ · peligro $< 1.10$

**Por qué se elimina $X_5$ en la tercera.** La rotación de activos varía enormemente entre
sectores: un supermercado rota 3 veces, una eléctrica 0,4. Incluirla penalizaría
sistemáticamente a los sectores intensivos en capital por razones que **nada tienen que ver con
el riesgo de quiebra**. Nótese, además, que en el ejercicio principal $X_5$ aportaba el 57 % del
Z-Score de ClassicGrid — una empresa de energía, precisamente el tipo de caso donde la fórmula
original distorsiona.

**Recalculemos ClassicGrid con $Z''$**, que es la variante adecuada para una utility:

$$Z'' = 6.56(0.100) + 3.26(0.200) + 6.72(0.125) + 1.05(0.500)$$

$$Z'' = 0.656 + 0.652 + 0.840 + 0.525 = \mathbf{2.67}$$

Sigue en zona gris ($1.10$–$2.60$)… **apenas por encima del umbral superior de 2,60**. Con la
fórmula correcta, ClassicGrid está **al borde de la zona segura**, un diagnóstico algo mejor que
el anterior, pero igualmente sin margen.

!!! warning "Los límites del Z-Score que hay que declarar siempre"
    * **Es un modelo de 1968**, calibrado sobre 66 manufactureras estadounidenses. La economía
      ha cambiado: hoy el valor de muchas empresas está en intangibles que el balance no recoge.
    * **Penaliza estructuralmente a las empresas jóvenes**, porque $X_2$ (utilidades retenidas
      acumuladas) es bajo por definición en una empresa reciente aunque sea muy rentable.
    * **No sirve para instituciones financieras.** Un banco tiene capital de trabajo negativo y
      un apalancamiento de 10:1 por diseño; la fórmula lo declararía en quiebra permanente.
    * **Es sensible a la contabilidad creativa.** Todos sus componentes salen de estados
      financieros que se pueden maquillar. Contrástalo con el flujo de caja (Semana 9).

    **Cómo usarlo bien:** no como veredicto, sino como **sistema de alerta temprana** y sobre
    todo **en tendencia**. Un Z de 2,6 estable durante cinco años dice algo muy distinto de un
    Z de 2,6 que viene cayendo desde 3,3. Complétalo siempre con el ciclo de conversión de
    efectivo, el calendario de vencimientos de la deuda y la cobertura de intereses.

---
