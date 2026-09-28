# Semana 25 · Sesión 2: Profundización

## 4. El Payback Descontado (Discounted Payback)
Ni el VAN ni la TIR te dicen *cuándo* recuperas tu dinero. El Payback mide cuántos años tarda la empresa en recuperar la inversión inicial, **pero descontando los flujos a valor presente**.

* **Regla de Decisión:** Si el Payback es menor al límite de tiempo impuesto por la empresa (ej. queremos recuperar el dinero en menos de 3 años), se acepta.
* **Uso real:** No se usa para decidir si un proyecto crea valor, sino para calibrar el **riesgo de liquidez**. Un proyecto con un VAN altísimo pero un Payback de 10 años puede ser rechazado si la empresa necesita efectivo rápido para sobrevivir a una crisis.

---

## 5. El Conflicto Clásico: VAN vs. TIR (Proyectos Mutuamente Excluyentes)
A veces, tienes dos proyectos excelentes, pero solo puedes elegir uno (ej. construir un puente de peaje o un túnel de peaje en el mismo río; son mutuamente excluyentes).
* **Proyecto A (Túnel):** Inversión $1,000. Retorno porcentual (TIR) = 25%. VAN = $500.
* **Proyecto B (Puente):** Inversión $5,000. Retorno porcentual (TIR) = 15%. VAN = $2,000.

**El Analista Novato** elige el Proyecto A porque "rinde un 25%". 
**El Analista Profesional** elige el Proyecto B porque crea **$2,000 de riqueza absoluta** en lugar de $500. El VAN siempre gana en proyectos mutuamente excluyentes porque mide el tamaño total de la torta, no el porcentaje.

---

## Opciones reales: el valor que el VAN no captura

El VAN tradicional asume una decisión **estática**: se invierte hoy y se ejecuta el plan pase lo
que pase. En la realidad, la dirección puede reaccionar, y esa flexibilidad **vale dinero**.

$$\text{VAN ampliado} = \text{VAN tradicional} + \text{Valor de las opciones reales}$$

| Tipo de opción | En qué consiste | Ejemplo |
|---|---|---|
| **De diferir** | Esperar a tener más información antes de invertir | Una concesión minera que no obliga a explotar de inmediato |
| **De expandir** | Ampliar si el proyecto va bien | Abrir una tienda piloto con opción a 50 más |
| **De abandonar** | Salir y recuperar valor residual | Maquinaria con mercado de segunda mano |
| **De cambiar** | Alterar insumos o productos | Una planta que puede quemar gas o fuel según precios |
| **De crecimiento** | El proyecto habilita otros futuros | Entrar en un mercado nuevo aunque el primer proyecto sea marginal |

**Por qué importa.** Un proyecto con VAN de $-\$50{,}000$ puede ser aceptable si incorpora una
opción de expansión valiosa. Y al revés: un VAN positivo puede ser un espejismo si el proyecto
**elimina** flexibilidad.

**Ejemplo.** Una farmacéutica invierte $\$10$ M en la fase I de un fármaco con VAN esperado
negativo. Pero esa inversión **compra el derecho** a invertir $\$100$ M en la fase III si los
resultados son buenos. Sin la fase I, esa opción no existe. Valorar solo el flujo de la fase I
es como valorar una opción de compra ignorando que da derecho a comprar.

!!! warning "El riesgo de abusar del concepto"
    Las opciones reales son un argumento legítimo y también la excusa favorita para justificar
    proyectos malos: *"tiene valor estratégico"*.

    Para que una opción real sea real deben cumplirse tres condiciones:

    1. **Existe incertidumbre genuina** que se resolverá con el tiempo.
    2. **La decisión es genuinamente diferible o reversible** — hay flexibilidad real, no
       retórica.
    3. **La empresa tiene la capacidad efectiva de ejercerla** (capital, capacidad, derechos).

    Si no se cumplen las tres, no hay opción: hay un proyecto con VAN negativo y una narrativa.

---
