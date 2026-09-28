# Semana 36 · Sesión 2: Profundización

## 4. Pérdidas Netas Operativas (NOLs) en M&A
El fisco no te devuelve dinero si pierdes plata, pero te permite compensar las pérdidas de este año contra las ganancias de los próximos años (Net Operating Losses - NOLs). 

**El efecto en M&A (Semana 27):**
Si una empresa rentable (que paga $10M de impuestos al año) compra a una empresa en bancarrota que tiene $50M en NOLs acumuladas, la empresa rentable puede usar esas pérdidas de la empresa comprada para no pagar impuestos durante 5 años. 

> **⚠️ La trampa regulatoria (Sección 382):** Para evitar que los fondos de inversión compren empresas moribundas solo para usar sus impuestos, el gobierno limita el uso de NOLs en adquisiciones. Como analista, debes aplicar un descuento (haircut) al valor de las NOLs, ya que no se pueden aprovechar al 100% ni de golpe.

---

## 5. Fiscalidad Internacional y "Precios de Transferencia"
Las multinacionales operan en países con distintas tasas de impuestos (EE. UU. 21%, Irlanda 12.5%, Bermudas 0%). Para minimizar el pago global, usan estrategias de planificación de precios de transferencia.

* **Precios de Transferencia:** Es el precio al que una filial le vende bienes o servicios a otra filial del mismo grupo corporativo. 
  *Ejemplo:* "BigTech USA" desarrolla la patente de un software y la vende a "BigTech Irlanda" por $1,000. BigTech Irlanda lo revende al mundo por $1,000,000. La utilidad de $999,000 queda en Irlanda (12.5% de impuesto), no en USA (21%). 
  *(La OCED regularmente interviene con el plan BEPS para evitar este abuso, obligando a que los precios entre filiales sean los de mercado "Arm's Length").*

---

## DTA, DTL y la conciliación de la tasa efectiva

Las diferencias entre contabilidad y fiscalidad generan dos partidas simétricas:

| | **DTL** (pasivo por impuesto diferido) | **DTA** (activo por impuesto diferido) |
|---|---|---|
| Origen | Pagas **menos** impuesto hoy del que dice el P&L | Pagas **más** impuesto hoy del que dice el P&L |
| Causa típica | Depreciación acelerada | Pérdidas fiscales (NOL), provisiones no deducibles |
| Naturaleza | Obligación futura | Beneficio futuro |
| Reversión | Pagarás más adelante | Pagarás menos adelante |

**La prueba de recuperabilidad del DTA.** Un DTA solo vale algo si la empresa **generará
utilidades futuras** contra las que compensarlo. Si no es probable, hay que registrar una
**corrección valorativa** que lo elimina del balance.

Es una señal muy potente: cuando una empresa castiga su DTA, **su propia dirección está
admitiendo que no espera ser rentable** en el horizonte previsto. Suele preceder a problemas
mayores.

**Las diferencias permanentes.** No todas las diferencias revierten:

* Gastos **no deducibles** (multas, ciertas atenciones) → suben la tasa efectiva para siempre.
* Ingresos **exentos** (algunos dividendos intragrupo) → la bajan para siempre.

Solo las **temporarias** generan DTA/DTL. Las permanentes explican por qué la tasa efectiva
difiere de la estatutaria de forma estructural.

**La conciliación de tasa** es la nota más informativa del informe anual:

| Concepto | % |
|---|---|
| Tasa estatutaria | 25,0 |
| Diferencias permanentes no deducibles | +1,5 |
| Ingresos exentos | −2,0 |
| Diferencias de tasa en filiales extranjeras | **−8,5** |
| Créditos fiscales por I+D | −3,0 |
| **Tasa efectiva** | **13,0** |

!!! tip "Qué buscar en esa tabla"
    La línea de **filiales extranjeras** es la que revela la planeación tributaria internacional
    del ejercicio de esta semana. Si aporta −8,5 puntos, la empresa está localizando beneficio
    en jurisdicciones de baja tributación.

    La pregunta del analista no es si es legal, sino **si es sostenible**: con el impuesto
    mínimo global del 15 %, buena parte de ese ahorro desaparece. **No proyectes una tasa
    efectiva del 13 % a perpetuidad**; modela una convergencia y trata la diferencia como
    pasivo contingente.

---
