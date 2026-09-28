# Semana 19 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El "Stress Test" que salvó al banco
*Eres parte del equipo de Originación de un fondo de Private Equity. Quieren comprar una cadena de cines. El modelo Base muestra que genera Flujo de Caja Libre de $10M al año, suficiente para pagar la deuda del LBO ( compra apalancada).*

El Comité de Inversión te pide un *Stress Test* (prueba de estrés). Construyes un modelo con escenarios dinámicos:
* **Escenario Pesimista:** Modelas que la asistencia de público cae un 20%, el costo de las palomitas de maíz sube un 15% (inflación) y el banco sube la tasa de interés de la deuda del 5% al 9%.

Al accionar tu SWITCH de "ELEGIR 3", las Tablas Dinámicas muestran que, en el Escenario Pesimista, el Flujo de Caja Libre cae a $0M (cero). Peor aún, la empresa quema $2M en efectivo porque no puede subir los precios de los boletos por la competencia del streaming. La deuda se vuelve impagable.

**El Veredicto:** El comité no rechaza la compra, pero rechaza la **estructura de capital**. Gracias a la modelación de escenarios, decides no financiar la compra con un 80% de deuda, sino con un 50%. El modelo pesimista ahora muestra que la empresa puede sobrevivir a una recesión sin ir a quiebra.

---

## 8. Tareas y Evaluación de la Semana 19

**A. Lectura y Práctica Obligatoria:**
* *Lectura*: "Investment Banking: Valuation, Leveraged Buyouts, and Mergers and Acquisitions" (Rosenbaum & Pearl) - Capítulo sobre cómo construir escenarios operativos.
* *Práctica Youtube*: Busca "Excel CHOOSE function scenario analysis" y "Excel Pivot Tables for accounting".

**B. Preguntas de Reflexión:**
1. ¿Por qué un analista financiero debe agregar la función `SI.ERROR` (IFERROR) a su modelo al dividir cuentas contables como "Cuentas por Cobrar" entre "Ventas" para calcular los días de cobro?
2. Imagina que te entregan un Excel con 4 años de datos diarios de la bolsa (100,000 filas). ¿Cuál es la forma más eficiente de saber el rendimiento promedio mensil sin usar fórmulas complejas?

**C. Ejercicio Práctico de Excel a entregar:**
Crea en un Excel limpio el siguiente "Dashboard de Escenarios":

* Imagina 3 tasas de inflación proyectadas (En una tabla): Base 3%, Optimista 1%, Pesimista 8%.
* En la celda A1, usa Validación de Datos para crear una lista desplegable que solo permita elegir los números 1, 2 o 3.
* En la celda B1, usa la función `ELEGIR` (CHOOSE) para que, dependiendo del número en A1, jale automáticamente la tasa correspondiente (3%, 1% u 8%).
* En la celda C1, escribe una fórmula financiera que calcule el Valor Futuro de $1,000 invertidos a 1 año usando la tasa de B1: `=1000 * (1 + B1)`.
* Agrega un `SI.ERROR` a C1 que proteja la fórmula en caso de que alguien borre B1 por accidente.


??? success "Solución del Ejercicio C"

    **Paso 1 — Tabla de escenarios**

    Coloca los tres escenarios en un rango auxiliar, por ejemplo `E1:F3`:

    | | E | F |
    |---|---|---|
    | **1** | Base | 3% |
    | **2** | Optimista | 1% |
    | **3** | Pesimista | 8% |

    **Paso 2 — Validación de datos en A1**

    Cinta **Datos → Validación de datos → Permitir: Lista**, y en *Origen* escribe:

    ```
    1;2;3
    ```

    (En algunas configuraciones regionales el separador es la coma: `1,2,3`.)

    Alternativa más robusta: **Permitir: Número entero**, *entre* 1 y 3. Así el
    usuario tampoco puede pegar un valor inválido desde el portapapeles — la lista
    desplegable por sí sola no bloquea el pegado.

    **Paso 3 — Función ELEGIR en B1**

    ```excel
    =ELEGIR(A1; 3%; 1%; 8%)
    ```

    O, mejor aún, enlazada a la tabla para no tener números incrustados en la fórmula:

    ```excel
    =ELEGIR(A1; $F$1; $F$2; $F$3)
    ```

    `ELEGIR` toma el índice de `A1` y devuelve el argumento en esa posición: si `A1`
    vale 3, devuelve el tercer valor (8 %).

    **Paso 4 — Valor Futuro protegido en C1**

    ```excel
    =SI.ERROR(1000*(1+B1); "⚠ Revisa el escenario en A1")
    ```

    **Resultados según el escenario elegido:**

    | A1 | Escenario | B1 | C1 (VF de $1,000) |
    |---|---|---|---|
    | 1 | Base | 3 % | **$1,030.00** |
    | 2 | Optimista | 1 % | **$1,010.00** |
    | 3 | Pesimista | 8 % | **$1,080.00** |

    !!! warning "Qué protege realmente SI.ERROR — y qué no"
        Si alguien borra `B1`, la celda vacía se evalúa como 0 y
        `1000*(1+0) = 1000`: **una respuesta plausible pero equivocada, sin ningún
        error visible.** `SI.ERROR` no la atrapa, porque técnicamente no hay error.

        `SI.ERROR` sí actúa cuando `A1` queda fuera de rango (0, 4 o texto):
        `ELEGIR` devuelve `#¡VALOR!` y el mensaje aparece.

        Para blindar de verdad el caso de la celda vacía, encadena una comprobación
        explícita:

        ```excel
        =SI(O(B1=""; NO(ESNUMERO(B1))); "⚠ Falta la tasa"; SI.ERROR(1000*(1+B1); "⚠ Error"))
        ```

        Es la diferencia entre un modelo que *parece* funcionar y uno auditable. En
        finanzas, **un número silenciosamente equivocado es peor que un error
        visible**: el error lo corriges, el número malo se te cuela al comité de
        inversión.

---
*¡Felicidades por completar la Semana 19! Tu modelo ahora respira y reacciona a las crisis. En la Semana 20 cerraremos el Nivel 2 con broche de oro: Análisis de sensibilidad y Simulación Monte Carlo básica para medir el riesgo de pérdida.*