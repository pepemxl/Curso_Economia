# Semana 23 · Sesión 2: Profundización

## 3. El Análisis de Quiebra: El Modelo Altman Z-Score
En 1968, el profesor Edward Altman analizó cientos de empresas quebradas y descubrió que, combinando 5 ratios financieros con pesos matemáticos específicos, se podía predecir la bancarrota con hasta un 80% de exactitud **dos años antes de que ocurriera**.

* **Fórmula Original (Para empresas manufactureras cotizadas en bolsa):**
  $$ Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 1.0X_5 $$

* **Componentes:**
  * $X_1 = \frac{\text{Capital de Trabajo}}{\text{Activos Totales}}$ *(Mide liquidez)*
  * $X_2 = \frac{\text{Utilidades Retenidas}}{\text{Activos Totales}}$ *(Mide la edad y auto-financiamiento de la empresa)*
  * $X_3 = \frac{\text{EBIT}}{\text{Activos Totales}}$ *(Mide rentabilidad operativa)*
  * $X_4 = \frac{\text{Valor de Mercado del Patrimonio}}{\text{Pasivo Total}}$ *(Mide si la empresa cotizada vale más que sus deudas)*
  * $X_5 = \frac{\text{Ventas}}{\text{Activos Totales}}$ *(Mide la eficiencia o rotación)*

**Las Zonas de Interpretación (La brújula del riesgo):**
1. **Zona Segura:** $Z > 2.99$. La empresa está sana. Riesgo de quiebra muy bajo.
2. **Zona Gris (Zona de Penumbra):** $1.81 < Z < 2.99$. El riesgo de quiebra es incierto. Hay que vigilar de cerca.
3. **Zona de Peligro (Distress):** $Z < 1.81$. La empresa está en grave riesgo de ir a bancarrota dentro de 2 años.

> **💥 Impacto Financiero:** Los bancos usan el Z-Score para decidir si otorgan préstamos. Los fondos de cobertura (Hedge Funds) lo usan para hacer **Short Selling** (vender en corto). Si detectan una empresa con un Z-Score de 1.2, se preparan para que las acciones caigan a cero. Para empresas privadas, Altman ajustó la fórmula (el coeficiente de $X_4$ baja a 0.717 y $X_5$ se elimina a veces) adaptándola a industrias no manufactureras.

---

## Más allá del Z-Score: las otras señales de dificultad

El Z-Score es un modelo estadístico. Un analista de crédito lo complementa siempre con señales
que ningún ratio recoge:

**Señales financieras**

* **Vencimientos concentrados.** Una empresa sana puede quebrar si le vence el 60 % de su deuda
  en un año en que los mercados están cerrados. Revisa siempre el **calendario de vencimientos**
  en las notas, no solo el nivel de deuda.
* **Covenants al límite.** Un incumplimiento técnico puede acelerar toda la deuda
  (*cross-default*), convirtiendo un problema pequeño en insolvencia inmediata.
* **CFO negativo sostenido** con deuda creciente: la empresa está financiando su operación
  con crédito.
* **Deterioro del crédito comercial:** proveedores que acortan plazos o exigen pago anticipado.
  Ellos ven la caja de la empresa antes que el mercado.

**Señales de mercado**

* **Spread de los CDS** sobre su deuda: es la opinión del mercado sobre su probabilidad de
  impago, actualizada a diario.
* **Cotización por debajo del valor en libros** de forma persistente.
* **Interés corto elevado**: hay quien está apostando activamente a su caída.

**Señales cualitativas**

* Rotación del CFO o del auditor sin explicación clara.
* Retrasos en la publicación de resultados.
* Salvedades o párrafos de énfasis en el informe de auditoría (especialmente el de **empresa en
  funcionamiento**, *going concern*).
* Ventas de acciones por parte de directivos.

!!! tip "La jerarquía de la información"
    Cuando las fuentes se contradicen, este es el orden de fiabilidad:

    1. **El mercado de crédito** (spreads de CDS y bonos). Los tenedores de deuda solo pierden;
       tienen incentivo a detectar problemas antes que nadie.
    2. **El flujo de caja.** Difícil de manipular.
    3. **El balance.** Manipulable, pero acumula la historia.
    4. **El estado de resultados.** El más manipulable de los tres.
    5. **La presentación a inversores.** Es material de marketing.

    Si el CDS se dispara mientras la presentación corporativa habla de un año récord, cree al CDS.

---
