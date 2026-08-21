# Semana 13 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: El Cuadro de Amortización Francés
Pides un préstamo al banco de **$1,000** a una tasa del **10% anual** para pagar en **2 años (2 cuotas anuales)**. 

**Paso 1: Calcular la Cuota Fija (Sistema Francés)**
Usamos la fórmula de VP de anualidad ordinaria: $VP = C \times \frac{1 - (1+i)^{-n}}{i}$
$1,000 = C \times \frac{1 - (1.10)^{-2}}{0.10}$
$1,000 = C \times 1.7355$
**$C = \$576.19$** (Esta será tu cuota fija durante los 2 años).

**Paso 2: Construcción del Cuadro de Amortización**

| Año | Saldo Inicial | Cuota Total | Interés (10% s/ Saldo) | Amort. Capital | Saldo Final |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | $1,000.00 | $576.19 | $100.00 | $476.19 | **$523.81** |
| 2 | $523.81 | $576.19 | $52.38 | $523.81 | **$0.00** |

*Análisis de la tabla:*
* Año 1: Debes $1,000. El interés es 100. Tu cuota de 576.19 paga los 100 de interés y sobran 476.19 para bajar el capital. El saldo final es 523.81.
* Año 2: Ahora debes 523.81. El interés es 52.38. La misma cuota de 576.19 paga los intereses y sobra justo 523.81 para saldar la deuda por completo.

---

