# Semana 17 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Automatizar el cálculo del Valor Presente Neto (VAN/VNA) y la Tasa Interna de Retorno (TIR) en Excel.
* Entender la diferencia fundamental entre flujos periódicos (TIR) e irregulares (TIR.NO.PER).
* Calcular cuotas de préstamos con la función PAGO (conectando con la Semana 13).
* Dominar las funciones de búsqueda (BUSCARV / BUSCARX) para extraer datos de estados financieros masivos.

---

## 2. Funciones de Evaluación de Proyectos (VNA y TIR)
En la Semana 11 aprendiste a traer flujos futuros al Valor Presente uno por uno. Excel automatiza esto para flujos múltiples.

**A. VNA (Valor Presente Neto / NPV en inglés)**
Calcula el valor presente de una serie de flujos de caja futuros **iguales o diferentes**, asumiendo que ocurren al final de cada periodo.
* **Sintaxis:** `=VNA(tasa; rango_flujos)`
* > **⚠️ LA TRAMPA MORTAL DE EXCEL (Error de los Analistas Junior):**
  > La función VNA de Excel asume que el primer flujo del rango ocurre en el **Año 1**. Si tu inversión inicial ocurre hoy (Año 0), **NO** debes incluirla dentro de la función VNA. 
  > *Fórmula correcta:* `=-Inversión_Inicial + VNA(tasa; rango_flujos_del_año_1_al_año_5)`
  > Si incluyes la inversión inicial dentro del VNA, Excel la descontará un año extra, destruyendo la matemática del proyecto.

**B. TIR (Tasa Interna de Retorno / IRR en inglés)**
Es la tasa de descuento que hace que el VNA sea exactamente cero. Es el retorno porcentual que genera el proyecto.
* **Sintaxis:** `=TIR(rango_flujos; [estimación])`
* A diferencia de VNA, aquí **SÍ** debes incluir la inversión inicial (negativa) en el rango, porque Excel necesita buscar la tasa que iguala todos los flujos (incluyendo el desembolso inicial) a cero.

---

## 3. TIR.NO.PER (Tir no periódica / XIRR en inglés)
En la vida real, las empresas no reciben dinero en fechas perfectas cada 365 días. Un proyecto puede empezar el 15 de enero, recibir un flujo el 3 de mayo y terminar el 20 de diciembre. La función TIR normal falla aquí porque asume periodos exactos de 1 año.

* **Sintaxis:** `=TIR.NO.PER(rango_flujos; rango_fechas)`
* **Requisito:** Las fechas deben estar en celdas con formato de "Fecha real" de Excel, no como texto. 
> **💥 Impacto Financiero:** Para evaluarfondos de Private Equity o Venture Capital, donde las inversiones y los exits (salidas a bolsa) ocurren en días irregulares, TIR.NO.PER es la única herramienta matemáticamente correcta. Usar TIR normal puede inflar el retorno aparente en un 2% o 3%.

---

