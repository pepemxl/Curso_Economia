# Semana 15 · Sesión 3: Aplicación Práctica

## 6. Ejercicio Práctico: El primer cálculo de Riesgo (VaR)
Tu portafolio de inversiones tiene un Retorno Promedio Esperado ($\mu$) del **10%** y una Desviación Estándar ($\sigma$) de la rentabilidad del **15%**. Asumimos que sigue una distribución Normal.

Tu jefe te pregunta: *¿Cuál es la probabilidad de que el portafolio pierda dinero (tenga un retorno menor al 0%) el próximo año?*

**Cálculo paso a paso:**
1. Tenemos $x = 0\%$. Queremos saber $P(X < 0)$.
2. Estandarizamos a Variable $Z$:
   $$ Z = \frac{0 - 10}{15} = \frac{-10}{15} = -0.667 $$
3. Buscamos en la Tabla de Distribución Normal Estándar (Tabla Z) el valor de $-0.667$.
4. La tabla nos arroja un valor de **0.2524**.

**Conclusión:** Hay una **25.24% de probabilidad** matemática de que el portafolio tenga un rendimiento negativo (pérdida) este año. Con esa probabilidad, el área de "Gestión de Riesgos" exige que el fondo reserve capital en efectivo como colchón para soportar esa posible caída.

---

