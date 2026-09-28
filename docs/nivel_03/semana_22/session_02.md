# Semana 22 · Sesión 2: Profundización

## 4. El Flujo de Caja Libre (FCF - Free Cash Flow)
El EBITDA te dice cuánta caja genera el negocio *antes* de pagar impuestos y antes de mantener la maquinaria. El **FCF** te dice cuánta caja **realmente sobra** para repartir entre bancos y accionistas *después* de pagar impuestos y mantener el negocio vivo (CapEx).

Existen dos tipos de FCF:

**A. FCFF (Free Cash Flow to the Firm - Flujo de Caja Libre de la Firma):**
Es el efectivo que sobra para TODOS los inversores (bancos y accionistas). Se usa para valorar toda la empresa (Valuación Enterprise Value).
* **Fórmula:** 
  $FCFF = EBIT \times (1 - \text{Tasa de Impuestos}) + \text{Depreciación} - \text{CapEx} - \text{Aumento en Capital de Trabajo}$
  *(Nota: $EBIT \times (1-T)$ se conoce como NOPAT - Net Operating Profit After Taxes).*

**B. FCFE (Free Cash Flow to Equity - Flujo de Caja Libre del Accionista):**
Es el efectivo que sobra **únicamente para los accionistas**, después de pagar impuestos, CapEx, y **después de pagar intereses y recibir/pagar deuda**. Se usa para valorar directamente las acciones (Market Cap).
* **Fórmula simplificada:** 
  $FCFE = FCFF - \text{Intereses} \times (1 - T) + \text{Nueva Deuda} - \text{Amortización de Deuda}$

---

## El Dupont extendido de cinco factores

La versión de tres factores dice **qué** impulsa el ROE. La de cinco dice **dónde exactamente**
está el problema, separando lo operativo de lo financiero y lo fiscal:

$$ROE = \underbrace{\frac{UN}{EBT}}_{\text{carga fiscal}} \times \underbrace{\frac{EBT}{EBIT}}_{\text{carga financiera}} \times \underbrace{\frac{EBIT}{Ventas}}_{\text{margen operativo}} \times \underbrace{\frac{Ventas}{Activos}}_{\text{rotación}} \times \underbrace{\frac{Activos}{Patrimonio}}_{\text{apalancamiento}}$$

**Qué mide cada factor:**

| Factor | Rango típico | Qué revela |
|---|---|---|
| Carga fiscal | 0,70–0,80 | Eficiencia fiscal (1 − tasa efectiva) |
| Carga financiera | 0,80–1,00 | Cuánto se lleva la deuda; **cae al endeudarse más** |
| Margen operativo | varía por sector | La calidad real del negocio |
| Rotación de activos | varía por sector | Eficiencia en el uso del capital |
| Apalancamiento | 1,5–3,0 | Riesgo financiero |

**La utilidad de separar los dos primeros:** en la versión de tres factores, un ROE que cae
podría deberse a márgenes, eficiencia o desapalancamiento. En la de cinco se ve si el problema
es **operativo** (margen), **financiero** (carga financiera cayendo porque los intereses
crecen) o **fiscal** (pérdida de un beneficio tributario).

*Ejemplo:* una empresa cuyo ROE cae del 18 % al 12 %. Con cinco factores descubres que el margen
operativo y la rotación **no cambiaron**; lo que cayó fue la carga financiera, de 0,90 a 0,65.
**El negocio está igual de sano: lo que pasó es que los intereses se comieron la utilidad.** Es
un problema de balance, no de operación, y la solución es refinanciar, no reestructurar.

!!! tip "El apalancamiento que mejora el ROE y el que lo destruye"
    Endeudarse sube el **apalancamiento** (quinto factor) pero baja la **carga financiera**
    (segundo). El efecto neto sobre el ROE depende de una sola condición:

    $$ROE \uparrow \iff ROA > \text{costo de la deuda después de impuestos}$$

    Si la empresa genera un 10 % sobre sus activos y la deuda le cuesta un 6 % neto, cada peso
    prestado añade 4 puntos al accionista: **el apalancamiento crea valor**.

    Si el ROA cae al 5 % y la deuda sigue costando 6 %, **cada peso prestado destruye valor**, y
    el apalancamiento amplifica la caída en lugar de la subida.

    Por eso el apalancamiento es especialmente peligroso en negocios cíclicos: funciona
    magníficamente en la expansión y mata en la recesión, que es exactamente cuando el ROA cae
    por debajo del costo de la deuda.

---
