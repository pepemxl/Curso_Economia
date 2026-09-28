# Semana 21 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: La "Muerte" de Blockbuster vs. Netflix
*Eres un gestor de fondos en el año 2005. Posees acciones de Blockbuster (renta de películas en tiendas físicas) y te planteas invertir en Netflix (envío de DVD por correo y streaming incipiente).*

Al mirar los ratios de eficiencia, descubres algo revelador:
* **Blockbuster:** Tenía un ratio de "Días de Inventario" altísimo (las películas físicas tardaban meses en rentarse lo suficiente para recuperar su costo). Su Activo Corriente estaba atascado en cintas de video y edificios físicos (Activos Fijos). Su **ROA era decreciente** porque requería muchísimo capital para abrir tiendas, pero el retorno por cada tienda estaba bajando.
* **Netflix:** Estaba migrando a streaming (cero inventario físico, cero costo de envío). Su **Rotación de Activos** ($Ventas / Activos$) era astronómicamente superior a la de Blockbuster porque Netflix no necesitaba activos fijos masivos para crecer. Su ROE estaba en expansión.

**El Veredicto Financiero:** Un analista que solo mirara el Estado de Resultados diría "Blockbuster gana miles de millones, Netflix apenas gana millones". Pero el analista de ratios vio que **la eficiencia en el uso de activos** de Blockbuster estaba colapsando. Vendiste tus acciones de Blockbuster e invertiste en Netflix. El resto es historia.

> **Nota sobre la próxima semana:** El ROE de Netflix creció mágicamente en los siguientes años, no solo por la Utilidad Neta, sino por algo más complejo llamado "Apalancamiento Financiero". Eso lo desglosaremos en la Semana 22 con el **Análisis Dupont**.

---

## 6. Tareas y Evaluación de la Semana 21

**A. Lectura Obligatoria:**
* *Análisis de Estados Financieros* (John J. Wild) o capítulos de *Fundamentos de Finanzas Corporativas* sobre Análisis de Estados Financieros.
* *Práctica en Excel:* Descarga los estados financieros de cualquier empresa en Yahoo Finance y calcula estos 4 ratios en Excel.

**B. Preguntas de Reflexión:**
1. Imagina que una empresa tiene una Razón Corriente de 4.0. Esto significa que es súper líquida y sana. ¿Existe algún escenario financiero donde un ratio de liquidez __demasiado alto__ sea una mala señal para los accionistas? (Pista: Pensemos en costo de oportunidad).
2. Explica por qué el ratio "Margen Neto" es engañoso en industrias con altísima rotación (ej. supermercados) y qué ratio sería más útil analizar allí.

**C. Ejercicio Práctico a entregar:**
La empresa "RetailMax" presenta los siguientes datos (en millones):
* Ventas: $2,000
* COGS: $1,500
* Utilidad Neta: $50
* Activo Corriente: $400 (Inventario = $200)
* Pasivo Corriente: $300
* Activos Totales: $1,000
* Patrimonio: $500
* Deuda Total: $500
* EBIT: $120; Gastos por Intereses: $40

Contesta:
1. Liquidez: Calcula la Razón Corriente y la Prueba Ácida. ¿Existe riesgo de iliquidez a corto plazo?
2. Solvencia: Calcula la Cobertura de Intereses. Si el Banco Central sube las tasas y el gasto financiero se duplica a $80, ¿cuál sería el nuevo ratio? ¿Sobrevive la empresa?
3. Rentabilidad y Eficiencia: Calcula el Margen Neto, el ROA y el ROE. Interpreta el significado de cada uno en este caso específico (comparado con el sector donde el ROE promedio es del 15%).

??? success "Solución del Ejercicio C"

    **1. Liquidez**

    $$\text{Razón Corriente} = \frac{\text{Activo Corriente}}{\text{Pasivo Corriente}} = \frac{400}{300} = \mathbf{1.33}$$

    $$\text{Prueba Ácida} = \frac{400 - 200}{300} = \frac{200}{300} = \mathbf{0.67}$$

    **Sí existe riesgo, y está escondido en el inventario.**

    La razón corriente de $1.33$ parece aceptable: hay $\$1.33$ de activo líquido por
    cada peso de deuda a corto plazo. Pero **la mitad de ese activo corriente es
    inventario**, y la prueba ácida lo excluye porque no siempre se convierte en
    efectivo rápido ni a su valor en libros.

    Con $0.67$, RetailMax **solo puede cubrir el 67 % de sus obligaciones inmediatas
    sin vender mercancía**. Si las ventas se frenan, tendría que liquidar inventario
    con descuento —destruyendo margen— o refinanciarse de urgencia.

    **2. Solvencia — cobertura de intereses**

    $$\text{Cobertura} = \frac{EBIT}{\text{Intereses}} = \frac{120}{40} = \mathbf{3.0\times}$$

    Con el gasto financiero duplicado a $\$80$:

    $$\text{Cobertura}_{nueva} = \frac{120}{80} = \mathbf{1.5\times}$$

    **Sobrevive, pero queda en cuidados intensivos.** Genera 1.5 veces lo necesario
    para pagar intereses, así que técnicamente no incumple. El problema es el margen
    de error:

    * La mayoría de los *covenants* bancarios exigen cobertura **mínima de 2.0×**.
      A 1.5× la empresa estaría **en incumplimiento técnico**, y el banco podría
      exigir el pago anticipado del crédito.
    * Solo queda $\$40$ tras pagar intereses, y de ahí aún salen impuestos, CapEx y
      amortización de capital.
    * Bastaría una caída del EBIT del 33 % para que la cobertura llegue a 1.0× —
      el punto donde toda la utilidad operativa se va en intereses.

    **3. Rentabilidad y eficiencia**

    $$\text{Margen Neto} = \frac{50}{2{,}000} = \mathbf{2.5\%}$$

    $$ROA = \frac{50}{1{,}000} = \mathbf{5.0\%}$$

    $$ROE = \frac{50}{500} = \mathbf{10.0\%}$$

    | Ratio | Valor | Qué dice |
    |---|---|---|
    | Margen Neto | 2.5 % | De cada $\$100$ vendidos solo quedan $\$2.50$. Típico de retail: márgenes finos, se gana por volumen. |
    | ROA | 5.0 % | Cada $\$100$ de activos genera $\$5$ de utilidad. Mide la eficiencia del negocio **antes** de cómo se financió. |
    | ROE | 10.0 % | Cada $\$100$ que pusieron los accionistas rinde $\$10$. |

    **Comparación con el sector (ROE 15 %): RetailMax rinde un tercio menos.**

    Un accionista que exige 15 % está recibiendo 10 %: la empresa **destruye valor**
    frente a su alternativa sectorial. Y conviene notar de dónde viene ese 10 %,
    anticipando el Dupont de la Semana 22:

    $$ROE = \underbrace{2.5\%}_{\text{margen}} \times \underbrace{2.0}_{\text{rotación}} \times \underbrace{2.0}_{\text{apalancamiento}} = 10\%$$

    La rotación de activos ($2{,}000/1{,}000 = 2.0$) es buena y el apalancamiento
    ($1{,}000/500 = 2.0$) ya es alto. **El problema está en el margen**, no en la
    eficiencia operativa ni en la falta de deuda. Subir más el apalancamiento
    mejoraría el ROE en el papel, pero con cobertura de intereses de 3.0× (o 1.5×
    si suben las tasas) sería jugar con fuego.
