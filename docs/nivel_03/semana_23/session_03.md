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
