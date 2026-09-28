# Semana 5 · Sesión 4: Caso de Estudio y Evaluación

## 7. Análisis de Caso: Estrategia de trading basada en DA-OA
*Eres gestor de un fondo de inversión (Portfolio Manager) y tu trabajo es decidir la asignación de activos (Asset Allocation).*

El Banco Central y el Ministerio de Economía anuncian un plan conjunto:
1. El Banco Central baja las tasas de interés (Política Monetaria Expansiva).
2. El Ministerio aprueba un megaproyecto de infraestructura de $10,000 millones (Política Fiscal Expansiva).

**Tu análisis macroeconómico:** Ambas medidas desplazan la curva de Demanda Agregada (DA) fuertemente hacia la derecha. A corto plazo, la curva de Oferta Agregada no se mueve. Por lo tanto, pronosticas que el PIB crecerá (final de la recesión) y que los precios comenzarán a subir (inflación).

**Tu decisión de inversión (Asset Allocation):**
* **Acciones cíclicas:** Vendo acciones de empresas defensivas (farmacéuticas, utilities de agua) y compró masivamente acciones de empresas cíclicas (banca, construcción, industria pesada, aerolíneas). En el ciclo de recuperación, sus beneficios crecen más rápido que el PIB gracias al multiplicador keynesiano y al apalancamiento operativo (tema de finanzas corporativas).
* **Renta fija (Bonos):** Vendo bonos soberanos a largo plazo. La inflación futura destruirá el valor real de los intereses fijos que pagan esos bonos. Con el dinero, compro **materias primas (Commodities)** como oro o petróleo, que suelen apreciarse en entornos inflacionarios.

---


## 8. Tareas y Evaluación de la Semana 5

**A. Lectura Obligatoria:**
* Mankiw, N. Gregory. *Principios de Economía*. Capítulos 20 (La Demanda Agregada y La Oferta Agregada) y 21 (La Influencia de la Política Monetaria y Fiscal en la Demanda Agregada).

**B. Preguntas de Reflexión:**
1. ¿Por qué la curva de Oferta Agregada a Corto Plazo es pendiente positiva, pero la de Largo Plazo es una línea vertical? Justifica basándote en la rigidez de los salarios.
2. Define qué es un "Choque adverso de oferta" y menciona un ejemplo histórico reciente (hint: pandemia, crisis energética). ¿Qué implicó para la inflación y el crecimiento del país impactado?

**C. Ejercicio Matemático a entregar:**
La economía de "Econolutia" está en una profunda brecha recesaria. El PIB actual es de $\$5,000$ millones, y se calcula que el PIB Potencial de pleno empleo es de $\$5,500$ millones. El gobierno de Econolutia quiere aplicar política fiscal para cerrar la brecha. En este país, la gente gasta el $60\%$ de cada peso adicional que gana ($PMgC = 0.60$).

Contesta:
1. Calcula el multiplicador keynesiano ($k$) en Econolutia. Muestra tus pasos.
2. ¿Cuánto tiene que aumentar el gasto público ($G$) exactamente para cerrar la brecha recesaria y llevar el PIB exacto a su nivel potencial de pleno empleo? (Pista: Recuerda que el impacto en el PIB será $k \times \Delta G$. Sustituye el valor del impacto deseado y despeja $\Delta G$).

??? success "Solución del Ejercicio C"

    **1. Multiplicador keynesiano**

    $$k = \frac{1}{1 - PMgC} = \frac{1}{1 - 0.60} = \frac{1}{0.40} = \mathbf{2.5}$$

    Significa que cada peso de gasto público adicional genera $\$2.50$ de PIB:
    el primer peso se gasta, el 60 % de eso vuelve a gastarse, y así sucesivamente.

    **2. Aumento de gasto público necesario**

    Brecha recesiva a cerrar:

    $$\Delta PIB\ \text{deseado} = 5{,}500 - 5{,}000 = 500 \text{ millones}$$

    Como $\Delta PIB = k \times \Delta G$, despejamos:

    $$\Delta G = \frac{\Delta PIB}{k} = \frac{500}{2.5} = \mathbf{200 \text{ millones}}$$

    **Comprobación:** $2.5 \times 200 = 500$ ✓ → el PIB pasa de $5{,}000$ a $5{,}500$.

    La idea potente del multiplicador: el gobierno **no necesita gastar los 500
    millones de la brecha**, le bastan 200. Los otros 300 los genera el propio
    circuito de consumo privado.

    !!! note "Matiz que suele preguntarse en examen"
        Este resultado supone el multiplicador simple (economía cerrada, sin
        impuestos proporcionales al ingreso ni importaciones). Con impuestos y
        propensión a importar, el multiplicador real es **menor**, y el gobierno
        tendría que gastar **más** de 200 millones para cerrar la misma brecha.

---
