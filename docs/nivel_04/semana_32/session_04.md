# Semana 32 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El Hedging Inmobiliario de Silicon Valley Bank (SVB)
*En marzo de 2023, el Silicon Valley Bank (SVB) colapsa en 48 horas. Eres el auditor de riesgo retrospectivo analizando por qué ocurrió.*

**El Error de Omisión de Cobertura (Falta de Hedging de Tasa de Interés):**
SVB tenía miles de millones de depósitos de empresas tecnológicas. En la pandemia (2020), con tasas al 0%, SVB invirtió ese dinero en Bonos del Tesoro a 10 años al 1.5% de interés (Rent Fija). 
Ellos midieron su **VaR de Crédito** (riesgo de que el gobierno de EEUU no pague) y era cero. Pensaron que estaban seguros.

**Lo que ignoraron:** No hicieron **Hedging de Tasa de Interés**.
En 2022, la FED sube las tasas del 0% al 5%. Los Bonos del Tesoro a 10 años que pagaban 1.5% se desplomaron en precio de mercado (Semana 28). SVB tenía "pérdidas no realizadas" masivas en su balance.
Si hubieran ido al mercado de Swaps y hubieran firmado un contrato para recibir Tasa Variable y pagar Tasa Fija, el valor de ese Swap habría subido $2 Billones de dólares cuando las tasas subieron, compensando perfectamente la caída de los bonos.

**El Veredicto:** SVB gestionó el riesgo de que el deudor no pagara (Crédito), pero no gestionó el riesgo de que las tasas de interés subieran (Mercro). *Una cartera de renta fija a largo plazo sin cobertura de derivados (Hedging) es una posición especulativa disfrazada de inversión segura.* El pánico se desató, los clientes sacaron su dinero (Bank Run), y SVB tuvo que vender los bonos a precio de remate realizando las pérdidas. Quiebra total.

---

## 6. Tareas y Evaluación de la Semana 32

**A. Lectura y Práctica Obligatoria:**
* Hull, John C. *Risk Management and Financial Institutions*. Capítulos sobre Value at Risk y Expected Shortfall.
* *Práctica Excel:* Descarga de Yahoo Finance el histórico de un ETF (ej. SPY o QQQ) del último año. Calcula en Excel el retorno diario (`=Ln(PrecioHoy/PrecioAyer)`). Usa `=DESVEST()` para hallar la volatilidad diaria.

**B. Preguntas de Reflexión:**
1. Si el Value at Risk (VaR) al 99% de confianza de tu portafolio es de $1 Millón, ¿significa que es la pérdida máxima absoluta que puedes sufrir? Explica qué detalle matemático falta en esta afirmación.
2. ¿Por qué el Expected Shortfall (CVaR) es considerado por Basilea III como una métrica superior al VaR para determinar el capital de reserva de un banco?

**C. Ejercicio Práctico a entregar:**
Gestionas un portafolio_accionario valorado en **$5,000,000**. Descargas el historial y calculas que la volatilidad diaria ($\sigma_{diaria}$) es del **2%** (0.02). El promedio de retorno diario ($\mu$) será asumido como 0% para ser conservadores. Necesitas calcular el riesgo al **99% de confianza** ($Z = 2.326$).

Contesta y muestra las fórmulas:
1. Calcula el **VaR Paramétrico** para 1 día. ¿Cuánto es la máxima pérdida esperada en un día normal?
2. Calcula el **VaR para 10 días**. (Fórmula: $VaR_{10d} = VaR_{1d} \times \sqrt{10}$). ¿Por qué no se multiplica por 10 directamente?
3. Debido a tus cálculos, decides hacer un **Hedge** vendiendo Futuros del S&P 500. Si tu portafolio tiene una Beta ($\beta$) de 1.2 respecto al S&P 500, y el valor del contrato de futuro del S&P 500 es de $250,000. ¿Cuántos contratos de futuros tienes que vender para cubrir perfectamente tu riesgo de mercado? (Fórmula Hedge: $\text{Nº Contratos} = (\text{Valor Portafolio} \times \beta) / \text{Valor Contrato Futuro}$).
