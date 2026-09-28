# Semana 25 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: La Oil Major y el campos de shale
*Eres el CFO de una petrolera internacional. El precio del petróleo está alto. Tienes dos proyectos de exploración en la mesa (Mutuamente Excluyentes).*

* **Proyecto A (Pozo Tradicional):** Costo de perforación $500 Millones. Genera una enorme producción en los primeros 3 años y luego el pozo se seca. Retorno (TIR) altísimo de 40%, pero poca reutilización de la infraestructura. VAN = $800 Millones.
* **Proyecto B (Campo de Fracturación / Shale):** Costo de perforación $2,000 Millones. Genera producción constante durante 15 años. Retorno (TIR) más modesto del 18%, pero crea infraestructura de gasoductos para futuros pozos. VAN = $1,500 Millones.

**El Conflicto en la Junta Directiva:**
El equipo geológico presiona por el Proyecto A porque "rinde el doble (40% vs 18%)". 
Tu análisis de Presupuesto de Capital detiene el argumento: *"El Proyecto A crea $800 millones de riqueza absoluta. El Proyecto B crea $1,500 millones. Nuestro objetivo como directivos no es maximizar el porcentaje de retorno, sino maximizar los dólares absolutos en el bolsillo de los accionistas"*. 

**Decision Final:** Apruebas el Proyecto B (VAN más alto). El Proyecto B además te da infraestructura de gasoductos que actúa como "opción real" (Real Option) para perforar 5 pozos más en el futuro.

---

## 8. Tareas y Evaluación de la Semana 25

**A. Lectura Obligatoria:**
* *Fundamentos de Finanzas Corporativas* (Ross, Westerfield, Jordan). Capítulos 8 y 9 (Presupuesto de Capital y Análisis de Flujos de Efectivo).
* Repaso de la Semana 11 (Valor del dinero en el tiempo) y Semana 24 (WACC).

**B. Preguntas de Reflexión:**
1. ¿Por qué dos proyectos independientes con flujos de caja convencionales siempre darán la misma decisión de aceptar/rechazar tanto usando el VAN como usando la TIR, pero al ser proyectos *mutuamente excluyentes* pueden dar decisiones contradictorias?
2. ¿Por qué un proyecto con un incredible VAN de $5 mil millones pero con un Payback Descontado de 12 años podría ser rechazado por la mesa de directivos de una empresa joven startup? (Pista: Liquidez y Riesgo de Cola).

**C. Ejercicio Matemático a entregar:**
La empresa "CyberSec Corp" tiene un WACC del 8%. Está evaluando un proyecto de desarrollo de un nuevo software antivirus.
* Inversión Inicial (Año 0): -$2,000,000
* Flujos de Caja esperados: Año 1: $500,000 | Año 2: $800,000 | Año 3: $1,200,000 | Año 4: $1,000,000

Contesta:
1. Calcula manualmente el VAN del proyecto descontando cada año a la tasa del 8%. ¿Aceptas o rechazas el proyecto?
2. Calcula mentalmente o estima si la TIR será mayor o menor al 8%. Justifica matemáticamente tu respuesta basándote en el resultado del VAN. 
3. Calcula el Payback Descontado del proyecto. ¿En qué año y fracción de año la empresa logra recuperar sus $2,000,000 invertidos en valor presente?

??? success "Solución del Ejercicio C"

    **1. Valor Actual Neto al 8 %**

    $$VAN = -I_0 + \sum_{t=1}^{n} \frac{FC_t}{(1 + WACC)^t}$$

    | Año | Flujo | Factor de descuento $1/(1.08)^t$ | Valor Presente |
    |---|---|---|---|
    | 0 | −2,000,000 | 1.0000 | −2,000,000.00 |
    | 1 | 500,000 | 0.9259 | 462,962.96 |
    | 2 | 800,000 | 0.8573 | 685,871.06 |
    | 3 | 1,200,000 | 0.7938 | 952,598.69 |
    | 4 | 1,000,000 | 0.7350 | 735,029.85 |
    | | | **Suma de VP** | **2,836,462.56** |
    | | | **VAN** | **+836,462.56** |

    $$\mathbf{VAN = +\$836{,}462.56}$$

    **Se ACEPTA el proyecto.** Genera $\$836{,}463$ de valor presente **por encima**
    del 8 % que exigen los proveedores de capital. Si CyberSec cotiza en bolsa y el
    mercado cree en estas proyecciones, su capitalización debería subir
    aproximadamente en ese monto.

    **2. ¿La TIR será mayor o menor al 8 %?**

    **Mayor al 8 %, con certeza matemática.**

    El razonamiento no requiere calcular nada. La TIR es, por definición, la tasa que
    hace $VAN = 0$. El VAN es una **función decreciente** de la tasa de descuento:
    cuanto más se descuenta, menos valen los flujos futuros.

    Como al 8 % el VAN es **positivo** ($+\$836{,}463$), hay que **subir** la tasa
    para empujarlo hasta cero. Por tanto $TIR > 8\%$.

    *Verificación:* la TIR real es **23.41 %**, casi el triple del costo de capital.

    Esta es la regla general que conviene interiorizar:

    | Si… | Entonces… | Decisión |
    |---|---|---|
    | $VAN > 0$ | $TIR > WACC$ | Aceptar |
    | $VAN = 0$ | $TIR = WACC$ | Indiferente |
    | $VAN < 0$ | $TIR < WACC$ | Rechazar |

    **3. Payback Descontado**

    Se acumulan los **valores presentes** (no los flujos nominales) hasta cubrir la
    inversión:

    | Año | VP del flujo | VP acumulado | Falta por recuperar |
    |---|---|---|---|
    | 1 | 462,962.96 | 462,962.96 | 1,537,037.04 |
    | 2 | 685,871.06 | 1,148,834.02 | 851,165.98 |
    | 3 | 952,598.69 | 2,101,432.71 | **recuperado** ✓ |
    | 4 | 735,029.85 | 2,836,462.56 | |

    La recuperación ocurre **durante el año 3**. La fracción:

    $$\text{Fracción} = \frac{851{,}165.98}{952{,}598.69} = 0.8935$$

    $$\text{Payback Descontado} = 2 + 0.8935 = \mathbf{2.89 \text{ años}}$$

    Es decir, **2 años y 10.7 meses** (unos 2 años, 10 meses y 21 días).

    !!! tip "Descontado vs. simple, y por qué el payback nunca decide solo"
        El payback **simple** (sin descontar) daría: $500 + 800 = 1{,}300$ al año 2,
        faltan $700$ de los $1{,}200$ del año 3 → $2 + 700/1200 = \mathbf{2.58}$ años.

        La diferencia de casi cuatro meses es exactamente el costo del dinero en el
        tiempo, que la versión simple ignora. **Siempre usa el descontado.**

        Aun así, el payback tiene un defecto que ninguna versión corrige: **ignora
        por completo lo que ocurre después de la recuperación.** Aquí desprecia el
        millón del año 4 —que en valor presente son $\$735{,}030$, casi todo el VAN
        del proyecto—. Un proyecto con payback rápido pero sin flujos posteriores
        puede ser mucho peor que otro de recuperación lenta y cola larga.

        Úsalo como **filtro de liquidez** (¿cuánto tiempo estoy expuesto?), nunca
        como criterio de decisión. **Quien decide es el VAN.**
