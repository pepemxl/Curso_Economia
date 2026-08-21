# Semana 23 · Sesión 4: Caso de Estudio y Evaluación

## 5. Análisis de Caso: El "Supuesto" Z-Score JGA y JGB
*Eres un gestor de un fondo de pensiones en 2007, Evaluando dos empresas legendarias del sector inmobiliario. Ambos bancos tienen puertas de madera caoba y ascensores de oro.*

Aplicas la fórmula Z-Score a sus balances del año 2006.
* **Empresa Inmobiliaria "JGA"** tiene un Z-Score de **3.5**. Tiene Capital de Trabajo alto, y sus Utilidades Retenidas son masivas. Opera con muy poca deuda.
* **Bank "JGB":** Su Estado de Resultados muestra utilidades récord gracias a paquetes de hipotecas subprime. Pero al calcular su Z-Score, arroja **1.25** (Zona de Peligro). ¿Por qué? Su $X_4$ (Patrimonio / Deuda) es pésimo porque tiene billones en pasivos fuera de balance; y su $X_1$ (Capital de trabajo) es casi cero porque invirtió todo en activos tóxicos ilíquidos.

**El Veredicto de Riesgo:**
El mercado en 2007 decía que ambos eran sólidos. Tus colegas se rieron de ti por desconfiar de JGB debido a "una simple fórmula matemática". En 2008, la crisis financiera golpea. JGB colapsa, es rescatada por el gobierno y sus accionistas lo pierden todo. JGA sobrevive y a la postre compra los activos de JGB a precio de remate.
El Z-Score no predijo "cuándo" iba a caer JGB, pero identificó que su estructura financiera oculta era un castillo de naipes años antes de que el mercado se diera cuenta.

---

## 6. Tareas y Evaluación de la Semana 23

**A. Lectura Obligatoria:**
* Altman, E. I. (1968). *Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy* (Artículo original, lectura de conceptos introductorios).
* *Lectura recomendada*: "The Z-Score_Model: Predicting Bankruptcy" (Artículos modernos de Altman adaptados a empresas emergentes y no cotizadas).

**B. Preguntas de Reflexión:**
1. ¿Por qué una empresa con altísimas utilidades contables y un EBITDA espectacular puede tener un bajo Z-Score y estar al borde de la quiebra? (Pista: Analiza el $X_4$ y el apalancamiento).
2. Explique la diferencia entre financiar el Capital de Trabajo con Deuda a Corto plazo vs. Largo Plazo. ¿Por qué las empresas eligen la opción agresiva si es tan riesgosa?

**C. Ejercicio Matemático a entregar:**
Analizas a la empresa manufacturera cotizada "FragileMold". Sus datos son:
* Activos Totales = $5,000
* Pasivos Totales = $3,500
* Capital de Trabajo = $500
* Utilidades Retenidas = $800
* EBIT = $300
* Ventas = $6,000
* El precio de la acción es $10. Hay 100 acciones en circulación.

Contesta:
1. Calcula los 5 componentes ($X_1$ a $X_5$) del Z-Score. (Recuerda que el Valor de Mercado del Patrimonio = Precio por acción * Número de acciones).
2. Aplica los coeficientes y haya el Z-Score total de FragileMold.
3. En qué zona se encuentra (Segura, Gris o Peligro)? Como analista, ¿recomendarías a tu fondo comprar acciones de FragileMold hoy o cortarlas (short selling)? Justifica.
