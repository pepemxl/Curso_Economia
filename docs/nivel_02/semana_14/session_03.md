# Semana 14 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: Comparando dos Fondos de Inversión

Eres un asesor financiero y tienes que recomendar un fondo a un cliente conservador. Analizas los retornos anuales de los últimos 5 años de dos fondos:

* **Fondo "Crecimiento Agresivo" (Retornos %):** 5, 15, -20, 30, 20
* **Fondo "Value Conservador" (Retornos %):** 6, 8, 5, 7, 9

**Cálculo para el Fondo "Crecimiento Agresivo":**
1. **Media:** $(5 + 15 - 20 + 30 + 20) / 5 = 50 / 5 = \mathbf{10\%}$
2. **Desviaciones respecto a la media:** $(5-10) = -5$; $(15-10) = 5$; $(-20-10) = -30$; $(30-10) = 20$; $(20-10) = 10$.
3. **Varianza:** $[(-5)^2 + (5)^2 + (-30)^2 + (20)^2 + (10)^2] / (5-1) = [25 + 25 + 900 + 400 + 100] / 4 = 1450 / 4 = \mathbf{362.5}$
4. **Desviación Estándar:** $\sqrt{362.5} = \mathbf{19.03\%}$

**Cálculo para el Fondo "Value Conservador":**
1. **Media:** $(6 + 8 + 5 + 7 + 9) / 5 = 35 / 5 = \mathbf{7\%}$
2. **Varianza:** $[(-1)^2 + (1)^2 + (-2)^2 + (0)^2 + (2)^2] / 4 = 10 / 4 = \mathbf{2.5}$
3. **Desviación Estándar:** $\sqrt{2.5} = \mathbf{1.58\%}$

**Conclusión Financiera con Coeficiente de Variación:**
* Fondo Agresivo: $CV = 19.03 / 10 = 1.90$ (1.9 unidades de riesgo por cada 1 de retorno).
* Fondo Conservador: $CV = 1.58 / 7 = 0.22$ (0.22 unidades de riesgo por cada 1 de retorno).
*El Fondo Conservador es matemáticamente superior en relación riesgo/return. Se lo recomiendas al cliente.*

---

