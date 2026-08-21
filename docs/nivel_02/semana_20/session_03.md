# Semana 20 · Sesión 3: Aplicación Práctica

## 5. Ejercicio Práctico: Monte Carlo Básico para un VNA

Tienes un proyecto de 1 año. La inversión inicial es de **$1,000** (segura). Las Ventas son inciertas: Media = **$1,500**, Desviación Estándar = **$300**. Costos fijos de $200. Tasa de descuento 10%.

**Construcción en Excel:**
1. En la celda A1 escribes el generador aleatorio de Ventas: 
   `=INV.NORM(ALEATORIO(); 1500; 300)`
2. En A2 calculas el Flujo de Caja Libre: `=A1 - 200` *(Ventas aleatorias menos costos).*
3. En A3 calculas el VNA: `=-1000 + VNA(10%; A2)` *(Traes a valor presente el flujo de 1 año y restas la inversión inicial).*

**La Simulación (El truco de la Tabla de Datos):**
En lugar de apretar F9 mil veces, creas una columna del 1 al 1,000 (que representa 1,000 simulaciones). Al lado pones `=A3` (la celda de tu VNA). Seleccionas ambas columnas y vas a *Datos > Análisis de hipótesis > Tabla de datos*. 
En "Celda de entrada de columna" seleccionas **una celda vacía y basura** (ej. celda Z1). 
*¿Por qué Z1?* Porque al referenciar una celda vacía, Excel no altera tu modelo principal, pero se ve forzado a recalcular toda la hoja (re-lanzando los ALEATORIO) 1,000 veces seguidas. 

Al instante, tendrás 1,000 VNAs diferentes. Usas la función `=CONTAR.SI(rango_VNAs; ">0") / 1000` y obtienes la **probabilidad exacta de que el proyecto sea rentable**.

---

