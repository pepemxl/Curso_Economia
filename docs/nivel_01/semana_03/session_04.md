# Semana 3 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El "Foso" de Warren Buffett y los Beneficios Monopolísticos
Warren Buffett, uno de los inversores más grandes de la historia, busca empresas que cotizan en bolsa que tengan un "foso económico" (Economic Moat). 
¿Qué es un foso? Es una barrera de entrada que da a la empresa **poder de monopolio u oligopolio**.

* **El caso Coca-Cola vs. Refresco Genérico:** La marca Coca-Cola es un foso. Aunque el costo de producción de un refresco de cola es de unos centavos (CMg constante y bajo), Coca-Cola cobra un sobreprecio (Premium) importante. No es una competencia perfecta; tiene poder de fijación de precios porque el consumidor está dispuesto a pagar más por la marca.
* **Impacto Financiero:** Las empresas en competencia perfecta tienen márgenes de beneficio muy bajos (ROIC bajo) y no son atractivas para inversión a largo plazo. Las empresas con características de monopolio u oligopolio (como patentes de farmacéuticas, sistemas operativos de Microsoft, redes de Visa) pueden aumentar precios sin perder clientes (demanda inelástica combinada con poder de mercado), generando flujos de caja libre (FCF) masivos.
* El analista financiero valora mucho más alto (mayor P/E, mayores múltiplos) a una empresa con poder de monopolio que a una en competencia perfecta.

---


## 8. Tareas y Evaluación de la Semana 3

**A. Lectura Obligatoria:**
* Mankiw, N. Gregory. *Principios de Economía*. Capítulos 13 (Costos de producción), 14 (Competencia perfecta) y 15 (Monopolio).

**B. Preguntas de Reflexión:**
1. ¿Por qué una empresa competidora perfecta sigue operando a corto plazo incluso si tiene pérdidas económicas (siempre que el precio sea mayor que el Costo Variable Medio)?
2. Menciona una empresa cotizada en bolsa actual que consideres que opera en un oligopolio y explica cuál es su principal barrera de entrada (poder de mercado).

**C. Ejercicio Práctico a entregar:**
Una empresa produce tabletas gráficas. Su Costo Fijo Total es de $5,000. Su Costo Variable Total se comporta de forma no lineal según la producción ($Q$), con la siguiente función:
$CVT = 10Q + 0.01Q^2$
El precio de mercado de cada tabletas es constante en $50 (asumimos mercado altamente competitivo por simplicidad).

Contesta:
1. Escribe la fórmula del Costo Total (CT) y del Costo Marginal (CMg). *(Pista: El CMg es la derivada del CT respecto a Q).*
2. ¿A qué cantidad ($Q$) maximiza sus beneficios la empresa? Establece la condición $P = CMg$ y resuelve la ecuación matemática. *(Recuerda que es una ecuación cuadrática).*
3. Calcula el Beneficio Económico Total para esa cantidad óptima de producción.

??? success "Solución del Ejercicio C"

    **1. Costo Total y Costo Marginal**

    El Costo Total es la suma del fijo y el variable:

    $$CT = CFT + CVT = 5000 + 10Q + 0.01Q^2$$

    El Costo Marginal es la derivada del CT respecto a $Q$:

    $$CMg = \frac{d\,CT}{dQ} = 10 + 0.02Q$$

    (El costo fijo desaparece al derivar: por definición no cambia con la producción.)

    **2. Cantidad que maximiza el beneficio**

    En competencia perfecta la empresa es precio-aceptante, así que $IMg = P = 50$.
    La condición de óptimo es $P = CMg$:

    $$50 = 10 + 0.02Q$$
    
    $$40 = 0.02Q \Longrightarrow Q^* = 2{,}000 \text{ unidades}$$

    **3. Beneficio Económico Total**

    $$IT = P \times Q = 50 \times 2{,}000 = 100{,}000$$
    
    $$CT = 5000 + 10(2{,}000) + 0.01(2{,}000)^2 = 5{,}000 + 20{,}000 + 40{,}000 = 65{,}000$$
    
    $$\pi = IT - CT = 100{,}000 - 65{,}000 = \mathbf{35{,}000}$$

    **Comprobación de que conviene producir:** el Costo Variable Medio en $Q^*$ es
    $CVMe = (10Q + 0.01Q^2)/Q = 10 + 0.01(2{,}000) = 30$, muy por debajo del precio
    de $50$. La empresa cubre todo su costo variable y aún aporta $\$40{,}000$ para
    amortizar los $\$5{,}000$ de costo fijo.

    !!! warning "Corrección al enunciado"
        El enunciado sugiere que hay que resolver "una ecuación cuadrática". No es
        así: el **costo total** es cuadrático, pero el **costo marginal** es su
        derivada, y por tanto **lineal**. La condición $P = CMg$ da una ecuación de
        primer grado. Solo aparecería una cuadrática si el CVT fuera cúbico
        (la forma en S del manual clásico).

---
