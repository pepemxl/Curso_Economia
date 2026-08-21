# Semana 32 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: El VaR y CVaR de un Portafolio en Excel

Gestionas un portafolio de acciones de tecnología valorado en **$10,000,000**. Descargas el historial de los últimos 5 años de retornos diarios. En Excel calculas que la volatilidad diaria ($\sigma$) es de **1.5%** (0.015). Asumimos que el retorno promedio diario ($\mu$) es 0% para ser conservadores. (Confianza del 99% -> $Z = 2.326$).

**Cálculo del VaR Paramétrico en Excel:**
1. Valor = 10,000,000
2. $Z = 2.326$
3. $\sigma = 0.015$
* **VaR (1 día, 99%)** = $10,000,000 \times 2.326 \times 0.015 = \mathbf{\$348,900}$
* *Interpretación:* Estás 99% seguro de que mañana no perderás más de $348,900.

**Calculando el CVaR en Excel (Método Histórico simulado):**
Sabes que el VaR es el límite (el $348,900). Pero estás preocupado por el 1% de probabilidad de que ocurra un Cisne Negro.
Para calcular el Expected Shortfall, usas la función de Excel sobre tu base de datos histórica: `=PROMEDIO.SI.CONJUNTO(rango_retornos; rango_retornos; "<-0.03489")`.
(Sacas el promedio de todos los días en la historia donde la pérdida fue mayor al 3.489%).
El Excel te arroja que el promedio de esos días desastrosos fue un retorno de **-4.8%**.
* **CVaR (1 día, 99%)** = $10,000,000 \times 0.048 = \mathbf{\$480,000}$
* *Interpretación:* Si ocurre un evento extremo (caes en el 1% de la cola), tu pérdida esperada real será de $480,000, no de $348,900. Por eso el regulador te exige reservar capital por $480,000.

---
