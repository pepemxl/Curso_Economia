# Semana 20 · Sesión 4: Caso de Estudio y Evaluación

## 6. Análisis de Caso: La Mina de Cobre "CopperPeak"
*Eres el analista senior de un fondo de Private Equity evaluando la compra de una mina de cobre. La inversión inicial es monstruosa: $500 Millones.*

El equipo geólogo ha dicho: "Creemos que la mina producirá 10,000 toneladas de cobre al año, pero depende de la calidad de la roca (puede ser 8,000 o 12,000)".
El equipo macroeconómico ha dicho: "El precio del cobre hoy es $4.00 el kg, pero es altamente volátil, puede subir a $5 o caer a $3".

Un analista junior hace un análisis de sensibilidad bidimensional y dice: "En el peor caso (8,000 toneladas y $3 precio), el VNA es -$50M. En el mejor caso, es +$200M". El comité directivo no sabe siinvertir porque el rango es demasiado amplío.

**Tu Solución con Monte Carlo:**
1. Modelas el Precio del cobre con una Media de $4.00 y una Desviación del $0.50 (Distribución Normal).
2. Modelas la Producción con una Media de 10,000 y una Desviación de 1,000.
3. Corres una simulación de 10,000 iteraciones (10,000 posibles combinaciones de precio y producción cruzadas aleatoriamente).
4. El resultado arroja: *"El VNA promedio es de +$75M. Sin embargo, la probabilidad de que el VNA sea menor a cero (pérdida de la inversión) es del 8.5% (850 de cada 10,000 simulaciones)."*

**Veredicto Financiero:** El comité directivo aprueba la compra de la mina, pero exige inmediatamente contratar un *Hedge* (cobertura) con futuros de cobre para bloquear el precio de venta a $4.00, eliminando la volatilidad del precio y reduciendo drásticamente la probabilidad de pérdida (el 8.5%) a casi cero. La simulación matemática salvó de un apuro aleatorio al fondo y aseguró el retorno.

---

## 7. Tareas y Evaluación de la Semana 20 (Cierre de Nivel 2)

**A. Lectura y Práctica Obligatoria:**
* *Lectura*: *Principles of Finance with Excel* (Simon Benninga) - Capítulo sobre Simulations and Monte Carlo.
* *Práctica*: Busca en YouTube "Excel Monte Carlo Simulation NPV" y replica la tabla de datos en tu propio Excel.

**B. Preguntas de Reflexión:**
1. ¿Por qué el análisis de sensibilidad tradicional (Data Tables bidimensionales) es insuficiente para proyectos commodities (petróleo, cobre, soya) donde hay múltiples variables inciertas interactuando al mismo tiempo?
2. Explica la función de la celda "basura" (Z1) cuando usas una Tabla de Datos en Excel para forzar una simulación Monte Carlo. ¿Por qué Excel recalcula los números aleatorios si la celda Z1 está vacía?

**C. Ejercicio Práctico Final a entregar:**
Vas a modelar un proyecto inmobiliario en Excel.
* **Inversión Inicial:** -$2,000,000 (hoy, Año 0).
* **Precio de Venta proyectado (Año 1):** Incierto. Media = $2,500,000. Desviación Estándar = $300,000. Asume Distribución Normal.
* **Costos de Construcción (Año 1):** Incierto. Media = $300,000. Desviación = $50,000. (Distribución Normal).
* **Tasa de Descuento:** 8% fija.
* **Flujo del Año 1:** Precio de VentaAleatorio - Costos Aleatorios.
* **VNA:** = -2,000,000 + (Flujo Año 1 / (1+8%)^1)

Contesta / Construye:
1. Escribe las dos fórmulas de Excel exactas (`=INV.NORM(ALEATORIO()...)`) que usarías para generar el Precio de Venta Aleatorio y el Costo Aleatorio.
2. Construye una simulación en Excel de 1,000 iteraciones usando Tablas de Datos y la celda "basura".
3. Usa la función `=PROMEDIO` para hallar el VNA medio de las 1,000 iteraciones.
4. Usa la función `=CONTAR.SI` para calcular qué porcentaje de las 1,000 iteraciones tuvo un VNA > 0 (Probabilidad de éxito). Reporta este porcentaje.

---

### 🎉 ¡FELICIDADES! HAS COMPLETADO EL NIVEL 2 🎉

Has demostrado un dominio sobresaliente de las herramientas cuantitativas. Ya sabes cómo valora el dinero en el tiempo, cómo medir el riesgo estadístico y cómo programar el futuro de una empresa en Excel bajo escenarios de incertidumbre. Eres matemáticamente capaz de tasar cualquier activo.

**Próximo paso: NIVEL 3 (Análisis Financiero, Finanzas Corporativas y Mercados Financieros).**
A partir de la Semana 21, entraremos en el mundo de la valuación real. Usaremos todo lo que has aprendido para leer los estados financieros de empresas reales, calcular el costo de capital (WACC), valorar empresas por Descuento de Flujos de Caja (DCF) y entender cómo operan los mercados bursátiles y los derivados. ¡Nos vemos en la cima!