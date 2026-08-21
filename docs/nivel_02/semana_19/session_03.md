# Semana 19 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: El Switch de Escenarios

Estás proyectando las cosas (Ventas de la empresa "TechCorp"). En tu pestaña de Supuestos tienes 3 columnas: Base, Optimista, Pesimista.
* Tasa de Crecimiento Base: 5%
* Tasa de Crecimiento Optimista: 15%
* Tasa de Crecimiento Pesimista: -2%

**Paso a paso en Excel:**
1. En la celda A1 creas una lista desplegable con validación de datos permitiendo solo 1, 2 o 3. Llama a A1 "Selector".
2. En la celda B1 (Tu Tasa de Crecimiento para el modelo) escribes:
   `=ELEGIR(A1; 5%; 15%; -2%)`
3. En tu Estado de Resultados: `Ventas Año 1 = Ventas Año 0 * (1 + $B$1)`

*Si el director quiere ver el caso optimista, le basta con cambiar el número de A1 a 2. Todo el modelo se recalcula a exceso de ventas al instante, permitiéndole ver si la empresa tendrá capacidad de planta para producir tanto o necesitará pedir más deuda (CapEx).*

---

