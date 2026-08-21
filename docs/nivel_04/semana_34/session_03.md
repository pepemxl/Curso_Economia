# Semana 34 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: ¿Pasa el banco "TrustBank" la prueba de Basilea III?
El regulador revisa la bóveda de TrustBank y encuentra lo siguiente:

* **Activos Líquidos de Alta Calidad (HQLA):** 
  * Efectivo en bóveda: $500 Millones
  * Bonos del Tesoro a 1 año: $300 Millones
  * *Total HQLA = $800 Millones*
* **Salidas Netas estimadas de Efectivo en 30 días (si hay pánico):** $700 Millones.

**Cálculo del LCR:**
$$ LCR = \frac{800 \text{ Millones}}{700 \text{ Millones}} = 1.1428 \text{ (114.28\%)} $$

**Veredicto del Regulador:** ¡Aprobado! El LCR es superior al 100%. TrustBank tiene $800M en efectivo listo para soportar una corrida bancaria de $700M en el próximo mes. No necesitará rescates del Banco Central.

**El giro del Stress Testing:**
El regulador aplica un shock: *"Imaginemos que hay una crisis y el rating del país cae, los Bonos del Tesoro que tienes pierden el 20% de su valor y se evaporan de la categoría HQLA"*.
* Nuevo HQLA = Efectivo ($500M) + Bonos desvalorizados al 80% ($240M) = $740M.
* Nuevo LCR = $740M / $700M = 105.7%. 
*Aprobado, pero apenas. El banco recibe una advertencia de liquidez.*

---
