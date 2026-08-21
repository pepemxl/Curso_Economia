# Semana 24 · Sesión 2: Profundización

## 4. El Costo del Patrimonio ($r_e$) y el CAPM
Calcular el costo de la deuda es fácil (solo miras el contrato del banco). Pero, ¿cuál es el costo del dinero de los accionistas? No hay contrato. Se usa el **CAPM** (Capital Asset Pricing Model), desarrollado por William Sharpe (Premio Nobel de Economía).

* **Fórmula del CAPM:**
  $$ r_e = R_f + \beta \times (E(R_m) - R_f) $$

**Desglossando la fórmula:**
1. **$R_f$ (Tasa Libre de Riesgo):** El retorno del activo más seguro del mundo (generalmente el Bono del Tesoro de EE. UU. a 10 años). Aprox. 4%. Es el rendimiento mínimo que un inversor exige solo por apartar su dinero del mercado.
2. **$(E(R_m) - R_f)$ (Prima por Riesgo de Mercado):** El retorno extra que el inversor exige por invertir en la bolsa de valores en lugar del bono seguro. Suele rondar el 5% al 7%.
3. **$\beta$ (Beta):** Es la **medida de riesgo sistemático** (no diversificable). Indica qué tan volátil es la acción respecto al mercado global.
   * $\beta = 1.0$: La acción se mueve igual que el mercado.
   * $\beta = 1.5$: Si el mercado sube 10%, la acción sube 15%. (Alto riesgo). (Vimos cómo calcularlo por regresión lineal en la Semana 16).
   * $\beta = 0.5$: La acción se mueve a la mitad que el mercado. (Bajo riesgo, empresas defensivas).

> **💥 Impacto Financiero:** El CAPM codifica la regla de oro de las finanzas: *"A mayor riesgo, mayor rendimiento exigido"*. Una empresa tecnológica volátil con $\beta = 1.5$ tendrá un Costo de Patrimonio altísimo (ej. 14%). Por eso, las startups de tecnología no pueden jugar en modelos de bajo retorno; matemáticamente, destruirían valor.

---

## 5. La Ecuación Maestra del WACC
Integramos todo en la fórmula final:

$$ WACC = \left( \frac{E}{V} \times r_e \right) + \left( \frac{D}{V} \times r_d \times (1 - T) \right) $$

* $E/V$: Porcentaje del capital que proviene de los accionistas.
* $D/V$: Porcentaje del capital que proviene de la deuda.
