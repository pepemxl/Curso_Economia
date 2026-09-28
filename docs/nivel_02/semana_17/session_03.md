# Semana 17 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Evaluando una Startup
Tienes los siguientes flujos de caja para una inversión en tecnología:
* Fecha de Inversión (15-Ene-2024): -$500,000
* Primer Retiro (20-Dic-2024): $100,000
* Segundo Retiro (10-Jul-2025): $200,000
* Venta Final / Exit (30-Dic-2026): $400,000

**Cómo lo modelas en Excel en 1 minuto:**
1. En la columna A pones las fechas (formato fecha). En la columna B pones los flujos (-500k, 100k, 200k, 400k).
2. En una celda calculas el retorno anualizado exacto considerando los días: `=TIR.NO.PER(B1:B4; A1:A4)`. 
   * *Resultado aproximado:* **15.6% anual real**.
3. Si tu exigencia de rentabilidad (Costo de Capital) es del 10%, calculas el VNA: `=B1 + VNA(10%; B2:B4)`. *(Recuerda dejar la inversión inicial B1 fuera del VNA y restarla, o usa la función VNA.NO.PER).*
   * *Resultado:* Valor Presente Neto de **+$48,500**. (El proyecto es viable, crea valor).

---

## Las diez funciones que resuelven el 90 % del trabajo financiero

Antes de seguir, ten a mano este repertorio. Los nombres van en español (Excel los traduce
según el idioma de la instalación) con el equivalente inglés entre paréntesis:

| Función | Para qué sirve | Trampa habitual |
|---|---|---|
| `VNA` (NPV) | Valor presente de flujos periódicos | **No incluyas el Año 0** en el rango |
| `TIR` (IRR) | Tasa de rentabilidad | **Sí incluye** el Año 0; puede haber TIR múltiples |
| `VNA.NO.PER` (XNPV) | VAN con fechas reales | Requiere una columna de fechas |
| `TIR.NO.PER` (XIRR) | TIR con fechas reales | El resultado es **siempre anualizado** |
| `PAGO` (PMT) | Cuota de un préstamo | Devuelve negativo por convención de signos |
| `PAGOINT` / `PAGOPRIN` | Descompone la cuota en interés y capital | Útil para cuadros de amortización |
| `TASA` (RATE) | Despeja la tasa implícita | Puede no converger; dale una estimación inicial |
| `BUSCARX` (XLOOKUP) | Búsqueda moderna | Sustituye a `BUSCARV`; no se rompe al insertar columnas |
| `SI.ERROR` (IFERROR) | Blindar fórmulas | **No atrapa celdas vacías** (ver Semana 19) |
| `ELEGIR` (CHOOSE) | Selector de escenarios | Índice fuera de rango → `#¡VALOR!` |

---

## Segundo ejercicio: cuando los flujos no son anuales

El proyecto inmobiliario del ejercicio anterior suponía flujos exactamente anuales. En la
realidad casi nunca lo son. Supongamos las fechas reales:

| Fecha | Concepto | Flujo |
|---|---|---|
| 15/01/2026 | Compra del terreno | −2,000,000 |
| 30/09/2026 | Costos de construcción | −3,000,000 |
| 20/06/2027 | Primera preventa | +3,500,000 |
| 10/03/2028 | Entrega final | +3,800,000 |

Con fechas en `A2:A5` y flujos en `B2:B5`:

```excel
=VNA.NO.PER(12%; B2:B5; A2:A5)
=TIR.NO.PER(B2:B5; A2:A5)
```

**Diferencias clave frente a `VNA`/`TIR`:**

1. **El primer flujo SÍ va incluido** en el rango. `VNA.NO.PER` lo descuenta a la fecha del
   primer elemento, es decir con factor 1. No hay que sumarlo por fuera.
2. Descuenta por **días reales** ($/365$), no por períodos enteros.
3. El resultado de `TIR.NO.PER` ya está **anualizado**.

En este caso, como el desembolso del terreno se hace en enero y la construcción en septiembre
(no en el mes 12), el proyecto sale **mejor** que con el cálculo anual: el dinero está menos
tiempo inmovilizado.

**Regla práctica:** si los flujos son mensuales, trimestrales o irregulares, usa **siempre** las
funciones `.NO.PER`. Usar `VNA` con flujos mensuales y una tasa anual es un error de dos órdenes
de magnitud.

---

## Cómo se estructura un modelo que otro pueda auditar

Las funciones son la parte fácil. Lo que separa un modelo profesional de una hoja de cálculo es
la **estructura**. Las convenciones de la banca de inversión:

**1. Separa entradas, cálculos y salidas.**

* Una hoja (o zona) exclusiva de **supuestos**, con las celdas de entrada en **azul o fondo
  amarillo**.
* Las fórmulas, en negro.
* Las referencias a otras hojas, en verde.

Es una convención universal: cualquier analista abre tu modelo y sabe al instante qué puede
tocar.

**2. Nunca escribas un número dentro de una fórmula.**

`=B5*1.21` es una bomba de tiempo: dentro de seis meses nadie sabrá qué era ese 1,21 ni dónde
buscarlo cuando cambie el IVA. Escribe `=B5*(1+$C$2)` con la tasa en una celda etiquetada.

**3. Una fila, una fórmula.**

Toda la fila debe poder rellenarse arrastrando la primera celda. Si el año 3 tiene una fórmula
distinta al año 2, es un error esperando a ocurrir. Usa referencias absolutas ($) y relativas
con criterio.

**4. Incluye filas de comprobación.**

`=Total Activo - Total Pasivo y Patrimonio` debe dar 0 siempre. Ponla visible, con formato
condicional. Es el equivalente a las pruebas automáticas en programación.

**5. Documenta los supuestos y sus fuentes.**

Cada supuesto relevante debería tener una nota indicando de dónde salió: informe anual, consenso
de analistas, dato del banco central. Sin eso, el modelo no es auditable.

!!! danger "El costo real de un error de Excel"
    No es teoría. Casos documentados:

    * **JPMorgan, "London Whale" (2012):** un modelo de valor en riesgo copiaba valores entre
      hojas y dividía entre una suma en lugar de un promedio. Subestimó la volatilidad a la
      mitad. Pérdida: **$\$6.200$ millones**.
    * **Reinhart y Rogoff (2010):** un rango de celdas mal seleccionado excluyó cinco países de
      un estudio sobre deuda y crecimiento que sirvió de base para políticas de austeridad en
      media Europa.
    * **TransAlta (2003):** un error de copiar y pegar en una hoja de contratos costó
      **$\$24$ millones**.

    Un estudio de auditoría encontró errores materiales en el **88 %** de las hojas de cálculo
    revisadas. La disciplina estructural no es pedantería: es la única defensa.

---
