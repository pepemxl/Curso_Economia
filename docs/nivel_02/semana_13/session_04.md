# Semana 13 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: "Refinanciamiento de deuda corporativa en tiempos de tasas altas"
*Eres el CFO (Director Financiero) de una empresa de logística. Tienes un préstamo corporativo de $10 millones a 5 años. Originalmente lo sacaste a tasa flotante, y el Banco Central acaba de subir las tasas del 5% al 12%.*

El banco te ofrece dos opciones de reestructuración de la deuda:
1. **Pasar a Sistema Francés:** Cuotas fijas anuales a 5 años al 12%.
2. **Pasar a Sistema Americano (Bullet):** Pagar solo intereses al 12% durante 5 años, y refinanciar los $10M al final del año 5.

**Tu análisis estratégico:**
1. **Sistema Francés:** Al ser tasa alta (12%) y a 5 años, el calculo matemático arroja una cuota anual altísima. Parte importante de tu Flujo de Caja Libre (FCF) se irá en pagar la deuda, dejando poco margen para repartir dividendos a los accionistas o hacer inversiones de crecimiento (CapEx).
2. **Sistema Americano:** Tu cuota anual será mucho más baja (solo el 12% de 10M = $1.2M). TU FCF queda aliviado. Sin embargo, transfieres el riesgo al futuro. Dentro de 5 años tendrás que pagar los $10M de golpe. Si para entonces las tasas bajaron, puedes refinanciar fácilmente; si subieron más, la empresa entra en riesgo de default (quiebra).

**Decisión:** Como CFO de una empresa que está generando buenos ingresos pero necesita reactivar su inversiónCapEx inmediatamente, eliges el **Sistema Americano**. Aceptas el riesgo de tasa futura a cambio de oxigenar tu flujo de caja actual. (*Un analista de riesgo bancario rechazaría esto si tu empresa tiene calificaciones crediticias bajas*).

---

## 7. Tareas y Evaluación de la Semana 13

**A. Lectura Obligatoria:**
* Ross, Westerfield, Jordan. *Fundamentos de Finanzas Corporativas*. Capítulo 4 y 5 (Sección de Anualidades y Perpetuidades) y apéndice sobre amortización de préstamos.

**B. Preguntas de Reflexión:**
1. En el Sistema Francés, ¿por qué el banco cobra más intereses al principio del préstamo incluso cuando tu cuota es siempre la misma? Explica la relación matemática entre el saldo insoluto y el cálculo del interés del periodo.
2. ¿Por qué el Sistema Americano es considerado el más riesgoso para el prestamista (el banco) pero el más cómodo a corto plazo para el prestatario (la empresa)?

**C. Ejercicio Matemático a entregar:**
1. **Perpetuidad:** Una acción preferente pagará un dividendo fijo de $8 cada año, de forma indefinida. Si los inversionistas exigen un rendimiento del 10% anual, ¿cuál es el Valor Presente (precio teórico) de esta acción preferente?
2. **Amortización Alemán:** Un préstamo de **$3,000** al 10% anual a ser pagado en 3 cuotas con **Sistema Alemán** (amortización de capital constante).
   * a) Calcula la cuota de amortización a capital fija que se pagará cada año.
   * b) Construye el cuadro de amortización de los 3 años (Saldo Inicial, Interés, Cuota Total, Saldo Final). Recuerda que en el Alemán, la cuota total varía, pero la amortización al capital es fija.


??? success "Solución del Ejercicio C"

    **1. Perpetuidad — acción preferente**

    Una perpetuidad paga un flujo constante para siempre. Su valor presente es:

    $$VP = \frac{D}{r} = \frac{8}{0.10} = \mathbf{\$80}$$

    El precio teórico de la acción preferente es **$\$80**.

    Conviene entender por qué una serie infinita da un número finito: el flujo del
    año 50 descontado al 10 % vale $8/(1.10)^{50} = \$0.068$, y el del año 100 vale
    prácticamente cero. La serie **converge**.

    *Sensibilidad al rendimiento exigido:* si los inversionistas pasaran a exigir
    12 % (por ejemplo, porque el banco central subió tasas), el precio caería a
    $8/0.12 = \$66.67$, un **−16.7 %**, sin que el dividendo cambiara ni un centavo.
    Es la mecánica de por qué la renta fija pierde valor cuando suben las tasas.

    **2. Sistema Alemán — préstamo de $3,000 al 10 % en 3 años**

    *a) Amortización a capital fija:*

    $$A = \frac{\text{Capital}}{n} = \frac{3{,}000}{3} = \mathbf{\$1{,}000 \text{ por año}}$$

    *b) Cuadro de amortización:*

    | Año | Saldo Inicial | Interés (10 %) | Amortización | Cuota Total | Saldo Final |
    |---|---|---|---|---|---|
    | 1 | 3,000 | 300 | 1,000 | **1,300** | 2,000 |
    | 2 | 2,000 | 200 | 1,000 | **1,200** | 1,000 |
    | 3 | 1,000 | 100 | 1,000 | **1,100** | 0 |
    | | | **600** | **3,000** | **3,600** | |

    Comprobaciones de que el cuadro está bien: la columna de amortización suma
    exactamente el capital prestado ($3{,}000$) y el saldo final del último año
    cierra en **cero**. Si no cuadra, hay un error.

    !!! tip "Alemán vs. Francés: cuál conviene"
        En el **Alemán** la cuota es **decreciente** ($1{,}300 \to 1{,}100$) porque el
        interés se calcula sobre un saldo que baja rápido y en línea recta.

        En el **Francés** la cuota sería **constante**: con estos datos,
        $C = 3{,}000 \times \frac{0.10}{1-(1.10)^{-3}} \approx \$1{,}206.34$ los tres
        años, y el total pagado sería $\approx \$3{,}619$ — unos **$\$19$ más de
        intereses** que en el Alemán.

        El Alemán siempre paga menos intereses en total, porque amortiza capital más
        rápido al principio. A cambio, exige mayor esfuerzo de caja en las primeras
        cuotas. El Francés se prefiere en crédito hipotecario al consumidor
        justamente porque la cuota fija es más fácil de presupuestar.

---
*¡Felicidades por completar la Semana 13! Ya dominas la matemática detrás de los créditos bancarios y las pensiones. En la Semana 14 entraremos de lleno en el mundo de la incertidumbre con la **Estadística Aplicada**: Medidas de tendencia central, dispersión y el análisis de riesgo.*