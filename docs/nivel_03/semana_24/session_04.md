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

??? success "Solución del Ejercicio C"

    **1. Costo del Patrimonio ($r_e$) por CAPM**

    $$r_e = R_f + \beta \times MRP$$

    $$r_e = 3.5\% + 1.1 \times 5.5\% = 3.5\% + 6.05\% = \mathbf{9.55\%}$$

    Lectura: los accionistas exigen 9.55 % anual. De ese total, $3.5\%$ es lo que
    obtendrían sin riesgo (bono soberano) y **$6.05\%$ es la compensación por asumir
    el riesgo de GoldRush**. Con $\beta = 1.1$, la acción amplifica un 10 % los
    movimientos del mercado: si el índice sube 10 %, se espera que GoldRush suba 11 %
    (y que caiga 11 % cuando el índice caiga 10 %).

    **2. Costo de la Deuda después de impuestos**

    $$r_d^{(neto)} = r_d \times (1 - t) = 7\% \times (1 - 0.30) = \mathbf{4.90\%}$$

    La empresa paga 7 % al banco, pero como los intereses son **deducibles**, el
    fisco le devuelve el 30 % de ese gasto. El costo real que soporta es 4.90 %.
    Esos $2.10$ puntos porcentuales son el **escudo fiscal de la deuda**, y son la
    razón matemática de que la deuda sea más barata que el patrimonio.

    **3. Pesos de la estructura de capital**

    $$V = E + D = 400 + 200 = \$600 \text{ millones}$$

    $$\frac{E}{V} = \frac{400}{600} = 0.6667 \;(66.67\%) \qquad \frac{D}{V} = \frac{200}{600} = 0.3333 \;(33.33\%)$$

    **4. WACC**

    $$WACC = \frac{E}{V} \cdot r_e + \frac{D}{V} \cdot r_d (1-t)$$

    $$WACC = 0.6667 \times 9.55\% + 0.3333 \times 4.90\%$$

    $$WACC = 6.3667\% + 1.6333\%$$

    $$\mathbf{WACC = 8.00\%}$$

    | Fuente | Peso | Costo | Contribución |
    |---|---|---|---|
    | Patrimonio | 66.67 % | 9.55 % | 6.3667 % |
    | Deuda (neta de impuestos) | 33.33 % | 4.90 % | 1.6333 % |
    | | | **WACC** | **8.00 %** |

    !!! tip "Qué significa este 8 % y dónde se usa"
        El WACC es la **tasa mínima de rendimiento** que GoldRush debe obtener para
        no destruir valor. Un proyecto que rinda 7 % parece rentable, pero **destruye
        valor**: no alcanza a pagar lo que cuestan el capital y la deuda que lo
        financian.

        Es la tasa que usarás para descontar el FCFF en el DCF (Semana 37) y para
        evaluar proyectos por VAN (Semana 25).

        **Dos advertencias sobre los pesos:** se usan valores de **mercado**, nunca
        contables — el patrimonio contable puede diferir enormemente de la
        capitalización bursátil. Y el WACC **no es constante**: si GoldRush se
        endeudara más, el $\beta$ del patrimonio subiría (mayor riesgo financiero) y
        con él $r_e$, compensando parcialmente el ahorro de sustituir capital por
        deuda barata. Ese tira y afloja es justamente el tema de Modigliani-Miller
        en la Semana 26.
