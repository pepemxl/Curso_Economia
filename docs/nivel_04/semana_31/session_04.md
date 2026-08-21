# Semana 31 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: El escándalo de "Fat Finger" en Knight Capital (La fusión de los 3 riesgos)
*Eres un regulador el 1 de agosto de 2012. Knight Capital Group, uno de los mayores creadores de mercado de Wall Street, pierde $440 millones en 45 minutos.*

**La Autopsia del Riesgo:**
1. **Riesgo Operativo (El origen):** Knight Capital actualizó su software de trading. En un servidor viejo, olvidaron borrar un código de prueba. Al abrir el mercado, ese código muerto se activó y empezó a comprar acciones al precio más alto del día y venderlas al precio más bajo, automáticamente y miles de veces por segundo.
2. **Riesgo de Mercado (El efecto):** Este error operativo se tradujo en una posición masiva y desastrosa en el mercado de acciones. El algoritmo compró millones de acciones que no valían nada en nanosegundos. El mercado reaccionó bajando los precios.
3. **Riesgo de Crédito (El desenlace):** Knight Capital quedó en bancarrota técnica. No podía pagar a sus contrapartes (Clearinghouses). Tuvo que ser rescatada por un consorcio de bancos a un precio de liquidación.

**Lección de Gestión de Riesgos:** Los riesgos no viven en frascos separados. Un fallo tecnológico (Op Risk) se convierte instantáneamente en una pérdida masiva de trading (Market Risk), lo que desencadena un impago a los clearinghouses (Credit Risk). El Risk Management moderno exige pruebas de estrés cruzadas: *"¿Qué pasa si nuestro sistema falla (Op) justo el día que la Reserva Federal sube tasas sorpresivamente (Market) y nuestro mayor cliente se declara en bancarrota (Credit)?"*

---

## 6. Tareas y Evaluación de la Semana 31

**A. Lectura Obligatoria:**
* *Risk Management and Financial Institutions* (John C. Hull). Capítulos 2 y 3 (Tipos de Riesgo y Riesgo de Crédito).
* *Lectura recomendada:* Normativa de Basilea III (Resumen ejecutivo del Banco de Pagos Internacionales - BIS).

**B. Preguntas de Reflexión:**
1. Menciona por qué el riesgo operativo es más difícil de cuantificar matemáticamente y de cubrir con derivados financieros que el riesgo de mercado o el riesgo de crédito.
2. Si una empresa vende sus productos a crédito a 90 días a clientes en el extranjero (ej. el cliente está en Europa y la empresa en USA), ¿Qué dos tipos de riesgos de los tres vistos en clase está enfrentando simultáneamente la empresa? Explica cómo interactúan.

**C. Ejercicio Práctico a entregar:**
Evalúas a una empresa petrolera que pidió un préstamo corporativo de **$50 Millones** al banco donde trabajas. Debido a la caída del precio del petróleo, tu equipo de análisis ajusta sus métricas de riesgo:

* **Exposición al Default (EAD):** $50 Millones ( la empresa aún debe todo el principal).
* **Probabilidad de Default (PD):** Aumenta del 2% al 8% anual (recesión inminente).
* **Pérdida Dado el Default (LGD):** Si quiebra, sus plataformas petroleras(inservibles para otros fines) sólo se venden a precio de chatarra. Tu recuperación será del 30% (LGD = 70%).

Contesta:
1. Calcula la Pérdida Esperada (Expected Loss - EL) para el banco en el escenario actual (PD 8% y LGD 70%). Muestra la fórmula detallada.
2. El banco exige provisiones de capital iguales a la Pérdida Esperada más un colchón de seguridad (Capital Económico). Si esta pérdida esperada es mayor al 1% de la cartera total del banco, el regulador intervendrá la institución. ¿Cuánto dinero en efectivo debe apartar el banco hoy en su cuenta de provisiones para cubrir este único cliente?
3. Como Director de Riesgos, ¿qué instrumento de los vistos en la Semana 30 (Derivados) sugerirías usar para mitigar el Riesgo de Crédito si la empresa efectivamente entra en default en 12 meses? (Pista: Piensa en un contrato que pague si la empresa se va a cero).
