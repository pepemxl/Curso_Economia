# Semana 23 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: El "Supuesto" Z-Score JGA y JGB
*Eres un gestor de un fondo de pensiones en 2007, Evaluando dos empresas legendarias del sector inmobiliario. Ambos bancos tienen puertas de madera caoba y ascensores de oro.*

Aplicas la fórmula Z-Score a sus balances del año 2006.
* **Empresa Inmobiliaria "JGA"** tiene un Z-Score de **3.5**. Tiene Capital de Trabajo alto, y sus Utilidades Retenidas son masivas. Opera con muy poca deuda.
* **Bank "JGB":** Su Estado de Resultados muestra utilidades récord gracias a paquetes de hipotecas subprime. Pero al calcular su Z-Score, arroja **1.25** (Zona de Peligro). ¿Por qué? Su $X_4$ (Patrimonio / Deuda) es pésimo porque tiene billones en pasivos fuera de balance; y su $X_1$ (Capital de trabajo) es casi cero porque invirtió todo en activos tóxicos ilíquidos.

**El Veredicto de Riesgo:**
El mercado en 2007 decía que ambos eran sólidos. Tus colegas se rieron de ti por desconfiar de JGB debido a "una simple fórmula matemática". En 2008, la crisis financiera golpea. JGB colapsa, es rescatada por el gobierno y sus accionistas lo pierden todo. JGA sobrevive y a la postre compra los activos de JGB a precio de remate.
El Z-Score no predijo "cuándo" iba a caer JGB, pero identificó que su estructura financiera oculta era un castillo de naipes años antes de que el mercado se diera cuenta.

---

## 6. Tareas y Evaluación de la Semana 23

**A. Lectura Obligatoria:**
* Altman, E. I. (1968). *Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy* (Artículo original, lectura de conceptos introductorios).
* *Lectura recomendada*: "The Z-Score_Model: Predicting Bankruptcy" (Artículos modernos de Altman adaptados a empresas emergentes y no cotizadas).

**B. Preguntas de Reflexión:**
1. ¿Por qué una empresa con altísimas utilidades contables y un EBITDA espectacular puede tener un bajo Z-Score y estar al borde de la quiebra? (Pista: Analiza el $X_4$ y el apalancamiento).
2. Explique la diferencia entre financiar el Capital de Trabajo con Deuda a Corto plazo vs. Largo Plazo. ¿Por qué las empresas eligen la opción agresiva si es tan riesgosa?

**C. Ejercicio Matemático a entregar:**
Analizas a la empresa manufacturera cotizada "FragileMold". Sus datos son:
* Activos Totales = $5,000
* Pasivos Totales = $3,500
* Capital de Trabajo = $500
* Utilidades Retenidas = $800
* EBIT = $300
* Ventas = $6,000
* El precio de la acción es $10. Hay 100 acciones en circulación.

Contesta:
1. Calcula los 5 componentes ($X_1$ a $X_5$) del Z-Score. (Recuerda que el Valor de Mercado del Patrimonio = Precio por acción * Número de acciones).
2. Aplica los coeficientes y haya el Z-Score total de FragileMold.
3. En qué zona se encuentra (Segura, Gris o Peligro)? Como analista, ¿recomendarías a tu fondo comprar acciones de FragileMold hoy o cortarlas (short selling)? Justifica.

??? success "Solución del Ejercicio C"

    **1. Los cinco componentes del Z-Score**

    | | Definición | Cálculo | Valor |
    |---|---|---|---|
    | $X_1$ | Capital de Trabajo / Activos Totales | $500/5{,}000$ | **0.100** |
    | $X_2$ | Utilidades Retenidas / Activos Totales | $800/5{,}000$ | **0.160** |
    | $X_3$ | EBIT / Activos Totales | $300/5{,}000$ | **0.060** |
    | $X_4$ | Valor de Mercado del Patrimonio / Pasivos Totales | $(10 \times 100)/3{,}500$ | **0.286** |
    | $X_5$ | Ventas / Activos Totales | $6{,}000/5{,}000$ | **1.200** |

    Valor de Mercado del Patrimonio $= \$10 \times 100 \text{ acciones} = \$1{,}000$.

    **2. Z-Score total** (modelo Altman original, empresa manufacturera cotizada)

    $$Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 1.0X_5$$

    | Término | Cálculo | Aporte |
    |---|---|---|
    | $1.2 X_1$ | $1.2 \times 0.100$ | 0.120 |
    | $1.4 X_2$ | $1.4 \times 0.160$ | 0.224 |
    | $3.3 X_3$ | $3.3 \times 0.060$ | 0.198 |
    | $0.6 X_4$ | $0.6 \times 0.286$ | 0.171 |
    | $1.0 X_5$ | $1.0 \times 1.200$ | 1.200 |
    | | **Z** | **1.913** |

    $$\mathbf{Z = 1.91}$$

    **3. Zona y recomendación**

    | Zona | Rango | FragileMold |
    |---|---|---|
    | Segura | $Z > 2.99$ | |
    | **Gris** | $1.81 \le Z \le 2.99$ | **← 1.91** |
    | Peligro | $Z < 1.81$ | |

    **Zona Gris, pero apenas 0.10 puntos por encima de la frontera de quiebra.**

    Lo que revela el desglose es dónde está el daño. **El 63 % del Z-Score
    ($1.20$ de $1.91$) proviene de un solo componente: $X_5$, la rotación de
    ventas.** Los cuatro indicadores restantes aportan apenas $0.71$ entre todos:

    * $X_3 = 0.06$ — la empresa genera solo $\$6$ de EBIT por cada $\$100$ de
      activos. Rentabilidad operativa muy pobre.
    * $X_2 = 0.16$ — históricamente ha acumulado poca utilidad; es una empresa que
      apenas se autofinancia.
    * $X_4 = 0.286$ — el mercado valora el patrimonio en $\$1{,}000$ frente a
      $\$3{,}500$ de pasivos. **Los acreedores han puesto 3.5 veces más dinero que
      los accionistas.**

    Nota además que el patrimonio contable es $5{,}000 - 3{,}500 = \$1{,}500$,
    mientras el mercado lo valora en $\$1{,}000$: cotiza a **0.67× su valor en
    libros**, señal de que los inversionistas ya descuentan problemas.

    **Recomendación como analista: no comprar.**

    El perfil es el de una empresa que **vende mucho y gana poco**, financiada
    mayormente por deuda. Sobrevive por volumen, y ese volumen depende del ciclo:
    una recesión que reduzca ventas hundiría $X_5$ y con él el Z-Score a la zona de
    peligro.

    !!! warning "Sobre recomendar un short"
        Un $Z$ de 1.91 justifica **evitar** la acción, no necesariamente venderla en
        corto. El short tiene pérdida potencial ilimitada y aquí faltan elementos
        clave: la tendencia del Z-Score de los últimos 3 años (¿mejora o empeora?),
        el calendario de vencimientos de esa deuda, el costo del préstamo de acciones
        y el interés corto ya existente.

        Un analista serio pondría **"Vender / Infraponderar"** con la tesis de
        deterioro, y condicionaría el short a ver el Z-Score cruzar por debajo de
        1.81 en el siguiente reporte trimestral. Y recuerda que el Z-Score es un
        modelo de 1968 calibrado sobre manufactura estadounidense: es una señal de
        alarma, no un veredicto.
