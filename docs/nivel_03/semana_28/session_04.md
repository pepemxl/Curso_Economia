# Semana 28 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: La ruina del "Carry Trade" en 2008
*Eres un analista en un Hedge Fund. Te das cuenta de que en Japón las tasas de interés estaban en 0%, mientras que en EE. UU. los bonos del tesoro pagaban 5% anual.*

Ideas una estrategia "supuestamente sin riesgo" llamada **Carry Trade**: 
Pides prestados $100 Millones de Yenes Japoneses al 0.5%. Conviertes los Yenes a Dólares (Forex). Compras Bonos del Tesoro de USA al 5% anul. 
*Situación ideal:* Pagas 0.5% de interés en Japón y ganas 5% en USA. Ganancias de 4.5% millonarias "gratis" (apalancados por la deuda en Yenes).

**El Efecto Dominó (Black Swan de 2008):**
La crisis de Lehman Brothers hace pánico global. Los inversores entran en modo "Risk Off" (aversionar el riesgo) y venden todo lo estadounidense para refugiarse. Deben devolver los Yenes prestados. La demanda masiva de Yenes hace que la moneda Japonesa se **aprecíe bruscamente** un 20% frente al Dólar. 

**La Matemática de la Ruina:**
Ahora tus Dólares valen 20% menos en Yenes. Cuando intentas devolver el préstamo yen Japonés, la pérdida cambiaria del 20% aniquila la ganancia del 4.5% de los bonos. Pierdes el 15% de tu capital en días. Los mercados no entienden de reservas internacionales; un movimiento repentino en el mercado de divisas (Forex) puede destruir billones de dólares más rápido de lo que la macro fundamental se mueve.

---

## 8. Tareas y Evaluación de la Semana 28

**A. Lectura Obligatoria:**
* *Fundamentos de Finanzas Corporativas* (Ross, Westerfield, Jordan) – Capítulos 7 (Mercados de Renta Variable) y 8 (Valuación de Bonos).
* Repasa el impacto de las subidas de tasas en la banca y los bonos, visto en la Semana 6 (Política Monetaria).

**B. Preguntas de Reflexión:**
1. Si la Reserva Federal anuncia una política de recorte de tasas de interés (bajan las tasas del 5% al 2%), ¿qué le ocurriría matemáticamente al precio de un bono del tesoro a 10 años que pagaba un cupón fijo del 5%?
2. En tiempos de guerra geopolítica o pandemia, ¿qué suele ocurrir con el riesgo fiscal y el tipo de cambio de emerging markets respecto a la "Renta Fija Refugio" (el dólar / bonos del tesoro de EE.UU.)?

**C. Ejercicio Práctico a entregar:**
1. **Renta Variable:** Si la empresa "TechGlobal" tiene 50 millones de acciones en circulación y cada acción cotiza a $120 en bolsa. Su Utilidad Neta fue de $200 millones. Calcula su Market Cap (Capitalización de mercado) y su Ratio P/E (Precio / Utilidad por acción, EPS). ¿Qué significa este P/E para el mercado?
2. **Renta Fija:** Tienes un bono corporativo con valor nominal de $10,000 que vence en exactamente 1 año y paga un cupón final del 8% ($10,800 en total al vencimiento). La inflación y la crisis han hecho que los inversores exijan un rendimiento de mercado (YTM) del 12% para comprar bonos de tu empresa. ¿A qué precio máximo un inversor estará dispuesto a comprarte el bono en el mercado secundario hoy? (Usa la fórmula de Valor Presente).

??? success "Solución del Ejercicio C"

    **1. Renta Variable — "TechGlobal"**

    *Capitalización de mercado:*

    $$\text{Market Cap} = \text{Acciones} \times \text{Precio} = 50{,}000{,}000 \times \$120$$

    $$\mathbf{= \$6{,}000 \text{ millones}}$$

    *Utilidad por acción (EPS):*

    $$EPS = \frac{\text{Utilidad Neta}}{\text{Acciones}} = \frac{200{,}000{,}000}{50{,}000{,}000} = \mathbf{\$4.00}$$

    *Ratio Precio / Utilidad:*

    $$P/E = \frac{\text{Precio}}{EPS} = \frac{120}{4} = \mathbf{30\times}$$

    **Qué significa un P/E de 30:**

    * **Lectura literal:** el mercado paga $\$30$ por cada $\$1$ de utilidad anual.
    * **Lectura de plazo:** a utilidades constantes, se necesitarían **30 años** para
      recuperar la inversión vía beneficios.
    * **Lectura de rendimiento:** el *earnings yield* inverso es
      $1/30 = 3.33\%$ anual.

    **Lo que realmente comunica: expectativas de crecimiento.** Nadie paga 30 años de
    utilidades por una empresa estancada. Un P/E de 30 dice que el mercado espera que
    esas utilidades **crezcan sustancialmente**. Como referencia, el S&P 500 promedia
    históricamente un P/E de 15-20; las tecnológicas en expansión cotizan a 30-50;
    las utilities maduras, a 10-15.

    El P/E alto es un arma de doble filo: si TechGlobal decepciona en su próximo
    reporte, no solo caen las utilidades — el múltiplo también se comprime. **Los dos
    factores se multiplican a la baja**, y por eso las acciones de alto P/E caen tan
    violentamente ante una mala noticia.

    **2. Renta Fija — el bono corporativo**

    Solo hay un flujo: $\$10{,}800$ dentro de un año (principal + cupón del 8 %).
    Se descuenta al rendimiento que el mercado exige **hoy**:

    $$P = \frac{VF}{1 + YTM} = \frac{10{,}800}{1.12}$$

    $$\mathbf{P = \$9{,}642.86}$$

    **El bono cotiza con descuento**: vale $\$9{,}642.86$ frente a un nominal de
    $\$10{,}000$, una pérdida de **$\$357.14$ (−3.57 %)** para quien lo tenga en cartera.

    La razón es el desajuste entre el cupón y la tasa de mercado. El bono está
    contractualmente obligado a pagar solo 8 %, pero los inversionistas ahora
    consiguen 12 % en otra parte. **El cupón es fijo; lo único que puede ajustarse es
    el precio.** Al bajar a $\$9{,}642.86$, el comprador obtiene su 12 %:
    $(10{,}800 - 9{,}642.86)/9{,}642.86 = 12\%$ ✓

    !!! tip "La relación inversa precio-tasa"
        Es el principio más importante de la renta fija:

        | Situación | Precio del bono |
        |---|---|
        | Cupón $>$ YTM | Cotiza **con prima** (sobre par) |
        | Cupón $=$ YTM | Cotiza **a la par** |
        | Cupón $<$ YTM | Cotiza **con descuento** ← este caso |

        Aquí la pérdida fue de solo 3.57 % porque el bono vence en **un año**. Si
        venciera en 10 años, la misma subida de tasas provocaría una caída de precio
        cercana al **22 %**. Esa sensibilidad se mide con la **duración**, y explica
        por qué los fondos de bonos de largo plazo sufrieron pérdidas de dos dígitos
        en los ciclos de alza de tasas.

        Y ojo con el nombre: la renta fija se llama así porque el *cupón* es fijo,
        **no porque el precio lo sea**.
