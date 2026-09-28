# Semana 31 · Sesión 2: Profundización

## 2. La Santísima Trinidad del Riesgo (Marco de Basilea) (continuación)

### B. Riesgo de Crédito (Credit Risk)
Es el riesgo de que una contraparte (un prestatario o un socio) no cumpla con sus obligaciones de pago (Default) o que su calidad crediticia se deteriore.
* **Componentes Matemáticos:**
  1. **PD (Probability of Default):** Probabilidad de que el cliente quiebre. (Ej. 2%).
  2. **LGD (Loss Given Default):** Si el cliente quiebra, ¿qué porcentaje del préstamo pierdo definitivamente? (Si el préstamo era $100, pero recuperé $40 vendiendo los activos colaterales, mi LGD es 60%).
  3. **EAD (Exposure at Default):** Cuánto dinero le debía el banco al cliente en el exacto momento del default.
* **Medición:** La **Pérdida Esperada (EL - Expected Loss)**, que se calcula multiplicando los tres factores: $EL = PD \times LGD \times EAD$. Los bancos deben apartar este monto de sus utilidades como "provisión de cartera".

### C. Riesgo Operativo (Operational Risk)
Es el riesgo de pérdida resultante de procesos internos inadecuados, personas, sistemas fallidos o eventos externos. Es el riesgo más "humano" y el más difícil de predecir con matemáticas puras.
* **Ejemplos:**
  * *Fraude interno:* Un cajero roba dinero de la bóveda.
  * *Error del sistema:* Un bug informático duplica los depósitos de 10,000 clientes (como ocurrió con Citibank por un error tipográfico que envió $900 millones al fondo de Revlon por error).
  * *Ciberataques:* Hackeos que paralizan los servidores del banco (Ransomware).
  * *Riesgo Legal:* Multas regulatorias por lavado de dinero.
* **Medición:** Como no sigue una distribución Normal limpia, se mide construyendo bases de datos históricas internas (registrando cuántas veces ha pasado un error y cuánto costó) y usando Indicadores Clave de Riesgo (KRI), como "número de transacciones que requieron reversión manual al mes".

---

## La medición del riesgo de crédito en la práctica

Los tres parámetros de la pérdida esperada no se estiman igual, ni tienen la misma fiabilidad:

**PD — Probabilidad de incumplimiento**

* **Modelos de *scoring*:** regresión logística sobre variables del deudor (ingresos, historial,
  ratios financieros). Es lo que aplicaste en el ejercicio de Bayes de la Semana 15.
* **Calificaciones externas:** las agencias publican tasas históricas de impago por escalón. Un
  BBB a 5 años ronda el 2 %; un B, el 20 %.
* **Modelos de mercado (Merton):** tratan el patrimonio como una **opción de compra** sobre los
  activos de la empresa. Si el valor de los activos cae por debajo de la deuda, los accionistas
  "no ejercen" y entregan la empresa a los acreedores. Es la base de las métricas EDF de
  Moody's KMV.

**LGD — Pérdida dado el incumplimiento**

Depende sobre todo de la **garantía** y de la **prelación** en el orden de cobro:

| Tipo de exposición | LGD típica |
|---|---|
| Hipoteca residencial | 10-25 % |
| Préstamo con garantía real | 25-45 % |
| Deuda senior sin garantía | 45-60 % |
| Deuda subordinada | 70-90 % |
| Activos muy específicos (plataformas, maquinaria a medida) | **70-90 %** |

**EAD — Exposición en el momento del incumplimiento**

Sencilla en un préstamo amortizable; difícil en líneas de crédito revolventes, porque **los
deudores en dificultades tienden a disponer del máximo disponible justo antes de impagar**. Por
eso se estima con un *factor de conversión* sobre el importe no dispuesto.

!!! warning "El parámetro que más se subestima"
    De los tres, la **PD** es la que más se revisa en las crisis y la **correlación** entre PD
    la que directamente se ignora. Un error del 20 % en la LGD cambia la pérdida esperada un
    20 %; asumir independencia cuando la correlación real es 0,15 puede multiplicar por diez el
    capital necesario, como viste en el ejercicio de esta semana.

---
