# Semana 9 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: El "Cash Burn" en Startups y la trampa del Enfoque en Crecimiento
*Eres analista de capital de riesgo (Venture Capital) evaluando si invertir en una startup de entrega de alimentos a domicilio (ej. estilo UberEats o Rappi).*

La startup muestra su Estado de Resultados: "¡Nuestro Ingreso creció 300%! Nuestra Utilidad Bruta es altísima". 
Pero tú pides el Estado de Flujos de Efectivo y ves la realidad:
* **CFO es altamente negativo ($- \text{millones}$):** La startup regala el delivery subsidiando el costo de envío. Paga a los repartidores en efectivo de inmediato, pero cobra una comisión a los restaurantes a 60 días. El descalce de efectivo quema (burn) millones.
* **CFI es negativo:** Gasta millones desarrollando su app y comprando servidores.
* **CFF es altamente positivo:** Solo sobrevive porque cada 12 meses convence a fondos de inversión de darle capital fresco a cambio de acciones (Financing).

**Tu decisión como analista:**
Entiendes que el modelo de negocio tiene **FCF negativo masivo**. No es un negocio sostenible por sí solo; es un esquema de "esperar el monopolio" (Blitzscaling). Evalúas si su posicionamiento de mercado justifica tanto *cash burn* antes de lograr dominar el mercado y poder subir precios al consumidor final. Si no logran dominar el mercado, irán a quiebra cuando se acabe el efectivo de los fondos de inversión, sin importar cuántos "ingresos" contables muestren. *El Flujo de Efectivo es el polígrafo de la empresa.*

---


## 7. Tareas y Evaluación de la Semana 9

**A. Lectura Obligatoria:**
* Warren, Reeve, Duchac. *Contabilidad Financiera* (Capítulo de Estado de Flujos de Efectivo).
* *Lectura recomendada:* Capítulo 2 de *Valuación de Empresas* (McKinsey & Company) sobre la relación entre el ROIC, el Crecimiento y el FCF.

**B. Preguntas de Reflexión:**
1. ¿Por qué la Depreciación se suma a la Utilidad Neta al calcular el Flujo de Caja Operativo por el método indirecto?
2. Explica con un ejemplo por qué una empresa puede reportar una Utilidad Neta millonaria y al mismo tiempo ir a la quiebra por falta de efectivo.

**C. Ejercicio Práctico a entregar:**
La empresa "GreenLeaf S.A." reportó en 2024 las siguientes cifras (en millones):
* Utilidad Neta: $\$500$
* Depreciación y Amortización: $\$120$
* Disminución en Cuentas por Cobrar: $\$50$ *(Ojo: si disminuye, es positivo para efectivo)*
* Aumento en Inventario: $\$80$ *(Negativo para efectivo)*
* Aumento en Cuentas por Pagar: $\$40$ *(Positivo para efectivo)*
* Compra de nueva planta física (CapEx): $\$200$
* Pago de dividendos en efectivo a accionistas: $\$100$
* Emisión de nuevos bonos a largo plazo: $\$150$

Contesta paso a paso:
1. Calcula el Flujo de Efectivo de Operación (CFO) usando el método indirecto.
2. ¿Cuál es el Flujo de Efectivo de Inversión (CFI)?
3. ¿Cuál es el Flujo de Efectivo de Financiamiento (CFF)? *(Recuerda que el pago de dividendos es salida, la emisión de bonos es entrada).*
4. Calcula el Flujo de Caja Libre (FCF) para este año. ¿Cuánto efectivo excedente le quedó a GreenLeaf para reducir deuda o hacer adquisiciones?

??? success "Solución del Ejercicio C"

    **1. Flujo de Efectivo de Operación (CFO) — método indirecto**

    | Concepto | Monto |
    |---|---|
    | Utilidad Neta | 500 |
    | (+) Depreciación y Amortización | 120 |
    | (+) Disminución en Cuentas por Cobrar | 50 |
    | (−) Aumento en Inventario | (80) |
    | (+) Aumento en Cuentas por Pagar | 40 |
    | **= CFO** | **630** |

    La lógica de los signos: se **suma** la D&A porque es un gasto contable que
    nunca salió en efectivo. Cobrar cartera pendiente (CxC baja) **entra** efectivo;
    acumular inventario **inmoviliza** efectivo; y estirar el pago a proveedores
    (CxP sube) **retiene** efectivo.

    **2. Flujo de Efectivo de Inversión (CFI)**

    $$CFI = -200 \text{ (CapEx: compra de planta física)}$$

    **3. Flujo de Efectivo de Financiamiento (CFF)**

    $$CFF = \underbrace{+150}_{\text{emisión de bonos}} \underbrace{-100}_{\text{dividendos}} = +50$$

    **4. Flujo de Caja Libre (FCF)**

    $$FCF = CFO - CapEx = 630 - 200 = \mathbf{430}$$

    **Interpretación:** a GreenLeaf le quedaron **430 millones** de efectivo
    genuinamente libre tras operar y mantener su capacidad productiva. Con eso pagó
    los 100 de dividendos y aún le sobran **330 millones** para amortizar deuda,
    hacer adquisiciones o recomprar acciones. Es una empresa sana: **genera más caja
    de la que necesita.**

    **Variación neta del efectivo del año** (para cuadrar con el Balance):

    $$\Delta \text{Efectivo} = CFO + CFI + CFF = 630 - 200 + 50 = +480$$

    !!! tip "Por qué el FCF importa más que la Utilidad Neta"
        Aquí la utilidad neta es 500 y el CFO es 630: la empresa genera **más caja
        que utilidad contable**, señal de calidad. Cuando ocurre lo contrario —
        utilidad alta y CFO bajo o negativo — suele haber ventas a crédito que no
        se cobran o inventario que no rota. Ese es exactamente el caso que analizas
        en el ejercicio integrador de la Semana 10.

        El FCF, no la utilidad, es lo que descontarás en el modelo DCF (Semana 37).

---
