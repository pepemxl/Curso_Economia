# Semana 22 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: La narco-economía del EBITDA en las Telecomunicaciones
*Eres un analista de renta fija evalUando comprar los bonos de una gran empresa de telecomunicaciones (ej. estilo AT&T o Vodafone).*

La empresa presume en sus presentaciones de titulares: *"Generamos un EBITDA récord de $10,000 millones este año"*. El CEO propone pagar un dividendo gigantesco usando ese dinero.

**Tu Autopsia Financiera:**
1. **La trampa del EBITDA:** Una empresa de telecom requiere laying miles de kilómetros de cable de fibra óptica y construir torres celulares cada año para seguir compitiendo. Ese desgaste es "Depreciación". El EBITDA lo ignora.
2. **La Realidad del FCF:** Tomas el EBITDA de $10,000M. Le restas impuestos ( aprox $2,000M). Le restas el **CapEx** requerido para mantener la red viva y expandirla ($5,000M). Le restas aumento en capital de trabajo ($500M). 
3. **El Resultado:** El FCFF real es de solo $2,500M. 
4. **El Verdicto:** Si la empresa paga $4,000M en dividendos (basándose en su EBITDA), destruirá su flujo de caja. Tendrá que emitir más deuda ($1,500M) para pagar el dividendo que prometió. Rápidamente, advertimos a los tenedores de bonos que el dividendo es suicida y la calificación crediticia de la empresa debe ser degradada a "Bonos Basura" (High Yield/Junk).

---

## 7. Tareas y Evaluación de la Semana 22

**A. Lectura Obligatoria:**
* *Fundamentos de Finanzas Corporativas* (Ross, Westerfield, Jordan). Capítulo 3 (Análisis de Estados Financieros y Dupont) y lectura de Capítulo sobre Flujos de Caja y Valuación de Empresas.
* *Lectura recomendada:* Cartas de Warren Buffett a accionistas de Berkshire Hathaway (Busca "Buffett EBITDA quote" para leer sus argumentos sobre la depreciación y los capex fantasma).

**B. Preguntas de Reflexión:**
1. Basado en el Modelo Dupont, describe una empresa que tenga un ROE alto totalmente impulsado por el "Multiplicador del Capital". ¿Qué le pasaría a ese ROE si el Banco Central sube las tasas de interés de forma agresiva?
2. ¿Por qué el EBITDA puede ser una métrica engañosa para empresas de software y tecnología en comparación con empresas de aviación o acero? (Pista: Diferencia de CapEx y Depreciación).

**C. Ejercicio Práctico a entregar:**
La empresa "LogisticsPro" reporta su año fiscal:
* Ventas: $5,000,000
* Utilidad Neta: $300,000
* Activos Totales: $2,500,000
* Patrimonio: $1,000,000 (Lo demás es deuda)
* EBITDA: $600,000
* Depreciación: $100,000
* Tasa de Impuestos: 25% (Nota: Para simplificar, asume que los impuestos pagados son exactamente el 25% del EBT. El EBT es el EBIT menos gastos financieros. Asumamos que el EBIT = $500,000 y el Gasto Financiero fue de $50,000. El EBT = $450,000. Impuestos = $112,500. Comprueba que la Utilidad Neta cuadra con el inventario de cuentas dadas).
*(Nota 2: La Utilidad Neta fue $300,000, para que ignore el desglose impositivo y se focalice en las fórmulas que te doy abajo).*

Contesta:
1. **Análisis Dupont:** Usa los datos (Ventas, Utilidad Neta, Activos Totales, Patrimonio) para calcular los 3 componentes del modelo Dupont y comprueba que el ROE final es del 30%. (Muestra las 3 multiplicaciones).
2. **Cálculo de FCFF:** Usando el EBITDA de $600k, Depreciación de $100k, y asumiendo que el EBIT es de $500k. Calcula el NOPAT ($EBIT \times (1 - 0.25)$). 
3. Si la empresa tuvo un CapEx de $150,000 y un aumento en capital de trabajo de $50,000, ¿cuál es el Flujo de Caja Libre de la Firma (FCFF)? Muestra el desglose paso a paso.

??? success "Solución del Ejercicio C"

    **1. Análisis Dupont de "LogisticsPro"**

    El modelo descompone el ROE en tres palancas independientes:

    $$ROE = \underbrace{\frac{UN}{Ventas}}_{\text{Margen}} \times \underbrace{\frac{Ventas}{Activos}}_{\text{Rotación}} \times \underbrace{\frac{Activos}{Patrimonio}}_{\text{Apalancamiento}}$$

    *Componente 1 — Margen Neto (rentabilidad):*

    $$\frac{300{,}000}{5{,}000{,}000} = 0.06 = \mathbf{6\%}$$

    *Componente 2 — Rotación de Activos (eficiencia):*

    $$\frac{5{,}000{,}000}{2{,}500{,}000} = \mathbf{2.0\times}$$

    *Componente 3 — Multiplicador de Apalancamiento (financiamiento):*

    $$\frac{2{,}500{,}000}{1{,}000{,}000} = \mathbf{2.5\times}$$

    *Producto de los tres:*

    $$ROE = 0.06 \times 2.0 \times 2.5 = 0.30 = \mathbf{30\%} \quad ✓$$

    **Comprobación directa:** $300{,}000 / 1{,}000{,}000 = 30\%$ ✓

    !!! warning "De dónde sale realmente ese 30 %"
        Un ROE del 30 % suena espectacular, pero el Dupont revela su origen: el
        margen es modesto (6 %) y la eficiencia es normal (2.0×). **El
        apalancamiento de 2.5× es lo que infla el resultado.**

        Traducido: de los $\$2.5$ millones de activos, **$\$1.5$ millones son deuda**
        ($2{,}500{,}000 - 1{,}000{,}000$). La empresa opera con 60 % de deuda sobre
        activos.

        Sin apalancamiento (financiada 100 % con patrimonio), su ROE sería
        $6\% \times 2.0 = 12\%$. El resto —18 puntos porcentuales— es **riesgo
        financiero, no talento operativo**. Y ese mismo apalancamiento multiplica las
        pérdidas cuando el ciclo se voltea. Es exactamente la razón por la que se
        descompone el ROE en lugar de mirarlo como un solo número.

    **2. Cálculo del NOPAT**

    $$NOPAT = EBIT \times (1 - t) = 500{,}000 \times (1 - 0.25) = \mathbf{\$375{,}000}$$

    El NOPAT es la utilidad operativa después de impuestos **como si la empresa no
    tuviera deuda**. Se parte del EBIT, no del EBT, precisamente para excluir el
    efecto del financiamiento: el FCFF pertenece a *todos* los proveedores de capital
    (accionistas **y** acreedores), así que el ahorro fiscal de la deuda no se cuenta
    aquí — ya está recogido en el WACC (Semana 24).

    **3. Flujo de Caja Libre de la Firma (FCFF)**

    $$FCFF = NOPAT + D\&A - CapEx - \Delta \text{Capital de Trabajo}$$

    | Concepto | Monto |
    |---|---|
    | NOPAT | 375,000 |
    | (+) Depreciación y Amortización | 100,000 |
    | (−) CapEx | (150,000) |
    | (−) Aumento en Capital de Trabajo | (50,000) |
    | **= FCFF** | **275,000** |

    **FCFF = $275,000.**

    Los signos, uno a uno: la **D&A se suma** porque redujo el EBIT sin salida de
    caja; el **CapEx se resta** porque es caja real que sale a mantener la capacidad
    productiva; y el **aumento de capital de trabajo se resta** porque más inventario
    o más cartera por cobrar inmovilizan efectivo.

    Estos $\$275{,}000$ son lo que se descuenta al WACC en un modelo DCF (Semana 37).
    Nota la distancia con el EBITDA de $\$600{,}000$: **el EBITDA sobreestima la caja
    disponible en más del doble**, porque ignora impuestos, inversión y capital de
    trabajo. Por eso se dice que el EBITDA no es flujo de caja.
