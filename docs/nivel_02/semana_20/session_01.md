# Semana 20 · Sesión 1: Fundamentos

## 1. Objetivos de la Semana
* Comprender la diferencia fundamental entre Sensibilidad, Escenarios y Simulación.
* Dominar las Tablas de Datos (Data Tables) en Excel para análisis de sensibilidad unidimensionales y bidimensionales.
* Entender la lógica estadística detrás de la Simulación de Monte Carlo.
* Construir un modelo básico de Monte Carlo en Excel combinando el Valor Presente Neto (VNA) con la Distribución Normal (vista en la Semana 15).

---

## 2. El Análisis de Sensibilidad (Pruebas de Estrés Estáticas)
El análisis de sensibilidad responde a la pregunta: *"Si cambio una sola variable, ¿cuánto se altera mi resultado final (VNA o Utilidad)?"*

**A. Sensibilidad Unidimensional (Una variable):**
Mide el impacto de una sola variable (ej. Precio de venta) sobre el resultado (ej. VNA). 
* *Ejemplo:* Si el precio del producto baja de $10 a $8, ¿el VNA sigue siendo positivo o el proyecto destruye valor?

**B. Sensibilidad Bidimensional (Dos variables - "Tablas de Datos"):**
Es la herramienta más usada en presentaciones a directivos. Muestra una matriz (una cuadrícula) donde cruzas dos variables simultáneamente.
* *Ejemplo:* Eje horizontal: Tasa de descuento (WACC) del 8% al 12%. Eje vertical: Tasa de crecimiento de ventas del 0% al 10%. En el cruce de cada fila y columna, Excel calcula automáticamente el VNA resultante.
> **💥 Cómo hacerlo en Excel:** Usas la herramienta *Datos > Análisis de hipótesis > Tabla de datos*. Seleccionas la fila de tasas y la columna de crecimientos, y Excel rellena la matriz entera en un segundo. (Esto evita tener que reescribir la fórmula VNA 50 veces).

---

## 3. La Simulación de Monte Carlo (Riesgo Probabilístico)
El problema del Análisis de Sensibilidad es que asume que las variables son seguros ("cambia el precio a $8 y mira qué pasa"). En la vida real, el precio puede ser $8.50, $9.10, $7.20, etc. Hay infinitas posibilidades.

Monte Carlo es una técnica matemática que **simula miles de escenarios posibles al azar**, basándose en las probabilidades estadísticas de cada variable (usando la Distribución Normal o la Triangular), para darte un rango de resultados y la probabilidad de que tu proyecto sea exitoso.

**La Lógica de Monte Carlo:**
1. Defines una variable (Ej. Precio de venta: Media = $10, Desviación Estándar = $1).
2. Le pides a Excel que genere un **número aleatorio** que siga esa distribución.
3. Calculas el VNA del proyecto usando ese número aleatorio.
4. Repites este proceso **1,000 o 10,000 veces**.
5. Al final, puedes decir: *"De 10,000 simulaciones, el proyecto tuvo un VNA positivo en el 85% de los casos. Hay un 15% de probabilidad de pérdida"*.

---

