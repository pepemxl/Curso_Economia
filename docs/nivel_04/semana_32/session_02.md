# Semana 32 · Sesión 2: Profundización

## 4. Expected Shortfall (CVaR): El Sucesor del VaR
Basilea III (la regulación bancaria moderna) obliga a los bancos a usar el **Expected Shortfall** (también llamado CVaR o Conditional VaR) porque resuelve el defecto del VaR.
* **Definición:** Es el promedio matemático de todas las pérdidas que exceden el VaR. Te dice: *"Si las cosas salen mal (caes en el peor 1%), ¿cuánto perderás en promedio?"*
* **Cálculo en Excel (VaR Histórico):** Si tuviste 100 días malos peores que el VaR, el CVaR es el `=PROMEDIO()` de esos 100 días.

---

## 5. Uso de Derivados para Cobertura (Hedging)
La cobertura (Hedging) es tomar una posición en un derivado que genere una ganancia si tu cartera principal pierde valor, neutralizando el riesgo. 

**A. Hedging de Renta Variable (Acciones) con Futuros:**
Si gestionas un portafolio de $10 Millones en acciones del S&P 500 y temes que la bolsa caiga un 10% el próximo mes por una decisión del Banco Central, puedes vender Futuros del S&P 500.
* *Cálculo:* Necesitas vender $10 Millones en futuros. Si la bolsa cae 10%, tu portafolio pierde $1 Millón, pero tu futuro corto te genera +$1 Millón. 
* *Matemática con Beta:* Si tu portafolio tiene una Beta de 1.5 (Semana 24), debes sobre-cubrirte. Venderás $15 Millones en futuros ($10M \times 1.5$) para compensar que tus acciones caerán más fuerte que el mercado.

**B. Hedging de Renta Fija (Bonos) con Swaps:**
Si tienes una cartera de bonos a largo plazo y temes que las tasas de interés suban (lo que destruiría el precio de tus bonos, como vimos en la Semana 28), entras en un **Swap de Tasa de Interés** donde pagas una tasa fija y recibes una tasa variable. Al subir las tasas, la tasa variable que recibes sube, compensando la caída del precio de tus bonos.

---
