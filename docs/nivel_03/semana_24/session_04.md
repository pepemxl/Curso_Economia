# Semana 24 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El "Efecto Martillo" de las Tasas de Interés en la Tecnología
*En 2022, la Reserva Federal sube agresivamente la tasa libre de riesgo ($R_f$) del 1% al 5% para combatir la inflación.*

Tienes en tu portafolio acciones de una empresa de software "CloudFast" que no tiene deuda (WACC = Costo de Patrimonio). Su beta es de 1.5. La prima por riesgo de mercado es 6%.

**El Efecto Matemático en la Valuación (DCF):**
* **WACC Antiguo (2021):** $1\% + (1.5 \times 6\%) = 10\%$. Si proyectas los flujos de caja de CloudFast a 10 años y los descuentas al 10%, el Valor Presente de la empresa es de, digamos, $100 millones.
* **WACC Nuevo (2022):** $5\% + (1.5 \times 6\%) = 14\%$. Al subir la tasa libre de riesgo, el WACC salta al 14%. 
* Descuentas los *exactos mismos* flujos de caja futuros al 14%. Matemáticamente, el divisor $(1+0.14)^t$ es mucho más grande. 
* El Valor Presente de CloudFast se desploma de $100 millones a $60 millones. **La acción se desploma el 40% en bolsa.**

CloudFast no vendió menos productos, ni perdió clientes. Su negocio es idéntico. Pero el cambio en la macroeconomía alteró su WACC, destruyendo el 40% del valor contable matemático para sus accionistas. Es por esto que las acciones de "growth" ( alto beta) son castigadas tan duramente cuando los Bancos Centrales suben las tasas de interés.

---

## 8. Tareas y Evaluación de la Semana 24

**A. Lectura Obligatoria:**
* *Fundamentos de Finanzas Corporativas* (Ross, Westerfield, Jordan). Capítulo 12 (El Costo de Capital) y Capítulo 13 (Apalancamiento y Estructura de Capital).
* *Recomendado:* Repasa el concepto de Beta en la Semana 16 (Regresión Lineal).

**B. Preguntas de Reflexión:**
1. ¿Por qué el costo de la deuda se calcula "después de impuestos" en la fórmula del WACC, pero el costo del patrimonio NO se ajusta por impuestos?
2. ¿Qué le sucedería al WACC de una empresa si se endeuda masivamente (su deuda pasa del 0% al 90% de su estructura de capital)? El costo de deuda promedio bajaría (es más barata que el equity), ¿significa esto que el WACC siempre bajará y la empresa creará más valor? (Pista: Piensa en el riesgo de quiebra, $X_4$ del Z-Score visto la semana pasada).

**C. Ejercicio Matemático a entregar:**
Calcula el WACC de la minera "GoldRush Inc.":
* Tasa Libre de Riesgo ($R_f$): 3.5%
* Beta de la empresa ($\beta$): 1.1
* Prima por Riesgo de Mercado ($MRP$): 5.5%
* Costo de la deuda antes de impuestos ($r_d$): 7%
* Tasa de Impuestos: 30%
* Valor de Mercado del Patrimonio ($E$): $400 millones
* Valor de Mercado de la Deuda ($D$): $200 millones

Contesta:
1. Calcula el $r_e$ (Costo del Patrimonio) usando CAPM.
2. Calcula el $r_d$ (Costo de la Deuda después de impuestos).
3. Calcula los pesos $E/V$ y $D/V$. 
4. Integra todo en la fórmula maestra y halla el WACC final de GoldRush Inc. (Muestra todos los despejes matemáticos).
