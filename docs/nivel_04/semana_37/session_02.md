# Semana 37 · Sesión 2: Profundización

## 4. Del Enterprise Value al Precio por Acción (El Puente)
El DCF te da el **Enterprise Value (EV)** o Valor de la Firma. EV es el valor de las operaciones del negocio (lo que le costaría comprar el 100% de la empresa y asumir su deuda). Pero los accionistas no quieren el EV, quieren saber cuánto vale **su acción**. 

El puente matemático es:
1. **Enterprise Value (EV):** Calculado por el DCF.
2. **(-) Deuda Neta:** (Deuda Total - Efectivo). Los accionistas no reciben esto, los bancos sí. Se resta.
3. **(=) Valor del Patrimonio (Equity Value):** Lo que pertenece a los accionistas.
4. **(/) Número de Acciones en Circulación:** (Shares Outstanding).
5. **(=) Valor Intrínseco por Acción (Target Price):** Lo que deberías pagar hoy por la acción.

---

## Los tres métodos para calcular el Valor Terminal

El valor terminal suele ser el 60-80 % de una valuación por DCF. Merece más de una línea.

**A. Crecimiento perpetuo (Gordon)**

$$TV_n = \frac{FCFF_{n+1}}{WACC - g} = \frac{FCFF_n(1+g)}{WACC - g}$$

* **Ventaja:** conceptualmente correcto; el valor sale de los fundamentales del propio negocio.
* **Riesgo:** extremadamente sensible a $g$. Y $g$ **no puede superar el crecimiento nominal de
  la economía a largo plazo** (2-3 %), porque una empresa que creciera más rápido que el PIB
  para siempre acabaría **siendo** el PIB.

**B. Múltiplo de salida**

$$TV_n = EBITDA_n \times \text{múltiplo del sector}$$

* **Ventaja:** anclado en lo que el mercado paga hoy realmente.
* **Riesgo:** importa el múltiplo **actual** al futuro. Si el sector cotiza hoy en máximos
  históricos, estás proyectando esa euforia a perpetuidad. Y mezcla valuación intrínseca con
  relativa, que es lo que el DCF pretendía evitar.

**C. Valor de liquidación**

$$TV_n = \text{Valor de realización de los activos} - \text{Pasivos}$$

* **Ventaja:** el más conservador; adecuado para activos con vida finita (una concesión, una
  mina, una patente).
* **Riesgo:** irrelevante para un negocio en marcha, cuyo valor supera con creces sus activos.

**La buena práctica: calcular los dos primeros y comprobar que convergen.** Si Gordon da un EV
de $\$1{,}200$ M y el múltiplo de salida da $\$600$ M, uno de los dos supuestos está mal. La
diferencia obliga a explicar por qué.

**El puente entre ambos.** Dados un $TV$ por múltiplo, se puede despejar la $g$ implícita:

$$g_{implícita} = WACC - \frac{FCFF_{n+1}}{TV_n}$$

Si esa $g$ implícita resulta ser del 6 %, tu múltiplo de salida es insostenible.

---

## Los errores que arruinan un DCF

Ordenados por frecuencia con la que aparecen en modelos reales:

1. **Descontar el valor terminal un período de más.** Gordon lo sitúa en el año $n$, no en
   $n+1$, aunque use el flujo del año $n+1$ en el numerador. Divide por $(1+WACC)^n$.
2. **$g \ge WACC$.** El denominador se vuelve cero o negativo y el modelo devuelve infinito o
   un valor negativo. Matemáticamente imposible; económicamente absurdo.
3. **Restar los intereses del FCFF.** Doble conteo: el costo de la deuda ya está en el WACC.
4. **Usar el valor contable del patrimonio** para calcular los pesos del WACC en lugar del valor
   de mercado.
5. **Proyectar márgenes crecientes a perpetuidad.** La competencia existe. Si tu modelo asume
   que el margen EBIT sube del 15 % al 25 % y se queda ahí, tienes que justificar qué barrera de
   entrada lo protege (Semana 3).
6. **Ignorar el capital de trabajo.** Una empresa que crece **siempre** consume caja en capital
   de trabajo. Omitirlo infla el FCFF sistemáticamente.
7. **Olvidar la normalización del último año explícito.** El año $n$ debe representar un estado
   **estacionario**: CapEx ≈ depreciación, capital de trabajo creciendo al ritmo de $g$. Si el
   año $n$ tiene un CapEx anormalmente bajo, el valor terminal hereda esa anomalía multiplicada
   por una perpetuidad.
8. **Falsa precisión.** Presentar "$\$116{,}79$ por acción" cuando el rango razonable es
   $\$95$–$\$140$. Un DCF serio se presenta con matriz de sensibilidad.

!!! tip "La prueba de humo de todo DCF"
    Antes de presentar el resultado, hazte tres preguntas:

    1. **¿Qué está descontando el mercado?** Invierte el modelo: ¿qué crecimiento y qué márgenes
       justifican el precio **actual** de la acción? Si el mercado implica un 3 % de crecimiento
       y tú asumes un 12 %, tienes que explicar por qué sabes algo que el mercado no.
    2. **¿Cuánto pesa el valor terminal?** Si supera el 85 %, tu valuación no depende de tu
       análisis de los flujos: depende de un supuesto de perpetuidad.
    3. **¿Sobrevive el rango a la sensibilidad?** Si con WACC ±1 punto y $g$ ±0,5 puntos la
       recomendación cambia de comprar a vender, **no tienes una tesis**: tienes un número.

---
