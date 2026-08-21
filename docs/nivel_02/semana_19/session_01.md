# Semana 19 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Aprender a blindar un modelo financiero con la Validación de Datos y el Control de Errores.
* Dominar las Tablas Dinámicas para resumir grandes volúmenes de información contable.
* Construir un switches de escenarios (Base, Optimista, Pesimista) para evaluar la resiliencia de un proyecto.

---

## 2. Blindando el Modelo: Validación de Datos
Un modelo financiero solo es tan bueno como los datos que se introducen en él. Si tu modelo asume que el PIB crecerá un 3% y alguien escribe "3 dolares", todo el modelo colapsará dando un error `#¡VALOR!`.

* **Validación de Datos (Pestaña Datos > Validación de Datos):** 
  Restringe lo que un usuario puede escribir en una celda. 
  * *Lista desplegable:* Solo permite elegir entre opciones predefinidas (Ej. Año 1, Año 2).
  * *Decimales/Números enteros:* Solo permite escribir números (Ej. La tasa de impuesto debe estar entre 0 y 100%).
  * *Mensaje de entrada y error:* Puedes programar un cartelito que diga "Por favor ingrese un porcentaje válido" cuando alguien intenta escribir texto.

---

## 3. Control de Errores (Las Funciones "Guardián")
En finanzas, es mejor ver un "0" o un guion "-" que un molesto error de Excel que rompe las fórmulasposteriores. 

1. **SI.ERROR (IFERROR):** Es tu mejor amiga. Si una fórmula arroja un error (#N/A, #DIV/0!), la función SI.ERROR intercepta el error y te devuelve lo que tú configures.
   * *Ejemplo Calculando margen:* `=SI.ERROR(Utilidad_Neta / Ventas; 0)`. 
   * Si las Ventas son 0, en lugar de dar error de división por cero (`#DIV/0!`), la celda mostrará un 0 de forma elegante.
2. **ESBLANCO (ISBLANK):** Útil para que tu modelo no calcule años futuros que aún no han comenzado. `=SI(ESBLANK(Año5); ""; Fórmula_Cálculo)`. 
3. **Tip de oro:** Un modelo profesional de Wall Street no debe contener ni un solo `#REF!` o `#N/A`. SIERROR lo soluciona.

---

