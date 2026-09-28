# Semana 10 · Sesión 3: Aplicación Práctica

## 4. Ejercicio Práctico Integrador: El analista frente a los reportes

La empresa retailer "GlobalStores" reporta sus resultados del año 2024:
* Las Ventas crecieron un **40%** respecto a 2023. 
* El PIB del país creció **2%** y la inflación anual fue del **8%**.
* Su Razón Corriente es de **1.8** (muy saludable).
* Su ratio Deuda/Patrimonio es de **0.5** (muy bajo, casi no tiene deudas).

El CEO declara en televisión: *"Hemos tenido un año espectacular, nuestras ventas crecieron 40% gracias a nuestra excelente gestión comercial"*.

**Tu análisis como profesional integral:**
1. **Desmitificación del Crecimiento:** La inflación fue 8% y la economía creció 2%. El "crecimiento base" esperado de cualquier empresa en ese país era de 10%. Si las ventas crecieron 40%, el **crecimiento orgánico real** fue de un 30%. Sí, fue un año excelente, pero no del 40%; parte fue ilusión inflacionaria.
2. **Análisis del Flujo:** como no tiene casi deuda y su liquidez es buena, si hay una recesión el próximo año (el Banco Central sube tasas al 15%), está blindada para sobrevivir. No irá a quiebra. Es un buen candidato para inversión defensiva en tu portafolio.

---

## Ejercicio integrador: diagnosticar una empresa con los tres estados

Aquí converge todo el Nivel 1. Tienes tres años de "NorthWind S.A." y debes emitir un
diagnóstico.

| Concepto | 2023 | 2024 | 2025 |
|---|---|---|---|
| Ventas | 1,000 | 1,250 | 1,600 |
| Utilidad neta | 80 | 110 | 160 |
| Cuentas por cobrar | 120 | 190 | 340 |
| Inventario | 150 | 210 | 330 |
| Cuentas por pagar | 100 | 115 | 125 |
| CFO | 95 | 60 | **−40** |
| CapEx | 50 | 60 | 70 |
| Deuda total | 300 | 380 | 550 |

**Paso 1 — Lo que ve un inversionista superficial**

Ventas **+60 %** en dos años. Utilidad neta **+100 %**. Márgenes que mejoran del 8,0 % al
10,0 %. **Parece una historia de crecimiento excelente.**

**Paso 2 — Las tasas de crecimiento comparadas**

| Partida | Crecimiento 2023→2025 |
|---|---|
| Ventas | +60 % |
| Utilidad neta | +100 % |
| **Cuentas por cobrar** | **+183 %** |
| **Inventario** | **+120 %** |
| Cuentas por pagar | +25 % |
| **Deuda** | **+83 %** |

**Tres señales rojas simultáneas:**

* Las **cuentas por cobrar crecen tres veces más rápido que las ventas**. La empresa vende, pero
  no cobra.
* El **inventario crece el doble que las ventas**. Produce más de lo que coloca.
* Las **cuentas por pagar apenas crecen**: los proveedores ya no le dan más plazo, señal de que
  su crédito comercial se está deteriorando.

**Paso 3 — Los días de rotación confirman el diagnóstico**

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| **DSO** (días de cobro) | 43.8 | 55.5 | **77.6** |
| **Calidad del beneficio** (CFO/UN) | 1.19 | 0.55 | **−0.25** |

**El DSO casi se duplica** y la calidad del beneficio se desploma de 1,19 a negativa.

**Paso 4 — El diagnóstico**

NorthWind está **comprando crecimiento con condiciones de venta cada vez más laxas**. Está
colocando producto en clientes que no pagan, y financiando el desfase con deuda (+83 %).

El mecanismo es autodestructivo y tiene fecha de caducidad:

1. Para sostener el crecimiento reportado, relaja el crédito a clientes.
2. Las ventas suben; el cobro no.
3. El CFO se vuelve negativo, así que se endeuda para operar.
4. Llegado el momento, la cartera vieja hay que provisionarla como incobrable y el inventario
   obsoleto hay que castigarlo.
5. **Ambos cargos golpean el P&L de golpe**, y ese trimestre la utilidad se desploma.

**Paso 5 — La conexión macro**

Y ahora la pregunta del nivel: **¿qué pasa si el banco central sube las tasas 300 puntos
básicos?**

* Su deuda de $\$550$ se encarece → mayores intereses sobre un CFO ya negativo.
* Sus clientes, también endeudados, tardan **aún más** en pagar → el DSO sigue subiendo.
* La demanda agregada se enfría → las ventas dejan de crecer, y con ellas se acaba el único
  argumento de la historia.
* Refinanciar la deuda se vuelve caro o imposible.

**NorthWind no quiebra por no ser rentable. Quiebra por no tener caja.** Es exactamente el caso
que planteaba la sesión anterior, y el motivo por el que un analista lee el flujo de efectivo
**antes** que el estado de resultados.

---
