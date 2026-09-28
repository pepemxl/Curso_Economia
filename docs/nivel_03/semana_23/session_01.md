# Semana 23 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Entender el Capital de Trabajo Neto y la importancia del Ciclo de Conversión de Efectivo (CCC) como mecanismo de supervivencia.
* Diferenciar entre estrategias de financiamiento conservadoras y agresivas.
* Comprender la fórmula del Modelo Altman Z-Score de 5 variables.
* Calcular e interpretar el Z-Score para predecir la probabilidad de bancarrota de una empresa.

---

## 2. La Gestión del Capital de Trabajo (WCM)
El **Capital de Trabajo Neto (CTN)** es el dinero que la empresa necesita para operar el día a día. 
* **Fórmula:** $CTN = Activo \text{ Corriente} - Pasivo \text{ Corriente}$.
Si es positivo, la empresa tiene holgura para pagar sus cuentas. Si es negativo, la empresa está operando con riesgo de iliquidez permanente. 

El motor de este capital es el **Ciclo de Conversión de Efectivo (CCC)** (visto en la Semana 21), pero hoy veremos cómo se financia.

**Estrategias de Financiamiento del Capital de Trabajo:**
1. **Estrategia Conservadora:** La empresa usa Deuda a Largo Plazo o Patrimonio (dinero permanente) para financiar sus inventarios y cuentas por cobrar. Es segura, pero el costo de capital es alto (destruye un poco el ROE).
2. **Estrategia Agresiva:** La empresa usa Deuda a Corto Plazo (préstamos bancarios de 30-90 días) para financiar todo su capital de trabajo. Es barato, pero es mortal: si el banco no renueva el préstamo a 30 días y el inventario no se ha vendido, la empresa quiebra por falta de caja, aunque sea rentable.

---

## El capital de trabajo: el activo que nadie ve

$$\text{Capital de trabajo neto} = \text{Activo corriente} - \text{Pasivo corriente}$$

Para el análisis operativo se usa una versión depurada, que excluye caja y deuda financiera:

$$NWC_{operativo} = (CxC + \text{Inventario}) - CxP$$

**Por qué importa tanto:** el capital de trabajo **no aparece en el Estado de Resultados** y sin
embargo consume o libera caja real cada año. Una empresa que crece necesita más inventario y
tiene más cartera pendiente de cobro; ese dinero está **inmovilizado**.

**El ciclo de conversión de efectivo** lo mide en días:

$$CCE = DIO + DSO - DPO$$

| Empresa tipo | DIO | DSO | DPO | **CCE** |
|---|---|---|---|---|
| Fabricante industrial | 90 | 60 | 45 | **+105 días** |
| Supermercado | 25 | 3 | 55 | **−27 días** |
| Software SaaS | 0 | 45 | 30 | **+15 días** |

**Un CCE negativo es una máquina de generar caja**: los proveedores financian la operación. Es
la ventaja estructural de las grandes superficies y del comercio electrónico, y explica por qué
pueden crecer agresivamente sin necesitar deuda.

Un CCE de +105 días significa lo contrario: **cada peso de crecimiento exige financiación
adicional**. Es la razón por la que las empresas industriales en expansión rápida son
candidatas naturales a la crisis de liquidez que estudiarás con el Z-Score en esta misma semana.

---
