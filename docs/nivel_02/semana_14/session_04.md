# Semana 14 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El pelotón de caza de los Hedge Funds
*Gestionas un fondo de cobertura (Hedge Fund). Comparas tus dos mejores traders estrella.*

* **Trader A:** Tiene un retorno promedio anual del 25%, pero con una desviación estándar altísima del 40%. Es brillante, pero volátil. Sus "drawdowns" (caídas de capital máximas) llegan al -35%.
* **Trader B:** Tiene un retorno promedio del 15%, con una desviación estándar minúscula del 4%. Nunca tiene malos meses, sube lento pero constante (como un bono).

**La trampa de la "Media":**
El gerente del fondo quiere despedir al Trader B porque "sus retornos son la mitad de buenos que los del Trader A". 
Tu análisis estadístico lo detiene: El Trader A toma riesgos asimétricos negativos. En un año malo puede borrar toda la ganancia de 3 años buenos (Riesgo de Cola Negra o *Black Swan*). El Trader B genera un "Sharpe Ratio" altísimo (Retorno ajustado por volatilidad que veremos en el Nivel 4). 

*Acción:* No despides al Trader B, sino que hiper-apalancas su capital, porque su baja desviación estándar permite usar deuda bancaria barata para multiplicar su retorno seguro. Al Trader A se le reduce el capital asignado por riesgo de wipe-out.

---

## 8. Tareas y Evaluación de la Semana 14

**A. Lectura Obligatoria:**
* *Estadística para Administración y Economía* de Anderson, Sweeney y Williams. Capítulos 2 y 3 (Descriptiva, Tendencia central y Dispersión).

**B. Preguntas de Reflexión:**
1. ¿Por qué en finanzas se suele elevar al cuadrado las desviaciones para calcular la varianza, y por qué se usa $(n - 1)$ en el denominador al calcular una muestra en lugar de $n$?
2. Explica con un ejemplo financiero por qué confiar únicamente en la "Media" de los retornos históricos de un índice bursátil puede ser una decisión catastrófica para un fondos de pensiones.

**C. Ejercicio Estadístico a entregar:**
Los siguientes datos representan la tasa de retorno anual (en %) de un portafolio inmobiliario durante los últimos 8 años:
`[8, 12, -4, 15, 9, 11, -2, 13]`

1. Calcula la Media (Promedio).
2. Calcula la Mediana (Recuerda ordenar de menor a mayor primero).
3. Calcula la Varianza (Muestral, divisor $n - 1$).
4. Calcula la Desviación Estándar y el Coeficiente de Variación. Interpreta qué significa el resultado del CV en términos de riesgo.


??? success "Solución del Ejercicio C"

    Datos: `[8, 12, -4, 15, 9, 11, -2, 13]`, con $n = 8$.

    **1. Media**

    $$\bar{x} = \frac{8+12-4+15+9+11-2+13}{8} = \frac{62}{8} = \mathbf{7.75\%}$$

    **2. Mediana**

    Ordenamos: $-4,\; -2,\; 8,\; 9,\; 11,\; 12,\; 13,\; 15$

    Con $n$ par, es el promedio de los dos valores centrales (4.º y 5.º):

    $$Me = \frac{9 + 11}{2} = \mathbf{10\%}$$

    Nota que **la mediana (10 %) es mayor que la media (7.75 %)**. Eso indica
    asimetría negativa: los dos años malos ($-4$ y $-2$) arrastran el promedio hacia
    abajo más de lo que refleja el comportamiento típico del portafolio.

    **3. Varianza muestral**

    $$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$$

    | $x_i$ | $x_i - \bar{x}$ | $(x_i-\bar{x})^2$ |
    |---|---|---|
    | 8 | 0.25 | 0.0625 |
    | 12 | 4.25 | 18.0625 |
    | −4 | −11.75 | 138.0625 |
    | 15 | 7.25 | 52.5625 |
    | 9 | 1.25 | 1.5625 |
    | 11 | 3.25 | 10.5625 |
    | −2 | −9.75 | 95.0625 |
    | 13 | 5.25 | 27.5625 |
    | | **Suma** | **343.5** |

    $$s^2 = \frac{343.5}{7} = \mathbf{49.07}$$

    **4. Desviación estándar y Coeficiente de Variación**

    $$s = \sqrt{49.07} = \mathbf{7.01\%}$$

    $$CV = \frac{s}{\bar{x}} = \frac{7.01}{7.75} = \mathbf{0.904 \;\; (90.4\%)}$$

    **Interpretación del CV — riesgo por unidad de retorno**

    Un $CV$ de $0.90$ significa que **por cada 1 % de retorno esperado, el
    inversionista asume 0.90 % de volatilidad**. Es una relación riesgo-retorno
    **pobre**: la dispersión casi iguala al premio.

    El CV sirve precisamente para comparar activos de escalas distintas. Si otro
    fondo rindiera 20 % con desviación de 12 %, su $CV = 0.60$ — es *más* volátil en
    términos absolutos, pero **más eficiente**, porque compensa mejor cada unidad de
    riesgo asumida. Entre dos alternativas, se prefiere el CV más bajo.

    !!! note "Por qué el divisor es $n-1$ y no $n$"
        Se usan $n-1$ **grados de libertad** porque la media $\bar{x}$ fue estimada
        a partir de los mismos datos. Dividir entre $n$ subestimaría sistemáticamente
        la varianza poblacional. Con solo 8 observaciones la diferencia es notable:
        $343.5/8 = 42.94$ frente a $49.07$.

        En Excel: `=VAR.S()` y `=DESVEST.M()` usan $n-1$ (muestral, lo correcto para
        series de retornos); `=VAR.P()` y `=DESVEST.P()` usan $n$.

---
*¡Felicidades por completar la Semana 14! Ya sabes medir el riesgo básico. En la Semana 15 dejaremos los datos pasados y entraremos en el futuro con la Teoría de Probabilidades y las Distribuciones de Probabilidad (Normal, Binomial y Poisson).*