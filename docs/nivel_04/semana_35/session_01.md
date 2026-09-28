# Semana 35 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Comprender el funcionamiento del Impuesto a las Sociedades (Corporate Tax) y su cálculo sobre el EBT.
* Entender la mecánica del IVA/IGV como impuesto al valor agregado y su impacto en el capital de trabajo.
* Dominar el concepto del **Escudo Fiscal (Tax Shield)** de la depreciación y de los intereses.
* Aprender a proyectar los impuestos en un modelo de Flujo de Caja Libre (FCFF) correctamente.

---

## 2. El Impuesto a las Sociedades (Corporate Income Tax)
Es el tributo que las empresas pagan sobre su beneficio neto (Utilidad Antes de Impuestos - EBT). 
* **Tasa Efectiva vs. Tasa Legal:** La tasa legal es la que dicta el gobierno (ej. 25% o 30%). La tasa efectiva es lo que la empresa *realmente* paga después de usar deducciones legales, créditos fiscales o teniendo operaciones en paraísos fiscales. (En la Semana 36 veremos planeación tributaria).
* **Regla Matemática de los Impuestos:** Los impuestos son un gasto de **efectivo real**. Aparecen en el Estado de Resultados (restando del EBT para hallar la Utilidad Neta) y en el Flujo de Efectivo de Operación (CFO) como una salida de caja.

> **💥 El concepto del "Escudo Fiscal" (Tax Shield):**
> No todos los gastos contables son salida de efectivo. La **Depreciación** (visto en la Semana 8) es un gasto contable que refleja el desgaste de la maquinaria, pero no sale dinero del banco. Al restar la depreciación del EBIT para calcular el EBT, reducimos la base imponible. 
> *Fórmula:* `Escudo Fiscal = Depreciación × Tasa de Impuesto`
> Si depreciaste $1,000 y la tasa es 25%, le "ahorraste" $250 al pago de impuestos en el banco. ¡La depreciación crea efectivo real!

---

## 3. El IVA / IGV (Impuesto al Valor Agregado)
Es un impuesto **indirecto** que grava el consumo. La empresa actúa solo como un recaudador del gobierno. 
* **Mecánica:** La empresa cobra el IVA a sus clientes (IVA de Salida / Crédito Fiscal) y paga el IVA a sus proveedores (IVA de Entrada / Débito Fiscal).
* **Liquidación:** Al final del mes, la empresa declara: `IVA Cobrado - IVA Pagado`. Si la diferencia es positiva, le transfiere ese efectivo al gobierno. Si es negativa (compró más de lo que vendió), el government le debe un saldo a favor.

**El Impacto Financiero Oculto (La Trampa del Capital de Trabajo):**
El IVA **NO** aparece en el Estado de Resultados (no es un gasto, es un pasivo con el fisco). Pero **SÍ destruye el Flujo de Caja Libre** a corto plazo si hay un desfase temporal.
* *Ejemplo:* Una constructora compra materiales en Enero y paga $21,000 de IVA. Pero la casa no se vende hasta Junio, momento en el que cobra el IVA al cliente.
* De Enero a Junio, la empresa tuvo que financiar $21,000 de su propio bolsillo para pagarle el IVA al gobierno, sin haberlo cobrado todavía. Esto inmoviliza el Capital de Trabajo y exige líneas de crédito bancarias a corto plazo para no quebrar por falta de liquidez (ilíquida pero rentable).

---
