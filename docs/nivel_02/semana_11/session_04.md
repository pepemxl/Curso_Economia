# Semana 11 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: "¿Verdad o trampa en la sala de ventas?"
*Estás analizando un proyecto de "Crowdfunding Inmobiliario" para invertir tus ahorros. La plataforma te vende la siguiente promesa:* 

*"Invierte $10,000 hoy. Te pagaremos 3% de rentabilidad FIJA cada trimestre (cada 3 meses) durante 5 años. Al final de los 5 años te devolveremos tus $10,000 íntegros."*
*La vendedora te dice con una sonrisa "¡Es un rendimiento del 12% anual, mejor que cualquier banco!"*

**Tu análisis como profesional financiero:**
1. **La Tasa Nominal:** Efectivamente, 3% por 4 trimestres = 12% anual. (Es la Tasa Nominal). 
2. **La Capitalización Oculta:** Como te pagan 3% cada 3 meses, esos intereses se quedan en la plataforma generando nuevo interés cada trimestre. Hay un efecto compuesto oculto.
3. **El cálculo real:** La Tasa Efectiva Anual (EAR) es: $(1 + 0.12/4)^4 - 1 = (1.03)^4 - 1 = 12.55\%$.
4. **El red flag contable:** Si te pagan el 3% trimestral y te devuelven el principal íntegro al final, los flujos de caja no son un interés puro a vencimiento. Debemos traer esos dividendos trimestrales al Valor Presente usando una tasa de descuento (tu costo de oportunidad real, quizás comparative con un bono del tesoro a 5 años que rinda 5%).
5. **Veredicto:** La inversión no es una "estafa" matemática, pero te están vendiendo la Tasa Nominal para que se vea más bonita. Tú debes calcular el Valor Presente de todos esos pagos trimestrales de $300 ($10,000 x 3%) más el principal final, descontados a tu tasa exigida, para saber si en realidad el Valor Presente Neto (VAN) de esta inversión supera los $10,000 que cuesta hoy.

---

## 8. Tareas y Evaluación de la Semana 11

**A. Lectura Obligatoria:**
* Ross, Westerfield, Jordan. *Fundamentos de Finanzas Corporativas*. Capítulo 4 (Valoración de flujos de efectivo). Mc Graw Hill.

**B. Preguntas de Reflexión:**
1. Explica por qué en la economía moderna, el "Interés Simple" no se usa para evaluar proyectos de inversión a largo plazo. ¿Qué suposición rompe el interés simple frente a la realidad del mercado?
2. Si la inflación de un país es del 100% anual (hiperinflación), ¿qué le sucede al "Valor Presente" de una utilidad que la empresa espera recibir en 5 años más? ¿Por qué los analistas en estos países desechan proyectos de retorno a largo plazo?

**C. Ejercicio Matemático a entregar (Calculator y papel en mano):**
1. **Cálculo de Interés Compuesto:** Inviertes $15,000 al 8% anual con capitalización compuesta. ¿Cuánto tendrás exactamente después de 10 años?
2. **Cálculo de Valor Presente:** Te ofrecen un pagaré que te pagará $50,000 dentro de 5 años. Si tu costo de oportunidad (tasa de descuento exigida) es del 6% anual, ¿Cuál es el Valor Presente de ese pagaré? ¿Cuánto deberías pagar hoy por él como máximo?
3. **Comparación de Tasas:** El Banco A te ofrece un Certificado a Plazo al 12% capitalizable semestralmente ($m=2$). El Banco B te ofrece el 11.8% capitalizable mensualmente ($m=12$). ¿Cuál banco te da realmente la mejor Tasa Efectiva Anual (muestra tus cálculos)?


??? success "Solución del Ejercicio C"

    **1. Interés compuesto — $15,000 al 8 % durante 10 años**

    $$VF = VP(1+i)^n = 15{,}000\,(1.08)^{10}$$

    $$(1.08)^{10} = 2.158925$$

    $$VF = 15{,}000 \times 2.158925 = \mathbf{\$32{,}383.87}$$

    De ese total, $\$15{,}000$ es tu capital y **$\$17{,}383.87$ son intereses**: el
    dinero más que se duplicó. Con interés *simple* solo habrías obtenido
    $15{,}000 \times 0.08 \times 10 = \$12{,}000$ de intereses. La diferencia de
    $\$5{,}383.87$ es, literalmente, el valor de los intereses sobre los intereses.

    **2. Valor Presente del pagaré**

    $$VP = \frac{VF}{(1+i)^n} = \frac{50{,}000}{(1.06)^5} = \frac{50{,}000}{1.338226}$$

    $$VP = \mathbf{\$37{,}362.91}$$

    **Máximo a pagar hoy: $\$37,362.91.** A ese precio exacto obtienes justo tu 6 %
    exigido, ni más ni menos. Si te lo venden más barato, el rendimiento supera tu
    costo de oportunidad (VAN positivo). Si te piden más, estarías aceptando un
    rendimiento inferior al que puedes conseguir en otra parte.

    **3. Comparación de tasas efectivas**

    La tasa nominal **no es comparable** entre bancos con distinta frecuencia de
    capitalización. Hay que llevar ambas a Tasa Efectiva Anual:

    $$EAR = \left(1 + \frac{j}{m}\right)^{m} - 1$$

    *Banco A — 12 % capitalizable semestralmente ($m=2$):*

    $$EAR_A = \left(1 + \frac{0.12}{2}\right)^{2} - 1 = (1.06)^2 - 1 = \mathbf{12.36\%}$$

    *Banco B — 11.8 % capitalizable mensualmente ($m=12$):*

    $$EAR_B = \left(1 + \frac{0.118}{12}\right)^{12} - 1 = (1.0098333)^{12} - 1 = \mathbf{12.4596\%}$$

    **Gana el Banco B**, por 0.10 puntos porcentuales.

    !!! tip "La lección del ejercicio"
        El Banco B ofrece una tasa **nominal más baja** (11.8 % contra 12 %) y aun así
        paga **más**. La capitalización mensual reinvierte los intereses 12 veces al
        año en lugar de 2, y esa frecuencia compensa con creces los 0.2 puntos de
        desventaja nominal.

        Por eso, ante dos productos financieros, **nunca compares tasas nominales**:
        convierte todo a EAR. Es el mismo principio que protege al consumidor cuando
        una tarjeta anuncia "3 % mensual" (que en realidad es 42.6 % efectivo anual,
        como verás en la Semana 12).

---
*¡Felicidades por completar la Semana 11! Ya dominas la base matemática de las finanzas. Comprender el interés compuesto y descontar valores cambiará para siempre cómo ves los préstamos y las inversiones. En la Semana 12 subiremos la complejidad: Tasas equivalentes, inflación y el manejo de Series de Pagos (Anualidades y Perpetuidades).*