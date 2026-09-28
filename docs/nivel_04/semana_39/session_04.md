# Semana 39 · Sesión 4: Caso de Estudio y Evaluación

## 8. Análisis de Caso: El colapso de Long-Term Capital Management (LTCM)
*Eres un regulador en 1998. el Fondo "LTCM" (gestionado por dos Premios Nobel de Economía, Merton y Scholes) usa la Teoría de Markowitz y matemáticas avanzadas para encontrar "ineficiencias" en el mercado.*

Tienen un portafolio masivamente diversificado en bonos de docenas de países. Su Ratio de Sharpe histórico era de 4.0 (prácticamente imposible, sin riesgo y con altísimo retorno). 

**La falla en la Teoría Moderna de Portafolios:**
Markowitz asume que la correlación histórica se mantendrá en el futuro. En agosto de 1998, Rusia entra en default y los inversores entran en pánico mundial. De repente, *todos* los mercados del mundo se vuelven a vender al mismo tiempo. La correlación de todos los activos del mundo saltó de 0 a **1.0** instantáneamente. 

Al moverse todos a la baja juntos, la diversificación de LTCM falló matemáticamente. El portafolio sumamente diversificado perdió el 90% de su valor en semanas y la FED tuvo que organizar un rescate de $3.6 billones.

**Lección de Inversión:** La Teoría de Markowitz funciona el 99% de los días normales, pero en las crisis extremas ("Black Swans"), las correlaciones convergen a 1. En el Nivel 4, los nuevos modelos de Asset Allocation buscan activos "anti-frágiles" (como el oro o la volatilidad misma) que suban precisamente cuando todo lo demás colapsa, para blindar los portafolios ante la ruptura de la correlación.

---

## 9. Tareas y Evaluación de la Semana 39

**A. Lectura y Práctica Obligatoria:**
* *Investments* (Bodie, Kane, Marcus). Capítulos sobre "Optimal Risky Portfolios" (Markowitz) y "The Capital Asset Pricing Model" (CAPM).
* *Lectura opcional:* "A Random Walk Down Wall Street" (Burton Malkiel) sobre la eficiencia del mercado y la importancia de la Asset Allocation.

**B. Preguntas de Reflexión:**
1. Explica la diferencia fundamental entre el "Riesgo Sistemático" y el "Riesgo No Sistemático". ¿Por qué el mercado financiero NO recompensa (no paga una prima de riesgo) a un inversor por asumir Riesgo No Sistemático?
2. Describe cómo el "Wealth Management" para un cliente multimillonario difiere de un fondo de "Asset Management" de BlackRock que cotiza en la bolsa para millones de clientes. ¿Por qué el Wealth Management cobra más comisiones?

**C. Ejercicio Práctico a entregar:**
Eres un Wealth Manager evaluando dos fondos de inversión para un cliente:
* **Fondo Alfa:** Retorno = 12%. Volatilidad ($\sigma$) = 15%.
* **Fondo Beta:** Retorno = 8%. Volatilidad ($\sigma$) = 5%.
* La Tasa Libre de Riesgo ($R_f$) actual en el mercado es del **3%**.

Contesta:
1. Calcula el **Ratio de Sharpe** para ambos fondos: $(R_p - R_f) / \sigma_p$.
2. Aunque el Fondo Alfa rinde más (12% vs 8%), ¿qué fondo es matemáticamente superior en términos de rentabilidad ajustada por riesgo? Justifica.
3. Si el cliente ultra conservador te dice "Quiero el fondo que rinde 12% porque necesito más dinero", ¿qué contraargumento basado en el Ratio de Sharpe y la Teoría de Markowitz le das para convencerlo de que rentabilidad absoluta no es la métrica correcta?

??? success "Solución del Ejercicio C"

    **1. Ratio de Sharpe de ambos fondos**

    $$S = \frac{R_p - R_f}{\sigma_p}$$

    *Fondo Alfa:*

    $$S_{Alfa} = \frac{12\% - 3\%}{15\%} = \frac{9}{15} = \mathbf{0.60}$$

    *Fondo Beta:*

    $$S_{Beta} = \frac{8\% - 3\%}{5\%} = \frac{5}{5} = \mathbf{1.00}$$

    **2. ¿Cuál es matemáticamente superior?**

    **El Fondo Beta, con claridad.** Su Sharpe de 1.00 supera en 67 % al 0.60 de Alfa.

    | | Fondo Alfa | Fondo Beta |
    |---|---|---|
    | Retorno | 12 % | 8 % |
    | Volatilidad | 15 % | 5 % |
    | Exceso sobre $R_f$ | 9 % | 5 % |
    | **Sharpe** | **0.60** | **1.00** |

    El Sharpe mide **cuánto retorno por encima del activo libre de riesgo se obtiene
    por cada unidad de riesgo asumida**. Beta entrega $\$1.00$ de exceso de retorno
    por cada punto de volatilidad; Alfa solo $\$0.60$.

    Alfa rinde más en términos absolutos, pero **paga con creces por ese retorno**:
    triplica la volatilidad para conseguir apenas 4 puntos porcentuales más.

    **3. El contraargumento para el cliente**

    Aquí está el argumento decisivo, y no es retórico sino aritmético:

    > *"Si lo que le preocupa es el retorno, puedo darle **más del 12 % asumiendo
    > exactamente el mismo riesgo** que el Fondo Alfa. Y lo hago con el Fondo Beta."*

    **La Línea de Asignación de Capital (CAL).** Si el cliente tolera una volatilidad
    del 15 %, se invierte en el Fondo Beta **apalancado 3 veces** (con $\$1$ propio y
    $\$2$ prestados a la tasa libre de riesgo del 3 %):

    $$\sigma_{cartera} = 3 \times 5\% = 15\% \quad (\text{idéntico a Alfa})$$

    $$R_{cartera} = 3 \times 8\% - 2 \times 3\% = 24\% - 6\% = \mathbf{18\%}$$

    | Con volatilidad del 15 % | Retorno |
    |---|---|
    | Fondo Alfa | 12 % |
    | **Fondo Beta apalancado 3×** | **18 %** |
    | | **+600 puntos básicos** |

    Comprobación con la ecuación de la CAL:

    $$R = R_f + S \times \sigma$$
    
    $$\text{Alfa:} \quad 3\% + 0.60 \times 15\% = 12\% \quad ✓$$
    
    $$\text{Beta:} \quad 3\% + 1.00 \times 15\% = 18\% \quad ✓$$

    **La conclusión que hay que transmitirle al cliente:** el retorno absoluto no es
    la métrica correcta porque **el nivel de riesgo se elige por separado** —vía
    apalancamiento o vía mezcla con activo libre de riesgo—. Lo único que no se puede
    fabricar es la **eficiencia** del gestor, y eso es justamente lo que mide el
    Sharpe. Se elige primero el fondo con mayor Sharpe, y *después* se ajusta el
    riesgo a la tolerancia del cliente.

    Y para un cliente **ultra conservador** hay una alternativa sin apalancamiento:
    mezclar Beta con el activo libre de riesgo. Un 60 % en Beta y 40 % en letras da
    $\sigma = 3\%$ y retorno $0.6(8) + 0.4(3) = 6\%$ — **la mitad de la volatilidad
    de Alfa** con un retorno digno.

    !!! warning "Los límites del Sharpe (y la lección de LTCM)"
        El propio caso de esta semana muestra por qué el ratio no basta. **LTCM
        reportaba un Sharpe histórico de 4.0** justo antes de perder el 90 % de su
        capital. Las limitaciones:

        * **Asume normalidad.** El Sharpe usa $\sigma$, que no distingue entre
          volatilidad al alza y a la baja, y subestima el riesgo cuando hay colas
          gordas o asimetría negativa.
        * **Es histórico y retrospectivo.** Estrategias que venden riesgo de cola
          —vender opciones, arbitrajes apalancados— muestran Sharpes altísimos
          durante años hasta el día en que estallan.
        * **Ignora la iliquidez.** Un activo que no cotiza a diario parece poco
          volátil simplemente porque no se marca a mercado.
        * **El apalancamiento tiene límites reales.** El ejemplo del 3× asume que se
          puede pedir prestado a $R_f$ ilimitadamente. En una crisis el crédito
          desaparece y llegan las llamadas de margen — precisamente lo que mató a LTCM.

        Por eso se complementa con el **ratio de Sortino** (que solo penaliza la
        volatilidad a la baja), el **máximo drawdown** y pruebas de estrés.
