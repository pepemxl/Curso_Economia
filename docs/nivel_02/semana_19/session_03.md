# Semana 19 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: El Switch de Escenarios

Estás proyectando las cosas (Ventas de la empresa "TechCorp"). En tu pestaña de Supuestos tienes 3 columnas: Base, Optimista, Pesimista.
* Tasa de Crecimiento Base: 5%
* Tasa de Crecimiento Optimista: 15%
* Tasa de Crecimiento Pesimista: -2%

**Paso a paso en Excel:**
1. En la celda A1 creas una lista desplegable con validación de datos permitiendo solo 1, 2 o 3. Llama a A1 "Selector".
2. En la celda B1 (Tu Tasa de Crecimiento para el modelo) escribes:
   `=ELEGIR(A1; 5%; 15%; -2%)`
3. En tu Estado de Resultados: `Ventas Año 1 = Ventas Año 0 * (1 + $B$1)`

*Si el director quiere ver el caso optimista, le basta con cambiar el número de A1 a 2. Todo el modelo se recalcula a exceso de ventas al instante, permitiéndole ver si la empresa tendrá capacidad de planta para producir tanto o necesitará pedir más deuda (CapEx).*

---

## Segundo ejercicio: análisis de sensibilidad con tabla de datos

El *dashboard* anterior cambia **un escenario completo**. La tabla de datos hace algo distinto y
complementario: muestra **cómo responde un resultado a un rango continuo de valores**.

**Montaje de una tabla de una variable:**

Supón un modelo cuyo VAN está en `B10` y cuya tasa de descuento está en `B4`.

1. En `D2:D8` escribe los valores a probar de la tasa: 6 %, 8 %, 10 %, 12 %, 14 %, 16 %, 18 %.
2. En `E1` —la celda **arriba y a la derecha** de la columna de valores— escribe `=B10`.
3. Selecciona `D1:E8`.
4. **Datos → Análisis de hipótesis → Tabla de datos.**
5. En *Celda de entrada (columna)* pon **`B4`** (porque los valores están en una columna).

Excel sustituirá `B4` por cada valor y recalculará el modelo completo, rellenando la columna E.

**Tabla de dos variables** (la que de verdad se presenta a un comité): valores de la primera
variable en una **columna** (D3:D8), los de la segunda en una **fila** (E2:J2), y la referencia
`=B10` en la **esquina** `D2`. Al ejecutar, se indican *ambas* celdas de entrada.

!!! warning "Los tres fallos que hacen que la tabla de datos no funcione"
    1. **La referencia va en la esquina**, no encima de la primera columna de resultados. Es el
       error más común y no da ningún mensaje: simplemente sale vacía o mal.
    2. **Las celdas de entrada deben estar en la misma hoja** que la tabla. Si tu modelo está en
       otra pestaña, crea una celda puente.
    3. **El recálculo se vuelve lentísimo** en modelos grandes: la tabla recalcula el libro
       entero por cada celda. Si tu tabla es de 6 × 6, son 36 recálculos completos. Cambia a
       cálculo manual (`Fórmulas → Opciones para el cálculo → Automático excepto en tablas de
       datos`) y refresca con ++f9++.

    Alternativa moderna y auditable: **escribir la matriz de fórmulas explícitas**, como hace la
    hoja *Sensibilidad* de la plantilla DCF de la Semana 37. Es más transparente, se puede
    auditar celda por celda y no depende de una función oculta de Excel.

---

## Herramientas de control de errores y validación

Un modelo que otro va a usar necesita defensas. Las cuatro capas, de menor a mayor robustez:

**1. Validación de datos** (Datos → Validación de datos)

* **Lista:** restringe a un conjunto cerrado de opciones.
* **Número entero / decimal entre X e Y:** impide valores absurdos (una tasa del 500 %).
* **Personalizada:** una fórmula lógica, p. ej. `=Y(B1>0;B1<1)` para forzar una tasa entre 0 y 1.
* **Mensaje de entrada y alerta de error:** explica al usuario qué se espera antes de que se
  equivoque.

**2. Formato condicional para hacer visibles los problemas**

* La fila de comprobación del balance: verde si es 0, roja si no.
* Semáforos en ratios clave (cobertura de intereses, deuda/EBITDA) frente a sus *covenants*.
* Escalas de color en matrices de sensibilidad.

**3. Auditoría de fórmulas** (pestaña Fórmulas)

* **Rastrear precedentes / dependientes:** dibuja flechas mostrando de dónde viene y a dónde va
  cada celda. Imprescindible al heredar el modelo de otra persona.
* **Evaluar fórmula:** ejecuta la fórmula paso a paso, mostrando el resultado intermedio.
* **Ventana de inspección:** fija en pantalla las celdas críticas (VAN, TIR, comprobaciones)
  mientras navegas por otras hojas.
* **Comprobación de errores:** localiza `#¡REF!`, `#¡DIV/0!`, referencias circulares.

**4. Protección de hoja**

Bloquea todas las celdas salvo las de entrada. Es la única forma real de garantizar que quien
use el modelo no sobrescriba una fórmula por accidente.

---

## Tercer ejercicio: detectar el error en un modelo ajeno

Recibes este modelo de un compañero. Encuentra los cuatro problemas:

| Celda | Fórmula | |
|---|---|---|
| B5 | `=B4*1.21` | Ventas con IVA |
| B8 | `=SUMA(B5:B7)` | Total ingresos |
| C8 | `=SUMA(C5:C6)` | Total ingresos año 2 |
| B12 | `=SI.ERROR(B8/B10;0)` | Margen |
| B15 | `=VNA(10%;B8:F8)` | VAN del proyecto |

**Los cuatro problemas:**

1. **B5 — número mágico.** El 1,21 está incrustado. Cuando cambie el IVA, habrá que buscarlo por
   todo el modelo. Debe ser `=B4*(1+$C$2)` con la tasa etiquetada.
2. **C8 — inconsistencia de rango.** La fila 8 suma `B5:B7` en una columna y `C5:C6` en la
   siguiente. Alguien arrastró mal o insertó una fila. **Toda la fila debe tener la misma
   fórmula.**
3. **B12 — `SI.ERROR` que oculta el problema.** Si `B10` está vacía, la división da `#¡DIV/0!` y
   la función devuelve **0**, un margen del 0 % que parece un dato real. Es preferible
   `=SI(B10=0;"⚠ falta base";B8/B10)`.
4. **B15 — tasa incrustada y Año 0 mal tratado.** El 10 % debería estar en una celda, y si `B8`
   es el flujo del Año 0, `VNA` lo está descontando un período de más.

!!! tip "El test de los dos minutos"
    Antes de entregar cualquier modelo, haz esto:

    * Selecciona todo y pulsa ++ctrl+grave++ (mostrar fórmulas). ¿Ves números sueltos dentro de
      las fórmulas? Corrígelos.
    * `Inicio → Buscar y seleccionar → Constantes`: resalta todas las celdas con valores
      escritos a mano. Deberían estar **solo** en la hoja de supuestos.
    * Cambia un supuesto clave a un valor extremo (crecimiento del −50 %). ¿El modelo devuelve
      un resultado coherente o explota? Un modelo robusto degrada con elegancia.

---
