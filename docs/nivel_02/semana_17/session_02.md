# Semana 17 · Sesión 2: Profundización

## 4. Función PAGO (Cálculo de Préstamos)
Conectado con la Semana 13 (Sistema Francés), Excel calcula la cuota fija de una anualidad con una sola fórmula.

* **Sintaxis:** `=PAGO(tasa; núm_periodos; valor_presente)`
* *Ejemplo:* Préstamo de $10,000, al 12% anual a 5 años.
  * `=PAGO(12%; 5; 10000)` -> Te dará una cuota anual de **-$2,774.10**. (Excel pone el número en negativo porque es una salida de efectivo desde la perspectiva del prestatario). 
* *Nota de oro:* Si el préstamo es mensual, la tasa debe ser mensual y los periodos en meses. `=PAGO(1%; 60; 10000)`.

---

## 5. Funciones de Búsqueda: BUSCARV vs. BUSCARX (XLOOKUP)
Para modelar financieramente, necesitas extraer datos de hojas enormes (Ej. el Inventario desde la Hoja "Balance" hacia tu Hoja "Ratios").

**A. BUSCARV (VLOOKUP): La veterana**
Busca un valor en la primera columna de una tabla y devuelve un valor en la misma fila pero en otra columna.
* **Sintaxis:** `=BUSCARV(valor_buscado; matriz_tabla; indicador_columna; [coincidencia])`
* **Problemas:** (1) Solo busca de izquierda a derecha. (2) Si insertas una columna nueva en medio de la tabla, el "indicador de columna" (un número fijo como 3 o 4) se rompe y devuelve datos erróneos.

**B. BUSCARX (XLOOKUP): La evolución definitiva**
Reemplaza a BUSCARV y es la estándar en modelos modernos (requiere Excel 365 o versiones recientes).
* **Sintaxis:** `=BUSCARX(valor_buscado; matriz_buscada; matriz_devuelta)`
* **Ventajas abrumadoras:** 
  1. Puede buscar de derecha a izquierda (no importa el orden de las columnas).
  2. No se rompe si insertas columnas nuevas, porque las referencias son rangos (A:A), no índices numéricos fijos.
  3. Tiene un manejo de errores integrado (si no encuentra el dato, puedes configurarla para que diga "No encontrado" en vez de arrojar el molesto #N/A).

---

