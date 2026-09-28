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
Gestionas un portafolio accionario valorado en **$5,000,000**. Descargas el historial y calculas que la volatilidad diaria ($\sigma_{diaria}$) es del **2%** (0.02). El promedio de retorno diario ($\mu$) será asumido como 0% para ser conservadores. Necesitas calcular el riesgo al **99% de confianza** ($Z = 2.326$).

Contesta y muestra las fórmulas:
1. Calcula el **VaR Paramétrico** para 1 día. ¿Cuánto es la máxima pérdida esperada en un día normal?
2. Calcula el **VaR para 10 días**. (Fórmula: $VaR_{10d} = VaR_{1d} \times \sqrt{10}$). ¿Por qué no se multiplica por 10 directamente?
3. Debido a tus cálculos, decides hacer un **Hedge** vendiendo Futuros del S&P 500. Si tu portafolio tiene una Beta ($\beta$) de 1.2 respecto al S&P 500, y el valor del contrato de futuro del S&P 500 es de $250,000. ¿Cuántos contratos de futuros tienes que vender para cubrir perfectamente tu riesgo de mercado? (Fórmula Hedge: $\text{Nº Contratos} = (\text{Valor Portafolio} \times \beta) / \text{Valor Contrato Futuro}$).

??? success "Solución del Ejercicio C"

    **1. VaR Paramétrico a 1 día, 99 % de confianza**

    $$VaR_{1d} = V \times Z \times \sigma_{diaria}$$

    $$VaR_{1d} = \$5{,}000{,}000 \times 2.326 \times 0.02$$

    $$\mathbf{VaR_{1d} = \$232{,}600}$$

    **Cómo se enuncia correctamente:** *"Con un 99 % de confianza, la pérdida del
    portafolio en un día no excederá $\$232{,}600$."*

    O, dicho al revés y de forma más útil para el gestor: **hay un 1 % de
    probabilidad de perder más de $\$232{,}600$ en un solo día.** Con ~252 días
    hábiles, eso son unos **2 o 3 días al año** en que se espera superar ese umbral.
    Que ocurra no significa que el modelo falle; que ocurra 15 veces, sí.

    **2. VaR a 10 días**

    $$VaR_{10d} = VaR_{1d} \times \sqrt{10} = \$232{,}600 \times 3.1623$$

    $$\mathbf{VaR_{10d} = \$735{,}545.78}$$

    **¿Por qué $\sqrt{10}$ y no $10$?**

    Porque **la varianza escala con el tiempo, pero la desviación estándar escala con
    su raíz cuadrada.** Bajo el supuesto de retornos independientes e idénticamente
    distribuidos:

    $$\sigma^2_{T} = T \times \sigma^2_{1d} \;\Longrightarrow\; \sigma_T = \sqrt{T} \times \sigma_{1d}$$

    Intuitivamente: si los retornos diarios son independientes, **las pérdidas y
    ganancias se cancelan parcialmente entre sí**. Diez días malos consecutivos son
    mucho menos probables que un día malo multiplicado por diez. La raíz cuadrada
    captura ese efecto de diversificación temporal.

    Multiplicar por 10 daría $\$2{,}326{,}000$ y **sobreestimaría el riesgo en más
    del triple**, obligando a inmovilizar capital innecesariamente.

    (El horizonte de 10 días no es casual: es el que **Basilea** exige para el
    riesgo de mercado de la cartera de negociación.)

    **3. Cobertura con futuros del S&P 500**

    $$N_{contratos} = \frac{V_{portafolio} \times \beta}{V_{contrato}}$$

    $$N = \frac{\$5{,}000{,}000 \times 1.2}{\$250{,}000} = \frac{\$6{,}000{,}000}{\$250{,}000}$$

    $$\mathbf{N = 24 \text{ contratos a vender (posición corta)}}$$

    **Por qué entra la Beta.** El portafolio no se mueve igual que el índice: con
    $\beta = 1.2$, amplifica un 20 % los movimientos del mercado. Si el S&P cae 10 %,
    el portafolio cae ~12 %, es decir $\$600{,}000$ y no $\$500{,}000$.

    Cubrir solo $\$5$ millones nominales dejaría **un 20 % de la exposición sin
    cubrir**. Por eso se cubre la **exposición ajustada por beta** de $\$6$ millones:
    es el equivalente del portafolio expresado en unidades de índice.

    **Verificación de la cobertura** ante una caída del 10 % en el S&P:

    | | Cálculo | Resultado |
    |---|---|---|
    | Pérdida del portafolio | $5{,}000{,}000 \times 10\% \times 1.2$ | −$600,000 |
    | Ganancia en los futuros cortos | $24 \times 250{,}000 \times 10\%$ | +$600,000 |
    | **Neto** | | **$0** ✓ |

    !!! warning "Lo que esta cobertura sí hace, y lo que no"
        La cobertura es **simétrica**: si el mercado *sube* 10 %, el portafolio gana
        $\$600{,}000$ y los futuros pierden $\$600{,}000$. **Se renuncia al alza
        igual que se elimina la baja.** No es un seguro (como el put de la Semana 30),
        es una neutralización.

        Además, esta operación solo elimina el **riesgo sistemático** ($\beta$). El
        **riesgo idiosincrásico** —que una empresa concreta de tu cartera colapse por
        un fraude— sobrevive intacto: los futuros del índice no cubren eso.

        Consideraciones prácticas que el ejercicio simplifica: los contratos son
        **indivisibles** (si salieran 24.7, hay que elegir 24 o 25 y aceptar cobertura
        imperfecta); el $\beta$ **no es estable** en el tiempo y obliga a rebalancear;
        y la posición corta exige **margen inicial y llamadas de margen diarias**, que
        consumen liquidez justo cuando el mercado se mueve en contra.

    !!! danger "El talón de Aquiles del VaR paramétrico"
        Todo el cálculo asume **normalidad** de los retornos, y los mercados reales
        tienen **colas gordas**: los eventos extremos ocurren mucho más seguido de lo
        que predice la campana de Gauss.

        Peor aún, el VaR responde *"¿cuál es mi pérdida máxima en el 99 % de los
        casos?"* pero **no dice absolutamente nada sobre el 1 % restante**. Podría ser
        $\$300{,}000$ o $\$3$ millones — el modelo no distingue.

        Por eso Basilea III migró al **Expected Shortfall (CVaR)**, que responde la
        pregunta correcta: *"si estoy en ese peor 1 %, ¿cuánto pierdo en promedio?"*.
        El VaR mide dónde empieza la cola; el ES mide qué tan profunda es.
