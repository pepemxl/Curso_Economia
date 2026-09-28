# Semana 18 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: El Error #REF y el "Cash Sweep"
*Eres un analista junior en un banco de inversión. Estás proyectando 5 años de una empresa altamente apalancada (mucha deuda).*

Entras en pánico porque tu modelo arroja `#REF!` en la celda de Deuda del Año 3. El Director entra y mira tu pantalla.

**El Análisis del Director (Por qué falló tu modelo):**
* Tu modelo permitía que la empresa pidiera préstamos (emitir deuda) automáticamente si se quedaba sin efectivo. Pero no conectaste bien el interés de esa nueva deuda en el P&L. Rompiste el **Circulo Virtuoso**.
* Al no registrar el nuevo gasto financiero, tu Utilidad Neta era artificialmente alta. Esa utilidad iba a Ganancias Retenidas, inflando el Patrimonio. Pero como la deuda no se actualizó bien, el balance estaba desbalanceado.
* *Solución* (La técnica del Cash Sweep): Configuras el modelo para que, en lugar de acumular efectivo ocioso, la empresa use cualquier excedente de caja (FCF) para **prepagar deuda automáticamente** (reducir el pasivo). Esto reduce el riesgo de quiebra y ahorra intereses, pero requiere macros (circular references) o un cambio en el orden iterativo de Excel (File > Options > Formulas > Enable iterative calculation) porque el interés depende de la deuda, y la deuda depende del efectivo disponible para pagarla. ¡El modelo se vuelve un loop infinito matemático!

---

## 6. Tareas y Evaluación de la Semana 18

**A. Lectura y Práctica Obligatoria:**
* *Lectura*: *Principles of Financial Modeling* (Christian M. Benesh) o manuales estándar de Wall Street Prep /Breaking Into Wall Street. (Busca videos de YouTube: "3 Statement Model Walkthrough").
* *Práctica Excel*: Activa el cálculo iterativo de Excel para evitar errores de referencias circulares.

**B. Preguntas de Reflexión:**
1. En modelación financiera, ¿por qué es obligatorio tener una pestaña separada de "Supuestos" (Assumptions) en lugar de escribir directamente las tasas de crecimiento dentro de las celdas del Estado de Resultados? ¿Qué principio de diseño de modelos está detrás de esto?
2. Explica cómo funciona el "Círculo Virtuoso" o el "Plug de Efectivo" en la modelación de 3 estados. ¿Por qué varía el efectivo elynchronously con la Utilidad Neta?

**C. Ejercicio de Modelación a entregar:**
Descarga o crea una plantilla en blanco en Excel. Vas a proyectar 1 solo año (Año 1) de una empresa de logística.

* **Supuestos Año 1:** Crecimiento de Ventas: 10%. Margen EBITDA: 20%. Depreciación: 20. Tasa de Impuestos: 25%. CapEx: 50.
* **Datos Año 0 (Balance Inicial):** Efectivo: 100, Inventario: 200, PP&E neto: 800 (Total Activos = 1,100). Cuentas por Pagar: 100, Deuda Largo Plazo: 600. Ganancias Retenidas: 400 (Total Pasivo+Patrimonio = 1,100). 
* **Ventas Año 0:** 1,000.
* **No hay cambios en Deuda, ni Dividendos por simplicidad.** El Inventario y Cuentas por Pagar se mantienen constantes.

Contesta / Construye en Excel:
1. Proyecta el P&L del Año 1 (Ventas, EBITDA, EBIT, EBT, Utilidad Neta). *(Ojo: Falta el gasto por Interés. Asumamos que la deuda a 600 paga 5% de interés. Gasto Financiero = 30).*
2. Proyecta el PP&E del Año 1: 800 (Año 0) + 50 (CapEx) - 20 (Depreciación) = ¿Cuál es el PP&E final?
3. Haz un mini Flujo de Efectivo del Año 1: Utilidad Neta + Depreciación - CapEx. Ese es tu Flujo neto de efectivo.
4. Calcula el "Plug" de Efectivo en el Balance del Año 1: Efectivo Año 0 (100) + Flujo neto de efectivo.
5. Comprueba si tu Balance Año 1 cuadra: Total Activos debe ser igual a Total Pasivos (100) + Deuda (600) + Ganancias Retenidas (400 + Utilidad Neta Año 1).


??? success "Solución del Ejercicio C"

    **1. P&L proyectado del Año 1**

    | Concepto | Cálculo | Año 1 |
    |---|---|---|
    | Ventas | $1{,}000 \times 1.10$ | **1,100.0** |
    | EBITDA | $1{,}100 \times 20\%$ | **220.0** |
    | (−) Depreciación | supuesto | (20.0) |
    | **EBIT** | $220 - 20$ | **200.0** |
    | (−) Gasto Financiero | $600 \times 5\%$ | (30.0) |
    | **EBT** | $200 - 30$ | **170.0** |
    | (−) Impuestos (25 %) | $170 \times 0.25$ | (42.5) |
    | **Utilidad Neta** | | **127.5** |

    **2. PP&E del Año 1**

    $$PP\&E_1 = PP\&E_0 + CapEx - Depreciación = 800 + 50 - 20 = \mathbf{830}$$

    **3. Mini Flujo de Efectivo del Año 1**

    $$FE = \text{Utilidad Neta} + \text{Depreciación} - CapEx = 127.5 + 20 - 50 = \mathbf{97.5}$$

    (El inventario y las cuentas por pagar se mantienen constantes por supuesto, así
    que el capital de trabajo no consume ni libera caja.)

    **4. El "Plug" de Efectivo**

    $$\text{Efectivo}_1 = \text{Efectivo}_0 + FE = 100 + 97.5 = \mathbf{197.5}$$

    **5. Comprobación del Balance — ¿cuadra?**

    | ACTIVO | Año 1 | | PASIVO + PATRIMONIO | Año 1 |
    |---|---|---|---|---|
    | Efectivo | 197.5 | | Cuentas por Pagar | 100.0 |
    | Inventario | 200.0 | | Deuda Largo Plazo | 600.0 |
    | PP&E neto | 830.0 | | Ganancias Retenidas ($400 + 127.5$) | 527.5 |
    | **Total Activo** | **1,227.5** | | **Total Pasivo + Patrimonio** | **1,227.5** |

    $$\mathbf{1{,}227.5 = 1{,}227.5} \quad ✓$$

    !!! tip "Por qué el modelo cuadra (y qué hacer cuando no)"
        El balance cierra por una razón estructural, no por suerte: **la utilidad
        neta entra dos veces al modelo**. Sube las Ganancias Retenidas del lado
        derecho, y por el flujo de efectivo sube el Efectivo del lado izquierdo. Las
        partidas no monetarias (depreciación) y el CapEx hacen el ajuste entre ambos
        lados vía PP&E.

        **Cuando tu modelo no cuadre**, revisa en este orden:

        1. ¿La depreciación se restó en el P&L **y** se sumó de vuelta en el flujo?
        2. ¿El CapEx se sumó al PP&E **y** se restó del flujo?
        3. ¿Los cambios en capital de trabajo tienen el signo correcto?
        4. ¿Los dividendos se restaron de Ganancias Retenidas **y** del flujo?

        Regla de oro profesional: **nunca "cuadres" el balance a mano** metiendo un
        número forzado. Un balance que no cierra es el modelo avisándote de un error
        real de lógica. Deja una fila de verificación
        `=Total Activo - Total Pasivo y Patrimonio` que debe marcar 0 siempre.

---
*¡Felicidades por completar la Semana 18! Has programado el futuro financiero de una empresa. En la Semana 19 pasaremos a la validación de datos, tablas dinámicas y análisis de sensibilidad para ver qué pasa cuando nuestras "suposiciones" fallan.*