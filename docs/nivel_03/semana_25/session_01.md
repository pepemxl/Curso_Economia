# Semana 25 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Comprender el proceso de Presupuesto de Capital y la decisión de aceptar o rechazar proyectos.
* Dominar el cálculo e interpretación del Valor Actual Neto (VAN / NPV) como regla suprema.
* Entender la Tasa Interna de Retorno (TIR / IRR) y sus peligros matemáticos (Tirajes múltiples).
* Calcular el Payback Descontado como herramienta de control de liquidez y riesgo.
* Resolver el conflicto clásico cuando el VAN y la TIR dan señales contradictorias.

---

## 2. El Valor Actual Neto (VAN / NPV): El Rey Absoluto
El VAN es la suma de todos los flujos de caja futuros de un proyecto, trayéndolos a valor presente usando el WACC, y restando la inversión inicial. Te dice cuánta riqueza *absoluta* (en dólares de hoy) está creando el proyecto.

* **Fórmula:** 
  $$ VAN = -Inversión + \sum \frac{FC_t}{(1 + WACC)^t} $$
  
* **Regla de Decisión:**
  * **VAN > 0:** ¡Aceptar! El proyecto genera más valor que el costo de financiarlo. Crea riqueza.
  * **VAN < 0:** Rechazar. El proyecto destruye valor.
  * **VAN = 0:** Punto de equilibrio. No crea ni destruye, solo cubre el costo de capital.

> **💥 Impacto Financiero:** Si un proyecto tiene un VAN de $10 millones, significa que si lo ejecutas, el valor de las acciones de tu empresa subirá exactamente $10 millones hoy mismo (porque el mercado descuenta ese valor presente futuro). El VAN es la única métrica que mide riqueza absoluta.

---

## 3. La Tasa Interna de Retorno (TIR / IRR): El Retador
La TIR es la tasa de descuento que hace que el VAN sea exactamente igual a cero. Es el **returno porcentual** que genera el proyecto. Es muy popular porque los directivos prefieren escuchar "este proyecto da un 20% de retorno" antes que "este proyecto da un VAN de $5.43M".

* **Regla de Decisión:** 
  * Si **TIR > WACC**: Aceptar (El proyecto rinde más de lo que cuesta la deuda/patrimonio).
  * Si **TIR < WACC**: Rechazar.

* **⚠️ Los Peligros de la TIR (Por qué los analistas prefieren el VAN):**
  1. **Tasa de Reinversión Implícita:** La TIR asume matemáticamente que los flujos de caja que recibes a mitad del proyecto se reinvierten a la misma tasa de la TIR (ej. 40%). ¡Imposible! El VAN asume que se reinvierte al WACC (mucho más realista).
  2. **TIRajes Múltiples:** Si un proyecto tiene flujos de caja negativos a mitad de su vida (ej. una minera que tiene que cerrar y pagar restauración ambiental en el año 5), la ecuación matemática arroja múltiple TIRs (ej. 10% y 50%). La TIR queda inservible.
