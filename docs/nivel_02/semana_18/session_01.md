# Semana 18 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Entender la arquitectura de un Modelo de 3 Estados integrados.
* Aprender a proyectar el Estado de Resultados (P&L) basado en supuestos de crecimiento y márgenes.
* Dominar las "Schedules" (Hoja de cálculo de apoyo) para proyectar Activos (PP&E) y Deudas.
* Entender el concepto del **"Circulo Virtuoso" (El Plug de Efectivo)** que conecta el Balance General y el Flujo de Efectivo.

---

## 2. La Arquitectura del Modelo de 3 Estados
Un modelo financiero no es un amontonamiento de números; es un sistema vivo donde una hoja alimenta a la otra. Las reglas de oro de la modelación son:
1. **Azul para supuestos:** Todo número que tú escribas a mano (ej. "La inflación será del 3%") debe ir en fuente color azul.
2. **Negro para fórmulas:** Todo número calculado por Excel debe ir en fuente negra.
3. **Hoja de Supuestos (Inputs):** Nunca pongas un supuesto dentro de tu Estado de Resultados. Debe haber una pestaña de *Assumptions* dedicada, y tu P&L debe "jalar" (referenciar) de ahí. Si quieres cambiar un escenario, cambias el supuesto en un solo lugar y todo el modelo se actualiza.

---

## Los *drivers*: de qué depende cada línea

Proyectar no es multiplicar todo por un porcentaje de crecimiento. Cada línea tiene su
**generador** natural:

| Línea | *Driver* habitual | Cómo se proyecta |
|---|---|---|
| **Ventas** | Volumen × precio, o crecimiento del mercado × cuota | El supuesto más importante del modelo |
| **Costo de ventas** | % de ventas (margen bruto) | Estable si no cambia la mezcla de producto |
| **Gastos de venta** | % de ventas | Debería crecer algo menos que las ventas |
| **Gastos de administración** | Crecimiento fijo o % decreciente de ventas | **Apalancamiento operativo**: si crecen igual que las ventas, no hay escala |
| **Depreciación** | % del PP&E bruto, o programa por activo | Sale del *schedule* de PP&E |
| **CapEx** | % de ventas, o plan de inversión declarado | Separa mantenimiento de expansión |
| **Capital de trabajo** | **Días de rotación** (DSO, DIO, DPO) | Nunca como % de ventas plano |
| **Gasto financiero** | Saldo de deuda × tasa | Sale del *schedule* de deuda |
| **Impuestos** | Tasa efectiva sobre EBT | Marginal, no media |

**La regla de oro:** cada supuesto debe poder justificarse con una frase que empiece por *"porque
en los últimos tres años…"* o *"porque el sector…"*. Un supuesto sin justificación es un número
inventado con formato de celda.

---

## Los dos *schedules* que sostienen el modelo

Son las hojas de apoyo que resuelven las dos líneas que el P&L no puede calcular por sí solo.

**A. Programa de PP&E**

$$PP\&E_t = PP\&E_{t-1} + CapEx_t - \text{Depreciación}_t$$

Alimenta dos cosas: la **depreciación** que baja al P&L y el **saldo de PP&E** que va al balance.

**B. Programa de deuda**

$$\text{Deuda}_t = \text{Deuda}_{t-1} + \text{Emisiones}_t - \text{Amortizaciones}_t$$

$$\text{Gasto financiero}_t = \text{Deuda}_{t-1} \times \text{tasa}$$

Nota el detalle: se calcula sobre el **saldo inicial**, no sobre el promedio. Usar el promedio es
más preciso pero **crea una referencia circular** (los intereses dependen de la deuda, que
depende del efectivo, que depende de la utilidad, que depende de los intereses). Para la mayoría
de los propósitos, el saldo inicial es suficiente y mantiene el modelo estable.

---

## El "plug" de efectivo: qué es y qué no es

El **plug** es la partida que absorbe el descuadre entre los activos y los pasivos proyectados.
Habitualmente es el **efectivo**: si el modelo genera más caja de la prevista, el efectivo sube;
si genera menos, baja.

$$\text{Efectivo}_t = \text{Efectivo}_{t-1} + CFO_t + CFI_t + CFF_t$$

**Lo que el plug NO es:** una celda donde escribir un número para que el balance cuadre.

Si el efectivo proyectado sale **negativo**, el modelo te está diciendo algo real: **la empresa
necesita financiamiento**. Un modelo profesional lo resuelve con una **línea de crédito
revolvente** que se dispara automáticamente:

```excel
=SI(Efectivo_antes < Mínimo; Mínimo - Efectivo_antes; 0)
```

Y esa línea genera intereses, que vuelven al P&L… lo que introduce otra circularidad. Es
exactamente el punto donde un modelo pasa de ser un ejercicio a ser una herramienta.

!!! danger "El síntoma de que tu modelo está roto"
    Si tienes que escribir un número a mano para cuadrar el balance, **el modelo está mal y lo
    acabas de ocultar**.

    Un balance que no cierra siempre tiene una causa concreta, y casi siempre es una de estas
    cuatro:

    1. La depreciación se restó en el P&L pero **no se sumó de vuelta** en el flujo de efectivo.
    2. El CapEx se sumó al PP&E pero **no se restó** del flujo (o al revés).
    3. Los cambios en capital de trabajo tienen el **signo cambiado**.
    4. Los dividendos se restaron de Ganancias Retenidas pero **no del flujo** (o viceversa).

    Deja siempre una fila de comprobación visible con formato condicional. Es el equivalente a
    una prueba automática en programación: no evita el error, pero te avisa el mismo día que lo
    cometes.

---
