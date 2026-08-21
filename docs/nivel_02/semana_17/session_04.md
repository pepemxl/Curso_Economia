# Semana 17 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: El error de $50 millones en el M&A
*El equipo de Fusiones y Adquisiciones (M&A) de un banco de inversión está evaluando comprar una cadena de hoteles.*

Un analista junior usa la función `=VNA(tasa, A1:A10)` e incluye la inversión inicial de $500M en la celda A1, junto con los flujos de los próximos 9 años en A2:A10. El resultado arroja un VNA de +$20M. La junta directiva aprueba la compra basándose en ese número.

Tú, como Director Financiero, revisas el modelo y te das cuenta del error: Al incluir la inversión inicial en A1 dentro de la función VNA, Excel asumió que los $500M se gastaron al final del Año 1, no el Día 0. Al descontar erroneamete esa massive cifra un año extra al 10%, el número estaba inflado.

**El cálculo correcto debió ser:** `-A1 + VNA(tasa; A2:A10)`. 
Al corregirlo, el VNA real resulta ser **-$30 Millones**. El proyecto destruiría valor. Debes detener la adquisición antes de que se firme el cheque. Este es el motivo por el cual los modelos en Excel deben ser auditados rigurosamente ("model review") por un tercer analista antes de cualquier decisión corporativa.

---

## 8. Tareas y Evaluación de la Semana 17

**A. Lectura y Práctica Obligatoria:**
* Abre Excel.Ve a Archivo > Opciones > Complementos > Activar "Análisis de Datos" y "Solver" (los usaremos en las próximas semanas).
* Repasa la documentación de Microsoft sobre `TIR.NO.PER` y `BUSCARX`.

**B. Preguntas de Reflexión:**
1. ¿Por qué la función TIR tradicional puede dar un resultado engañosamente alto en un proyecto de Venture Capital donde los flujos de caja ocurren de forma dispersa a lo largo del año?
2. Si estás construyendo un modelo dinámico en Excel y sabes que en el futuro se insertarán nuevas columnas de datos, ¿por qué es obligatorio usar BUSCARX y no BUSCARV para extraer las cuentas contables?

**C. Ejercicio Práctico de Excel a entregar:**
Crea una hoja de Excel con un modelo de evaluación de un proyecto inmobiliario. Debes entregar las fórmulas exactas que usarías:

* **Datos del Proyecto Inmobiliario:**
  * Compra del terreno hoy (Año 0): -$2,000,000
  * Costos de construcción Año 1: -$3,000,000
  * Ventas de los departamentos Año 2: +$3,500,000
  * Ventas finales Año 3: +$3,800,000
  * Costo de Capital exigido (Tasa de Descuento): 12%

1. **Función PAGO:** El constructor necesita un préstamo puente para la construcción de $3,000,000 al 15% anual a 3 años. Escribe la fórmula exacta de Excel para calcular la cuota anual.
2. **Función VNA:** Escribe la estructura exacta de la fórmula en Excel para calcular el Valor Presente Neto de este proyecto (recuerda la trampa del Año 0). Calcula manualmente si el proyecto es viable o no.
3. **Función TIR:** Escribe la fórmula para calcular la rentabilidad porcentual del proyecto. (Pista: para TIR incluyes TODOS los flujos, incluido el terreno).

---
*¡Felicidades por completar la Semana 17! Ya dominas la artillería pesada de Excel. En la Semana 18 subiremos la dificultad a nivel "Wall Street": Modelación de estados financieros proyectados (P&L, Balance, Flujo de Efectivo) desde cero en Excel.*